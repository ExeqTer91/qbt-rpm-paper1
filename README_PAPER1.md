# Paper 1 — Computational Package

Canonical v3 reproducibility package (post round-2 audit). This repository was originally assembled for a PCCP submission; it is now used as the public code/data/figure archive supporting a Journal of the Royal Society Interface submission. Legacy PCCP-specific files are retained for provenance only.

**Title:** Ratio-dependent response structure in a reduced radical-pair model of magnetoreception

**Author:** Andrei-Sebastian Ursachi, Independent Researcher (ORCID: 0009-0002-6114-5011)

**Current status:** Initial submission to *Journal of the Royal Society Interface* prepared/submitted in May 2026. The computational outputs, final figures, manuscript-supporting audit tables, and reproducibility infrastructure are frozen for review. A Zenodo DOI and final release tag are pending.

---

## What is this package

This is the complete computational package supporting Paper 1. It contains:

- the rebuilt v3 simulation code (`src/v3/`)
- raw NPZ outputs from all simulation sweeps (`results_v3/`)
- final figures for the manuscript at 600 dpi LZW TIFF + 300 dpi PNG (`figures_paper1_final/`)
- the manuscript and supporting audit documents (`docs_v3/`)
- the figure-generation script (`src/v3/figures/generate_paper1_figures.py`)
- a SHA256 manifest of every NPZ read and every figure written (`figures_paper1_final/figure_manifest.txt`)
- a figure-data mapping CSV (`docs_v3/PAPER1_FIGURE_DATA_MAP.csv`)
- a claim-support table mapping empirical claims to data sources (`docs_v3/claim_support_table_paper1.md`)
- a release-notes draft (`RELEASE_NOTES_PAPER1_DRAFT.md`)
- a Paper 1 → Paper 2 handoff document (`docs_v3/PAPER1_TO_PAPER2_HANDOFF.md`)
- a git status note (`docs_v3/PAPER1_GIT_STATUS.md`)

The package is designed to be auditable end-to-end: every numerical claim in the manuscript is supported by a specific NPZ file and a specific array key, all recorded in `PAPER1_FIGURE_DATA_MAP.csv` and `claim_support_table_paper1.md`.

---

## Journal-submission note

The same frozen v3 computational archive supports the retargeted *Journal of the Royal Society Interface* version of the manuscript. The journal framing changed from a physical-chemistry submission to a physical/life-sciences interface submission, but the numerical results, figures, raw outputs, validation tests, and claim-support boundaries are unchanged.

For the Interface submission, the work should be read as a reproducible computational biophysics baseline for radical-pair magnetoreception: a reduced spin-dynamical model that maps physical spin dynamics into orientation-dependent chemical yield readouts relevant to biological compass models.

---

## Reproduction

### Requirements

- Python 3.10+
- numpy, scipy, matplotlib, joblib, Pillow

### Reproducing the figures from existing NPZ outputs

```bash
PAPER1_RESULTS_DIR=./results_v3 \
PAPER1_FIG_OUT=./figures_paper1_final \
python3 src/v3/figures/generate_paper1_figures.py
```

The script reads only the NPZ files listed in `docs_v3/PAPER1_FIGURE_DATA_MAP.csv`, generates 600 dpi LZW TIFF + PNG previews for Figures 1–4, and writes a SHA256 manifest. Figure SHA256 hashes match those in `figures_paper1_final/figure_manifest.txt` if the underlying NPZ files are unchanged.

### Reproducing the NPZ outputs from source

```bash
python3 -m src.v3.run_all_v3
```

This runs the full pipeline: pre-flight calibration → ratio scans → kinetic scaling → exchange sweep → noise sweeps → spectral diagnostics → orientation maps. Total runtime depends on CPU count; on a 24-core node, ~30 minutes.

### Pre-flight calibration

Before any production run, the pre-flight calibration verifies the implementation:

- isotropic-hyperfine control: α at numerical precision (2.22e-16)
- axial-hyperfine control: α ≈ 1.08e-04 nonzero
- legacy v2/v3 agreement: max difference 0.0 (bit-identical)
- Haberkorn yield closure: 8.88e-16
- absorbing-product channel total conservation: 4.33e-15
- finite-time vs linear-solve spot checks: worst δY_S = 2.86e-12

All six tests must pass before any sweep is considered valid.

---

## What the package does NOT contain

- the published paper PDF (to be added only if/when accepted)
- a final Zenodo DOI (pending)
- a final archival release tag (pending)
- the toy yield-transducer or 3D-geometry exploratory work (these belong to Paper 2; see `PAPER1_TO_PAPER2_HANDOFF.md`)

---

## Important conventions

- Plot legends and figure labels use **"absorbing-product effective"** in place of "Lindblad" because the implemented `build_lindblad` function returns the same Liouvillian as `build_haberkorn` for the radical-pair sector. This is documented explicitly in the manuscript (§2.7), in the claim support table (claim 7), and in the `removed_or_softened_claims_paper1.md` log.
- The noise channel labels are: **z-dephasing on both electron spins** and **single-electron spin-flip relaxation**. The spin-flip relaxation channel is implemented only on electron 1 (S1+, S1-). Both are documented in the manuscript Methods §2.8 and in the claim support table.
- All Hamiltonian parameters are nondimensionalized by A∥ = 1.0; A⊥ = 0.5; B = 0.05 (geomagnetic regime).

---

## Citation

When citing this work prior to formal publication, please cite the repository/archive:

> Ursachi, A.-S. (2026). Ratio-dependent response structure in a reduced radical-pair model of magnetoreception (computational package, v3 reproducibility archive). GitHub repository: https://github.com/ExeqTer91/qbt-rpm-paper1. Archival DOI pending.

---

## Contact

Andrei-Sebastian Ursachi
Independent Researcher
Diepholz, Germany
contact@andreiursachi.eu
ORCID: 0009-0002-6114-5011
