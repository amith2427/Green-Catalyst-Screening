# Synthetic Chemoinformatics Testbed

**Status: code, data, and traceability artifacts are published. The archival DOI release and final manuscript PDFs are not yet complete.**

This repository supports the preliminary computational technical note **“A Synthetic Chemoinformatics Testbed for Evaluating Model Interpretability and Green Catalyst Prioritization.”** The benchmark is entirely synthetic and must not be interpreted as experimental chemistry evidence.

## Contents

- `synthetic_benchmark_dataset.csv` — 5,000-row Seed 42 dataset (13 columns) with synthetic yield, decoy features, selectivity/sustainability scores, and GPI score.
- `reproduce_benchmark.py` — consolidated script to recompute 20-seed random/grouped CV, SVR decoy ablation, oracle metrics, reference dataset, GPI top ten, TreeSHAP output, and environment manifest.
- `substrates.csv` — 22 substrate SMILES and fixed two-decimal exact-mass values.
- `20_seed_metrics_log.csv` — archived per-seed metrics (seeds 42–61) corresponding to the manuscript summary tables.
- `requirements.txt` — Python dependencies.
- `notebook_cell_trace.csv`, `notebook_source_manifest.json`, and `TRACEABILITY_REPORT.md` — notebook lineage and validation caveats.

## Reproduce

Use Python with the listed dependencies installed, then run:

```bash
python -m pip install -r requirements.txt
python reproduce_benchmark.py --output-dir outputs
```

The full cross-validation is computationally intensive. The script recomputes the model suite instead of silently reusing the archived metrics log. Generated files include `outputs/20_seed_metrics_log.csv`, `outputs/synthetic_benchmark_dataset.csv`, `outputs/gpi_top10.csv`, `outputs/shap_importance.csv`, `outputs/docs/Figure1_SHAP.png`, and `outputs/environment.json`.

## Traceability and limits

The reviewed notebook has 132 cells. Cell 125's recorded execution ran the full 20-seed CV loop. The latest finalization cell, 131, found an existing metric log and did not rerun CV during that recorded execution; it regenerated the Seed 42 dataset and SHAP/GPI outputs. The uploaded CSV's generation logic and archived metric summary were checked for consistency. A separate clean run of the full CV suite has **not** yet completed successfully in this environment, so the archived results are traceable but not independently reproduced here.

- Labels and reactions are synthetic.
- Substrate identity affects the target through exact mass; no substrate-specific random effects are modeled.
- Decoy features are independent uniform draws.
- Seed 42 TreeSHAP results are illustrative for one fitted model, not evidence of causal validity or attribution stability across seeds.
- GPI is an author-defined heuristic, not a validated sustainability metric.

## Publication / DOI status

This repository is public. No Zenodo record has been created or verified as part of this workflow. **Do not cite a Zenodo DOI yet.** The manuscript PDFs are not included because their public-availability links must be updated and verified after an archive record is published.
