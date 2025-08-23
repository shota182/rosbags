#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


# ========== Utility (from 0_pick_opos-relative.py) ==========
def detect_scale_to_seconds(first_value: float) -> float:
    fv = abs(float(first_value))
    if fv >= 1e15:   # ns
        return 1e9
    elif fv >= 1e12: # us
        return 1e6
    elif fv >= 1e9:  # ms
        return 1e3
    else:
        return 1.0   # s

def to_relative_seconds(t_series: pd.Series) -> np.ndarray:
    if t_series.isna().all():
        raise ValueError("%time が全て NaN です")
    t0 = t_series.dropna().iloc[0]
    scale = detect_scale_to_seconds(t0)
    t_int = t_series.astype("int64")
    return (t_int - int(t0)) / scale

def relative_from_first_valid(series: pd.Series) -> pd.Series:
    first_valid = series.dropna().iloc[0]
    return series - first_valid


# ========== Main unified pipeline ==========
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", type=str, help="入力CSV（bag_opos.csvなど）")
    parser.add_argument("--data", type=int, nargs=2, metavar=("I", "J"), required=True,
                        help="列番号を指定 (例: 2 3)")
    args = parser.parse_args()

    in_path = Path(args.csv)
    df = pd.read_csv(in_path)

    if "%time" not in df.columns:
        raise ValueError("CSVに %time 列がありません")

    col_i = f"field.data{args.data[0]}"
    col_j = f"field.data{args.data[1]}"
    for c in (col_i, col_j):
        if c not in df.columns:
            raise ValueError(f"列が見つかりません: {c}")

    # --- Step1: 相対化 ---
    x_time_s = to_relative_seconds(df["%time"]).to_numpy()
    rel_i = relative_from_first_valid(df[col_i]).to_numpy()
    rel_j = relative_from_first_valid(df[col_j]).to_numpy()

    rel_df = pd.DataFrame({
        "time_s": x_time_s,
        f"rel_{col_i}": rel_i,
        f"rel_{col_j}": rel_j,
    })

    # 出力用の名前（相対化結果CSVは保存せず，内部で使う）
    c2 = rel_df.iloc[:,1].to_numpy()
    c3 = rel_df.iloc[:,2].to_numpy()
    t  = rel_df.iloc[:,0].to_numpy()

    # --- Step2: 分類処理 (from 1_grouping_opos-state.py) ---
    EPS_SIGN = 0.0
    MIN_SEG  = 5
    choose_c2 = (c2 > EPS_SIGN) & ~(c3 > EPS_SIGN)
    chosen    = np.where(choose_c2, c2, c3)

    # 符号区間化
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

    # 再ラン検出
    starts = [0]
    for i in range(1, len(labels)):
        if labels[i] != labels[i-1]:
            starts.append(i)
    starts.append(len(labels))

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
            state[s:peak_idx+1] = "pos_pos"
            state[peak_idx+1:e] = "pos_neg"
        else:
            pk, _ = find_peaks(-seg)
            trough_local = int(pk[np.argmax((-seg)[pk])]) if len(pk)>0 else int(np.argmin(seg))
            trough_idx = s + trough_local
            ext_idx_all.append(trough_idx)
            state[s:trough_idx+1] = "neg_neg"
            state[trough_idx+1:e] = "neg_pos"

    # --- Step3: プロット表示 (保存しない) ---
    state_colors = {"pos_pos":"#2ca02c","pos_neg":"#1f77b4",
                    "neg_pos":"#ff7f0e","neg_neg":"#d62728"}
    state_bg = {"pos_pos":(0.7,1.0,0.7,0.18),"pos_neg":(0.7,0.7,1.0,0.18),
                "neg_pos":(1.0,0.85,0.6,0.18),"neg_neg":(1.0,0.7,0.7,0.18)}

    # 散布図
    plt.figure(figsize=(6,6))
    for st in state_colors:
        mask = (state == st)
        if np.any(mask):
            plt.scatter(c2[mask], c3[mask], s=12, label=st,
                        color=state_colors[st], alpha=0.9)
    plt.xlabel("Column 2"); plt.ylabel("Column 3")
    plt.title("Scatter: Column2 vs Column3")
    plt.grid(True, alpha=0.3); plt.axis("equal")
    plt.legend(loc="best", fontsize=9)
    plt.tight_layout()

    # 時間系列
    fig, ax = plt.subplots(figsize=(10,4))
    ax.plot(t, chosen, lw=1.6, color="k", label="chosen_series")

    sarr = np.array(state, dtype=object)
    chg = np.r_[0, np.flatnonzero(sarr[1:] != sarr[:-1]) + 1]
    ends = np.r_[chg[1:], len(sarr)]
    for s, e in zip(chg, ends):
        st = sarr[s]
        ax.axvspan(t[s], t[e-1], facecolor=state_bg[st], edgecolor="none")

    if ext_idx_all:
        ax.scatter(t[ext_idx_all], chosen[ext_idx_all], marker="x",
                   s=36, c="magenta", linewidths=1.5, label="extrema")

    ax.set_xlabel("Time"); ax.set_ylabel("Chosen value")
    ax.set_title("Time vs chosen series (state split by extremum)")
    ax.grid(True, alpha=0.3); ax.legend(loc="best", fontsize=9)
    plt.tight_layout()
    plt.show()

    # --- Step4: CSV保存（pos_pos と neg_negのみ）---
    out_dir = Path(__file__).resolve().parent / "output-3"
    out_dir.mkdir(exist_ok=True)
    # 保存ファイル名を入力ファイル名 + data番号付きにする
    base = in_path.with_suffix("").name
    i, j = args.data
    out_csv = out_dir / f"{base}_data{i}_{j}_pospos_negneg.csv"

    mask_keep = (sarr=="pos_pos") | (sarr=="neg_neg")
    out_df = pd.DataFrame({
        "time": t[mask_keep],
        "col2": c2[mask_keep],
        "col3": c3[mask_keep],
        "chosen": chosen[mask_keep],
        "state": sarr[mask_keep],
    })
    out_df.to_csv(out_csv, index=False, encoding="utf-8")
    print(f"Saved: {out_csv}")


if __name__ == "__main__":
    main()
