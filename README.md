# Synthetic Chemoinformatics Testbed

This repository is being initialized for the preliminary computational technical note:

**A Synthetic Chemoinformatics Testbed for Evaluating Model Interpretability and Green Catalyst Prioritization**

Author: Gagan Sai Amith Pennada, VIT-AP University.

## Scope

The project contains a synthetic benchmark of 5,000 catalytic alcohol-oxidation reactions and a 20-seed evaluation comparing Linear Regression, XGBoost, Random Forest, and RBF-SVR. The data-generating process is an additive synthetic heuristic, not a model of experimentally validated catalyst performance.

## Reproducibility status

This repository is being prepared from the final Google Colab notebook and associated outputs. The notebook contains older experimental cells as well as the final pipeline. Before claiming fully independent reproducibility, a clean run of the full 20-seed cross-validation must complete successfully.

The primary result-generation path identified so far is:
- Cell 125: full 20-seed / five-fold model evaluation and SVR decoy ablation.
- Cell 131: finalization path that reuses an existing metrics log when present, adds oracle metrics, regenerates the Seed 42 dataset, computes TreeSHAP and GPI outputs, and builds manuscript source/PDF outputs.

Please consult the traceability report and reproduction script in this repository for exact details and limitations.

## Files

Files will be added in subsequent commits:
- Dataset (Seed 42): `synthetic_benchmark_dataset.csv`
- Metrics log: `20_seed_metrics_log.csv`
- Final manuscript and supplementary information
- Reproduction script and traceability report

## Data and code availability

The Zenodo record / DOI is not yet verified or established for this release. A DOI will be added here only after the record is published and checked.

## Limitations

- All reactions and labels are synthetic.
- Substrate identity affects the target through exact monoisotopic mass without substrate-specific random effects.
- Decoy columns are independently sampled uniform noise.
- The SVR ablation is limited to the stated untuned configuration.
- Seed 42 TreeSHAP analysis is illustrative and does not demonstrate cross-seed attribution stability.
- The GPI is an author-defined illustrative decision heuristic, not a validated sustainability metric.
