# 2つのcsvファイルの全データをプロットするスクリプト
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def process_csv(csv_file, start_sec=0.0, end_sec=None, gradient_threshold=10.0, relative=True):
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

    # ノイズを検出して補間
    processed_data = {}
    for col in df.columns:
        if col.startswith("field.data"):
            if(relative):
                data_raw = df_range[col].to_numpy() - df_range[col].iloc[0]  # 相対値に変換
            else:
                data_raw = df_range[col].to_numpy()

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

            processed_data[col] = (df_range["relative_time"].to_numpy(), data_raw)

    return processed_data

def plot_csv_data(csv_file1, csv_file2, start_sec=0.0, end_sec=None, gradient_threshold=10.0):
    # CSVファイルを処理
    data1 = process_csv(csv_file1, start_sec, end_sec, gradient_threshold, False)
    data2 = process_csv(csv_file2, start_sec, end_sec, gradient_threshold)

    # プロット
    fig, axes = plt.subplots(2, 1, figsize=(10, 12), sharex=True)

    # 1つ目のCSVデータをプロット
    colorlist = ["red", "blue", "green", "orange", "cyan", "pink", "yellow", "lime"]
    c = 0
    for col, (time, values) in data1.items():
        axes[0].plot(time, values, label=col, color=colorlist[c])
        c += 1
    axes[0].set_title("CSV File 1", fontsize=16)
    axes[0].set_ylabel("Data Value", fontsize=14)
    axes[0].legend(fontsize=12)
    axes[0].grid()

    # 2つ目のCSVデータをプロット
    colorlist = ["red", "blue", "green", "orange", "cyan", "pink", "yellow", "lime"]
    c = 0
    for col, (time, values) in data2.items():
        axes[1].plot(time, values, label=col, color=colorlist[c])
        c += 1
    axes[1].set_title("CSV File 2", fontsize=16)
    axes[1].set_xlabel("Relative Time (seconds)", fontsize=14)
    axes[1].set_ylabel("Data Value", fontsize=14)
    axes[1].legend(fontsize=12)
    axes[1].grid()

    plt.tight_layout()
    plt.show()

# 入力CSVファイル
input_csv1 = "/home/sskr3/bags/ros1/2025-07-12-15-27-54/2025-07-12-15-27-54.bag_ipos.csv"
input_csv2 = "/home/sskr3/bags/ros1/2025-07-12-15-27-54/2025-07-12-15-27-54.bag_opos.csv"

# 時刻範囲を指定 (相対秒単位)
start_sec = 0.00  # 開始時刻（相対秒）
end_sec = 50.00    # 終了時刻（相対秒）

# プロット
plot_csv_data(input_csv1, input_csv2, start_sec, end_sec, gradient_threshold=10.0)