import pandas as pd
import matplotlib.pyplot as plt

# 入力CSVファイル
input_csv = "output.csv"

# 時刻範囲を指定 (相対秒単位)
start_sec = 20.0  # 開始時刻（相対秒）
end_sec = 20.05    # 終了時刻（相対秒）

# CSVを読み込む
df = pd.read_csv(input_csv)

# ナノ秒を秒に変換し、相対時刻を計算
df["time_sec"] = df["%time"] * 1e-9
start_time = df["time_sec"].iloc[0]  # CSVの最初のデータを基準にする
df["relative_time"] = df["time_sec"] - start_time

# 指定範囲でデータを抽出
df_range = df[(df["relative_time"] >= start_sec) & (df["relative_time"] <= end_sec)]

# プロット用データをnumpy配列に変換
relative_time = df_range["relative_time"].to_numpy()
data_values = df_range["field.data0"].to_numpy()

# プロット
plt.figure(figsize=(10, 6))
plt.plot(relative_time, data_values, label="field.data0", marker="o")
plt.xlabel("Relative Time (seconds)")
plt.ylabel("Data Value")
plt.title(f"Data Plot from {start_sec}s to {end_sec}s")
plt.legend()
plt.grid()
plt.show()