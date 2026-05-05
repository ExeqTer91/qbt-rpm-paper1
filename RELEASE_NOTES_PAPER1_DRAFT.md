# Release Notes — Paper 1 v1.0-reproducible (DRAFT)

**Status:** DRAFT. Final tag `paper1-v1.0-reproducible` not yet created.

**Target submission:** Physical Chemistry Chemical Physics (PCCP).

**Snapshot date:** 2026-05-05.

---

## What this release contains

Computational package supporting the manuscript *"Ratio-dependent response structure in a reduced radical-pair model of magnetoreception."* The package is a complete, auditable rebuild (designated v3) of an earlier reduced-model study, with explicit attention to alignment between the manuscript text, the underlying numerical implementation, and the reported observables.

### Manuscript

- `docs_v3/manuscript_paper1_v3.md` — main manuscript (≈4,200 words, 4 figures, 25 references with DOIs)

### Supporting audit documents

- `docs_v3/claim_support_table_paper1.md` — every claim mapped to data source and status (6 supported, 3 with caveat, 8 removed/future-work)
- `docs_v3/removed_or_softened_claims_paper1.md` — log of every claim changed from earlier versions, with reasons
- `docs_v3/figure_plan_paper1.md` — figure specification with data sources
- `docs_v3/pccp_cover_letter_draft.md` — submission cover letter

### Figures

- `figures_paper1_final/Figure1_model_and_baseline.{png,tiff}`
- `figures_paper1_final/Figure2_kinetic_scale_and_exchange.{png,tiff}`
- `figures_paper1_final/Figure3_noise_channel_dependence.{png,tiff}`
- `figures_paper1_final/Figure4_spectral_correlate.{png,tiff}`
- `figures_paper1_final/figure_manifest.txt` — SHA256 of every NPZ read and every figure written

### Code and data

- `src/v3/` — simulation code (Hamiltonian, Liouvillian, solver, sweeps, spectral diagnostics)
- `src/v3/figures/generate_paper1_figures.py` — figure-generation script
- `results_v3/*.npz` — all raw simulation outputs

### Mappings and metadata

- `docs_v3/PAPER1_FIGURE_DATA_MAP.csv` — figure-data mapping (panel | NPZ | array keys | quantity | annotations)
- `docs_v3/PAPER1_TO_PAPER2_HANDOFF.md` — explicit list of work deferred to Paper 2
- `docs_v3/PAPER1_GIT_STATUS.md` — branch/commit state at snapshot
- `README_PAPER1.md` — package overview and reproduction instructions

---

## Key changes from earlier versions

1. **Hamiltonian formulation**: Methods section now matches the v3 code exactly (`H_Z`, `H_hf` axial, `H_J` isotropic). Earlier versions had several mismatches (hyperfine tensor convention, propagator type, orientation grid) that are documented in `removed_or_softened_claims_paper1.md`.

2. **Recombination formalism**: The "Haberkorn vs Lindblad" comparison is documented as an implementation-level consistency check rather than a claim of broad formalism independence. The implemented `build_lindblad` function returns the same Liouvillian as `build_haberkorn` for the radical-pair sector, by design. Plot legends use "absorbing-product effective" in place of "Lindblad."

3. **Noise channels**: Labels corrected to **z-dephasing on both electrons** (not isotropic dephasing) and **single-electron spin-flip relaxation** (not symmetric T1 on both electrons). The implementation operators are S1z + S2z for dephasing and S1+, S1- only for spin-flip.

4. **Absolute-rate scaling**: The earlier "scaling collapse" claim is removed. The data show that the form of the response is preserved across λ ∈ {0.1, 1.0, 10.0} but amplitude varies by approximately six orders of magnitude and peak location shifts at small λ.

5. **Spectral diagnostic**: The earlier "spectral gap does not track the response" claim is reversed. The slowest-decay-rate proxy correlates with the orientation anisotropy at Pearson r ≈ 0.91. Mode-reorganization diagnostics (S_loss, S_perm) are described as descriptive only, not as a robust independent signature.

6. **Toy yield-transducer**: Removed from main text. The earlier "interior basin" claim was based on a scan whose left boundary coincided with the reported peak (u* = −0.5, grid u_min = −0.5). The toy work and 3D-geometry extensions are deferred to Paper 2; see `PAPER1_TO_PAPER2_HANDOFF.md`.

---

## Reproducibility properties

- **Pre-flight calibration**: 6/6 tests passing at numerical precision.
- **Bit-identical reproducibility**: legacy v2/v3 outputs agree at max diff 0.0.
- **Yield closure**: 8.88×10⁻¹⁶.
- **Trace conservation (absorbing-product channel)**: max total error 4.33×10⁻¹⁵.
- **Finite-time vs linear-solve agreement**: worst δY_S = 2.86×10⁻¹² across five spot checks.
- **Spectral correlation**: r = 0.9125523536208335 (matches expected value within 1×10⁻⁶ in figure verification).
- **Haberkorn ↔ absorbing-product effective max difference**: 0.0 (tautological by implementation; documented as such).

---

## What is NOT in this release

- The Paper 1 GitHub release tag `paper1-v1.0-reproducible` (intentionally deferred until final review).
- The Zenodo DOI (will be created from the tagged release).
- Toy yield-transducer and 3D-geometry exploratory results (deferred to Paper 2 — see handoff document).
- The published paper PDF (will be added when accepted).

---

## How to verify a downloaded copy

```bash
# Verify the archive integrity
sha256sum -c paper1_final_computational_package.tar.gz.sha256

# Extract
tar -xzf paper1_final_computational_package.tar.gz

# Reproduce figures and check against manifest
cd paper1_final_computational_package
PAPER1_RESULTS_DIR=./results_v3 PAPER1_FIG_OUT=./figures_check \
    python3 src/v3/figures/generate_paper1_figures.py
diff figures_paper1_final/figure_manifest.txt figures_check/figure_manifest.txt
```

The figure SHA256 hashes should match (within deterministic-floating-point tolerances on the same matplotlib version) if the NPZ files are unchanged.

---

## Tagging plan

Once the manuscript is accepted by the target journal:

1. Final review of figures and text against the claim support table.
2. Create GitHub release tag `paper1-v1.0-reproducible`.
3. Upload package to Zenodo and obtain DOI.
4. Update `docs_v3/manuscript_paper1_v3.md` and `RELEASE_NOTES_PAPER1.md` with DOI.
5. Re-snapshot package as `paper1_final_computational_package_v1.0-reproducible.tar.gz`.

These steps are NOT performed at this snapshot.

---

## Author

Andrei-Sebastian Ursachi
Independent Researcher
Diepholz, Germany
contact@andreiursachi.eu
ORCID: 0009-0002-6114-5011
