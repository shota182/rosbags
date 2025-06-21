# /sensor/motor/output/positionや/sensor/motor/input/positionをプロットする
# 色は8なので4d bilateralに合わせている

import pandas as pd
import matplotlib.pyplot as plt

def process_csv(csv_file):
    # CSVを読み込む
    df = pd.read_csv(csv_file)

    # ナノ秒を秒に変換し、相対時刻を計算
    df["time_sec"] = df["%time"] * 1e-9
    start_time = df["time_sec"].iloc[0]  # 最初の時刻を基準にする
    df["relative_time"] = df["time_sec"] - start_time

    # データの相対変化を計算
    for col in df.columns:
        if col.startswith("field.data"):
            df[col] = df[col] - df[col].iloc[0]  # 各データ列の相対変化を計算

    return df

def plot_relative_data(df, data_columns, start_sec, end_sec):
    # 指定された時刻範囲でデータを抽出
    df_range = df[(df["relative_time"] >= start_sec) & (df["relative_time"] <= end_sec)]

    colors = ["red", "red", "red", "red", "blue", "blue", "blue", "blue"]
    # プロット
    plt.figure(figsize=(10, 6))
    # for i in range(len(data_columns)):
    #     plt.plot(df_range["relative_time"].to_numpy(), df_range[data_columns[i]].to_numpy(), label=data_columns[i], color=colors[i], lw=0.5)
    plt.plot(df_range["relative_time"].to_numpy(), df_range[data_columns[0]].to_numpy(), label=data_columns[0], color=colors[0], lw=0.5)
    plt.plot(df_range["relative_time"].to_numpy(), df_range[data_columns[5]].to_numpy(), label=data_columns[5], color=colors[5], lw=0.5)
    plt.xlabel("Relative Time (seconds)", fontsize=14)
    plt.ylabel("Relative Change", fontsize=14)
    # plt.ylim([-50, 50])
    plt.title(f"Relative Data Plot from {start_sec}s to {end_sec}s", fontsize=16)
    plt.legend(fontsize=12)
    plt.grid()
    plt.show()

# 入力CSVファイル
# input_csv = "/home/sskr3/bags/ros1/2025-06-16-12-38-32_ipos.csv"
# input_csv = "/home/sskr3/bags/ros1/2025-06-16-12-38-32_opos.csv"

# input_csv = "/home/sskr3/bags/ros1/2025-06-21-13-08-26_ipos.csv"
# input_csv = "/home/sskr3/bags/ros1/2025-06-21-13-08-26_opos.csv"
# 力は「データの相対変化を計算」をしないようにする
# input_csv = "/home/sskr3/bags/ros1/2025-06-21-13-08-26_f.csv"

# input_csv = "/home/sskr3/bags/ros1/2025-06-21-13-36-53_ipos.csv"
# input_csv = "/home/sskr3/bags/ros1/2025-06-21-13-36-53_opos.csv"
# 力は「データの相対変化を計算」をしないようにする
# input_csv = "/home/sskr3/bags/ros1/2025-06-21-13-36-53_f.csv"

input_csv = "/home/sskr3/bags/ros1/2025-06-21-13-58-49_ipos.csv"
# input_csv = "/home/sskr3/bags/ros1/2025-06-21-13-58-49_opos.csv"
# 力は「データの相対変化を計算」をしないようにする
# input_csv = "/home/sskr3/bags/ros1/2025-06-21-13-58-49_f.csv"

# 時刻範囲を指定 (相対秒単位)
start_sec = 0.0  # 開始時刻（相対秒）
end_sec = 10.0    # 終了時刻（相対秒）

# CSVを処理
df = process_csv(input_csv)

# プロットするデータ列を指定
data_columns = [col for col in df.columns if col.startswith("field.data")]

# プロット
plot_relative_data(df, data_columns, start_sec, end_sec)