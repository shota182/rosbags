#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
7/21
復元力をデータから取得できるか確認するため.
oposとfをプロットして比較する.
また，指定したファイルのディレクトリにファイルを保存する.
[time, opos.data1相対, opos.data2相対, f.data1補間, f.data2補間] の形式で保存する.

・ 機能
1.  CSV①（粗いデータ）から 2 列を選択し，
    各列を「初回サンプルとの差分（相対変化量）」に変換  
2.  CSV②（細かいデータ）から 2 列を選択し，
    CSV① の時刻に合わせて線形補間
3.  (相対変化量列1, 相対変化量列2, 補間列1) を 3 次元プロット  
4.  (相対変化量列1, 相対変化量列2, 補間列2) を 3 次元プロット  
"""

###############################################################################
# 変数 ----------------------------------------------------
###############################################################################
CSV1_PATH   = "/home/sskr3/bags/ros1/2025-07-21-12-17-06/2025-07-21-12-17-06.bag_opos.csv"                 # 粗い CSV
CSV2_PATH   = "/home/sskr3/bags/ros1/2025-07-21-12-17-06/2025-07-21-12-17-06.bag_f.csv"                 # 細かい CSV

CSV1_COLS   = ["field.data4", "field.data7"]      # 相対変化量を取る列 2 本
CSV2_COLS   = ["field.data4", "field.data7"]      # 絶対値で補間する列 2 本

PLOT_TITLE1 = f"3D Plot 1 : {CSV2_COLS[0]}"
PLOT_TITLE2 = f"3D Plot 2 : {CSV2_COLS[1]}"
SAVE_MERGED = True                                # False にすると保存しません
###############################################################################

import argparse
import pathlib
import sys
import os                # ← 保存先ディレクトリ取得用

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D          # noqa: F401  ← 3D 用に必要な import

###############################################################################
# ユーティリティ
###############################################################################

def load_and_prepare_csv1(path: pathlib.Path, col_a: str, col_b: str):
    """CSV① を読み込み、相対変化量 2 列と time を返す。"""
    df = pd.read_csv(path)
    t1 = df["%time"].to_numpy(dtype=np.int64)
    a_rel = df[col_a].to_numpy() - df[col_a].iloc[0]
    b_rel = df[col_b].to_numpy() - df[col_b].iloc[0]
    return t1, a_rel, b_rel


def load_and_interpolate_csv2(path: pathlib.Path, t_target: np.ndarray,
                              col_c: str, col_d: str):
    """CSV② を読み込み、t_target に合わせて 2 列を線形補間。"""
    df = pd.read_csv(path)
    t2 = df["%time"].to_numpy(dtype=np.int64)

    idx = np.argsort(t2)           # 念のため時刻でソート
    t2_sorted = t2[idx]
    c_vals = df[col_c].to_numpy()[idx]
    d_vals = df[col_d].to_numpy()[idx]

    c_interp = np.interp(t_target, t2_sorted, c_vals)
    d_interp = np.interp(t_target, t2_sorted, d_vals)
    return c_interp, d_interp


def make_3d_plot(x, y, z, title, ax, xlabel, ylabel):
    """3D 線プロットを 1 枚描画。"""
    ax.plot3D(x, y, z, lw=1.0)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(title.split(" : ")[-1])
    ax.set_title(title)
    ax.grid(True)


###############################################################################
# メイン処理
###############################################################################

def main():
    csv1_path = pathlib.Path(CSV1_PATH).expanduser().resolve()
    csv2_path = pathlib.Path(CSV2_PATH).expanduser().resolve()

    # 1) CSV① 読み込み（相対変化量）
    t1, x_rel, y_rel = load_and_prepare_csv1(
        csv1_path, CSV1_COLS[0], CSV1_COLS[1])

    # 2) CSV② 読み込み & 補間
    z1_abs, z2_abs = load_and_interpolate_csv2(
        csv2_path, t1, CSV2_COLS[0], CSV2_COLS[1])

    # 3) 3D プロット
    fig = plt.figure(figsize=(12, 5))
    ax1 = fig.add_subplot(1, 2, 1, projection="3d")
    ax2 = fig.add_subplot(1, 2, 2, projection="3d")

    xlabel = f"csv1 Δ{CSV1_COLS[0]}"
    ylabel = f"csv1 Δ{CSV1_COLS[1]}"

    make_3d_plot(x_rel, y_rel, z1_abs,
                 f"3D Plot 1 : {CSV2_COLS[0]}", ax1, xlabel, ylabel)
    make_3d_plot(x_rel, y_rel, z2_abs,
                 f"3D Plot 2 : {CSV2_COLS[1]}", ax2, xlabel, ylabel)

    plt.tight_layout()

    # 4) 整列済み CSV 保存
    if SAVE_MERGED:
        save_dir = csv1_path.parent
        out_name = f"{csv1_path.stem}_f.csv"
        out_path = save_dir / out_name

        merged_df = pd.DataFrame({
            "time": t1,
            f"csv1_{CSV1_COLS[0]}": x_rel,
            f"csv1_{CSV1_COLS[1]}": y_rel,
            f"csv2_{CSV2_COLS[0]}": z1_abs,
            f"csv2_{CSV2_COLS[1]}": z2_abs,
        })
        merged_df.to_csv(out_path, index=False)
        print(f"[INFO] Merged CSV saved to: {out_path}")

    plt.show()

###############################################################################
# エントリポイント
###############################################################################

if __name__ == "__main__":
    main()
