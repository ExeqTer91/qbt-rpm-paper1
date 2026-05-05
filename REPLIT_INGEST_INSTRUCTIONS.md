# Paper 1 Repo Ingest Instructions

This bundle contains the complete v3 Paper 1 computational package, ready for Git ingestion into a NEW repo (`paper1-rpm-radical-pair` or similar).

## Critical context

This is NOT an addition to the old paper repo. The OLD repo contains the previous (withdrawn) paper iteration with A1-A4 CSVs, toy_yield_transducer, and toy_3d_geometry data. That repo should be renamed for Paper 2 use; this Paper 1 bundle goes into a fresh repo.

## What to do

1. Create a new GitHub repo: `paper1-rpm-radical-pair` (or preferred name).
2. Initialize on branch `paper1/final-computational-package`.
3. Copy ALL contents of this bundle into the repo root. The structure already matches what the manuscript expects.
4. Commit with message: "Paper 1 v3 final computational package (canonical figures from RPM v3 data)".
5. Set `main` to point to this commit.
6. Push to origin.
7. **DO NOT** create the final tag `paper1-v1.0-reproducible` yet — that is deferred until manuscript acceptance.

## What is in this bundle

- `figures_paper1_final/`: Figure 1-4 PNG (300 dpi) + TIFF (600 dpi LZW), SHA256 manifest. Generated from v3 RPM NPZ data: u*=−0.30, α_peak=1.34e-04, FWHM=1.20, γ_opt=3.0, peak α=2.28e-04, Pearson r=0.9125523536208335. Numbers verified against manuscript.
- `docs_v3/`: manuscript + claim support table + removed/softened claims log + figure plan + cover letter draft + figure-data CSV + handoff to Paper 2 + Git status notes.
- `src/v3/figures/generate_paper1_figures.py`: figure-generation script (referenced for transparency; cannot run without v3 NPZ data, which is in the separate computational archive `qbt_v3_complete_artifacts.tar.gz`).
- `Paper1_PCCP_submission.docx`: Word document for submission with figures embedded inline.
- `README_PAPER1.md`, `RELEASE_NOTES_PAPER1_DRAFT.md`: package overview and release notes.

## What is NOT in this bundle (intentionally)

- The raw NPZ outputs from v3 sweeps. These are 30+ MB and live in `qbt_v3_complete_artifacts.tar.gz` (SHA256 d966108a86a82b0098aecc14b6098c4ea00e2d7d33d653be8e7072642f9d03f3), which is referenced in the README and Methods §2.10 but not included in this Git repo. The figures embedded here are sufficient for the paper; reproducibility goes through the separate archive.
- Any toy_yield_transducer or toy_3d_geometry data. These are PAPER 2 material and stay in the old repo.

## After creating the Paper 1 repo

The OLD repo (with toy_yield, 3D geometry, A1-A4) should be:
- Renamed to `paper2-polymorphic-response-manifolds` (or similar)
- Marked clearly in README that the previous "Paper 1" content is now Paper 2 material
- Used as the development base for Paper 2 work

## Verification after push

To confirm the repo is well-formed, run:

```bash
cd paper1-rpm-radical-pair
sha256sum -c figures_paper1_final/SHA256SUMS  # if you generated a SHA256SUMS file
ls figures_paper1_final/Figure*.png figures_paper1_final/Figure*.tiff
# Should list 4 PNG + 4 TIFF files
```

The four PNG SHA256s should match what is recorded in `figures_paper1_final/figure_manifest.txt`:

- Figure1_model_and_baseline.png:        9aa1b8c0d4f8118f78d39110d03ed1c45e68a803584dd35769bb5fb6e8f70399
- Figure2_kinetic_scale_and_exchange.png: 26b7cf0869368442a949d5e759b97022bc452d65aaf6d6173a4872c0978d74cf
- Figure3_noise_channel_dependence.png:  22285c2a3e827f079f00229dc941736777d14e16f5bbca9d1c0820ef02095c16
- Figure4_spectral_correlate.png:        32376fabad7ca96759c0f46333d303e411ce0ebd8d11eb5e8b612ff1e83e8ebe

If any hash mismatches, STOP and report.
