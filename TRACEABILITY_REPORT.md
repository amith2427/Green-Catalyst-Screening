# Traceability and validation report

## Notebook execution path

The reviewed `Chem_Re (1).ipynb` has 132 cells. The relevant path is **cell 125 → cell 131**, with cell 128 as an intermediate finalization pass and cells 129–130 limited to wording/layout.

- **Cell 125 (execution count 2)** ran the 20-seed validation/ablation loop for seeds 42–61, wrote `20_seed_metrics_log.csv`, generated the Seed 42 reference dataset, computed SHAP, and wrote LaTeX. PDF compilation failed afterward because `pdflatex` was unavailable.
- **Cell 128 (execution count 5)** explicitly reused an existing CV log, skipped the slow CV loop, added/recomputed oracle metrics, and refreshed other outputs.
- **Cell 131 (execution count 8)** is the final comprehensive result-generation/build cell. It contains a CV fallback if the log is absent/incomplete. In its saved execution, it found the existing metrics log and updated oracle columns rather than rerunning CV; it regenerated Seed 42 data, SHAP/GPI outputs and manuscript PDFs.

## Data and metric consistency

The latest uploaded Seed 42 dataset was compared against a direct reimplementation of the final cell's random-draw order and formulas:

- Both datasets contained 5,000 rows and 13 columns.
- Reaction IDs, substrate/catalyst/oxidant indices and exact-mass values matched exactly.
- Continuous values differed by no more than approximately 1.42e-14 due to floating-point representation.
- GPI top-ten order and rounded scores matched the manuscript table.

The uploaded 20-seed metrics log had 20 rows for seeds 42–61; aggregating seed-level scores with sample standard deviation (ddof=1) matched the manuscript's Tables 1–2 to three decimals.

**This is traceability/consistency checking, not a fresh independent rerun of the complete model suite.** A local run of the consolidated script timed out during the SVR fits. Until the full script finishes in a clean environment, do not claim full independent reproducibility.

## Modeling and interpretation caveats

All reactions and targets are synthetic. Substrate mass enters the yield formula without substrate-specific random effects; decoy features are independent uniform random variables. The Seed 42 TreeSHAP analysis explains one fitted reference model and does not establish causal validity or cross-seed attribution stability. GPI is an author-defined illustrative decision heuristic, not an experimentally validated sustainability metric.

## Publication status

The original notebook hard-coded a GitHub URL and Zenodo DOI without verifying either destination. This repository is now accessible and has been initialized, but the manuscript PDFs still contain unverified public-availability claims. No Zenodo record has been published or verified in this workflow. Do not cite a Zenodo DOI or treat those PDFs as archive-ready until the record exists and the manuscript links have been updated.
