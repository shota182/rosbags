#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
overlay_many_merged_csvs.py
  • merged CSV をリストで指定
  • (X_COL, Y_COL, Z_COL) を 3D 座標にして 1 枚の軌跡図に重ね描き
"""

###############################################################################
# ★ ここを書き換えてください ★
###############################################################################
MERGED_CSV_LIST = [
    "/home/sskr3/bags/ros1/2025-07-21-12-03-00/2025-07-21-12-03-00.bag_opos_f.csv",
    "/home/sskr3/bags/ros1/2025-07-21-12-06-31/2025-07-21-12-06-31.bag_opos_f.csv",
    "/home/sskr3/bags/ros1/2025-07-21-12-17-06/2025-07-21-12-17-06.bag_opos_f.csv"
    # 必要に応じて追加
]

X_COL = "csv1_field.data4"     # X 軸に使う列
Y_COL = "csv1_field.data7"     # Y 軸に使う列
Z_COL = "csv2_field.data4"     # Z 軸に使う列
###############################################################################

import pathlib
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D   # noqa: F401

def load_xyz(csv_path: pathlib.Path, xcol: str, ycol: str, zcol: str):
    """merged CSV ⇒ 指定 3 列を NumPy 配列で返す。"""
    df = pd.read_csv(csv_path)
    try:
        return df[xcol].to_numpy(), df[ycol].to_numpy(), df[zcol].to_numpy()
    except KeyError as e:
        raise KeyError(f"{csv_path.name} に列 {e} が見つかりません") from None

def main():
    if not MERGED_CSV_LIST:
        print("MERGED_CSV_LIST が空です。ファイルパスを設定してください。")
        return

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")

    for csv_str in MERGED_CSV_LIST:
        csv_path = pathlib.Path(csv_str).expanduser().resolve()
        x, y, z = load_xyz(csv_path, X_COL, Y_COL, Z_COL)
        ax.plot3D(x, y, z, lw=1.2, label=csv_path.stem)

    ax.set_xlabel(X_COL)
    ax.set_ylabel(Y_COL)
    ax.set_zlabel(Z_COL)
    ax.set_title("Overlay of Trajectories")
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
