# An Interpretable Chemoinformatics Benchmark for Evaluating Machine Learning Frameworks, Decoy Sensitivity, and Green Catalyst Prioritization

[![DOI](https://zenodo.org/badge/1419940824.svg)](https://doi.org/10.5281/zenodo.23383768)

This repository contains code and synthetic data accompanying the manuscript below. It examines model performance, cross-validation, sensitivity to non-causal decoy descriptors, TreeSHAP attribution, and an illustrative Green Performance Index (GPI) in a synthetic catalytic alcohol-oxidation benchmark.

**Scope:** all reactions and target values are synthetic. This is a methodological testbed, not experimental evidence, a validated prediction of real catalyst performance, or a validated sustainability assessment.

## Companion documents

**Main manuscript:** Pennada, Gagan Sai Amith. *An Interpretable Chemoinformatics Benchmark for Evaluating Machine Learning Frameworks, Decoy Sensitivity, and Green Catalyst Prioritization.* School of Computer Science and Engineering, VIT-AP University, India. Final PDF supplied 4 November 2026.

**Supplementary information:** Pennada, Gagan Sai Amith. *Supplementary Information: An Interpretable Chemoinformatics Benchmark for Evaluating Machine Learning Frameworks, Decoy Sensitivity, and Green Catalyst Prioritization.* VIT-AP University, India. Final PDF supplied 4 November 2026.

No separate manuscript or SI DOI is identified in the supplied files. The Zenodo concept DOI below identifies the supporting project, not a separate paper DOI. See [PUBLICATION_REFERENCES.md](PUBLICATION_REFERENCES.md).

## Repository contents

- `synthetic_benchmark_dataset.csv` — Seed 42 reference data (5,000 synthetic reactions; 13 columns), updated from the 4 November 2026 upload.
- `20_seed_metrics_log.csv` — per-seed metrics and TreeSHAP log (seeds 42–61; 20 rows; 34 columns), updated from the 4 November 2026 upload.
- `reproduce_benchmark.py` — reproduction script.
- `substrates.csv` — 22-substrate SMILES and exact-mass library.
- `requirements.txt` — Python dependencies.
- `TRACEABILITY_REPORT.md`, `notebook_cell_trace.csv`, `notebook_source_manifest.json` — execution and artifact traceability.
- `PUBLICATION_REFERENCES.md`, `RELEASE_NOTES_v0.3.0.md` — companion citations and release status.
- `LICENSE`, `LICENSE-DATA.md` — software and data/documentation licensing.

## Run

```bash
python -m pip install -r requirements.txt
python reproduce_benchmark.py --output-dir outputs
```

The script recomputes the evaluation suite. See the traceability report for known limitations.

## Interpretation and reproducibility

The target yield follows a specified synthetic data-generating process. Decoy features are independently sampled synthetic variables. TreeSHAP does not establish causal relationships. The GPI is an author-defined heuristic, not a validated sustainability metric.

The Seed 42 generation logic and archived metrics were checked for consistency with manuscript summary statistics. The saved notebook reused an existing metrics log rather than rerunning the complete CV suite, and a separate independent clean run has not completed successfully. Results are traceable and consistency-checked, not independently reproduced in a clean environment.

## Zenodo

The project concept DOI is [10.5281/zenodo.23383768](https://doi.org/10.5281/zenodo.23383768). The preliminary v0.1.0 version DOI is [10.5281/zenodo.23383769](https://doi.org/10.5281/zenodo.23383769). Cite the version DOI for a specific archived version and the concept DOI for the project across versions.

The existing v0.2.0 archive is historical. The two CSVs listed above have been updated on GitHub. The final manuscript and SI PDFs supplied on 4 November 2026 have **not** replaced the earlier PDFs currently in the repository; the available GitHub write interface did not provide a usable binary upload operation in this update.

The manuscript and SI refer to `supplementary_experiments_log.csv` (positive-control and learning-curve results, SI section S3). That CSV was not among the supplied files and was not found in the searchable file library. It has not been recreated. Before publishing a new Zenodo version, add the final PDFs and that CSV, or revise the documents so they accurately describe the deposited contents. `.zenodo.json` is prepared metadata only; no new Zenodo version has been uploaded or published.

Zenodo requires a new version for updates to a published archive. See [Zenodo versioning documentation](https://help.zenodo.org/docs/deposit/manage-versions/).

## Licenses

Code: MIT. Synthetic data and written documentation: CC BY 4.0, as described in `LICENSE-DATA.md`. Third-party dependencies retain their own licenses.
