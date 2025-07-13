#!/usr/bin/env python3
"""
interactive_plot_v3_py38_fix.py
  • Figure "Plot"    : データ曲線
  • Figure "Control" : TextBox×2（start/end）
                       + RadioButtons(3択)
                       + Button「Browse」（CSV 選択）
                       + Button「Plot / Update」
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button, RadioButtons
from typing import Optional

# -------- Tkinter のファイルダイアログ -----------------------------------
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()          # ルートウィンドウは表示しない


# -------- プロット関数 ---------------------------------------------------
def draw_plot(ax,
              csv_path: str,
              start_sec: float,
              end_sec: Optional[float],
              mode: str,
              gradient_threshold: float = 10.0) -> None:
    """CSV を読み込み、ax に描画（既存内容はクリア）"""
    ax.clear()

    df = pd.read_csv(csv_path)
    df["time_sec"] = df["%time"] * 1e-9
    t0 = df["time_sec"].iloc[0]
    df["relative_time"] = df["time_sec"] - t0

    if end_sec is None:
        end_sec = df["relative_time"].max()

    df_r = df[(df["relative_time"] >= start_sec) &
              (df["relative_time"] <= end_sec)]

    colors = ["red", "blue", "green", "orange",
              "cyan", "magenta", "yellow", "lime"]
    pattern = [-1, -1, 1, 1, -1, -1, 1, 1]   # 符号パターン

    for i, col in enumerate(df.columns):
        if not col.startswith("field.data"):
            continue

        if mode == "raw":
            data = df_r[col].to_numpy()

        elif mode == "relative":
            data = df_r[col].to_numpy() - df[col].iloc[0]

        elif mode == "relative_dir":
            sign = pattern[i % len(pattern)]          # ★ 添字を循環
            data = sign * (df_r[col].to_numpy() - df[col].iloc[0])

        else:    # フォールバック
            data = df_r[col].to_numpy()

        ax.plot(df_r["relative_time"].to_numpy(),
                data,
                lw=0.5,
                color=colors[i % len(colors)],
                label=col)

    title_mode = {"raw": "Raw",
                  "relative": "Relative",
                  "relative_dir": "Relative(dir)"}[mode]
    ax.set_title(f"{os.path.basename(csv_path)} "
                 f"[{start_sec:.2f}–{end_sec:.2f} s]  ({title_mode})")
    ax.set_xlabel("Relative Time [s]")
    ax.set_ylabel("Data Value")
    ax.grid(True)
    ax.legend(fontsize=8)
    ax.figure.canvas.draw_idle()


# -------- メイン ---------------------------------------------------------
def main() -> None:
    # プロットウィンドウ
    fig_plot, ax_plot = plt.subplots(num="Plot")

    # コントロールウィンドウ
    fig_ctl = plt.figure(num="Control", figsize=(4.6, 4.6))

    # TextBox（CSV パス表示のみ）―― 手入力不要・コピー可
    csv_path_var = {"path": ""}
    ax_txt_csv = fig_ctl.add_axes([0.05, 0.82, 0.90, 0.12])
    tb_csv = TextBox(ax_txt_csv, "CSV Path", initial="", color=".95")
    tb_csv.set_active(False)  # 編集不可

    # Browse ボタン
    ax_btn_browse = fig_ctl.add_axes([0.30, 0.70, 0.40, 0.10])
    btn_browse = Button(ax_btn_browse, "Browse")

    # TextBox（Start / End）
    ax_box_start = fig_ctl.add_axes([0.05, 0.55, 0.42, 0.10])
    tb_start = TextBox(ax_box_start, "Start [s]", initial="0")

    ax_box_end = fig_ctl.add_axes([0.53, 0.55, 0.42, 0.10])
    tb_end = TextBox(ax_box_end, "End [s] (空=全体)", initial="")

    # RadioButtons（3択）
    ax_radio = fig_ctl.add_axes([0.05, 0.30, 0.90, 0.18])
    radio = RadioButtons(ax_radio,
                         ("Raw", "Relative", "Relative(dir)"),
                         active=0)

    # Plot / Update ボタン
    ax_btn_plot = fig_ctl.add_axes([0.30, 0.10, 0.40, 0.12])
    btn_plot = Button(ax_btn_plot, "Plot / Update")

    # -------- コールバック ---------------------------------------------
    def browse(_event=None):
        file_path = filedialog.askopenfilename(
            title="Select CSV file",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if file_path:
            csv_path_var["path"] = file_path
            tb_csv.set_val(file_path)

    def update(_event=None):
        csv_path = csv_path_var["path"]
        if not csv_path:
            print("[警告] CSV ファイルが指定されていません。")
            return
        if not os.path.isfile(csv_path):
            print(f"[警告] CSV が見つかりません: {csv_path}")
            return

        start = float(tb_start.text or 0.0)
        end_txt = tb_end.text.strip()
        end: Optional[float] = float(end_txt) if end_txt else None

        mode_map = {"Raw": "raw",
                    "Relative": "relative",
                    "Relative(dir)": "relative_dir"}
        mode = mode_map[radio.value_selected]

        draw_plot(ax_plot, csv_path, start, end, mode)

    # イベント紐付け
    btn_browse.on_clicked(browse)
    btn_plot.on_clicked(update)
    tb_start.on_submit(lambda _txt: update())
    tb_end.on_submit(lambda _txt: update())
    radio.on_clicked(lambda _lbl: update())

    plt.show()


if __name__ == "__main__":
    main()
