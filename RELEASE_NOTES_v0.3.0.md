# Proposed v0.3.0 release notes — NOT PUBLISHED

## Project links

- GitHub repository: [amith2427/Green-Catalyst-Screening](https://github.com/amith2427/Green-Catalyst-Screening)
- Existing Zenodo project record (concept DOI): [10.5281/zenodo.23383768](https://doi.org/10.5281/zenodo.23383768)
- Preliminary v0.1.0 archive DOI: [10.5281/zenodo.23383769](https://doi.org/10.5281/zenodo.23383769)
- Zenodo versioning guide: [Create a new version](https://help.zenodo.org/docs/deposit/manage-versions/)

## Synchronized on GitHub

- `synthetic_benchmark_dataset.csv`: supplied final Seed 42 dataset (5,000 rows × 13 columns).
- `20_seed_metrics_log.csv`: supplied final 20-seed metrics and TreeSHAP log (20 rows × 34 columns; seeds 42–61).
- `supplementary_experiments_log.csv`: supplied positive-control and learning-curve log (47 data rows × 12 columns: 40 positive-control observations and 7 Seed 42 learning-curve observations).
- `README.md`: direct GitHub and Zenodo project links, repository contents, and v0.3.0 upload instructions.
- `PUBLICATION_REFERENCES.md`: companion manuscript/SI references and archive synchronization status.
- `.zenodo.json`: proposed v0.3.0 metadata with related links to the GitHub repository and existing Zenodo concept DOI.
- `CITATION.cff`: software citation and existing project concept DOI.

## Final PDFs supplied but not yet synchronized to GitHub

- `main_manuscript_final.pdf` — 16 pages.
- `supplementary_info_final.pdf` — 2 pages.

The available GitHub write interface did not provide a working binary-file upload operation; the earlier PDF files remain in the repository. The final PDFs are included in the proposed v0.3.0 ZIP upload package.

## Zenodo upload and publication

The proposed v0.3.0 ZIP is intended to be uploaded as a single file to a **new version** of the existing [Zenodo project record](https://doi.org/10.5281/zenodo.23383768). Use the `.zenodo.json` included in the ZIP as a reference when entering or confirming the deposit metadata. The metadata file inside the ZIP does not itself create or publish a Zenodo deposit.

No v0.3.0 record/version has been uploaded or published, and no new version DOI has been assigned. The existing project concept DOI remains [10.5281/zenodo.23383768](https://doi.org/10.5281/zenodo.23383768). After uploading the ZIP, check its filename and metadata, publish the new version, and then update this file and `CITATION.cff` with the DOI assigned by Zenodo.

## Scientific scope

All benchmark reactions and target values are synthetic. The results are traceable and consistency-checked, but an independent complete clean rerun has not completed successfully; see `TRACEABILITY_REPORT.md`.
