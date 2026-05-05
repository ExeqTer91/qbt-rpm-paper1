# Paper 1 — Git Status

**Snapshot date:** 2026-05-05

## Branch

`paper1/final-computational-package`

This branch is a local-only branch within the package archive. It contains the complete computational package for Paper 1, ready for review before the public release tag is created.

## Tagging plan

The final public release tag `paper1-v1.0-reproducible` is **NOT** yet created. The tag will be created only after:

1. Final claim audit by GPT-Pro on the manuscript text + computational package coherence.
2. Final review of the figures against `docs_v3/PAPER1_FIGURE_DATA_MAP.csv`.
3. Final approval to submit to PCCP.

When all three are complete, the tagging procedure is:

```bash
git tag -a paper1-v1.0-reproducible -m "Paper 1 final reproducible computational package"
git push origin paper1-v1.0-reproducible
# then upload to Zenodo
```

This step is intentionally deferred at the present snapshot.

## Working tree state

The working tree is clean at the time the package archive is created: all generated files (figures, manifest, mapping CSV, README, RELEASE_NOTES, HANDOFF, manuscript markdown) are committed to the branch.

The exact commit hash for this snapshot is in the package archive root (`COMMIT_HASH`) and in the `git log` output of the embedded git history.

## Files included in the commit

```
README_PAPER1.md
RELEASE_NOTES_PAPER1_DRAFT.md
docs_v3/
  PAPER1_FIGURE_DATA_MAP.csv
  PAPER1_TO_PAPER2_HANDOFF.md
  PAPER1_GIT_STATUS.md
  manuscript_paper1_v3.md
  claim_support_table_paper1.md
  removed_or_softened_claims_paper1.md
  figure_plan_paper1.md
  pccp_cover_letter_draft.md
figures_paper1_final/
  Figure1_model_and_baseline.png
  Figure1_model_and_baseline.tiff
  Figure2_kinetic_scale_and_exchange.png
  Figure2_kinetic_scale_and_exchange.tiff
  Figure3_noise_channel_dependence.png
  Figure3_noise_channel_dependence.tiff
  Figure4_spectral_correlate.png
  Figure4_spectral_correlate.tiff
  figure_manifest.txt
src/v3/figures/
  generate_paper1_figures.py
```

## Files NOT included in this commit (separate archives)

The following are kept separately and not embedded in the Paper 1 package commit:

- `results_v3/*.npz` — raw simulation outputs (referenced by SHA256 in figure_manifest.txt; provided alongside as the existing v3 archive `qbt_v3_complete_artifacts.tar.gz`, SHA256: `d966108a86a82b0098aecc14b6098c4ea00e2d7d33d653be8e7072642f9d03f3`)
- `src/v3/*.py` — full simulation source (in the existing v3 archive)
- Toy-yield-transducer and 3D-geometry files (deferred to Paper 2)

This separation keeps the Paper 1 package compact and reproducible from the existing v3 archive.

## Branch divergence

The `paper1/final-computational-package` branch diverges from the main development line as follows:

- It does NOT contain the toy yield-transducer or 3D-geometry exploratory work.
- It contains the patched manuscript (`manuscript_paper1_v3.md`) with all claim adjustments applied.
- It contains the final figures generated from the existing v3 NPZ outputs.
- It is a snapshot suitable for review and (after approval) for final tagging.

## Next steps

1. Review the package contents.
2. Run the figure-generation script against the v3 archive NPZs to verify deterministic reproduction.
3. After approval: create the `paper1-v1.0-reproducible` tag and submit to Zenodo.
