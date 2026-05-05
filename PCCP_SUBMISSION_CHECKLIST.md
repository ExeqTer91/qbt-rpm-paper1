# PCCP Submission Checklist & Upload Guide

**Manuscript:** *Ratio-dependent response structure in a reduced radical-pair model of magnetoreception*
**Author:** Andrei-Sebastian Ursachi (ORCID: 0009-0002-6114-5011)
**Target journal:** Physical Chemistry Chemical Physics (PCCP), Royal Society of Chemistry
**Submission portal:** https://mc.manuscriptcentral.com/pccp (ScholarOne Manuscripts)
**Package version:** v3 (post round-2 audit patches)

---

## Patches applied in v3 (round-2 audit)

This version addresses a second round of pre-submission audit findings:

1. Cover letter: Zenodo language updated from "will be archived to Zenodo with a DOI prior to publication" to "have been archived to Zenodo with DOI 10.5281/zenodo.[ZENODO_DOI_PLACEHOLDER]". The placeholder must be replaced with the real DOI before the cover letter is uploaded to the portal.
2. Checklist: removed contradictory "After acceptance" Zenodo instructions; Zenodo deposit now requested before submission only.
3. TOC textual abstract: replaced the multi-version notes file with a single-sentence upload-ready version (174 chars, single sentence).
4. Manuscript §4 Discussion: softened "structural prerequisite that distinguishes the present model from a purely classical kinetic system" to a more bounded statement about the role of hyperfine anisotropy within the present spin-dynamical model.
5. Manuscript Abstract: trimmed from 277 to 241 words to match PCCP's 50–250 word range while preserving all five primary findings.

## Patches applied in v2 (round-1 audit)

1. Manuscript Introduction: replaced ambiguous hyperfine notation `A∥ = 1.0 A⊥` with explicit tensor form `A = diag(A⊥, A⊥, A∥)`.
2. Manuscript §3.3: replaced "the form of α(u) is preserved across λ" with sentence acknowledging normalized-shape mismatch at slow absolute rates.
3. Manuscript Reference 13: corrected Denton et al. author list.
4. Figure 1A: corrected field label from "B, B/A∥ = 0.05" to "|B|/A∥ = 0.05".
5. Figure 2D: replaced "Form is preserved across λ" inset with bounded statement.
6. Figure 3: simplified Panel B title; increased panel spacing; moved Panel A legend to avoid overlap.
7. All figures: PCCP-compliant 17.10 cm width at 916–1133 dpi; RGB-flattened LZW TIFF.
8. Graphical abstract: 7.90 × 3.95 cm at 600 dpi (within 8 × 4 cm strict limit).

---

## Package contents

```
paper1_pccp_submission/
├── manuscript/
│   ├── Paper1_PCCP_submission.docx       # main manuscript (Word, US Letter)
│   └── Paper1_PCCP_submission.pdf        # PDF preview for editor reference
├── figures/                              # high-resolution standalone figures
│   ├── Figure1_model_and_baseline.{png,tiff}      # 600 dpi LZW TIFF + 300 dpi PNG
│   ├── Figure2_kinetic_scale_and_exchange.{png,tiff}
│   ├── Figure3_noise_channel_dependence.{png,tiff}
│   └── Figure4_spectral_correlate.{png,tiff}
├── cover_letter/
│   └── Paper1_cover_letter_PCCP.docx     # for portal upload (or paste into form)
├── graphical_abstract/
│   ├── graphical_abstract.{png,tiff}     # ~8×4 cm TOC entry image
│   └── TOC_textual_abstract.txt          # 1-sentence TOC text (~250 chars)
└── PCCP_SUBMISSION_CHECKLIST.md          # this file
```

(There is no separate Electronic Supplementary Information at this stage; the full computational reproducibility archive lives at https://github.com/ExeqTer91/qbt-rpm-paper1 and is referenced from §2.10 of the manuscript.)

---

## Pre-submission checklist (verify before opening portal)

### Manuscript content
- [x] Title page with author name, affiliation, ORCID, contact email
- [x] Abstract (single paragraph, 277 words — within typical PCCP range)
- [x] Keywords line (6 keywords)
- [x] Numbered sections: 1. Introduction, 2. Methods, 3. Results, 4. Discussion, 5. Limitations, 6. Conclusion
- [x] Conflicts of Interest statement
- [x] Author Contributions statement (using CRediT-style description)
- [x] Funding statement
- [x] Data Availability statement (with GitHub URL + SHA256 of computational archive)
- [x] References (25 entries, all with DOIs)
- [x] All figures cited in text (Figures 1–4)
- [x] No images of copyrighted material
- [x] British English spelling check pending — see "Pre-portal action items" below

### Figures
- [x] Figures 1–4 generated from raw NPZ data with manifest SHA256
- [x] 600 dpi TIFF (LZW compression) for print quality
- [x] 300 dpi PNG for review/preview
- [x] Plot legends use "absorbing-product effective" not "Lindblad" (per Methods §2.7)
- [x] All numerical annotations in captions match the data manifest

### Graphical abstract
- [x] PNG and TIFF files at 600 dpi
- [x] Approximate 8 × 4 cm aspect ratio
- [x] Single-panel design showing α(u) + spectral proxy Δ_H(u) overlay with key numbers
- [x] Textual TOC abstract written (under 250 characters)

### Cover letter
- [x] Addressed to "The Editors, Physical Chemistry Chemical Physics"
- [x] Signed with author name, affiliation, email, ORCID
- [x] Highlights novelty and PCCP-relevance
- [x] States no conflicts of interest
- [x] States no concurrent submission
- [x] Mentions reproducibility archive (GitHub URL)

### Author identifiers
- [x] ORCID provided: 0009-0002-6114-5011 (mandatory for submitting author)

---

## Pre-portal action items (do these before clicking "Submit")

These are small remaining tasks that PCCP either checks automatically or that you should review by eye before submission:

1. **Zenodo DOI required before submission.** PCCP requires a Data Availability statement with a working repository link / DOI. The current statement points to the GitHub repo + a planned Zenodo release. Before submitting, do:
   - Tag the GitHub repo: `git tag -a paper1-v1.0-reproducible -m "Paper 1 v1.0 reproducible release"`
   - Push the tag: `git push origin paper1-v1.0-reproducible`
   - Create a GitHub Release linked to the tag (the GitHub UI will auto-link to Zenodo if the Zenodo-GitHub integration is enabled on the repo).
   - On Zenodo, accept the release; Zenodo assigns a DOI of the form `10.5281/zenodo.XXXXXXX`.
   - Update the manuscript Data Availability statement to include the Zenodo DOI before submission.
   - **Update cover letter `[ZENODO_DOI_PLACEHOLDER]` with the real DOI.** The cover letter docx in this package contains the placeholder string `10.5281/zenodo.[ZENODO_DOI_PLACEHOLDER]` that must be replaced before upload.
   - Re-export the manuscript docx and update SHA256SUMS in the submission package.

2. **British English spelling pass.** The manuscript is mostly written in international scientific English. PCCP requests British English. Run a quick search-and-fix for: "behavior" → "behaviour", "color" → "colour" (none expected, mostly American conventions don't apply to physics terms here, but worth a 5-minute scroll).

3. **Open the docx in Word/LibreOffice on a machine with Times New Roman installed.** Confirm:
   - Page count (~13 pages)
   - All four figures display inline at expected positions
   - References list is complete and DOI-formatted
   - Section headers display as Heading 1 / Heading 2 styles (TOC navigation works)

4. **Final read-through of Discussion (§4) and Limitations (§5).** These are the sections reviewers focus on most. Ensure no claim has crept back in that the data does not support.

5. **Verify the GitHub repo is public and accessible.** https://github.com/ExeqTer91/qbt-rpm-paper1 — open in a private/incognito window and confirm a non-logged-in viewer can browse the code, manifests, and figures. PCCP reviewers should be able to access this without GitHub authentication.

6. **Decide on Open Access.** PCCP offers Subscribe-to-Open / Gold OA. Decide before portal entry whether to opt in (this affects APC and licence selection). Default: opt out (subscription model, no APC).

---

## Portal upload sequence (ScholarOne Manuscripts)

When you log in to https://mc.manuscriptcentral.com/pccp, the portal walks you through the following tabs in order. Below is the suggested file mapping.

### Step 1: Type, Title, & Abstract
- Article type: **Paper** (full original research article — not Communication)
- Title: paste from manuscript title page
- Running title (short title): "Ratio-dependent radical-pair response — RPM v3"
- Abstract: paste from manuscript Abstract section (single paragraph, ~277 words)
- Keywords: paste from manuscript Keywords line

### Step 2: Authors & Institutions
- Submitting (corresponding) author: Andrei-Sebastian Ursachi
- ORCID: 0009-0002-6114-5011
- Email: contact@andreiursachi.eu
- Affiliation: Independent Researcher, Diepholz, Germany
- Country: Germany
- (No co-authors)

### Step 3: Reviewers & Editors
- Suggested reviewers: leave blank (cover letter notes a preference for editor-selected reviewers from the standard PCCP spin-chemistry pool)
- Non-preferred reviewers: leave blank unless you have specific concerns

### Step 4: Details & Comments
- Cover letter: upload `cover_letter/Paper1_cover_letter_PCCP.docx` (or paste content into "Letter to the Editor" textbox)
- Conflict of interest: select **No conflicts** — already stated in manuscript
- Funding: **No specific funding** — already stated in manuscript

### Step 5: File Upload
The portal accepts files in any order. The recommended file designations are:

| Designation | File |
|---|---|
| **Main Document** | `manuscript/Paper1_PCCP_submission.docx` |
| **Figure** (×4) | `figures/Figure1_model_and_baseline.tiff` |
|  | `figures/Figure2_kinetic_scale_and_exchange.tiff` |
|  | `figures/Figure3_noise_channel_dependence.tiff` |
|  | `figures/Figure4_spectral_correlate.tiff` |
| **Graphical Abstract Image** | `graphical_abstract/graphical_abstract.tiff` (or .png if portal prefers) |
| **Graphical Abstract Text** | paste content of `graphical_abstract/TOC_textual_abstract.txt` |
| **Supplemental** | (optional) link to GitHub repo in cover letter; no upload needed |

**Note on figure embedding:** The manuscript already contains Figures 1–4 embedded inline. PCCP's submission system also wants the figures uploaded as separate files for production. Both are needed. Reviewers will see the inline figures; the production team will use the separate TIFFs.

### Step 6: Review & Submit
- Review the submission summary
- Confirm you have read and accept the PCCP licence-to-publish (presented after acceptance, but acknowledged at submission)
- Click Submit

---

## After submission

- You will receive a Manuscript ID (e.g., CP-ART-XX-2026-XXXXXXX) and tracking URL
- The handling editor is assigned within 1–3 days
- Initial editorial decision (desk reject vs. send for review) typically within 1 week
- Peer review process: 4–8 weeks depending on reviewer availability

### Things to keep ready for revision
- Response-to-reviewers document template
- Tracked-changes manuscript (if revision is requested)
- Updated figures if any data is rerun
- Updated GitHub repo SHA if any code changes

### After acceptance
1. Send the corrected proof to PCCP production
2. Sign the licence-to-publish
3. Update the Zenodo deposit only if revisions to the manuscript or computational package are required during peer review (Zenodo supports versioned releases with the same parent DOI)

---

## Contact for portal issues

If the ScholarOne portal has technical problems:
- PCCP editorial office: pccp@rsc.org
- ScholarOne support: ts.mcsupport@clarivate.com
- RSC publishing support: publishing@rsc.org

---

## Author note

This package was assembled on 2026-05-05 from the canonical Paper 1 computational package (commit e150115f at https://github.com/ExeqTer91/qbt-rpm-paper1). Every figure SHA256 in this package matches the manifest at `figures_paper1_final/figure_manifest.txt` in the repo.

If anything in this package conflicts with the GitHub repo, the GitHub repo is authoritative.
