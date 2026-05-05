# Paper 1 → Paper 2 Handoff

This document specifies what is **deferred** from Paper 1 to Paper 2, with enough detail that the work is not lost between manuscripts and Paper 2 has a clear starting point.

---

## What stays in Paper 1

Paper 1 is the **claim-aligned reduced radical-pair worked example**:

- single nucleus, two electron spins, axial hyperfine, geomagnetic field
- recombination-ratio response structure with broad peak at u* ≈ −0.3, FWHM ≈ 1.2 decades
- absolute-rate scaling tested (form preserved, amplitude/location modulated)
- z-dephasing enhancement window (γ_opt ≈ 3, factor ≈ 2× peak)
- single-electron spin-flip relaxation (max at Γ₁=0, no enhancement window)
- spectral correlate r ≈ 0.91
- full pre-flight calibration and reproducibility infrastructure

Paper 1 does **not** make framework-level claims about transduction stability across systems, basin attraction, formalism independence in the broad sense, scaling invariance, or universality. It is one carefully implemented worked example.

---

## What moves to Paper 2

### 1. Toy yield-transducer (1D)

**Status:** Implementation complete, scan complete, but unsuitable for Paper 1 main evidence.

**Reason:** The 1D scan grid `u_dense = np.linspace(-0.5, 2.5, 81)` produces a reported peak at u* = −0.5, which coincides with the leftmost grid point. The "interior basin" classification is therefore not supported by the present scan. Extending the u-range to verify whether the structure is genuinely localized or slides to the new boundary remains untested.

**Paper 2 work:**
- Re-run with extended u-range (e.g., `u ∈ [-3, 3]` or wider)
- Verify whether peak is genuinely interior or scan-boundary-dependent
- If interior: characterize FWHM, ensemble robustness, control sensitivity
- If boundary: report honestly as a different morphology class (boundary shelf or similar)

**Files relevant:**
- `src/v3/run_toy_yield_transducer.py`
- `src/v3/toy_yield_transducer.py`
- `results_v3/toy_yield_transducer/exp1_baseline.npz` and related
- `docs_v3/TOY_YIELD_TRANSDUCER_REPORT.md`

### 2. 3D-geometry / polymorphic response manifold work

**Status:** Tasks #14, #15, #16 explored Model A (tensor-only) and Model B (helix/ring) under multiple morphology classifications. Findings include:

- Under proper re-audit, Model A produces 64 LOCALIZED INTERIOR PEAK candidates and 14 MULTI-PEAK STRUCTURE candidates from 729 configurations, contradicting the earlier claim of pure monotonic saturation.
- Model A tensor-only produces orientation-address α ≈ 0.92 — the largest orientation-dependent yield variation observed in any of the explored systems.
- Model B ring with χ ≠ 0 produces structure that ring with χ = 0 does not, but the χ = 0 control was previously misclassified as NUMERICAL FAILURE due to an over-strict trace threshold; under corrected thresholds it is a non-trivial multi-peak structure.
- 2D ratio-space scans show that the structures classified as "LOCALIZED INTERIOR PEAK" in 1D are typically BOUNDARY MANIFOLDs in 2D (touching grid edges).

**Paper 2 working hypothesis:** *Polymorphic response architecture* — the same minimal open-transducer architecture expresses multiple stable response morphologies depending on topology, phase/chirality, kinetic scale, and orientation address. Two orthogonal axes (ratio-space morphology and orientation-address signature) appear independent.

**Paper 2 next steps:**
- Replicate Model A orientation-address α ≈ 0.92 finding in independent runs
- Extend Model B ring topology to 5–7 site rings (DNA-CT-relevant scale)
- Explicitly test whether the polymorphic morphology classes survive grid refinement and parameter extension
- Address the 2D-boundary-manifold problem: are these genuine connected interior basins seen through a too-narrow window, or are they always at boundaries?

**Files relevant:**
- `src/v3/toy_3d_geometry.py`, `run_toy_3d_geometry.py`, `run_focused_cleanup.py`
- `results_v3/toy_3d_geometry/*.npz` and `*.csv`
- `docs_v3/TOY_3D_GEOMETRY_MORPHOLOGY_ATLAS.md`
- `docs_v3/TOY_3D_GEOMETRY_FOCUSED_CLEANUP.md`
- `docs_v3/CHIRAL_TOPOLOGY_HYPOTHESIS_TEST.md`
- `docs_v3/POLYMORPHIC_RESPONSE_MANIFOLD_AUDIT.md`

### 3. Symmetric-spin-flip-on-both-electrons (T1 extension)

**Status:** Not implemented. Paper 1 reports the single-electron channel as a limitation.

**Paper 2 work:**
- Extend `_T1_super` in `liouvillian.py` to include S2+, S2- jumps
- Re-run T1 sweep with symmetric two-electron channel
- Report whether enhancement window appears for the symmetric channel
- If yes: this would partially restore the earlier "T1 enhancement" claim under proper specification
- If no: confirms that single-electron asymmetry is not the cause of suppression

**Estimated effort:** ~30 minutes implementation + ~30 minutes compute on RunPod.

### 4. Isotropic dephasing (Sx, Sy, Sz on both electrons)

**Status:** Not implemented. Paper 1 reports z-dephasing only.

**Paper 2 work:**
- Extend `_dephasing_super` to include S1x, S1y, S2x, S2y in addition to S1z, S2z
- Re-run dephasing sweep with isotropic channel
- Compare γ_opt, peak amplitude, enhancement factor with the z-dephasing-only result
- If enhancement window persists: reframes Paper 1's "z-dephasing channel-specific" finding
- If enhancement window changes character: documents that the enhancement is z-channel-specific in detail

**Estimated effort:** ~30 minutes implementation + ~30 minutes compute on RunPod.

### 5. Independent Lindblad with non-projector jump operators

**Status:** Not implemented. Paper 1 documents that the existing `build_lindblad` returns the same Liouvillian as `build_haberkorn` for the radical-pair sector by construction.

**Paper 2 work:** Implement a structurally independent Lindblad recombination formulation using non-projector jump operators (e.g., one-way decay channels with explicit product-state ladder). Compare yields directly. Only this comparison would constitute a genuine test of recombination-formalism independence in the broad sense.

**Estimated effort:** Significant — likely requires extending the Hilbert space and re-validating preflight calibration.

### 6. Functional warp / time-integrated channel-weighted observable

**Status:** A Discussion-level interpretation in Paper 1 mentions that the yield is a time-integrated channel-weighted observable. This is the standard formulation but Paper 1 does not develop it as a structural claim with measurable signatures.

**Paper 2 work:**
- Define a quantitative metric for the integrated channel-weighting (e.g., a winding number or topological invariant of the projected dynamics)
- Test whether the metric distinguishes the polymorphic morphology classes
- Test whether tensor-topology vs ring-topology produces measurably different "functional warp" signatures

**Status of conceptual development:** intuitive only; no formalization yet. This is genuinely future work, not deferred-but-ready work.

### 7. Cross-system extensions

**Status:** Outside scope of Paper 1.

**Paper 2 work (or Paper 3):**
- Apply the polymorphic response framework to other open-quantum-transducer systems (photosynthetic energy transfer, enzyme catalysis with quantum components, single-molecule electron transfer chains)
- Test whether the same morphology classes appear across systems
- This is the cross-system generalization that Paper 1 explicitly does NOT claim

---

## What is closed (not deferred)

The following claims from earlier versions of the work are removed and **not** to be reopened in Paper 2 unless new evidence emerges:

- "Universal plateau" / "basin attraction" framework — too strong relative to evidence
- "Coherence preservation is the wrong invariant" — a paradigm-level claim that one example cannot establish
- "Living systems sit inside the basin" — speculative without experimental link
- "Cross-scale ratio attractors in EEG" — separate body of work, not connected to radical-pair without additional evidence
- "Formalism independence" as a broad claim — current implementation does not test it; only a structurally independent Lindblad would

If Paper 2 produces evidence supporting any of these claims, they can be reopened with explicit data citations. They are not closed-with-prejudice; they are closed-pending-evidence.

---

## Author note

This handoff document is a living record. Paper 2 will inherit and extend it; future Paper-3 work (if undertaken) should reference Paper 2's handoff.

— Andrei-Sebastian Ursachi, 2026-05-05
