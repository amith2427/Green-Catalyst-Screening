# A Synthetic Chemoinformatics Testbed for Catalyst Prioritization

[![DOI](https://zenodo.org/badge/1419940824.svg)](https://doi.org/10.5281/zenodo.23383768)

Welcome, and thank you for visiting this repository.

I developed this project to explore how common machine-learning models behave on a controlled, synthetic benchmark of catalytic alcohol oxidation. It accompanies my preliminary computational technical note, **“A Synthetic Chemoinformatics Testbed for Evaluating Model Interpretability and Green Catalyst Prioritization.”**

**Important scope note:** every reaction and target in this benchmark is synthetic. The benchmark is for computational testing and methodological demonstration; it is not experimental evidence or a validated prediction of real catalyst performance.

## Repository contents

- **`synthetic_benchmark_dataset.csv`** — 5,000 synthetic reactions from the Seed 42 reference dataset, including reaction features, generated yield targets, decoy variables, and illustrative selectivity, sustainability, and GPI scores.
- **`20_seed_metrics_log.csv`** — archived seed-level evaluation metrics for seeds 42–61.
- **`reproduce_benchmark.py`** — consolidated script intended to regenerate the dataset and result outputs, run the 20-seed cross-validation suite, compare SVR with and without decoy features, and calculate oracle metrics and SHAP/GPI results.
- **`substrates.csv`** — the 22 substrate SMILES and fixed exact-mass values used by the benchmark.
- **`requirements.txt`** — Python dependencies.
- **`TRACEABILITY_REPORT.md`, `notebook_cell_trace.csv`, and `notebook_source_manifest.json`** — documentation of the notebook execution path, artifact checks, and validation limitations.
- **`LICENSE` and `LICENSE-DATA.md`** — licensing terms for the software and data/documentation, respectively.

## Running the reproduction script

With Python installed, run:

```bash
python -m pip install -r requirements.txt
python reproduce_benchmark.py --output-dir outputs
```

The complete cross-validation suite may take some time to run. The script recomputes the model-evaluation suite rather than silently reusing the archived metrics log. Its output directory is expected to contain regenerated metrics and dataset files, the GPI top-ten table, SHAP importance output and figure, and an environment manifest.

## Interpreting the results

The target yield is generated from fixed catalyst and oxidant baselines, exact substrate mass, temperature, and random noise. Decoy features are independently sampled synthetic variables and are not intended to represent chemically meaningful predictors.

The TreeSHAP analysis illustrates feature attribution for one fitted Seed 42 reference model. It does not establish causal relationships or attribution stability across random seeds. The Green Prioritization Index (GPI) is an author-defined heuristic for this demonstration, not a validated sustainability metric.

## Reproducibility status

I checked the Seed 42 dataset-generation logic against the final notebook formulas and verified that the archived 20-seed metrics reproduce the manuscript summary statistics to three decimal places. However, the saved final notebook execution reused an existing metrics log rather than rerunning the complete cross-validation suite, and a separate clean run of the full suite has not yet completed successfully in my validation environment. I therefore describe the results as traceable and consistency-checked, not independently reproduced in a clean environment.

## Citation and archival versions

The Zenodo **concept DOI** is [10.5281/zenodo.23383768](https://doi.org/10.5281/zenodo.23383768). It is the stable project-level DOI intended to lead readers to the latest archived version.

The DOI for the initial preliminary **v0.1.0** release is [10.5281/zenodo.23383769](https://doi.org/10.5281/zenodo.23383769). Use the version-specific DOI when citing that exact release; use the concept DOI when referring to the project across versions.

The GitHub release is [v0.1.0 — Preliminary Synthetic Benchmark Release](https://github.com/amith2427/Green-Catalyst-Screening/releases/tag/v0.1.0). The DOI-linked manuscript and supplementary-information PDFs are being prepared for the next complete release.

## Licenses

The Python source code is provided under the MIT License. The synthetic dataset files and written documentation are provided under CC BY 4.0, as described in `LICENSE-DATA.md`. Third-party dependencies remain subject to their own licenses.

Thank you for exploring this work. I hope it is useful as a transparent example of a synthetic benchmark for studying machine-learning performance, interpretability, and the limits of computational conclusions.
