import pandas as pd
import numpy as np
import os
import glob
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linear_func(x, a, b):
    return a * x + b

input_dir = '/home/sskr3/bags/ros1/resilience/clustered'
output_dir = '/home/sskr3/bags/ros1/resilience/fit_csv'
os.makedirs(output_dir, exist_ok=True)

pattern = os.path.join(input_dir, 'cluster_*.csv')

plt.figure()

colors = ['red', 'blue']
for i, filepath in enumerate(sorted(glob.glob(pattern))):
    basename = os.path.basename(filepath)
    df = pd.read_csv(filepath)
    df = df.dropna(subset=['opos', 'force'])

    df = df.sort_values('opos')
    x = df['opos'].to_numpy()
    y = df['force'].to_numpy()

    try:
        # 線形フィッティング
        popt, _ = curve_fit(linear_func, x, y, p0=[1.0, 0.0])
        a, b = popt

        # 1刻みのopos範囲生成
        x_min = min(np.floor(x.min()), -100)
        x_max = max(np.ceil(x.max()),  100)
        x_out = np.arange(x_min, x_max + 1, 1)
        y_out = linear_func(x_out, a, b)

        # CSV出力
        df_out = pd.DataFrame({'opos': x_out, 'force': y_out})
        output_path = os.path.join(output_dir, f'curve_{basename}')
        df_out.to_csv(output_path, index=False)
        print(f"✅ Saved: {output_path} ({len(df_out)} points)")

        # プロットに重ねる
        plt.scatter(x, y, s=5, alpha=0.2, label=f'{basename} raw', color=colors[i % len(colors)])
        plt.plot(x_out, y_out, linewidth=2, label=f'{basename} fit', color=colors[i % len(colors)])
    except Exception as e:
        print(f"❌ Fit failed for {basename}: {e}")

# プロット全体設定
plt.xlabel('opos')
plt.ylabel('force')
plt.title('Linear Fit for Each Cluster')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
