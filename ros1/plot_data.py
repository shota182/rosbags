# ふたつのcsvファイルからデータ列を読み込んで，並べてプロットする

import pandas as pd
import matplotlib.pyplot as plt

def load_csv(csv, start_time, time_length, data_id="", relative=False):
    # CSVを読み込む
    df = pd.read_csv(csv)

    # ナノ秒を秒に変換し、相対時刻を計算
    df["time_sec"] = df["%time"] * 1e-9
    start_time = df["time_sec"].iloc[0]  # CSVの最初のデータを基準にする
    df["relative_time"] = df["time_sec"] - start_time

    # 指定範囲でデータを抽出
    df_range = df[(df["relative_time"] >= start_sec) & (df["relative_time"] <= start_sec + time_length)]

    # プロット用データをnumpy配列に変換
    relative_time = df_range["relative_time"].to_numpy()
    data_values = df_range[f"field.data{data_id}"].to_numpy()
    if(relative): data_values -= data_values[0]  # 相対値に変換
    return relative_time, data_values, start_time



# 入力CSVファイル
# input_csv = "output_goal.csv"
# input_csv2 = "output_present.csv"

# input_csv = "/home/sskr3/bags/ros1/2025-06-16-11-41-41_ipos.csv"
# input_csv2 = "/home/sskr3/bags/ros1/2025-06-16-11-41-41_opos.csv"

# input_csv = "/home/sskr3/bags/ros1/2025-06-16-12-38-32_ipos.csv"
# input_csv2 = "/home/sskr3/bags/ros1/2025-06-16-12-38-32_opos.csv"

# input_csv = "/home/sskr3/bags/ros1/2025-06-21-13-08-26_ipos.csv"
# input_csv2 = "/home/sskr3/bags/ros1/2025-06-21-13-08-26_opos.csv"

input_csv = "/home/sskr3/bags/ros1/2025-06-21-13-36-53_ipos.csv"
input_csv2 = "/home/sskr3/bags/ros1/2025-06-21-13-36-53_opos.csv"

# 時刻範囲を指定 (相対秒単位)
start_sec = 0.0  # 開始時刻（相対秒）
time_length = 20.0  # 時間長（相対秒）

relative_time, data_values, s = load_csv(input_csv, start_sec, time_length, data_id="6", relative=True)
relative_time2, data_values2, _ = load_csv(input_csv2, s, time_length, data_id="0", relative=True)

# プロット
plt.figure(figsize=(10, 6))
plt.plot(relative_time, data_values, color="red", label="plot", marker="o")
plt.plot(relative_time2, data_values2, color="blue", label="plot2", marker="o")
plt.xlabel("Relative Time (seconds)", fontsize=14)
plt.ylabel("Data Value", fontsize=14)
# plt.ylim([-20, 20])  # Y軸の範囲を設定
plt.title(f"Data Plot from {start_sec}s to {start_sec+time_length}s")
plt.legend(fontsize=12)
plt.tick_params(axis='both', labelsize=16)  # X軸とY軸の目盛りサイズを変更
plt.grid()
plt.show()