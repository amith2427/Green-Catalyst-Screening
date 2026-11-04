# An Interpretable Chemoinformatics Benchmark for Evaluating Machine Learning Frameworks, Decoy Sensitivity, and Green Catalyst Prioritization

[![DOI](https://zenodo.org/badge/1419940824.svg)](https://doi.org/10.5281/zenodo.23383768)

This repository contains code and synthetic data accompanying the manuscript listed below. It examines regression-model performance, validation protocols, sensitivity to non-causal decoy descriptors, TreeSHAP attribution, and an illustrative Green Performance Index (GPI) in a controlled synthetic catalytic alcohol-oxidation benchmark.

**Scope limitation:** every reaction, yield, selectivity score, and sustainability score in the benchmark is synthetic. The benchmark is a methodological testbed, not experimental evidence, a validated prediction of real catalyst performance, or a validated sustainability assessment.

## Associated manuscript and supplementary information

**Main manuscript**

Pennada, Gagan Sai Amith. *An Interpretable Chemoinformatics Benchmark for Evaluating Machine Learning Frameworks, Decoy Sensitivity, and Green Catalyst Prioritization.* Manuscript, School of Computer Science and Engineering, VIT-AP University, India.

**Supplementary information**

Pennada, Gagan Sai Amith. *Supplementary Information for “An Interpretable Chemoinformatics Benchmark for Evaluating Machine Learning Frameworks, Decoy Sensitivity, and Green Catalyst Prioritization”.* VIT-AP University, India.

The manuscript and supplementary information do not have separate DOIs identified in the supplied files. The Zenodo concept DOI below identifies the archived software/data project, not a separately published paper DOI.

## Repository contents

- **`synthetic_benchmark_dataset.csv`** — the 5,000-row Seed 42 synthetic reference dataset (13 columns).
- **`20_seed_metrics_log.csv`** — the archived 20-seed metrics and TreeSHAP log (seeds 42–61).
- **`reproduce_benchmark.py`** — the reproduction script for the benchmark and reported analyses.
- **`substrates.csv`** — the 22-substrate SMILES and fixed exact-mass library.
- **`requirements.txt`** — Python dependencies.
- **`TRACEABILITY_REPORT.md`, `notebook_cell_trace.csv`, and `notebook_source_manifest.json`** — execution-path and artifact traceability documentation.
- **`LICENSE` and `LICENSE-DATA.md`** — the software and data/documentation licensing terms.

## Running the reproduction script

With Python installed, run:

```bash
python -m pip install -r requirements.txt
python reproduce_benchmark.py --output-dir outputs
```

The script recomputes the model-evaluation suite rather than silently reusing the archived metrics log. See the traceability report for the status and limitations of the archived artifacts.

## Interpreting the results

The target yield is generated from specified catalyst and oxidant baselines, exact substrate mass, temperature, and random noise. The decoy features are independently sampled synthetic variables and are not intended to represent chemically meaningful predictors.

The TreeSHAP analysis is an interpretation of fitted models in this synthetic benchmark; it does not establish causal relationships. The GPI is an author-defined heuristic for the demonstration, not a validated sustainability metric.

## Reproducibility status

The archived Seed 42 dataset-generation logic and 20-seed metrics have been checked for consistency with the manuscript summary statistics. However, the saved notebook execution reused an existing metrics log rather than rerunning the complete cross-validation suite, and an independent clean run of the full suite has not yet completed successfully. The results should therefore be described as traceable and consistency-checked, not independently reproduced in a clean environment.

## Zenodo archive and versioning

The Zenodo **concept DOI** is [10.5281/zenodo.23383768](https://doi.org/10.5281/zenodo.23383768). It is the stable project-level DOI intended to resolve to the latest archived version.

The DOI for the initial preliminary **v0.1.0** release is [10.5281/zenodo.23383769](https://doi.org/10.5281/zenodo.23383769). Use a version-specific DOI when citing a particular archived release; use the concept DOI when referring to the project across versions.

The previous **v0.2.0** release records the earlier project/manuscript metadata. The final manuscript and supplementary-information files supplied on 4 November 2026 have a different title and are not byte-identical to the PDFs currently stored in the repository. The uploaded 20-seed metrics CSV also differs from the current repository copy. These final files, the revised dataset/logs, and the positive-control/learning-curve log must be synchronized before publishing a new Zenodo version. In particular, `supplementary_experiments_log.csv` is referenced by the manuscript and SI but is not currently present in this GitHub repository or among the files supplied in the latest upload.

The next archive should be published as a new version rather than altering the files of a previously published version. Zenodo's versioning guidance explains that file updates belong in a new version, with a new version-specific DOI and the same concept DOI: [Zenodo versioning documentation](https://help.zenodo.org/docs/deposit/manage-versions/).

## Licenses

The Python source code is provided under the MIT License. The synthetic dataset files and written documentation are provided under CC BY 4.0, as described in `LICENSE-DATA.md`. Third-party dependencies remain subject to their own licenses.

Thank you for exploring this work. The benchmark is intended as a transparent methodological example for studying machine-learning behavior and the limits of computational conclusions.
