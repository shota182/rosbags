#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# ===== 入力 =====
csv_file = "/home/sskr3/bags/ros1/250825_opos-relative/output/2025-08-04-11-37-00.bag_opos_rel_field_data2_field_data3.csv"   # ここを置き換え
EPS_SIGN = 0.0
MIN_SEG  = 5

# ===== データ読み込み =====
df = pd.read_csv(csv_file)
t  = pd.to_numeric(df.iloc[:,0], errors="coerce").to_numpy()
c2 = pd.to_numeric(df.iloc[:,1], errors="coerce").to_numpy()
c3 = pd.to_numeric(df.iloc[:,2], errors="coerce").to_numpy()

# ===== 選択系列：片方のみ正→その正，それ以外→c3 =====
choose_c2 = (c2 > EPS_SIGN) & ~(c3 > EPS_SIGN)
chosen    = np.where(choose_c2, c2, c3)

# ===== 符号で大まか区間化（短区間吸収）=====
sign_flag = np.where(chosen >= EPS_SIGN, "pos", "neg")
starts = [0]
for i in range(1, len(sign_flag)):
    if sign_flag[i] != sign_flag[i-1]:
        starts.append(i)
starts.append(len(sign_flag))

labels = sign_flag.copy()
for k in range(len(starts)-1):
    s, e = starts[k], starts[k+1]
    if e - s < MIN_SEG:
        if s > 0:
            labels[s:e] = labels[s-1]
        elif e < len(labels):
            labels[s:e] = labels[e]

# 吸収後にランを取り直し
starts = [0]
for i in range(1, len(labels)):
    if labels[i] != labels[i-1]:
        starts.append(i)
starts.append(len(labels))

# ===== 区間内で極値1点→前後で2分割（pos: 最大, neg: 最小）=====
state = np.empty(len(chosen), dtype=object)
ext_idx_all = []
for k in range(len(starts)-1):
    s, e = starts[k], starts[k+1]
    seg = chosen[s:e]
    if len(seg) <= 1:
        state[s:e] = "pos_pos" if labels[s]=="pos" else "neg_neg"
        continue
    if labels[s] == "pos":
        pk, _ = find_peaks(seg)
        peak_local = int(pk[np.argmax(seg[pk])]) if len(pk)>0 else int(np.argmax(seg))
        peak_idx = s + peak_local
        ext_idx_all.append(peak_idx)
        state[s:peak_idx+1] = "pos_pos"   # 極値へ向かう：増加
        state[peak_idx+1:e] = "pos_neg"   # 極値から離れる：減少
    else:
        pk, _ = find_peaks(-seg)
        trough_local = int(pk[np.argmax((-seg)[pk])]) if len(pk)>0 else int(np.argmin(seg))
        trough_idx = s + trough_local
        ext_idx_all.append(trough_idx)
        state[s:trough_idx+1] = "neg_neg" # 極値へ向かう：減少
        state[trough_idx+1:e] = "neg_pos" # 極値から離れる：増加

# ===== プロット（表示のみ・保存なし）=====
state_colors = {"pos_pos":"#2ca02c","pos_neg":"#1f77b4","neg_pos":"#ff7f0e","neg_neg":"#d62728"}
state_bg = {"pos_pos":(0.7,1.0,0.7,0.18),"pos_neg":(0.7,0.7,1.0,0.18),
            "neg_pos":(1.0,0.85,0.6,0.18),"neg_neg":(1.0,0.7,0.7,0.18)}

# 図1: c2 vs c3
plt.figure(figsize=(6, 6))
for st in ["pos_pos","pos_neg","neg_pos","neg_neg"]:
    mask = (state == st)
    if np.any(mask):
        plt.scatter(c2[mask], c3[mask], s=12, label=st, color=state_colors[st], alpha=0.9)
plt.xlabel("Column 2"); plt.ylabel("Column 3")
plt.title("Scatter: Column2 vs Column3 (state by sign+extrema)")
plt.grid(True, alpha=0.3); plt.axis("equal"); plt.legend(loc="best", fontsize=9)
plt.tight_layout()

# 図2: 時間×選択系列（背景＝状態，×＝極値）
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(t, chosen, lw=1.6, color="k", label="chosen_series")

sarr = np.array(state, dtype=object)
chg = np.r_[0, np.flatnonzero(sarr[1:] != sarr[:-1]) + 1]  # 先頭0を入れて最初の区間を確実に塗る
ends = np.r_[chg[1:], len(sarr)]
for s, e in zip(chg, ends):
    st = sarr[s]
    ax.axvspan(t[s], t[e-1], facecolor=state_bg[st], edgecolor="none")

if len(ext_idx_all) > 0:
    ax.scatter(t[ext_idx_all], chosen[ext_idx_all], marker="x", s=36,
               c="magenta", linewidths=1.5, label="extrema")

ax.set_xlabel("Time"); ax.set_ylabel("Chosen series value")
ax.set_title("Time vs chosen series (states by sign + one-extremum split)")
ax.grid(True, alpha=0.3); ax.legend(loc="best", fontsize=9)
plt.tight_layout()
plt.show()

# ===== CSV保存：pos_pos と neg_neg だけ抽出 =====
out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output-3")
os.makedirs(out_dir, exist_ok=True)
base = os.path.splitext(os.path.basename(csv_file))[0]
out_csv = os.path.join(out_dir, f"{base}_pospos_negneg.csv")

mask_keep = (sarr == "pos_pos") | (sarr == "neg_neg")
# 元データに付帯情報を付けて保存（必要列のみでも可）
out_df = pd.DataFrame({
    "time": t[mask_keep],
    "col2": c2[mask_keep],
    "col3": c3[mask_keep],
    "chosen": chosen[mask_keep],
    "state": sarr[mask_keep],
})
out_df.to_csv(out_csv, index=False, encoding="utf-8")
print(f"Saved: {out_csv}")
