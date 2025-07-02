# csvファイルの全データをプロットするスクリプト
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_csv_data(csv_file, start_sec=0.0, end_sec=None, gradient_threshold=10.0):
    # CSVを読み込む
    df = pd.read_csv(csv_file)

    # ナノ秒を秒に変換し、相対時刻を計算
    df["time_sec"] = df["%time"] * 1e-9
    start_time = df["time_sec"].iloc[0]  # 最初の時刻を基準にする
    df["relative_time"] = df["time_sec"] - start_time

    # 時刻範囲でデータを抽出
    if end_sec is None:
        end_sec = df["relative_time"].max()
    df_range = df[(df["relative_time"] >= start_sec) & (df["relative_time"] <= end_sec)]

    colorlist = ["red", "blue", "green", "orange", "cyan", "pink", "yellow", "lime"]

    direction = [-1, -1, 1, 1, -1, -1, 1, 1]
    # ノイズを検出して補間
    c = 0
    for col in df.columns:
        if col.startswith("field.data"):
            data_raw = df_range[col].to_numpy()
            # data_raw = direction[c] * (df_range[col].to_numpy() - df[col].iloc[0])  # 相対値に変換

            # 変化率を計算
            gradients = np.abs(np.diff(data_raw))

            # ノイズを検出 (変化率が閾値を超える場合)
            outliers = gradients > gradient_threshold

            # ノイズのインデックスを取得
            outlier_indices = np.where(outliers)[0] + 1  # +1で次の点をノイズとして扱う

            # ノイズを直線補間
            data_raw[outlier_indices] = np.interp(
                outlier_indices,  # ノイズのインデックス
                np.arange(len(data_raw))[~np.isin(np.arange(len(data_raw)), outlier_indices)],  # ノイズ以外のインデックス
                data_raw[~np.isin(np.arange(len(data_raw)), outlier_indices)]  # ノイズ以外のデータ
            )

            # プロット
            plt.plot(df_range["relative_time"].to_numpy(), data_raw, label=col, color=colorlist[c])
            c += 1

    plt.xlabel("Relative Time (seconds)", fontsize=14)
    plt.ylabel("Data Value", fontsize=14)
    # plt.ylim([0, 5])  # Y軸の範囲を設定
    plt.title(f"Data Plot from {start_sec}s to {end_sec}s", fontsize=16)
    plt.legend(fontsize=12)
    plt.grid()
    plt.show()

# 入力CSVファイル
input_csv = "/home/sskr3/bags/ros1/2025-07-02-16-13-52_f.csv"

# 時刻範囲を指定 (相対秒単位)
start_sec = 0.00  # 開始時刻（相対秒）
end_sec = 50.00    # 終了時刻（相対秒）

# プロット
plot_csv_data(input_csv, start_sec, end_sec, gradient_threshold=10.0)