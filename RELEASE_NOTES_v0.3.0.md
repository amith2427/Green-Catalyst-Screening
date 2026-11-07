# Green Catalyst Screening v0.3.0 — published

## Archive identifiers and project links

- **Zenodo v0.3.0 version DOI:** [10.5281/zenodo.24032491](https://doi.org/10.5281/zenodo.24032491)
- **Zenodo project concept DOI:** [10.5281/zenodo.23383768](https://doi.org/10.5281/zenodo.23383768)
- Zenodo v0.2.0 archive: [10.5281/zenodo.23388862](https://doi.org/10.5281/zenodo.23388862)
- Zenodo v0.1.0 archive: [10.5281/zenodo.23383769](https://doi.org/10.5281/zenodo.23383769)
- GitHub repository: [amith2427/Green-Catalyst-Screening](https://github.com/amith2427/Green-Catalyst-Screening)

The v0.3.0 DOI identifies this exact archived version. The concept DOI identifies the project across versions.

## Included in the Zenodo v0.3.0 archive

- Final main manuscript PDF (16 pages) and supplementary-information PDF (2 pages).
- `synthetic_benchmark_dataset.csv`: Seed 42 reference dataset (5,000 rows × 13 columns).
- `20_seed_metrics_log.csv`: 20-seed metrics and TreeSHAP log (20 rows × 34 columns; seeds 42–61).
- `supplementary_experiments_log.csv`: positive-control and learning-curve log (47 data rows × 12 columns).
- `reproduce_benchmark.py`, `substrates.csv`, and `requirements.txt`.
- Citation references, checksums, licensing notices, and traceability documentation.

## GitHub synchronization

The three current CSVs and the reproduction source files are present on GitHub `main`. The final manuscript and SI PDFs are included in the Zenodo archive but the earlier PDF binaries in the GitHub repository have not been replaced because the connected GitHub write interface did not provide a working binary upload operation.

The GitHub `v0.3.0` tag/release is a separate marker from the Zenodo version and should point to the final repository commit.

## Scientific scope and reproducibility

All benchmark reactions and target values are synthetic. The results are traceable and consistency-checked, but an independent complete clean rerun has not completed successfully; see `TRACEABILITY_REPORT.md`. TreeSHAP results are illustrative for one fitted Seed 42 model, and the Green Performance Index is an author-defined heuristic rather than a validated sustainability metric.

## Licensing

Python source code: MIT. Synthetic datasets and written documentation: CC BY 4.0. Third-party dependencies retain their respective licenses.
