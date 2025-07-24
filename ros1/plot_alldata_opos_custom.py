# csvファイルの全データをプロットするスクリプト
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
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
    colorlist = ["green", "red", "blue", "orange", "pink", "lime", "yellow", "cyan"]
    # colorlist = ["cyan", "pink", "yellow", "lime", "red", "blue", "green", "orange"]

    direction = [-1, -1, 1, 1, -1, -1, 1, 1]

    # ノイズを検出して補間
    data_raw = [0]*10
    c = 0
    for col in df.columns:
        if (col.startswith("field.data")):
            # data_raw = df_range[col].to_numpy()
            # data_raw[c] = df_range[col].to_numpy() - df[col].iloc[0]  # 相対値に変換
            data_raw[c] = direction[c] * (df_range[col].to_numpy() - df[col].iloc[0])  # 相対値に変換

            # step -> angle[rad]
            data_raw[c] =  2 * np.pi * data_raw[c] / 4096

            # 変化率を計算
            # gradients = np.abs(np.diff(data_raw))

            # # ノイズを検出 (変化率が閾値を超える場合)
            # outliers = gradients > gradient_threshold

            # # ノイズのインデックスを取得
            # outlier_indices = np.where(outliers)[0] + 1  # +1で次の点をノイズとして扱う

            # # ノイズを直線補間
            # data_raw[outlier_indices] = np.interp(
            #     outlier_indices,  # ノイズのインデックス
            #     np.arange(len(data_raw))[~np.isin(np.arange(len(data_raw)), outlier_indices)],  # ノイズ以外のインデックス
            #     data_raw[~np.isin(np.arange(len(data_raw)), outlier_indices)]  # ノイズ以外のデータ
            # )

            c += 1
    
    one_isbig = [1 if abs(data_raw[2][i])<abs(data_raw[1][i]) else -1 for i in range(len(data_raw[2]))]
    # for i in range(1, len(one_isbig)):
    #     if(one_isbig[i] != one_isbig[i-1]):
    #         print(f"i: {i}, data: {one_isbig[i]}")
    # print(one_isbig)
    
    # プロット
    plt.plot(df_range["relative_time"].to_numpy(), data_raw[1], label=r"$\theta_{leader}$", color=colorlist[1], lw=6)
    plt.plot(df_range["relative_time"].to_numpy(), data_raw[4], label=r"$\theta_{follower}$", color=colorlist[4], lw=5)
    plt.plot(df_range["relative_time"].to_numpy(), data_raw[2], label=r"$\phi_{leader}$", color=colorlist[2], lw=6)
    plt.plot(df_range["relative_time"].to_numpy(), data_raw[7], label=r"$\phi_{follower}$", color=colorlist[7], lw=5)
    ## 誤差
    plt.plot(df_range["relative_time"].to_numpy(), data_raw[1]-data_raw[4], label=r"$\theta_{error}$", color=colorlist[0], lw=5)
    plt.plot(df_range["relative_time"].to_numpy(), data_raw[2]-data_raw[7], label=r"$\phi_{error}$", color=colorlist[5], lw=5)
    ## どっちがでかいか
    # plt.plot(df_range["relative_time"].to_numpy(), one_isbig, label=r"$\phi_{isbig}$", color=colorlist[6], lw=5)
    ## ストライプ
    plt.axvspan(0,                                           df_range["relative_time"].to_numpy()[11094],facecolor="lightcyan", alpha=0.4, zorder=-1)
    plt.axvspan(df_range["relative_time"].to_numpy()[11094], df_range["relative_time"].to_numpy()[19937],facecolor="mistyrose", alpha=0.4, zorder=-1)
    plt.axvspan(df_range["relative_time"].to_numpy()[19937], df_range["relative_time"].to_numpy()[26485],facecolor="lightcyan", alpha=0.4, zorder=-1)
    plt.axvspan(df_range["relative_time"].to_numpy()[26485], df_range["relative_time"].to_numpy()[32319],facecolor="mistyrose", alpha=0.4, zorder=-1)
    plt.axvspan(df_range["relative_time"].to_numpy()[32319], df_range["relative_time"].to_numpy()[37658],facecolor="lightcyan", alpha=0.4, zorder=-1)
    plt.axvspan(df_range["relative_time"].to_numpy()[37658], df_range["relative_time"].to_numpy()[-1],   facecolor="mistyrose", alpha=0.4, zorder=-1)

    plt.xlabel("Time [sec]", fontsize=40)
    plt.ylabel("Pulley Rotation Angle [rad]", fontsize=40)
    plt.xlim([0, 90])  # Y軸の範囲を設定
    plt.ylim([-6, 6])  # Y軸の範囲を設定
    # plt.title(f"Data Plot from {start_sec}s to {end_sec}s", fontsize=16)
    plt.tick_params(axis='both', labelsize=35)
    plt.legend(fontsize=40)
    plt.grid()
    plt.show()

# 入力CSVファイル
input_csv = "/home/sskr3/bags/ros1/2025-07-24-12-15-14/2025-07-24-12-15-14.bag_opos.csv"

# 時刻範囲を指定 (相対秒単位)
start_sec = 0.00  # 開始時刻（相対秒）
end_sec = 150.00    # 終了時刻（相対秒）

# プロット
plot_csv_data(input_csv, start_sec, end_sec, gradient_threshold=10.0)


"""
i: 11094, data: 1
i: 19937, data: -1
i: 26485, data: 1
i: 32319, data: -1
i: 37658, data: 1
"""