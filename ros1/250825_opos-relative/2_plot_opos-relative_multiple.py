#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

def main():
    import argparse
    parser = argparse.ArgumentParser(description="指定ディレクトリ内のCSVを重ねて散布図表示（保存なし）")
    parser.add_argument("directory", nargs="?", default=".", help="CSVを探すディレクトリ（省略時はカレントディレクトリ）")
    parser.add_argument("pattern", nargs="?", default="*.csv", help="読み込むCSVのパターン（既定: *.csv）")
    parser.add_argument("--size", type=float, default=12.0, help="散布点サイズ（既定: 12）")
    parser.add_argument("--alpha", type=float, default=0.8, help="点の透明度（既定: 0.8）")
    args = parser.parse_args()

    target_dir = os.path.abspath(args.directory)
    csv_files = sorted(glob.glob(os.path.join(target_dir, args.pattern)))
    if not csv_files:
        print(f"No CSV files matched: {os.path.join(target_dir, args.pattern)}")
        return

    print(f"Found {len(csv_files)} CSV files in {target_dir}")

    plt.figure(figsize=(7, 7))

    for csv_path in csv_files:
        df = pd.read_csv(csv_path)

        # 2列目 vs 3列目（列名は使わない）
        x = df.iloc[:, 1]
        y = df.iloc[:, 2]

        label = os.path.splitext(os.path.basename(csv_path))[0]
        plt.scatter(x, y, s=args.size, alpha=args.alpha, label=label)

    plt.xlabel("Column 2")
    plt.ylabel("Column 3")
    plt.title(f"Overlay Scatter ({len(csv_files)} files)")
    plt.grid(True, alpha=0.3)
    plt.axis("equal")
    plt.legend(loc="best", fontsize=7)
    plt.tight_layout()
    plt.show()  # 保存せず表示のみ

if __name__ == "__main__":
    main()
