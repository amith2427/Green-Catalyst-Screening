#!/usr/bin/env python3
"""Reproduce the synthetic chemoinformatics benchmark outputs.

Consolidated from the result-producing parts of Chem_Re.ipynb (late-stage
cells 125 and 128). Historical draft/manuscript-generation cells are omitted.
The reference dataset preserves the original NumPy random draw order.

Run: python reproduce_benchmark.py --output-dir outputs

This script recomputes the 20-seed model cross-validation by default; it does
not reuse an existing metric log. The local environment manifest is written
with each run because the uploaded notebook did not preserve a complete,
per-execution package freeze for the final run.
"""
from __future__ import annotations

import argparse
import importlib.metadata
import json
import platform
import sys
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import shap
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import GroupKFold, KFold
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from xgboost import XGBRegressor

SEEDS = list(range(42, 62))
N = 5000
CAT_BASELINES = [55, 45, 40, 30]
OX_BASELINES = [30, 20, 10]

METRIC_COLUMNS = [
    "LR_RND_MAE", "LR_RND_R2", "XGB_RND_MAE", "XGB_RND_R2",
    "RF_RND_MAE", "RF_RND_R2", "SVR_RND_MAE", "SVR_RND_R2",
    "SVR_NODECOY_MAE", "SVR_NODECOY_R2",
    "LR_GRP_MAE", "LR_GRP_R2", "XGB_GRP_MAE", "XGB_GRP_R2",
    "RF_GRP_MAE", "RF_GRP_R2", "SVR_GRP_MAE", "SVR_GRP_R2",
]


def load_substrate_library() -> pd.DataFrame:
    """Read the 22 SMILES/mass pairs used in the manuscript benchmark."""
    path = Path(__file__).with_name("substrates.csv")
    library = pd.read_csv(path)
    expected = list(range(22))
    if library["Substrate_Idx"].tolist() != expected:
        raise ValueError("substrates.csv must contain substrate indices 0..21 in order")
    if library["SMILES"].isna().any() or library["ExactMolWt_Da"].isna().any():
        raise ValueError("substrates.csv contains missing SMILES or masses")
    return library


def draw_reaction_inputs(seed: int, library: pd.DataFrame, n: int = N) -> dict[str, np.ndarray]:
    """Draw the DGP variables in the same order as the original result cells."""
    np.random.seed(seed)
    masses = library["ExactMolWt_Da"].to_numpy(dtype=float)
    substrate_idx = np.random.choice(22, n)
    exact_mass = masses[substrate_idx]
    temp = np.random.uniform(25, 110, n)
    cat_idx = np.random.choice(len(CAT_BASELINES), n)
    ox_idx = np.random.choice(len(OX_BASELINES), n)
    cat_val = np.array([CAT_BASELINES[i] for i in cat_idx])
    ox_val = np.array([OX_BASELINES[i] for i in ox_idx])
    noise = np.random.normal(0, 5, n)
    y_raw = cat_val + ox_val - (0.05 * exact_mass) + (0.15 * (temp - 25)) + noise
    y = np.clip(y_raw, 0, 100)
    return {
        "substrate_idx": substrate_idx,
        "exact_mass": exact_mass,
        "temp": temp,
        "cat_idx": cat_idx,
        "ox_idx": ox_idx,
        "cat_val": cat_val,
        "ox_val": ox_val,
        "noise": noise,
        "y": y,
    }


def build_cv_features(
    drawn: dict[str, np.ndarray], n: int = N
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Build full and ablated one-hot matrices and target/groups."""
    df = pd.DataFrame({
        "ExactMolWt": drawn["exact_mass"],
        "temp": drawn["temp"],
        "cat": drawn["cat_idx"],
        "ox": drawn["ox_idx"],
        "decoy_cat_load": np.random.uniform(1, 10, n),
        "decoy_rot_bonds": np.random.uniform(0, 10, n),
        "decoy_tpsa": np.random.uniform(20, 120, n),
    })
    X_all = pd.get_dummies(df, columns=["cat", "ox"]).values.astype(float)
    X_no = pd.get_dummies(
        df[["ExactMolWt", "temp", "cat", "ox"]], columns=["cat", "ox"]
    ).values.astype(float)
    groups = drawn["substrate_idx"]
    y = drawn["y"]
    if X_all.shape[1] != 12 or X_no.shape[1] != 9:
        raise ValueError(f"Unexpected feature dimensions: with={X_all.shape}, without={X_no.shape}")
    return X_all, X_no, y, groups


def evaluate_seed_model(
    model: Any,
    X: np.ndarray,
    y: np.ndarray,
    groups: np.ndarray,
    seed: int,
    is_grouped: bool,
    continuous_columns: list[int],
) -> tuple[float, float]:
    """Mean the five held-out fold scores for one seed/model/configuration."""
    cv = GroupKFold(n_splits=5) if is_grouped else KFold(
        n_splits=5, shuffle=True, random_state=seed
    )
    splits = cv.split(X, y, groups=groups) if is_grouped else cv.split(X, y)
    fold_maes: list[float] = []
    fold_r2s: list[float] = []
    for train_idx, test_idx in splits:
        X_train = X[train_idx].copy()
        X_test = X[test_idx].copy()
        scaler = StandardScaler()
        X_train[:, continuous_columns] = scaler.fit_transform(X_train[:, continuous_columns])
        X_test[:, continuous_columns] = scaler.transform(X_test[:, continuous_columns])
        model.fit(X_train, y[train_idx])
        pred = model.predict(X_test)
        fold_maes.append(mean_absolute_error(y[test_idx], pred))
        fold_r2s.append(r2_score(y[test_idx], pred))
    return float(np.mean(fold_maes)), float(np.mean(fold_r2s))


def run_cross_validation(library: pd.DataFrame) -> pd.DataFrame:
    """Run the 20-seed CV suite from the final model-results cell."""
    rows: list[dict[str, float | int]] = []
    for seed in SEEDS:
        drawn = draw_reaction_inputs(seed, library)
        X_all, X_no, y, groups = build_cv_features(drawn)
        cont_all = [0, 1, 2, 3, 4]
        cont_no = [0, 1]
        lr = LinearRegression()
        xgb = XGBRegressor(n_estimators=50, max_depth=3, learning_rate=0.1, random_state=seed)
        rf = RandomForestRegressor(n_estimators=50, max_depth=5, random_state=seed)
        svr = SVR(kernel="rbf", C=1.0, epsilon=0.1)
        result: dict[str, float | int] = {"Seed": seed}

        def store(key: str, model: Any, grouped: bool, X: np.ndarray, columns: list[int]) -> None:
            mae, r2 = evaluate_seed_model(model, X, y, groups, seed, grouped, columns)
            result[f"{key}_MAE"] = mae
            result[f"{key}_R2"] = r2

        store("LR_RND", lr, False, X_all, cont_all)
        store("XGB_RND", xgb, False, X_all, cont_all)
        store("RF_RND", rf, False, X_all, cont_all)
        store("SVR_RND", svr, False, X_all, cont_all)
        store("SVR_NODECOY", svr, False, X_no, cont_no)
        store("LR_GRP", lr, True, X_all, cont_all)
        store("XGB_GRP", xgb, True, X_all, cont_all)
        store("RF_GRP", rf, True, X_all, cont_all)
        store("SVR_GRP", svr, True, X_all, cont_all)
        rows.append(result)
        print(f"CV complete for seed {seed} ({len(rows)}/{len(SEEDS)})", flush=True)
    df_logs = pd.DataFrame(rows)
    return df_logs[["Seed", *METRIC_COLUMNS]]


def compute_oracle_metrics(library: pd.DataFrame) -> pd.DataFrame:
    """Compute each seed's clipped-noiseless oracle against its noisy target."""
    masses = library["ExactMolWt_Da"].to_numpy(dtype=float)
    records = []
    for seed in SEEDS:
        np.random.seed(seed)
        substrate_idx = np.random.choice(22, N)
        exact_mass = masses[substrate_idx]
        temp = np.random.uniform(25, 110, N)
        cat_idx = np.random.choice(len(CAT_BASELINES), N)
        cat_val = np.array([CAT_BASELINES[i] for i in cat_idx])
        ox_idx = np.random.choice(len(OX_BASELINES), N)
        ox_val = np.array([OX_BASELINES[i] for i in ox_idx])
        noise = np.random.normal(0, 5, N)
        target = np.clip(cat_val + ox_val - 0.05 * exact_mass + 0.15 * (temp - 25) + noise, 0, 100)
        oracle = np.clip(cat_val + ox_val - 0.05 * exact_mass + 0.15 * (temp - 25), 0, 100)
        records.append({
            "Seed": seed,
            "ORACLE_MAE": mean_absolute_error(target, oracle),
            "ORACLE_R2": r2_score(target, oracle),
        })
    return pd.DataFrame(records)


def generate_reference_dataset(library: pd.DataFrame) -> pd.DataFrame:
    """Generate the Seed 42 CSV using the exact order in the result-producing cells."""
    drawn = draw_reaction_inputs(42, library)
    cat_idx = drawn["cat_idx"]
    ox_idx = drawn["ox_idx"]
    temp = drawn["temp"]
    exact_mass = drawn["exact_mass"]
    y = drawn["y"]
    sel_bases = {0: 85, 1: 75, 2: 70, 3: 60}
    sus_bases = {0: 95, 1: 85, 2: 50}
    sel_arr = np.array([sel_bases[c] for c in cat_idx]) + np.random.normal(0, 2, N)
    sus_arr = np.array([sus_bases[o] for o in ox_idx]) - 0.5 * (temp - 25)
    raw_gpi = 0.40 * y + 0.25 * sel_arr + 0.35 * sus_arr
    norm_gpi = (raw_gpi / 100.0) * 4 + 1
    df_ref = pd.DataFrame({
        "RXN_ID": [f"RXN_{i:04d}" for i in range(N)],
        "Substrate_Idx": drawn["substrate_idx"],
        "ExactMolWt": exact_mass,
        "Temp": temp,
        "Cat_Idx": cat_idx,
        "Ox_Idx": ox_idx,
        "Decoy_Cat_Load": np.random.uniform(1, 10, N),
        "Decoy_Rot_Bonds": np.random.uniform(0, 10, N),
        "Decoy_TPSA": np.random.uniform(20, 120, N),
        "Target_Yield": y,
        "Selectivity_Score": sel_arr,
        "Sustainability_Score": sus_arr,
        "Norm_GPI": norm_gpi,
    })
    return df_ref


def compute_shap_and_plot(df_ref: pd.DataFrame, outdir: Path) -> pd.DataFrame:
    """Fit the full-reference XGBoost model and compute manuscript's SHAP aggregation."""
    features = df_ref[[
        "ExactMolWt", "Temp", "Decoy_Cat_Load", "Decoy_Rot_Bonds", "Decoy_TPSA", "Cat_Idx", "Ox_Idx"
    ]]
    X_df = pd.get_dummies(features, columns=["Cat_Idx", "Ox_Idx"])
    X_val = X_df.values.astype(float)
    model = XGBRegressor(n_estimators=50, max_depth=3, learning_rate=0.1, random_state=42)
    model.fit(X_val, df_ref["Target_Yield"].to_numpy())
    values = shap.TreeExplainer(model).shap_values(X_val)
    importances = [
        np.mean(np.abs(values[:, 5:9]).sum(axis=1)),
        np.mean(np.abs(values[:, 9:12]).sum(axis=1)),
        np.mean(np.abs(values[:, 1])),
        np.mean(np.abs(values[:, 0])),
        np.mean(np.abs(values[:, 2])),
        np.mean(np.abs(values[:, 3])),
        np.mean(np.abs(values[:, 4])),
    ]
    labels = [
        "Catalyst Identity", "Oxidant Identity", "Temperature", "ExactMolWt",
        "Decoy_Cat_Load", "Decoy_Rot_Bonds", "Decoy_TPSA",
    ]
    imp_df = pd.DataFrame({"Feature": labels, "MeanAbsSHAP": importances})
    imp_df.to_csv(outdir / "shap_importance.csv", index=False)
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(
        x=importances, y=labels, hue=labels,
        palette=["#c83b4c"] * 4 + ["#7d7d7d"] * 3,
        edgecolor="black", ax=ax, legend=False,
    )
    ax.set_title("Feature Attribution via TreeSHAP (Signal vs Synthetic Decoys)", fontsize=12, fontweight="bold")
    ax.set_xlabel("Mean |SHAP Value|", fontsize=10)
    plt.tight_layout()
    fig_dir = outdir / "docs"
    fig_dir.mkdir(parents=True, exist_ok=True)
    fig.savefig(fig_dir / "Figure1_SHAP.png", dpi=300)
    plt.close(fig)
    return imp_df


def write_environment_manifest(outdir: Path) -> None:
    packages = {}
    for name in ["numpy", "pandas", "scikit-learn", "xgboost", "shap", "matplotlib", "seaborn"]:
        try:
            packages[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            packages[name] = None
    manifest = {
        "python": sys.version,
        "platform": platform.platform(),
        "packages_this_run": packages,
        "note": "Manifest records the environment executing this script, not a recovered full freeze from the historic Colab runtime.",
    }
    (outdir / "environment.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", default="outputs", help="Directory for regenerated results (default: outputs)")
    args = parser.parse_args()
    outdir = Path(args.output_dir).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    library = load_substrate_library()

    print("[1/4] Running 20-seed CV and SVR ablation (this recomputes metrics; no existing log is reused).")
    df_logs = run_cross_validation(library)
    oracle = compute_oracle_metrics(library)
    df_logs = df_logs.merge(oracle, on="Seed", how="inner", validate="one_to_one")
    col_order = ["Seed", *METRIC_COLUMNS, "ORACLE_MAE", "ORACLE_R2"]
    df_logs = df_logs[col_order]
    df_logs.to_csv(outdir / "20_seed_metrics_log.csv", index=False)

    metrics_summary = []
    for col in df_logs.columns:
        if col == "Seed":
            continue
        metrics_summary.append({
            "Metric": col,
            "Mean": df_logs[col].mean(),
            "Sample_SD": df_logs[col].std(ddof=1),
        })
    pd.DataFrame(metrics_summary).to_csv(outdir / "metrics_summary.csv", index=False)

    print("[2/4] Regenerating Seed 42 reference dataset and GPI top ten.")
    df_ref = generate_reference_dataset(library)
    df_ref.to_csv(outdir / "synthetic_benchmark_dataset.csv", index=False)
    gpi_top10 = df_ref.sort_values(by="Norm_GPI", ascending=False).head(10).reset_index(drop=True)
    gpi_top10.to_csv(outdir / "gpi_top10.csv", index=False)

    print("[3/4] Fitting reference XGBoost model and computing TreeSHAP.")
    compute_shap_and_plot(df_ref, outdir)
    write_environment_manifest(outdir)

    print("[4/4] Finished. Outputs written to:", outdir)
    print("\nMetrics summary (mean ± sample SD across seed-level fold averages):")
    summary = pd.DataFrame(metrics_summary)
    for _, row in summary.iterrows():
        print(f"{row['Metric']}: {row['Mean']:.3f} ± {row['Sample_SD']:.3f}")
    print("\nTop 10 GPI reaction IDs:", ", ".join(gpi_top10["RXN_ID"].tolist()))


if __name__ == "__main__":
    main()
