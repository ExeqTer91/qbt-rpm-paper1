#!/usr/bin/env python3
"""
generate_paper1_figures.py — produces final Figures 1–4 for Paper 1.

Reads only NPZ files specified in figure_plan_paper1.md.
Saves 600 dpi LZW TIFF + 300 dpi PNG preview to figures_paper1_final/.
Records SHA256 of every NPZ read and every figure written to figure_manifest.txt.

Important conventions (per Paper 1 patch instructions):
  - Plot legend label: "absorbing-product effective" (NOT "Lindblad")
  - Channel naming: "single-electron spin-flip relaxation"
  - Figure 1B title: "Isotropic-hyperfine control"
"""

import hashlib
import json
import os
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# ------------------------------------------------------------------
# Paths
# ------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
RESULTS_DIR = Path(os.environ.get("PAPER1_RESULTS_DIR", "/home/claude/qbt_v3/results_v3"))
OUT_DIR = Path(os.environ.get("PAPER1_FIG_OUT", SCRIPT_DIR.parent.parent.parent / "figures_paper1_final"))
OUT_DIR.mkdir(parents=True, exist_ok=True)

MANIFEST = []  # list of (kind, path, sha256)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_npz(name: str):
    p = RESULTS_DIR / name
    if not p.exists():
        raise FileNotFoundError(f"Missing NPZ: {p}")
    digest = sha256_file(p)
    MANIFEST.append(("READ", str(name), digest))
    return np.load(p, allow_pickle=True)


def save_fig(fig, base: str):
    """Save figure as 600 dpi LZW TIFF + 300 dpi PNG preview."""
    png_path = OUT_DIR / f"{base}.png"
    tiff_path = OUT_DIR / f"{base}.tiff"

    fig.savefig(png_path, dpi=300, bbox_inches="tight", facecolor="white")
    # 600 dpi TIFF with LZW: render to PNG at 600 dpi, then re-save with PIL using LZW
    tmp_png = OUT_DIR / f"{base}_tmp_600.png"
    fig.savefig(tmp_png, dpi=600, bbox_inches="tight", facecolor="white")
    img = Image.open(tmp_png)
    img.save(tiff_path, format="TIFF", compression="tiff_lzw", dpi=(600, 600))
    tmp_png.unlink()

    plt.close(fig)
    MANIFEST.append(("WRITE", f"{base}.png", sha256_file(png_path)))
    MANIFEST.append(("WRITE", f"{base}.tiff", sha256_file(tiff_path)))
    print(f"  → {base}.png + {base}.tiff")


# ------------------------------------------------------------------
# Figure 1
# ------------------------------------------------------------------
def figure_1():
    print("Figure 1: Model and baseline response")
    pre = load_npz("preflight_calibration.npz")
    sw1 = load_npz("sweep_kSkT_main_lam1.0_haberkorn.npz")
    iso0 = load_npz("sweep_orient_main_isotropic_u0.0.npz")
    ax0 = load_npz("sweep_orient_main_axial_u0.0.npz")

    iso = pre["a_isotropic_limit"].item()
    if isinstance(iso, str):
        iso = json.loads(iso)
    ax = pre["c_axial_orientation"].item()
    if isinstance(ax, str):
        ax = json.loads(ax)
    iso_alpha = float(iso["alpha"])
    ax_alpha = float(ax["alpha"])

    u = sw1["u"]
    alpha = sw1["alpha"]
    peak_idx = int(np.argmax(alpha))
    u_star = float(u[peak_idx])
    a_peak = float(alpha[peak_idx])
    half = a_peak / 2.0
    above = alpha >= half
    if above.any():
        idx = np.where(above)[0]
        fwhm = float(u[idx[-1]] - u[idx[0]])
    else:
        fwhm = float("nan")

    print(f"  baseline: u*={u_star:.2f}, alpha_peak={a_peak:.3e}, FWHM={fwhm:.2f}")
    print(f"  isotropic α={iso_alpha:.3e}; axial α={ax_alpha:.3e}")

    fig = plt.figure(figsize=(13, 4.0))
    gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 1.1], wspace=0.32)

    # --- Panel A: schematic
    axA = fig.add_subplot(gs[0, 0])
    axA.set_xlim(0, 1)
    axA.set_ylim(0, 1)
    axA.axis("off")
    axA.set_title("A. Reduced radical-pair model", fontsize=11, loc="left", fontweight="bold")

    # Two electron spins
    axA.annotate("$S_1$", (0.18, 0.62), ha="center", fontsize=14, fontweight="bold", color="#1f4e79")
    axA.annotate("$S_2$", (0.55, 0.62), ha="center", fontsize=14, fontweight="bold", color="#1f4e79")
    axA.annotate("$I=1/2$", (0.18, 0.34), ha="center", fontsize=11, color="#7e2f8e")
    axA.plot([0.18, 0.18], [0.55, 0.40], color="#7e2f8e", lw=1.4)
    axA.text(0.235, 0.475, r"$A_\parallel,A_\perp$", fontsize=9, color="#7e2f8e")

    # Field arrow
    axA.annotate("", xy=(0.85, 0.85), xytext=(0.7, 0.7),
                 arrowprops=dict(arrowstyle="->", color="#c00000", lw=2))
    axA.text(0.8, 0.92, r"$\mathbf{B}$, $B/A_\parallel{=}0.05$", color="#c00000", fontsize=10)

    # Recombination
    axA.annotate("$P_S$", (0.92, 0.55), color="#2e7d32", fontsize=11)
    axA.annotate("$P_T$", (0.92, 0.20), color="#c62828", fontsize=11)
    axA.annotate("", xy=(0.88, 0.55), xytext=(0.62, 0.62),
                 arrowprops=dict(arrowstyle="->", color="#2e7d32", lw=1.4))
    axA.annotate("", xy=(0.88, 0.22), xytext=(0.62, 0.62),
                 arrowprops=dict(arrowstyle="->", color="#c62828", lw=1.4))
    axA.text(0.7, 0.605, "$k_S$", color="#2e7d32", fontsize=10)
    axA.text(0.7, 0.36, "$k_T$", color="#c62828", fontsize=10)
    axA.text(0.5, 0.05, r"$A_\parallel=1.0,\ A_\perp=0.5$", ha="center", fontsize=9)

    # --- Panel B: isotropic-hyperfine control
    axB = fig.add_subplot(gs[0, 1])
    axB.set_title("B. Isotropic-hyperfine control", fontsize=11, loc="left", fontweight="bold")
    axB.set_yscale("log")
    axB.bar(["isotropic", "axial"], [iso_alpha, ax_alpha],
            color=["#c62828", "#1f4e79"], width=0.55)
    axB.set_ylabel(r"$\alpha$ (log scale)")
    axB.set_ylim(1e-17, 1e-3)
    axB.text(0, iso_alpha * 3, f"{iso_alpha:.2e}", ha="center", fontsize=8.5, color="#c62828")
    axB.text(1, ax_alpha * 3, f"{ax_alpha:.2e}", ha="center", fontsize=8.5, color="#1f4e79")
    axB.grid(True, which="both", axis="y", ls=":", alpha=0.4)
    axB.text(0.5, 0.97, "machine-zero vs nonzero",
             transform=axB.transAxes, ha="center", va="top", fontsize=8.5, style="italic")

    # --- Panel C: baseline α(u)
    axC = fig.add_subplot(gs[0, 2])
    axC.set_title("C. Baseline ratio scan ($\\lambda{=}1$, $J{=}0$)", fontsize=11, loc="left", fontweight="bold")
    axC.plot(u, alpha, color="#1f4e79", lw=1.8)
    axC.axvline(u_star, color="#c00000", ls="--", lw=1.0, label=f"$u^*={u_star:+.2f}$")
    axC.axhline(half, color="grey", ls=":", lw=0.8)
    if above.any():
        axC.axhspan(0, half, color="grey", alpha=0.06)
    axC.set_xlabel(r"$u = \log_{10}(k_S/k_T)$")
    axC.set_ylabel(r"$\alpha(u)$")
    axC.legend(loc="upper right", fontsize=9, frameon=False)
    axC.text(0.04, 0.92, f"$\\alpha_\\mathrm{{peak}}={a_peak:.2e}$\nFWHM$\\approx{fwhm:.2f}$ decades",
             transform=axC.transAxes, va="top", fontsize=8.5,
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="grey", lw=0.5))
    axC.grid(True, ls=":", alpha=0.35)

    save_fig(fig, "Figure1_model_and_baseline")


# ------------------------------------------------------------------
# Figure 2
# ------------------------------------------------------------------
def figure_2():
    print("Figure 2: Kinetic scale and exchange dependence")
    sw01 = load_npz("sweep_kSkT_main_lam0.1_haberkorn.npz")
    sw1 = load_npz("sweep_kSkT_main_lam1.0_haberkorn.npz")
    sw10 = load_npz("sweep_kSkT_main_lam10.0_haberkorn.npz")
    swuJ = load_npz("sweep_uJ_main_final.npz")

    def stats(d):
        u = d["u"]; a = d["alpha"]
        i = int(np.argmax(a))
        h = a[i] / 2.0
        above = a >= h
        if above.any():
            idx = np.where(above)[0]
            fw = float(u[idx[-1]] - u[idx[0]])
        else:
            fw = float("nan")
        return float(u[i]), float(a[i]), fw

    u01s, a01s, f01 = stats(sw01)
    u1s, a1s, f1 = stats(sw1)
    u10s, a10s, f10 = stats(sw10)

    # Normalized RMS deviation between λ=0.1 and λ=1
    a01_n = sw01["alpha"] / a01s
    a1_n = sw1["alpha"] / a1s
    rms_01_1 = float(np.sqrt(np.mean((a01_n - a1_n) ** 2)))
    print(f"  λ=0.1: u*={u01s:+.2f}, peak={a01s:.3e}; λ=1: u*={u1s:+.2f}, peak={a1s:.3e}; λ=10: u*={u10s:+.2f}, peak={a10s:.3e}")
    print(f"  norm RMS dev (λ=0.1 vs λ=1) = {rms_01_1:.3f}")

    fig = plt.figure(figsize=(13, 9))
    gs = fig.add_gridspec(2, 2, hspace=0.38, wspace=0.30)

    # Panel A: raw
    axA = fig.add_subplot(gs[0, 0])
    axA.set_yscale("log")
    axA.plot(sw01["u"], sw01["alpha"], color="#0072b2", lw=1.6, label=r"$\lambda=0.1$")
    axA.plot(sw1["u"], sw1["alpha"], color="#000000", lw=1.6, label=r"$\lambda=1.0$")
    axA.plot(sw10["u"], sw10["alpha"], color="#d55e00", lw=1.6, label=r"$\lambda=10.0$")
    axA.set_xlabel(r"$u = \log_{10}(k_S/k_T)$")
    axA.set_ylabel(r"$\alpha(u)$ (log)")
    axA.set_title("A. Raw $\\alpha(u)$ under absolute-rate scaling", fontsize=11, loc="left", fontweight="bold")
    axA.legend(loc="lower left", fontsize=9, frameon=False)
    axA.grid(True, which="both", ls=":", alpha=0.35)
    axA.text(0.97, 0.97,
             f"peaks: {a01s:.2e}, {a1s:.2e}, {a10s:.2e}\n$u^*$: {u01s:+.2f}, {u1s:+.2f}, {u10s:+.2f}",
             transform=axA.transAxes, ha="right", va="top", fontsize=8.5,
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="grey", lw=0.5))

    # Panel B: normalized
    axB = fig.add_subplot(gs[0, 1])
    axB.plot(sw01["u"], sw01["alpha"] / a01s, color="#0072b2", lw=1.6, label=r"$\lambda=0.1$")
    axB.plot(sw1["u"], sw1["alpha"] / a1s, color="#000000", lw=1.6, label=r"$\lambda=1.0$")
    axB.plot(sw10["u"], sw10["alpha"] / a10s, color="#d55e00", lw=1.6, label=r"$\lambda=10.0$")
    axB.set_xlabel(r"$u = \log_{10}(k_S/k_T)$")
    axB.set_ylabel(r"$\alpha(u)/\max\alpha$")
    axB.set_title("B. Normalized $\\alpha(u)$", fontsize=11, loc="left", fontweight="bold")
    axB.legend(loc="upper right", fontsize=9, frameon=False)
    axB.grid(True, ls=":", alpha=0.35)
    axB.text(0.97, 0.05, f"RMS dev ($\\lambda{{=}}0.1$ vs $\\lambda{{=}}1$) $\\approx${rms_01_1:.2f}",
             transform=axB.transAxes, ha="right", va="bottom", fontsize=8.5,
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="grey", lw=0.5))

    # Panel C: heatmap
    axC = fig.add_subplot(gs[1, 0])
    Z = swuJ["ZH"]
    u_g = swuJ["u"]
    J_g = swuJ["J"]
    pcm = axC.pcolormesh(u_g, J_g, Z.T, cmap="viridis", shading="auto")
    fig.colorbar(pcm, ax=axC, label=r"$\alpha(u, J)$")
    axC.set_xlabel(r"$u = \log_{10}(k_S/k_T)$")
    axC.set_ylabel(r"$J$ (nondim)")
    axC.set_title("C. Heatmap $\\alpha(u, J)$", fontsize=11, loc="left", fontweight="bold")

    # Panel D: summary table
    axD = fig.add_subplot(gs[1, 1])
    axD.axis("off")
    axD.set_title("D. Peak summary", fontsize=11, loc="left", fontweight="bold")
    rows = [
        ["$\\lambda$", "$u^*$", "peak $\\alpha$", "FWHM"],
        ["0.1", f"{u01s:+.2f}", f"{a01s:.2e}", f"{f01:.2f}"],
        ["1.0", f"{u1s:+.2f}", f"{a1s:.2e}", f"{f1:.2f}"],
        ["10.0", f"{u10s:+.2f}", f"{a10s:.2e}", f"{f10:.2f}"],
    ]
    tbl = axD.table(cellText=rows, loc="center", cellLoc="center", colWidths=[0.18, 0.22, 0.32, 0.20])
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(11)
    tbl.scale(1, 1.6)
    for c in range(4):
        tbl[(0, c)].set_facecolor("#dde6ee")
        tbl[(0, c)].set_text_props(weight="bold")
    axD.text(0.5, 0.10,
             "Form is preserved across $\\lambda$;\namplitude varies by ~6 orders of magnitude;\npeak location shifts at small $\\lambda$.",
             transform=axD.transAxes, ha="center", va="top", fontsize=9, style="italic")

    save_fig(fig, "Figure2_kinetic_scale_and_exchange")


# ------------------------------------------------------------------
# Figure 3
# ------------------------------------------------------------------
def figure_3():
    print("Figure 3: Channel-dependent noise response")
    dh = load_npz("sweep_dephasing_main_haberkorn.npz")
    dl = load_npz("sweep_dephasing_main_lindblad.npz")
    t1 = load_npz("sweep_T1_main_final.npz")

    g_h = dh["gamma_v3"]; a_h = dh["alpha_v3"]
    g_l = dl["gamma_v3"]; a_l = dl["alpha_v3"]

    # γ=0 baseline (first point if grid contains 0)
    base_idx = int(np.argmin(g_h)) if (g_h == 0).any() else 0
    a0 = float(a_h[base_idx])
    # γ_opt
    iopt = int(np.argmax(a_h))
    g_opt = float(g_h[iopt])
    a_opt = float(a_h[iopt])
    print(f"  z-deph: γ_opt={g_opt:.2f}, peak={a_opt:.3e}, baseline={a0:.3e}")

    T1g = np.asarray(t1["T1_grid"])
    T1a = np.asarray(t1["alpha"])
    if T1g.ndim == 0:
        v = T1g.item()
        T1g = np.asarray(json.loads(v) if isinstance(v, str) else v)
    if T1a.ndim == 0:
        v = T1a.item()
        T1a = np.asarray(json.loads(v) if isinstance(v, str) else v)
    T1g = T1g.astype(float)
    T1a = T1a.astype(float)
    t1_opt_idx = int(np.argmax(T1a))
    t1_opt = float(T1g[t1_opt_idx])
    t1_amp = float(T1a[t1_opt_idx])
    print(f"  spin-flip: max at Γ₁={t1_opt:.3e}, α={t1_amp:.3e}")
    if t1_opt != 0.0:
        print(f"  WARNING: spin-flip max not at Γ₁=0 ({t1_opt}); per figure plan verification rule")

    fig = plt.figure(figsize=(15, 4.2))
    gs = fig.add_gridspec(1, 3, width_ratios=[1.05, 1.05, 1.05], wspace=0.32)

    # Panel A: dephasing
    axA = fig.add_subplot(gs[0, 0])
    # Filter γ>0 for log axis; show γ=0 as scatter
    pos = g_h > 0
    axA.semilogx(g_h[pos], a_h[pos], color="#1f4e79", lw=1.7, label="Haberkorn")
    axA.semilogx(g_l[g_l > 0], a_l[g_l > 0], color="#d55e00", lw=1.4, ls="--",
                 label="absorbing-product effective")
    axA.scatter([1e-4], [a0], color="#1f4e79", s=24, zorder=5, label=r"$\gamma=0$ baseline")
    axA.axvline(g_opt, color="#c00000", ls=":", lw=1.0, alpha=0.7)
    axA.set_xlabel(r"$\gamma$ (log)")
    axA.set_ylabel(r"$\alpha(\gamma)$")
    axA.set_title("A. $z$-dephasing: $\\mathcal{D}[S_{1z}]+\\mathcal{D}[S_{2z}]$", fontsize=11, loc="left", fontweight="bold")
    axA.legend(loc="upper left", fontsize=8.5, frameon=False)
    axA.grid(True, which="both", ls=":", alpha=0.35)
    axA.text(0.97, 0.97,
             f"$\\gamma_\\mathrm{{opt}}\\approx{g_opt:.2f}$\npeak $\\alpha\\approx${a_opt:.2e}\n($\\sim 2\\times$ over $\\gamma{{=}}0$)",
             transform=axA.transAxes, ha="right", va="top", fontsize=8.5,
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="grey", lw=0.5))

    # Panel B: T1 / spin-flip
    axB = fig.add_subplot(gs[0, 1])
    pos2 = T1g > 0
    axB.semilogx(T1g[pos2], T1a[pos2], color="#1f4e79", lw=1.7, label="Haberkorn (single channel)")
    axB.scatter([1e-4], [t1_amp], color="#1f4e79", s=24, zorder=5, label=r"$\Gamma_1=0$ maximum")
    axB.set_xlabel(r"$\Gamma_1$ (log)")
    axB.set_ylabel(r"$\alpha(\Gamma_1)$")
    axB.set_title("B. Single-electron spin-flip: $(\\Gamma_1/2)(\\mathcal{D}[S_{1+}]+\\mathcal{D}[S_{1-}])$",
                  fontsize=11, loc="left", fontweight="bold")
    axB.legend(loc="upper right", fontsize=8.5, frameon=False)
    axB.grid(True, which="both", ls=":", alpha=0.35)
    axB.text(0.97, 0.85,
             f"max at $\\Gamma_1=0$, $\\alpha\\approx${t1_amp:.2e}\nno enhancement window\n(electron 1 only)",
             transform=axB.transAxes, ha="right", va="top", fontsize=8.5,
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="grey", lw=0.5))

    # Panel C: comparison
    axC = fig.add_subplot(gs[0, 2])
    labels = [r"$\gamma=0$", r"$z$-deph peak", r"spin-flip max"]
    vals = [a0, a_opt, t1_amp]
    colors = ["grey", "#1f4e79", "#c62828"]
    axC.bar(labels, vals, color=colors, width=0.55)
    axC.set_ylabel(r"$\alpha$ at characteristic point")
    axC.set_title("C. Channel-dependent comparison", fontsize=11, loc="left", fontweight="bold")
    for i, v in enumerate(vals):
        axC.text(i, v + 0.04 * max(vals), f"{v:.2e}", ha="center", fontsize=8.5)
    axC.grid(True, axis="y", ls=":", alpha=0.35)
    axC.text(0.5, 0.95, "$z$-dephasing enhances within finite window;\nspin-flip max at $\\Gamma_1=0$ (no enhancement window).",
             transform=axC.transAxes, ha="center", va="top", fontsize=9, style="italic",
             bbox=dict(boxstyle="round,pad=0.3", fc="#f7f7f7", ec="grey", lw=0.5))

    fig.text(0.5, -0.02, "Both noise scans at $u=0$; baseline peak at $u\\approx-0.3$ (near, not exactly at, plateau center).",
             ha="center", fontsize=9, style="italic")

    save_fig(fig, "Figure3_noise_channel_dependence")


# ------------------------------------------------------------------
# Figure 4
# ------------------------------------------------------------------
def figure_4():
    print("Figure 4: Spectral correlate")
    sp = load_npz("sweep_spectral_main_final.npz")

    def to_np(arr):
        a = np.asarray(arr)
        if a.ndim == 0:
            v = a.item()
            if isinstance(v, str):
                v = json.loads(v)
            a = np.asarray(v)
        return a

    u = to_np(sp["u_grid"]).astype(float)
    proxy = to_np(sp["spectral_proxy"]).astype(float)
    alpha = to_np(sp["alpha"]).astype(float)
    eig_real = to_np(sp["eigenvalues_real"]).astype(float)
    s_loss = to_np(sp["S_loss"]).astype(float)
    s_perm = to_np(sp["S_perm"]).astype(float)
    r_proxy = float(sp["proxy_alpha_correlation"])

    expected_r = 0.9125523536208335
    if abs(r_proxy - expected_r) > 1e-6:
        print(f"  WARNING: proxy_alpha_correlation = {r_proxy:.10f} ≠ {expected_r:.10f}; per verification rule")
    else:
        print(f"  proxy_alpha_correlation = {r_proxy:.4f} OK")

    fig = plt.figure(figsize=(15, 4.5))
    gs = fig.add_gridspec(1, 3, width_ratios=[1.05, 1.05, 1.05], wspace=0.32)

    # Panel A: Liouvillian spectrum
    axA = fig.add_subplot(gs[0, 0])
    eig_arr = np.asarray(eig_real)
    if eig_arr.ndim == 2:
        # Plot up to 4 slowest-decaying modes
        slowest = np.sort(eig_arr, axis=1)[:, ::-1]  # least negative first
        n_modes = min(4, slowest.shape[1])
        for k in range(n_modes):
            axA.plot(u, slowest[:, k], lw=1.3, alpha=0.85, label=f"mode {k+1}")
    axA.set_xlabel(r"$u$")
    axA.set_ylabel(r"Re($\lambda_n$)")
    axA.set_title("A. Liouvillian eigenvalues (slowest-decaying)", fontsize=11, loc="left", fontweight="bold")
    axA.legend(loc="lower right", fontsize=8.5, frameon=False, ncol=2)
    axA.grid(True, ls=":", alpha=0.35)

    # Panel B: spectral proxy + α normalized
    axB = fig.add_subplot(gs[0, 1])
    proxy_n = np.asarray(proxy) / np.max(proxy)
    alpha_n = np.asarray(alpha) / np.max(alpha)
    axB.plot(u, proxy_n, color="#1f4e79", lw=1.7, label=r"$\Delta_H(u)/\max$")
    axB.plot(u, alpha_n, color="#c62828", lw=1.5, ls="--", label=r"$\alpha(u)/\max$")
    axB.set_xlabel(r"$u$")
    axB.set_ylabel("normalized")
    axB.set_title("B. Spectral proxy vs anisotropy", fontsize=11, loc="left", fontweight="bold")
    axB.legend(loc="lower left", fontsize=9, frameon=False)
    axB.grid(True, ls=":", alpha=0.35)
    axB.text(0.97, 0.97, f"Pearson $r={r_proxy:.4f}$",
             transform=axB.transAxes, ha="right", va="top", fontsize=9.5,
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="grey", lw=0.5))

    # Panel C: mode-reorganization
    axC = fig.add_subplot(gs[0, 2])
    axC.plot(u, s_loss, color="#2e7d32", lw=1.5, label=r"$S_\mathrm{loss}$ (tracking-loss)")
    axC.plot(u, s_perm, color="#7e2f8e", lw=1.5, ls="--", label=r"$S_\mathrm{perm}$ (permutation)")
    axC.set_xlabel(r"$u$")
    axC.set_ylabel("score")
    axC.set_title("C. Mode-reorganization (descriptive)", fontsize=11, loc="left", fontweight="bold")
    axC.legend(loc="upper right", fontsize=9, frameon=False)
    axC.grid(True, ls=":", alpha=0.35)
    axC.text(0.04, 0.96,
             "Descriptive only;\nnot a robust\nindependent signature.",
             transform=axC.transAxes, ha="left", va="top", fontsize=8.5, style="italic",
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="grey", lw=0.5))

    save_fig(fig, "Figure4_spectral_correlate")


# ------------------------------------------------------------------
# Manifest writer
# ------------------------------------------------------------------
def write_manifest():
    out = OUT_DIR / "figure_manifest.txt"
    with open(out, "w") as f:
        f.write("# Paper 1 figure manifest\n")
        f.write(f"# Generated by {Path(__file__).name}\n")
        f.write(f"# RESULTS_DIR: {RESULTS_DIR}\n")
        f.write(f"# OUT_DIR:     {OUT_DIR}\n")
        f.write("#\n")
        f.write("# kind  sha256                                                            path\n")
        for kind, path, digest in MANIFEST:
            f.write(f"{kind:<6} {digest}  {path}\n")
    print(f"\n  manifest written: {out}")


def main():
    figure_1()
    figure_2()
    figure_3()
    figure_4()
    write_manifest()


if __name__ == "__main__":
    main()
