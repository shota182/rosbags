#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt

# === 設定 ===
# csv_file = "/home/sskr3/bags/ros1/2025-05-11-16-27-40_mag.csv"
# csv_file = "/home/sskr3/bags/ros1/2025-05-11-17-37-45_mag.csv"
# csv_file = "/home/sskr3/bags/ros1/2025-05-11-17-46-12_mag.csv"
# csv_file = "/home/sskr3/bags/ros1/2025-05-11-17-55-37/2025-05-11-17-55-37_mag.csv"
# csv_file = "/home/sskr3/bags/ros1/2025-05-18-11-56-46_mag.csv"
# csv_file = "/home/sskr3/bags/ros1/2025-05-18-11-57-21_mag.csv"
# csv_file = "/home/sskr3/bags/ros1/2025-05-18-12-16-11_mag.csv"
# csv_file = "/home/sskr3/bags/ros1/2025-05-18-13-40-12_mag.csv"
# csv_file = "/home/sskr3/bags/ros1/2025-05-18-14-05-19_mag.csv"
# csv_file = "/home/sskr3/bags/ros1/2025-05-18-14-29-33_mag.csv"
# csv_file = "/home/sskr3/bags/ros1/2025-05-18-14-48-09_mag.csv"
# csv_file = "/home/sskr3/bags/ros1/2025-05-18-15-00-13_mag.csv"
# csv_file = "/home/sskr3/bags/ros1/2025-05-18-15-18-30_mag.csv"
# csv_file = "/home/sskr3/bags/ros1/2025-05-18-15-21-08_mag.csv"
# csv_file = "/home/sskr3/bags/ros1/2025-05-18-16-25-18/2025-05-18-16-25-18_mag.csv"
# csv_file = "/home/sskr3/bags/ros1/2025-05-26-08-01-10/2025-05-26-08-01-10_mag.csv"
# csv_file = "/home/sskr3/bags/ros1/2025-05-26-08-13-15/2025-05-26-08-13-15_mag.csv"
# csv_file = "/home/sskr3/bags/ros1/2025-05-26-08-32-51/2025-05-26-08-32-51_mag.csv"
# csv_file = "/home/sskr3/bags/ros1/2025-05-26-08-55-23/2025-05-26-08-55-23_mag.csv"
# csv_file = "/home/sskr3/bags/ros1/2025-05-26-09-10-39/2025-05-26-09-10-39_mag.csv"
# csv_file = "/home/sskr3/bags/ros1/2025-05-26-09-19-20/2025-05-26-09-19-20_mag.csv"
csv_file = "/home/sskr3/bags/ros1/2025-05-26-09-30-11/2025-05-26-09-30-11_mag.csv"

start_sec = 0.0   # ← 「開始から何秒後」
end_sec   = 300.0   # ← 「開始から何秒後」

# === ボタントリガーCSVを読み込む ===
base_name = csv_file.replace("_mag.csv", "")
trigger_file = base_name + "_trigger.csv"  # 例: _trigger.csv に保存されている想定

data = "data0"

# === CSV 読み込み ===
df = pd.read_csv(csv_file)

# === ナノ秒 → 秒 ＆ 開始時刻基準に変換 ===
if "%time" not in df.columns:
    raise ValueError("列 '%time' が見つかりません。")
df["time_sec"] = df["%time"] * 1e-9
start_time = df["time_sec"].iloc[0]
df["relative_time"] = df["time_sec"] - start_time  # ← 経過秒

# === 必要列チェックと NaN 排除 ===
for col in [f"field.{data}", "field.data2"]:
    if col not in df.columns:
        raise ValueError(f"{col} が存在しません")
df = df.dropna(subset=[f"field.{data}", "field.data2"])

# === 移動平均(n番目のデータはn-4からn+4番目のデータの平均値) ===
# df[f"field.{data}"] = df[f"field.{data}"].rolling(window=10, center=True).mean()
# df["field.data2"] = df["field.data2"].rolling(window=10, center=True).mean()


# === 指定範囲で抽出 ===
df_range = df[(df["relative_time"] >= start_sec) & (df["relative_time"] <= end_sec)]

# === プロット ===
plt.figure()
plt.plot(df_range["relative_time"].values, df_range[f"field.{data}"].values, label=f"field.{data}")
# plt.plot(df_range["relative_time"].values, df_range["field.data2"].values, label="field.data2")

try:
    df_trigger = pd.read_csv(trigger_file)
    # 秒に変換して、相対時刻に直す（1つ目のCSVと同じ開始基準に合わせる）
    df_trigger["time_sec"] = df_trigger["%time"] * 1e-9
    df_trigger["relative_time"] = df_trigger["time_sec"] - start_time  # ※ start_time は最初のmagファイルのもの
    # === 各トリガー時刻に縦線を引く ===
    for t in df_trigger["relative_time"]:
        plt.axvline(x=t, color='red', linestyle='--', linewidth=1.2, label="Trigger" if t == df_trigger["relative_time"].iloc[0] else None)
except:
    pass

plt.xlabel("Time since start [s]")
plt.ylabel("Value")
# plt.ylim([200,250])
plt.title(f"field.{data} and field.data2 from {start_sec}s to {end_sec}s")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
