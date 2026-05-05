# Cover Letter — PCCP Submission

**Date:** [submission date]

**To:** The Editors, Physical Chemistry Chemical Physics
Royal Society of Chemistry

**Subject:** Submission of original research article — *Ratio-dependent response structure in a reduced radical-pair model of magnetoreception*

---

Dear Editors,

I am submitting for your consideration the manuscript *"Ratio-dependent response structure in a reduced radical-pair model of magnetoreception."* The work falls within PCCP's scope of physical chemistry, chemical physics, and biophysical chemistry, with direct relevance to the active spin-chemistry community and the reduced-model literature on radical-pair magnetoreception.

The paper reports a claim-aligned reduced-model study of orientation-dependent reaction yields in a two-electron, one-nucleus radical pair with axial hyperfine coupling, geomagnetic-scale field, and spin-selective recombination. The central findings are:

1. The model exhibits a reproducible broad response peak in recombination-ratio space at *u** ≈ −0.3 with FWHM ≈ 1.2 decades.
2. Hyperfine anisotropy is structurally necessary: the isotropic-hyperfine control eliminates the response at numerical precision.
3. The response is organized by the recombination ratio but is meaningfully modulated by the absolute kinetic scale; amplitude and peak location both depend on it.
4. Two distinct noise channels behave qualitatively differently: *z*-dephasing on both electrons enhances the response within a finite window (γ_opt ≈ 3, factor ≈ 2× peak), while single-electron spin-flip relaxation has its maximum at zero relaxation and suppresses the response over the tested range, with no enhancement window.
5. The slowest-decay-rate Liouvillian spectral proxy correlates strongly with the orientation anisotropy across the ratio scan (Pearson *r* ≈ 0.91).

These results document a reproducible reduced-model mechanism while explicitly bounding the claims to the tested implementation.

## Reproducibility and claim alignment

This manuscript supersedes an earlier preprint and a previous, broader version of the work that the author refined following an internal claim-versus-code audit. The present submission is the result of a complete rebuild of the computational pipeline (designated v3) with explicit attention to alignment between the manuscript text, the underlying numerical implementation, and the reported observables.

The rebuild includes:

- a clean axial-hyperfine implementation with explicit unit nondimensionalization
- 100-orientation Fibonacci-sphere sampling (deterministic, no random seed required)
- infinite-time Liouvillian linear-solve yield computation with finite-time spot-check validation
- a full pre-flight calibration test suite (six tests, all passing at numerical precision)
- a public reproducibility archive with SHA256 hashes for all output files
- a written claim-versus-code audit table mapping every empirical claim to its data source and status
- an explicit log of removed or softened claims documenting all changes from earlier versions

The manuscript reports only those claims that are directly supported by the implemented model. The reproducibility infrastructure was developed specifically to make the supporting evidence inspectable by reviewers and by independent groups.

## Suggested expertise

The work sits at the intersection of theoretical spin chemistry, open quantum systems, and computational reproducibility methodology. Suggested reviewer expertise includes:

- radical-pair magnetoreception theory and reduced-model implementation
- Haberkorn / Jones-Hore recombination formalisms
- Liouvillian spectral analysis in open quantum systems
- numerical methods for spin-chemistry simulations

I will not suggest specific reviewer names; I would prefer the editor to draw from the standard PCCP reviewer pool for spin-chemistry computational work.

## Statements

This manuscript is original work that has not been published elsewhere and is not under consideration at any other journal.

The author declares no conflicts of interest and received no specific funding for this work.

The complete code, raw data, figures, and audit reports are archived in the public reproducibility package (`qbt_v3_complete_artifacts.tar.gz`, SHA256 `d966108a86a82b0098aecc14b6098c4ea00e2d7d33d653be8e7072642f9d03f3`) with a tagged GitHub release and a Zenodo DOI to be created prior to publication.

I would be glad to address any editorial or technical questions during the review process.

With respect,

**Andrei-Sebastian Ursachi**
Independent Researcher
Diepholz, Germany
contact@andreiursachi.eu
ORCID: 0009-0002-6114-5011
