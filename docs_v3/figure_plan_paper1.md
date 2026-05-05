# Figure Plan — Paper 1

Replit will generate the final figures from v3 NPZ outputs. This document specifies layout, panels, axes, annotations, and the exact numerical values that should appear.

All figures should be saved at 600 dpi LZW TIFF for submission and 300 dpi PNG for preview. Single-file composition (sub-panels assembled in the figure-generation script, not at submission time).

Color palette: use a colorblind-safe palette (e.g., wong palette or viridis for heatmaps). Use the same palette across all figures for consistency. Lambda variants: λ=0.1 blue, λ=1.0 black, λ=10.0 red (or similar three-color sequence). Haberkorn solid lines, absorbing-product effective dashed lines (when both shown).

---

## Figure 1 — Model and baseline response

**Layout:** 3 panels, single row.

**Panel A — Schematic of the reduced radical-pair model**
- Two electron spins (S₁, S₂) shown as arrows
- One nuclear spin (I=1/2) coupled to S₁ via the axial hyperfine tensor (anisotropic ellipsoid representation)
- External magnetic field B with orientation angle θ relative to the symmetry axis
- Recombination channels k_S → singlet products P_S, k_T → triplet products P_T
- Caption indicates B/A∥ = 0.05 (geomagnetic regime), A∥ = 1.0, A⊥ = 0.5 in simulation units
- Source: schematic; no NPZ needed

**Panel B — Isotropic-hyperfine control**
- Two curves: α(u) under axial hyperfine (A∥ ≠ A⊥) and α(u) under isotropic limit (A∥ = A⊥)
- Y-axis log scale
- Axial curve shows finite α (peak ~1.34e-04); isotropic curve shows machine-zero (~2.22e-16)
- Annotation: "isotropic α = 2.22e-16 (machine precision)" / "axial α_peak = 1.34e-04"
- Source: preflight_calibration.npz; sweep_orient_main_isotropic_*.npz; sweep_orient_main_axial_*.npz

**Panel C — Baseline ratio scan α(u)**
- Single curve at λ = 1, J = 0
- u-axis: log₁₀(k_S/k_T), range [-2, 3]
- α-axis: linear
- Mark u* = -0.3 with vertical dashed line
- Annotate FWHM = 1.2 decades (horizontal bar at half-max)
- Annotate peak amplitude α_peak = 1.34e-04
- Source: sweep_kSkT_main_lam1.0_haberkorn.npz (or sweep_kSkT_main_final.npz)

**Caption text (draft):**
*"Figure 1. Reduced radical-pair model and baseline ratio response. (A) Schematic showing two electron spins, one nuclear spin coupled to electron 1 via the axial hyperfine tensor (A∥/A⊥ = 2:1), external field B at orientation θ, and singlet/triplet recombination channels. The geomagnetic regime corresponds to B/A∥ ≈ 0.05. (B) Orientation anisotropy α under the isotropic-hyperfine control versus axial coupling. The isotropic-hyperfine control (red, A∥ = A⊥) gives α = 2.22 × 10⁻¹⁶ (numerical precision). The axial coupling (blue) gives α ≈ 1.08 × 10⁻⁴, more than ten orders of magnitude above the isotropic limit. Hyperfine anisotropy is structurally necessary for the orientation-dependent response in the tested implementation. (C) Baseline ratio scan α(u) at λ = 1, J = 0. The response exhibits a broad peak at u* ≈ −0.3 with FWHM ≈ 1.2 decades and peak amplitude α_peak ≈ 1.34 × 10⁻⁴."*

---

## Figure 2 — Kinetic scale and exchange dependence

**Layout:** 4 panels, 2×2 grid.

**Panel A — Raw α(u) under absolute-rate scaling**
- Three curves: λ = 0.1, λ = 1.0, λ = 10.0
- Y-axis log scale
- Each curve shows substantially different amplitude (six orders of magnitude span)
- Mark peak amplitudes: λ=0.1: 2.92e-2; λ=1: 1.34e-4; λ=10: 2.70e-8
- Mark peak locations: λ=0.1: u*=+0.5; λ=1: u*=-0.3; λ=10: u*=-0.3
- Annotation: "scaling does not collapse — amplitude varies by six orders of magnitude; peak location shifts at small λ"
- Source: sweep_kSkT_main_lam0.1_haberkorn.npz, sweep_kSkT_main_lam1.0_haberkorn.npz, sweep_kSkT_main_lam10.0_haberkorn.npz

**Panel B — Normalized α(u) / max(α) under absolute-rate scaling**
- Same three curves, each normalized by its own peak
- Linear y-axis
- Shows that the form is roughly preserved but not identical
- Annotation: "normalized RMS deviation between λ=0.1 and λ=1 is ≈0.43, exceeding any reasonable collapse threshold"
- Source: same NPZ as Panel A

**Panel C — Heatmap α(u, J)**
- 2D heatmap: u on x-axis [-2, 3], J on y-axis [0, 3]
- Color: α value (log scale or symmetric log)
- Show the broad peak in u that modulates as J varies
- Source: sweep_uJ_main_final.npz

**Panel D — Summary table inset (or separate text panel)**
- λ | u* | peak α | FWHM
- 0.1 | +0.5 | 2.92e-02 | ~1.2
- 1.0 | -0.3 | 1.34e-04 | ~1.2
- 10.0 | -0.3 | 2.70e-08 | ~1.2
- Source: derived from sweeps in panels A-B

**Caption text (draft):**
*"Figure 2. Absolute-rate scaling and exchange dependence. (A) Raw orientation anisotropy α(u) under absolute-rate scaling at λ ∈ {0.1, 1.0, 10.0}. The peak amplitude varies by approximately six orders of magnitude (2.92×10⁻², 1.34×10⁻⁴, 2.70×10⁻⁸), and the peak location shifts at small λ (u* = +0.5 at λ=0.1; u* = −0.3 at λ ∈ {1, 10}). (B) Normalized α(u)/max(α). The form of the response is roughly preserved across λ but not identical: normalized RMS deviation between λ=0.1 and λ=1 is ≈0.43. The response is organized by recombination ratio but is meaningfully modulated by absolute kinetic scale. (C) Heatmap α(u, J) over the v3 exchange-coupling range J ∈ [0, 3]. The broad peak in u persists across J, with amplitude modulation but no qualitative structural change in the scanned range. (D) Numerical summary of peak parameters by λ."*

---

## Figure 3 — Noise-channel dependence

**Layout:** 3 panels, single row.

**Panel A — z-dephasing scan**
- α(γ) for the z-dephasing channel
- X-axis log scale: γ ∈ {0} ∪ logspace(-3, 2, 41) (or v3 hybrid grid)
- Y-axis linear
- Two curves: Haberkorn (solid) and absorbing-product effective (dashed) — these overlap
- Mark γ_opt ≈ 3.0 with vertical line, annotate peak α ≈ 2.28e-04 (factor ≈2× over γ=0 baseline α≈1.08e-04)
- Mark local minimum at γ ≈ 0.2 (where α drops below γ=0 baseline)
- Annotation: "channel: D[S₁_z] + D[S₂_z] (z-dephasing on both electrons; not isotropic)"
- Source: sweep_dephasing_main_final.npz

**Panel B — Single-electron spin-flip relaxation scan**
- α(Γ₁) for the spin-flip channel
- X-axis log scale: Γ₁ ∈ {0} ∪ logspace(-3, 2, 41)
- Y-axis linear
- Single curve (Haberkorn — spin-flip only implemented in Haberkorn formalism)
- Mark maximum at Γ₁ = 0 with α ≈ 1.08e-04
- Show suppression with small partial recovery near Γ₁ ≈ 3, then tendency to zero
- Annotate: "no enhancement window over the tested range"
- Annotation: "channel: (Γ₁/2) (D[S₁_+] + D[S₁_-]) (electron 1 only; symmetric high-T jumps; S2 not affected)"
- Source: sweep_T1_main_final.npz

**Panel C — Side-by-side comparison**
- Bar plot or comparison plot showing peak α (z-deph), peak α (T1), and γ=0 baseline
- Highlights asymmetry: dephasing enhances; T1 suppresses
- Annotation: "noise effects are channel-dependent; the two channels behave qualitatively differently"
- Source: derived from panels A, B

**Caption text (draft):**
*"Figure 3. Channel-dependent noise response. (A) z-dephasing scan: response amplitude α(γ) for the channel D[S₁_z] + D[S₂_z]. The response exhibits a finite enhancement window with γ_opt ≈ 3 and peak α ≈ 2.28×10⁻⁴, approximately twice the γ=0 baseline. A local minimum at γ ≈ 0.2 separates the weak-noise plateau from the enhancement window. The Haberkorn (solid) and absorbing-product effective (dashed) implementations agree across the full γ range. The implemented channel is not fully isotropic (Sx and Sy components not included). (B) Single-electron spin-flip relaxation scan: response amplitude α(Γ₁) for the channel (Γ₁/2)(D[S₁_+] + D[S₁_-]). Single-electron spin-flip relaxation has its maximum at zero relaxation (Γ₁ = 0, α ≈ 1.08×10⁻⁴) and suppresses the response over the tested range, with no enhancement window; a small partial recovery appears near Γ₁ ≈ 3 before the response tends to zero at strong relaxation. The channel acts only on electron 1; symmetric spin-flip relaxation on both electrons remains untested. (C) Comparison: noise effects are qualitatively channel-dependent. Generic statements about "noise enhancement" require explicit channel specification. Both noise scans were performed at u = 0; the baseline peak is at u ≈ −0.3, so the scan characterizes the response near, but not exactly at, the plateau center."*

---

## Figure 4 — Spectral correlate

**Layout:** 3 panels, single row.

**Panel A — Liouvillian eigenvalue spectrum vs u**
- Plot Re(λₙ) for the slowest-decaying eigenvalues across the u scan
- u-axis: [-1.5, 2.5]
- y-axis: real part of Liouvillian eigenvalues (most negative = fastest decay)
- Color individual modes; show how the slowest mode tracks across u
- Source: sweep_spectral_main_final.npz; eigenvalues_real

**Panel B — Slowest-decay-rate proxy Δ_H(u) overlaid with α(u)**
- Two curves on twin axes, both normalized to their own peak
- Δ_H(u) blue, α(u) red dashed
- Show the close tracking
- Annotation: "Pearson r = 0.9125"
- Source: sweep_spectral_main_final.npz; spectral_proxy and alpha

**Panel C — Mode-reorganization diagnostics (descriptive)**
- Two sub-panels or overlay:
  - S_loss(u): tracking-loss score, mostly small with a single localized spike near u=0.10
  - S_perm(u): permutation score, oscillating 0.4–0.7
- Annotation: "descriptive only; not a robust independent signature; the slowest-decay-rate proxy is the more reliable spectral correlate"
- Source: sweep_spectral_main_final.npz; S_loss, S_perm

**Caption text (draft):**
*"Figure 4. Liouvillian spectral correlate of the response. (A) Real parts of the slowest-decaying Liouvillian eigenvalues across the u scan. The Haberkorn radical-pair Liouvillian is trace-decreasing under recombination and has no zero eigenvalue. (B) Slowest-decay-rate spectral proxy Δ_H(u) (blue, normalized to its own peak) overlaid with the orientation anisotropy α(u) (red dashed, normalized to its own peak). The two curves track each other closely across the u range with Pearson correlation r = 0.91. The proxy is reported as a descriptive correlate of the response, not as a mechanistic explanation or a phase-transition signature. (C) Mode-reorganization diagnostics. The tracking-loss score S_loss has a single localized spike near u = 0.10 with small values elsewhere; the permutation score S_perm oscillates at moderate values without a clear pattern. The slowest-decay-rate proxy in (B) is the more reliable spectral correlate."*

---

## Supplementary figures (proposed)

**S1 — Pre-flight diagnostic table**
- Six panels showing: isotropic α, axial α, Haberkorn closure error vs u, Lindblad/product total conservation error, finite-time spot-check δYS at five points, legacy v2/v3 max difference
- Source: preflight_calibration.npz

**S2 — Yield closure diagnostics across all sweeps**
- For each sweep (u-J, dephasing, T1, orientation), plot the worst yield closure error and trace conservation error vs scan parameter
- Should show all errors below 1e-10 throughout

**S3 — Orientation maps Y_S(θ, φ) at representative u values**
- Fibonacci-sphere plots at u = -1, 0, 1, 2 showing the orientation-dependent yield pattern
- Source: sweep_orient_main_*_u*.npz

**S4 — Implementation comparison: Haberkorn vs absorbing-product effective**
- For one sweep (kSkT main, λ=1), plot yield difference YS_Haberkorn − YS_AbsorbingProduct as function of u
- Difference should be at numerical precision (~1e-14 to 1e-15)
- Source: sweep_kSkT_main_lam1.0_haberkorn.npz, sweep_kSkT_main_lam1.0_lindblad.npz

**S5 — (Optional, exploratory) Polymorphic toy/3D-geometry response morphologies**
- Only included if explicitly labeled "exploratory" and clearly separated from main evidence
- Single panel showing the diversity of morphologies in the 3D toy work
- Caveat-laden caption noting that this is exploratory and treated separately
- Recommended: omit from Paper 1 entirely; reserve for Paper 2

---

## Figure generation notes for Replit

- All figures should pull data from NPZ files only — no hardcoded values
- Each figure script should print the values it puts in the figure as a sanity log
- Figures should fail gracefully (with a clear error message) if the expected NPZ keys are missing
- The figure-generation scripts should be in the v3 source tree (e.g., src/v3/figures/) so they are part of the reproducibility archive
- Save NPZ + figure together; SHA256 hash both

---

## Figure-data mapping table

This table specifies the exact NPZ file, array keys, plotted quantity, and numeric annotations for every panel in every main figure. Replit (or whoever generates the figures) must follow this mapping exactly. If an array key is missing from the specified NPZ, the figure-generation script should fail with a clear error message rather than substitute alternative data.

| Panel | NPZ file | Array keys | Plotted quantity | Numeric annotations |
|-------|----------|------------|------------------|---------------------|
| 1A | (schematic; no NPZ) | n/a | Cartoon of S₁, S₂, I, hyperfine tensor, B vector, k_S/k_T channels | A∥ = 1.0, A⊥ = 0.5, B/A∥ = 0.05 |
| 1B | preflight_calibration.npz; sweep_orient_main_axial_u0.0.npz; sweep_orient_main_isotropic_u0.0.npz | preflight: alpha_isotropic, alpha_axial; sweep_orient: u_grid, alpha (per file) | α(u) on log y-axis: axial curve (blue) and isotropic curve (red, ≈ machine zero) | "isotropic α = 2.22×10⁻¹⁶ (machine precision)"; "axial α_peak ≈ 1.08×10⁻⁴" |
| 1C | sweep_kSkT_main_lam1.0_haberkorn.npz | u_grid, alpha | α(u) at λ = 1, J = 0; linear y-axis | u* = −0.3 (vertical dashed line); FWHM ≈ 1.2 decades (horizontal half-max bar); α_peak ≈ 1.34×10⁻⁴ |
| 2A | sweep_kSkT_main_lam0.1_haberkorn.npz; sweep_kSkT_main_lam1.0_haberkorn.npz; sweep_kSkT_main_lam10.0_haberkorn.npz | u_grid, alpha (per file) | α(u) on log y-axis; three curves λ ∈ {0.1, 1.0, 10.0} | peaks: 2.92×10⁻², 1.34×10⁻⁴, 2.70×10⁻⁸; locations: u* = +0.5, −0.3, −0.3 |
| 2B | (same three files as 2A) | u_grid, alpha (per file) | α(u)/max(α) on linear y-axis; three curves | normalized RMS deviation between λ=0.1 and λ=1: ≈ 0.43 |
| 2C | sweep_uJ_main_final.npz | u_grid, J_grid, alpha_grid (2D) | Heatmap α(u, J); colorbar (linear or symmetric log) | J range: [0, 3], 21 points; u range: [-2, 3] |
| 2D | (derived from panels A–B) | n/a | Inset table | Rows for λ ∈ {0.1, 1, 10}: u*, peak α, FWHM |
| 3A | sweep_dephasing_main_haberkorn.npz; sweep_dephasing_main_lindblad.npz | gamma_grid, alpha (per file) | α(γ); log x-axis; linear y-axis; Haberkorn solid + Lindblad dashed | γ_opt ≈ 3.0 (vertical line); peak α ≈ 2.28×10⁻⁴; γ=0 baseline α ≈ 1.08×10⁻⁴; local min at γ ≈ 0.2; channel: "D[S₁_z] + D[S₂_z]" |
| 3B | sweep_T1_main_final.npz | T1_grid, alpha | α(Γ₁); log x-axis; linear y-axis; single curve | Maximum at Γ₁ = 0 with α ≈ 1.08×10⁻⁴; partial recovery near Γ₁ ≈ 3; "no enhancement window over the tested range"; channel: "(Γ₁/2)(D[S₁_+] + D[S₁_-])" (electron 1 only) |
| 3C | (derived from sweep_dephasing_main_*; sweep_T1_main_final.npz) | n/a | Bar plot: peak α (z-deph), peak α (spin-flip), γ=0 baseline | "z-dephasing enhances; spin-flip relaxation suppresses over tested range" |
| 4A | sweep_spectral_main_final.npz | u_grid, eigenvalues_real | Re(λ_n) vs u for slowest-decaying modes | None |
| 4B | sweep_spectral_main_final.npz | u_grid, spectral_proxy, alpha, proxy_alpha_correlation | Δ_H(u) (blue, normalized to its peak) overlaid with α(u) (red dashed, normalized) | "Pearson r = 0.9125" |
| 4C | sweep_spectral_main_final.npz | u_grid, S_loss, S_perm | S_loss(u) and S_perm(u) | "descriptive only; not a robust independent signature" |
| S1 | preflight_calibration.npz | All preflight test outputs | Six-panel diagnostic table | Test names + numerical results (closure 8.88×10⁻¹⁶; conservation 4.33×10⁻¹⁵; finite-time δYS 2.86×10⁻¹²; legacy max diff 0.0) |
| S2 | All sweep_*.npz | yield_closure_err, trace_diagnostic_err arrays per sweep | Worst-case errors vs scan parameter | All errors below 1×10⁻¹⁰ throughout |
| S3 | sweep_orient_main_axial_u-1.0.npz; sweep_orient_main_axial_u0.0.npz; sweep_orient_main_axial_u1.0.npz; sweep_orient_main_axial_u2.0.npz | theta, phi, Y_S | Fibonacci-sphere orientation maps Y_S(θ, φ) at u ∈ {−1, 0, 1, 2} | u value per panel |
| S4 | sweep_kSkT_main_lam1.0_haberkorn.npz; sweep_kSkT_main_lam1.0_lindblad.npz | u_grid, alpha (per file) | YS_Haberkorn − YS_AbsorbingProduct vs u | "max difference: 0.0 (numerical precision)" |
| S5 | (optional, exploratory; outside scope of Paper 1) | n/a | Polymorphic toy/3D morphologies | "exploratory; treated separately" |

### Verification rules

- The figure-generation script must verify `proxy_alpha_correlation = 0.9125523536208335` and `robust_tracking = True` in `sweep_spectral_main_final.npz` before generating Figure 4B; abort if mismatch.
- The figure-generation script must verify that `sweep_kSkT_main_lam1.0_haberkorn.npz` and `sweep_kSkT_main_lam1.0_lindblad.npz` produce alpha arrays with max absolute difference 0.0 before generating S4; abort if mismatch.
- The figure-generation script must verify that `sweep_T1_main_final.npz` peak T1 = 0 before generating 3B; abort if otherwise.
- The figure-generation script must record the SHA256 of every NPZ it reads and every PNG/TIFF it writes, and append both to a `figure_manifest.txt` file.
