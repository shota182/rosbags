import pandas as pd
import numpy as np
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt
import glob
import os

# --- 設定 ---
input_dir = '/home/sskr3/bags/ros1/resilience/cluster_input'     # 入力CSVのディレクトリ
output_dir = '/home/sskr3/bags/ros1/resilience/clustered'   # 出力先
scale_factor = 0.0001             # oposのスケール縮小係数
n_clusters = 2

os.makedirs(output_dir, exist_ok=True)

# --- 1. 複数CSVを結合 ---
csv_files = glob.glob(os.path.join(input_dir, '*.csv'))
df_list = []

for f in csv_files:
    df = pd.read_csv(f)
    df_list.append(df)

df_all = pd.concat(df_list, ignore_index=True)

# --- 2. 特徴量加工（xを縮小） ---
X = df_all[['opos', 'force']].copy()
X['opos_scaled'] = X['opos'] * scale_factor

# --- 3. GMMクラスタリング（上下分離） ---
gmm = GaussianMixture(n_components=n_clusters, random_state=0)
labels = gmm.fit_predict(X[['opos_scaled', 'force']])
df_all['cluster'] = labels  # 一時的に保持

# --- 4. 可視化（任意） ---
plt.scatter(df_all['opos'], df_all['force'], c=labels, cmap='coolwarm', s=10)
plt.xlabel('opos')
plt.ylabel('force')
plt.title('GMM clustering (merged CSVs)')
plt.grid(True)
plt.show()

# --- 5. 各クラスタを分割保存（余計な列は削除） ---
for cluster_id in range(n_clusters):
    df_cluster = df_all[df_all['cluster'] == cluster_id].drop(columns=['cluster'])
    df_cluster.to_csv(os.path.join(output_dir, f'cluster_{cluster_id}.csv'), index=False)

print("クラスタごとのCSVを保存しました")
