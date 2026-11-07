# An Interpretable Chemoinformatics Benchmark for Evaluating Machine Learning Frameworks, Decoy Sensitivity, and Green Catalyst Prioritization

[![Zenodo concept DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23383768.svg)](https://doi.org/10.5281/zenodo.23383768)

## Official project links

- **GitHub repository:** [amith2427/Green-Catalyst-Screening](https://github.com/amith2427/Green-Catalyst-Screening)
- **Latest Zenodo archive (v0.3.0):** [10.5281/zenodo.24032491](https://doi.org/10.5281/zenodo.24032491)
- **Zenodo project record (concept DOI):** [10.5281/zenodo.23383768](https://doi.org/10.5281/zenodo.23383768)
- **Zenodo v0.2.0 archive:** [10.5281/zenodo.23388862](https://doi.org/10.5281/zenodo.23388862)
- **Zenodo v0.1.0 archive:** [10.5281/zenodo.23383769](https://doi.org/10.5281/zenodo.23383769)

The version-specific DOI identifies the exact v0.3.0 archive. The concept DOI identifies the project across versions and resolves to the latest published version. The Zenodo record is not a separate DOI for the manuscript.

This repository contains code and synthetic data accompanying the manuscript below. It examines model performance, cross-validation, sensitivity to non-causal decoy descriptors, TreeSHAP attribution, and an illustrative Green Performance Index (GPI) in a synthetic catalytic alcohol-oxidation benchmark.

**Scope:** all reactions and target values are synthetic. This is a methodological testbed, not experimental evidence, a validated prediction of real catalyst performance, or a validated sustainability assessment.

## Companion documents

**Main manuscript:** Pennada, Gagan Sai Amith. *An Interpretable Chemoinformatics Benchmark for Evaluating Machine Learning Frameworks, Decoy Sensitivity, and Green Catalyst Prioritization.* School of Computer Science and Engineering, VIT-AP University, India. Final PDF supplied 4 November 2026.

**Supplementary information:** Pennada, Gagan Sai Amith. *Supplementary Information: An Interpretable Chemoinformatics Benchmark for Evaluating Machine Learning Frameworks, Decoy Sensitivity, and Green Catalyst Prioritization.* VIT-AP University, India. Final PDF supplied 4 November 2026.

No separate manuscript or SI DOI is identified in the supplied files. The Zenodo concept DOI above identifies the supporting project, not a separate paper DOI. See [PUBLICATION_REFERENCES.md](PUBLICATION_REFERENCES.md).

## Repository contents

- [`synthetic_benchmark_dataset.csv`](https://github.com/amith2427/Green-Catalyst-Screening/blob/main/synthetic_benchmark_dataset.csv) — Seed 42 reference dataset (5,000 synthetic reactions; 13 columns).
- [`20_seed_metrics_log.csv`](https://github.com/amith2427/Green-Catalyst-Screening/blob/main/20_seed_metrics_log.csv) — per-seed metrics and TreeSHAP log (seeds 42–61; 20 rows; 34 columns).
- [`supplementary_experiments_log.csv`](https://github.com/amith2427/Green-Catalyst-Screening/blob/main/supplementary_experiments_log.csv) — positive-control substrate-effect runs (40 rows across σsub = 0, 4, 8, 12 for seeds 42–51) and Seed 42 learning curves (7 train sizes from 200 to 4,000; 47 data rows, 12 columns).
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

## Zenodo archive and versions

The v0.3.0 archive was published on 7 November 2026 and has the version-specific DOI [10.5281/zenodo.24032491](https://doi.org/10.5281/zenodo.24032491). The project concept DOI is [10.5281/zenodo.23383768](https://doi.org/10.5281/zenodo.23383768); it identifies the project across versions. Earlier version DOIs are [v0.2.0: 10.5281/zenodo.23388862](https://doi.org/10.5281/zenodo.23388862) and [v0.1.0: 10.5281/zenodo.23383769](https://doi.org/10.5281/zenodo.23383769).

The published v0.3.0 ZIP contains the final main manuscript PDF, supplementary-information PDF, all three CSV files, the reproduction script, substrate library, dependency specifications, citation references, checksums, and license/traceability documentation. The three latest CSVs and source files are synchronized on GitHub. The final PDFs supplied on 4 November 2026 are archived in Zenodo, but have **not** replaced the earlier PDF files in this GitHub repository because the available GitHub write interface did not provide a working binary-PDF upload operation.

Cite the v0.3.0 version DOI when referring to this exact archive; cite the concept DOI when referring to the project across versions. The matching GitHub tag/release `v0.3.0` is a separate GitHub step and should point to the final repository commit.

## Licenses

Code: MIT. Synthetic data and written documentation: CC BY 4.0, as described in `LICENSE-DATA.md`. Third-party dependencies retain their own licenses.
