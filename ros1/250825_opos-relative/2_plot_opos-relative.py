import pandas as pd
import matplotlib.pyplot as plt
import os

# 入力CSVファイル名
csv_file = "/home/sskr3/bags/ros1/250825_opos-relative/output-3/2025-08-04-11-37-00.bag_opos_rel_field_data2_field_data3_pospos_negneg.csv"

# CSV読み込み
df = pd.read_csv(csv_file)

# 散布図作成（2列目 vs 3列目）
plt.scatter(df.iloc[:, 1], df.iloc[:, 2], s=10, c="blue")
plt.xlabel("Column 2")
plt.ylabel("Column 3")
plt.title("Scatter plot (2nd vs 3rd column)")
plt.grid(True)
plt.axis("equal")

# 保存ディレクトリ作成（スクリプトと同じ場所に output-2）
base_dir = os.path.dirname(__file__)
output_dir = os.path.join(base_dir, "output-2")
os.makedirs(output_dir, exist_ok=True)

# 出力ファイル名：入力CSVの拡張子を除いた名前 + ".png"
basename = os.path.splitext(os.path.basename(csv_file))[0]
save_path = os.path.join(output_dir, f"{basename}.png")

# 保存
plt.savefig(save_path, dpi=300)
plt.show()
plt.close()
print(f"Saved to {save_path}")
