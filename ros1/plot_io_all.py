import pandas as pd
import matplotlib.pyplot as plt

def process_csv(csv_file, relative=True):
    # CSVを読み込む
    df = pd.read_csv(csv_file)

    # ナノ秒を秒に変換し、相対時刻を計算
    df["time_sec"] = df["%time"] * 1e-9
    start_time = df["time_sec"].iloc[0]  # 最初の時刻を基準にする
    df["relative_time"] = df["time_sec"] - start_time

    # 相対値に変換する場合
    if relative:
        for col in df.columns:
            if col.startswith("field.data"):
                df[col] = df[col] - df[col].iloc[0]

    return df

def plot_csv_data(csv_file1, csv_file2, start_sec=0.0, end_sec=None, relative=True):
    # CSVファイルを処理
    df1 = process_csv(csv_file1, relative)
    df2 = process_csv(csv_file2, relative)

    # 時刻範囲でデータを抽出
    if end_sec is None:
        end_sec = max(df1["relative_time"].max(), df2["relative_time"].max())
    df1_range = df1[(df1["relative_time"] >= start_sec) & (df1["relative_time"] <= end_sec)]
    df2_range = df2[(df2["relative_time"] >= start_sec) & (df2["relative_time"] <= end_sec)]

    # プロット
    plt.figure(figsize=(12, 8))

    # 1つ目のCSVデータをプロット
    for col in df1_range.columns:
        if col.startswith("field.data"):
            plt.plot(df1_range["relative_time"].to_numpy(), df1_range[col].to_numpy(), label=f"CSV1: {col}")

    # 2つ目のCSVデータをプロット
    for col in df2_range.columns:
        if col.startswith("field.data"):
            plt.plot(df2_range["relative_time"].to_numpy(), df2_range[col].to_numpy(), label=f"CSV2: {col}")

    # ラベルとタイトル
    plt.xlabel("Relative Time (seconds)", fontsize=14)
    plt.ylabel("Data Value", fontsize=14)
    plt.title(f"Combined Data Plot from {start_sec}s to {end_sec}s", fontsize=16)
    plt.legend(fontsize=12)
    plt.grid()
    plt.tight_layout()
    plt.show()

# 入力CSVファイル
input_csv1 = "/home/sskr3/bags/ros1/2025-07-12-19-14-09/2025-07-12-19-14-09.bag_ipos.csv"
input_csv2 = "/home/sskr3/bags/ros1/2025-07-12-19-14-09/2025-07-12-19-14-09.bag_opos.csv"

# 時刻範囲を指定 (相対秒単位)
start_sec = 0.00  # 開始時刻（相対秒）
end_sec = 100.00   # 終了時刻（相対秒）

# 相対値を使用するかどうか
relative = True

# プロット
plot_csv_data(input_csv1, input_csv2, start_sec, end_sec, relative)