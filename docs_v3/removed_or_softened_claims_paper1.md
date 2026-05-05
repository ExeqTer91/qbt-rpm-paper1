# Removed or Softened Claims — Paper 1

This document logs every claim from the v2 manuscript that has been removed, softened, or replaced based on the v3 code and data inspection.

For each entry: **Old wording (v2)** → **Why removed** → **Replacement wording (v3)**.

---

## 1. Title

**Old:** *Beyond coherence preservation: transduction stability and ratio-controlled regimes in radical-pair magnetoreception*

**Why removed:** "Beyond coherence preservation" is a framework-level claim that the present numerical evidence does not support at the strength implied. "Transduction stability" and "ratio-controlled regimes" are framework labels rather than descriptions of the specific result. The v2 title implies a paradigm shift; the v3 paper documents a reduced-model result with explicit boundaries.

**Replacement:** *Ratio-dependent response structure in a reduced radical-pair model of magnetoreception*

## 2. Abstract opening

**Old:** *"Quantum biology has been largely organized around a single question: whether quantum coherence can survive physiological noise long enough to perform biological work. We argue this framing is incomplete. The biologically relevant problem is not coherence preservation but transduction stability."*

**Why removed:** Sets up a framework-level reorientation of quantum biology that one reduced-model worked example cannot support. Also presupposes that the field is organized around a single question, which is contestable.

**Replacement:** *"Radical-pair magnetoreception converts orientation-dependent spin dynamics into reaction-yield anisotropy, providing a working biological example of how transient quantum dynamics produce classical readouts. Computational claims about such systems can drift from the underlying numerical implementation if methods, code, and observables are not aligned."*

## 3. Abstract closing

**Old:** *"Together these results support a framework in which quantum-biological function is governed by basin attraction in ratio space, with dissipation and noise as constitutive elements of the transduction machinery rather than contaminants of it."*

**Why removed:** "Basin attraction" implies a dynamical-systems concept (flow in parameter space toward an attractor) not implemented or measured. "Constitutive elements of the transduction machinery" is a framework claim from one example. Multi-system universality is not tested.

**Replacement:** *"The results document a reproducible reduced-model mechanism for ratio-dependent response structure in radical-pair magnetoreception while highlighting limits to broad robustness claims."*

## 4. Introduction rhetorical framing

**Old:** *"Either the quantum hypothesis is wrong, or the question is."* and *"Coherence preservation is the wrong invariant."*

**Why removed:** Both are dichotomies that present a framework-level claim as forced. The v3 results do not establish that coherence preservation is wrong as an organizing principle; they establish a specific reduced-model result.

**Replacement:** Removed entirely. Replaced with a methodological framing: *"The aim is narrower and more methodological: to test whether a reduced radical-pair model, implemented with explicit attention to claim-code alignment, exhibits reproducible response structure in recombination-ratio space..."*

## 5. Plateau invariance under absolute scaling

**Old:** *"The plateau is invariant under absolute rate scaling spanning two orders of magnitude."*

**Why removed:** Inspection of sweep_kSkT_main_lam0.1 / lam1.0 / lam10.0: peak amplitudes vary from 2.92e-2 to 2.70e-8 (six orders of magnitude); peak location shifts from u*=+0.5 (λ=0.1) to u*=-0.3 (λ=1, 10); normalized RMS deviation ≈0.43 between λ=0.1 and λ=1. This fails any reasonable definition of collapse.

**Replacement:** *"The response is organized by recombination ratio but modulated by absolute kinetic scale: the form of α(u) is preserved across λ, but amplitude varies by orders of magnitude and peak location shifts."*

## 6. Haberkorn-Lindblad formalism independence

**Old:** *"The plateau is invariant under recombination formalism (Haberkorn versus Lindblad), demonstrating broad formalism-independence."*

**Why removed:** Inspection of liouvillian.py: build_lindblad function returns identical Liouvillian to build_haberkorn (verbatim from docstring: "Returns identical Liouvillian to build_haberkorn"). This is by design — the absorbing-product effective dynamics for the radical-pair sector reduces to the Haberkorn equation. Agreement is therefore tautological at the implementation level. No structurally independent Lindblad with non-projector jump operators is in the code.

**Replacement:** *"Haberkorn trace-loss dynamics and the absorbing-product effective yield implementation give identical results in the tested model. As noted in §2.7, this agreement is structural to the present implementation: the absorbing-product effective dynamics for the radical-pair sector reduce to the Haberkorn equation. The comparison is therefore an implementation-level consistency check; it does not constitute a test of broad recombination-formalism independence."*

## 7. Isotropic dephasing claim

**Old:** *"Moderate environmental dephasing enhances response within a finite window... isotropic spin dephasing at rate γ..."*

**Why removed:** Inspection of liouvillian.py _dephasing_super: implementation is `gamma * (lindblad_super(S1z) + lindblad_super(S2z))`. This is *z*-dephasing on both electrons, not isotropic dephasing. Isotropic would require Sx, Sy, Sz on both electrons.

**Replacement:** *"z-dephasing on both electron spins enhances the response within a finite window... The dephasing operator includes only Sz components on both electrons; this is not fully isotropic dephasing."*

## 8. T1 relaxation on both electrons

**Old:** *"Longitudinal (T1) relaxation channels..."* (implying both electrons).

**Why removed:** Inspection of liouvillian.py _T1_super: implementation uses S1p and S1m only (electron 1); no S2 jumps. T1 acts only on electron 1.

**Replacement:** *"Single-electron longitudinal relaxation"* and *"electron-1 spin-flip relaxation"* throughout. Limitation explicitly listed: "Symmetric T1 relaxation on both electrons may behave differently and remains untested."

## 9. Spectral gap doesn't track response

**Old:** *"A single-gap account of the response would predict that the anisotropy profile α(u) tracks 1/Δ(u). We test this prediction in §3.5 and find it is not satisfied: the mode-swap score, which captures collective spectral reorganization, tracks the response while Δ(u) does not."*

**Why removed:** Inspection of sweep_spectral_main_final.npz: proxy_alpha_correlation = 0.9125523536208335; robust_tracking: True. The slowest-decay-rate proxy (functionally the spectral gap) *does* track the response at strong correlation. Mode-swap S_loss is variable (single localized spike at u=0.10, small elsewhere); S_perm oscillates 0.4–0.7 without clear pattern. The v2 claim inverts the actual finding.

**Replacement:** *"The slowest-decay-rate spectral proxy Δ_H(u) correlates strongly with the anisotropy curve at Pearson r ≈ 0.91. The mode-reorganization diagnostic is descriptive but more variable; we do not claim it as a robust independent signature. The slowest-decay-rate proxy is the more reliable spectral correlate."*

## 10. Dissipative phase transition / mode-restructuring transition

**Old:** *"...indicating a collective mode-restructuring transition. The same qualitative structure recurs in a minimal two-level toy model..."* and *"...connected to the dissipative-phase-transition formalism..."*

**Why removed:** The Liouvillian spectrum diagnostics are correlative, not a formal phase-transition analysis. The toy model claim is separately disqualified (next entry).

**Replacement:** *"We do not interpret these spectral structures as evidence of a formal dissipative phase transition or mode-restructuring transition in the strict sense."*

## 11. Toy model reproduces same qualitative behavior

**Old:** *"The same qualitative structure recurs in a minimal two-level toy model with competing dissipative channels and internal coherent coupling. Together these results support a framework in which..."* and Figure 5 toy-yield as main evidence.

**Why removed:** Two reasons. First, inspection of run_toy_yield_transducer.py: u_dense = linspace(-0.5, 2.5, 81); peak at u*=-0.5 is at the leftmost grid boundary, not interior. The reported "interior basin" was misclassified. Second, the original two-level pumped toy fails under structured ensemble averaging (separately documented). Neither configuration supports primary-evidence claim.

**Replacement:** Toy model removed from main Results. Single Discussion sentence: *"Exploratory minimal-transducer simulations beyond the radical-pair system suggest that response morphology can be polymorphic across shelves, ridges, localized peaks, multi-peak structures, and orientation-address patterns; these models are not used as primary evidence here and will be treated separately."*

## 12. Cross-scale framing (EEG, photosynthesis, olfaction, neural systems)

**Old:** *"...cross-scale ratio attractors in EEG..."* and broad references to dephasing-assisted transport, olfactory tunneling, enzyme catalysis.

**Why removed:** The present work is one reduced radical-pair example. Cross-scale claims require multiple worked examples and are not supported by this single result.

**Replacement:** Removed entirely from Paper 1. May appear in a future framework paper that includes multiple worked examples.

## 13. "Living systems sit inside the basin"

**Old:** *"...living systems may sit inside the basin while purified or isolated preparations sit outside it."*

**Why removed:** Speculative interpretation of in-vivo vs in-vitro mismatch as basin location. The basin language is itself softened (§5 here), and the in-vivo/in-vitro claim is not directly tested.

**Replacement:** Removed.

## 14. "Approximately twentyfold" exchange suppression

**Old (v2 with my edit):** *"Strong exchange (J ≳ 5A∥) suppresses anisotropy relative to weak exchange by approximately 18 ± 2-fold."*

**Why removed:** The 18 ± 2-fold number was a placeholder I introduced when rewriting v2. The original number was "approximately twentyfold." Neither has been verified against the actual sweep_uJ_main_final data. The current v3 J range is [0, 3] in 21 linear points, which does not extend to J ≳ 5A∥. The factor claim has no v3 data to support it.

**Replacement:** *"The exchange coupling J ∈ [0, 3] modulates the response amplitude across the scanned range without eliminating the peak."* — Quantitative factor removed pending data inspection.

## 15. "Universal response plateau"

**Old (in figures and text):** *"Universal response plateau"* phrasing.

**Why removed:** The plateau is bounded to the tested implementation: specific hyperfine, specific noise channels, specific kinetic scale. "Universal" is not earned.

**Replacement:** *"Broad response peak"* or *"broad response region"* throughout.

## 16. "Falsifiable predictions" section as a confrontational frame

**Old (v2):** Falsifiability section that explicitly listed predictions distinguishing "this framework" from "coherence-preservation accounts" and "optimization accounts."

**Why softened:** The v2 framing reads as a paradigm contest. The v3 numerical results are more modest and do not require this confrontational frame.

**Replacement:** Falsifiable predictions discussion folded into Discussion §4 as part of "what the results support and where claims remain bounded." No standalone confrontation.

---

## Summary of removals

The v2 manuscript made approximately 14–16 claims at framework level (universal plateau, basin attraction, transduction stability across systems, formalism independence, scaling invariance, isotropic noise enhancement, T1 of both electrons, mode-swap as phase-transition signature, toy model as architectural generality, cross-scale EEG, etc.). The v3 inspection of code and data shows that **at least 11** of these are not supported by the implemented model. Paper 1 documents the supported subset and explicitly marks the rest as removed, future work, or out of scope.

This document should be retained as a record for the cover letter and for any reviewer questions about how the paper differs from the v2 preprint or from earlier framings of the work.
