import sys
import os
import io
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

root_dir = r"f:\0. bank\0. work\sys design"
assets_dir = os.path.join(root_dir, "linkedin_post_assets")
vault_dir = os.path.join(root_dir, "LinkedIn_Posting_Vault")

def setup_canvas(title, subtitle, step_text="", accent="#38bdf8"):
    fig, ax = plt.subplots(figsize=(16, 9), dpi=120)
    fig.patch.set_facecolor('#070b14')
    ax.set_facecolor('#070b14')
    ax.set_xlim(0, 160)
    ax.set_ylim(0, 90)
    ax.axis('off')

    bg_glow = patches.Circle((80, 45), 65, facecolor=accent, alpha=0.03)
    ax.add_patch(bg_glow)

    ax.text(8, 84, title, color='#ffffff', fontsize=14.5, fontweight='bold', fontfamily='sans-serif')
    sub_full = f"{step_text}  •  {subtitle}" if step_text else subtitle
    ax.text(8, 79.5, sub_full, color=accent, fontsize=9.5, fontfamily='sans-serif')
    
    ax.text(152, 84, "PREET KARWAL", color='#ffffff', fontsize=10.5, fontweight='bold', ha='right', fontfamily='sans-serif')
    ax.text(152, 79.5, "Distributed Systems Masterclass  •  @Mr-Elegant", color='#94a3b8', fontsize=8.2, ha='right', fontfamily='sans-serif')
    ax.plot([8, 152], [75, 75], color='#1e293b', lw=1.8)

    return fig, ax

def draw_node(ax, x, y, w, h, icon, title, subtitle, badge="", bg="#0f172a", border="#38bdf8", is_active=False):
    shadow = patches.FancyBboxPatch((x + 0.6, y - 0.6), w, h, boxstyle="round,pad=0.6", facecolor="#020617", edgecolor="none", alpha=0.8)
    ax.add_patch(shadow)
    
    edge_col = "#fde68a" if is_active else border
    bg_col = "#1e293b" if is_active else bg
    lw = 2.4 if is_active else 1.2
    box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.6", linewidth=lw, edgecolor=edge_col, facecolor=bg_col)
    ax.add_patch(box)
    
    if badge:
        b_box = patches.FancyBboxPatch((x + 2, y + h - 4.5), len(badge)*1.2 + 3.5, 3.6, boxstyle="round,pad=0.25", facecolor="#f59e0b" if is_active else "#0284c7", edgecolor="none")
        ax.add_patch(b_box)
        ax.text(x + 3.5, y + h - 2.8, badge.upper(), color="#ffffff", fontsize=6.8, fontweight='bold', fontfamily='sans-serif')

    ax.text(x + w/2, y + h/2 + 2.5, f"{icon}  {title}", color="#ffffff", fontsize=10, fontweight='bold', ha='center', va='center', fontfamily='sans-serif')
    if subtitle:
        ax.text(x + w/2, y + h/2 - 4.5, subtitle, color="#38bdf8" if is_active else "#94a3b8", fontsize=7.8, ha='center', va='center', fontfamily='sans-serif')

def draw_db_cylinder(ax, x, y, w, h, name, subtitle, status_text="", is_active=False):
    edge_col = "#10b981" if is_active else "#475569"
    bg_col = "#064e3b" if is_active else "#0f172a"
    lw = 2.4 if is_active else 1.2
    
    body = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.5", linewidth=lw, edgecolor=edge_col, facecolor=bg_col)
    ax.add_patch(body)
    
    top_disc = patches.Ellipse((x + w/2, y + h), w*0.85, 3.2, facecolor="#047857" if is_active else "#1e293b", edgecolor=edge_col, lw=lw)
    ax.add_patch(top_disc)
    
    ax.text(x + w/2, y + h/2 + 4, f"[DB]  {name}", color="#ffffff", fontsize=9.5, fontweight='bold', ha='center', va='center', fontfamily='sans-serif')
    if subtitle:
        ax.text(x + w/2, y + h/2 - 1.5, subtitle, color="#34d399" if is_active else "#94a3b8", fontsize=7.5, ha='center', va='center', fontfamily='sans-serif')
    if status_text:
        ax.text(x + w/2, y + h/2 - 6.5, status_text, color="#fde68a" if is_active else "#64748b", fontsize=7.2, fontweight='bold' if is_active else 'normal', ha='center', va='center', fontfamily='sans-serif')

def draw_insight_banner(ax, tag, text, is_success=True):
    banner = patches.FancyBboxPatch((8, 3), 144, 6.8, boxstyle="round,pad=0.4", facecolor="#0f172a", edgecolor="#10b981" if is_success else "#f59e0b", lw=1.5)
    ax.add_patch(banner)
    ax.text(12, 6.2, tag.upper(), color="#10b981" if is_success else "#f59e0b", fontsize=8.2, fontweight='bold', fontfamily='sans-serif')
    ax.text(42, 6.2, text, color="#e2e8f0", fontsize=7.8, fontfamily='sans-serif')

def save_flow_pack(frames, fname, sfolder, subfolder):
    # Save High-Res PNG (First frame or last summary frame)
    png_path = os.path.join(assets_dir, f"{fname}.png")
    frames[-1].save(png_path)
    
    # Save Animated GIF
    gif_path = os.path.join(assets_dir, f"{fname}.gif")
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=1800, loop=0)
    
    # Copy to Vault
    if sfolder and subfolder:
        vdir = os.path.join(vault_dir, sfolder, subfolder)
        os.makedirs(vdir, exist_ok=True)
        frames[-1].save(os.path.join(vdir, "high_res_diagram.png"))
        frames[0].save(os.path.join(vdir, "animated_diagram.gif"), save_all=True, append_images=frames[1:], duration=1800, loop=0)
    print(f"✅ Generated Physical Diagram & GIF: {fname}")

print("Physical Architecture Core Engine initialized.")
