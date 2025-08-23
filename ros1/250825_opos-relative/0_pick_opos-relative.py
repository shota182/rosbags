#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def detect_scale_to_seconds(first_value: float) -> float:
    fv = abs(float(first_value))
    if fv >= 1e15:
        return 1e9   # ns → s
    elif fv >= 1e12:
        return 1e6   # us → s
    elif fv >= 1e9:
        return 1e3   # ms → s
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", type=str, help="入力CSVパス")
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("--data", type=int, nargs=2, metavar=("I", "J"))
    g.add_argument("--names", type=str, nargs=2, metavar=("NAME_I", "NAME_J"))
    parser.add_argument("--show", action="store_true")
    args = parser.parse_args()

    in_path = Path(args.csv)
    df = pd.read_csv(in_path)

    if "%time" not in df.columns:
        raise ValueError("CSVに %time 列が見つかりません")

    if args.names:
        col_i, col_j = args.names
    else:
        col_i = f"field.data{args.data[0]}"
        col_j = f"field.data{args.data[1]}"

    for c in (col_i, col_j):
        if c not in df.columns:
            raise ValueError(f"列が見つかりません: {c}")

    x_time_s = to_relative_seconds(df["%time"]).to_numpy()
    rel_i = relative_from_first_valid(df[col_i]).to_numpy()
    rel_j = relative_from_first_valid(df[col_j]).to_numpy()

    # --- 保存先を「実行ファイルのディレクトリ/output」に設定 ---
    script_dir = Path(__file__).resolve().parent
    out_dir = script_dir / "output"
    out_dir.mkdir(exist_ok=True)

    safe_i = col_i.replace(".", "_")
    safe_j = col_j.replace(".", "_")
    stem = in_path.with_suffix("").name
    out_csv = out_dir / f"{stem}_rel_{safe_i}_{safe_j}.csv"
    out_png = out_dir / f"{stem}_rel_{safe_i}_{safe_j}.png"

    out_df = pd.DataFrame({
        "time_s": x_time_s,
        f"rel_{col_i}": rel_i,
        f"rel_{col_j}": rel_j,
    })
    out_df.to_csv(out_csv, index=False)

    plt.figure(figsize=(10, 5))
    plt.plot(x_time_s, rel_i, label=f"Relative {col_i}")
    plt.plot(x_time_s, rel_j, label=f"Relative {col_j}")
    plt.xlabel("time [s]")
    plt.ylabel("relative value")
    plt.title("Relative values from initial")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_png, dpi=150)

    if args.show:
        plt.show()
    else:
        plt.close()

    print(f"Saved CSV : {out_csv}")
    print(f"Saved Plot: {out_png}")


if __name__ == "__main__":
    main()
