import os
import csv
import matplotlib.pyplot as plt

def plot_csv_data(csv_path):
    times = []
    data2_1 = []
    data2_2 = []

    # CSVファイルを読み込む
    with open(csv_path, mode='r') as infile:
        reader = csv.DictReader(infile)

        for row in reader:
            times.append(int(row["%time"]))
            data2_1.append(float(row["opos"]))
            data2_2.append(float(row["force"]))

    # プロット
    plt.figure(figsize=(10, 6))
    plt.plot(data2_1, data2_2, label="force-opos", lw=0.5, color='blue')
    plt.xlabel("opos")
    plt.ylabel("force")
    plt.title("opos force plot")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("使用方法: python opos_force_plot.py <CSVファイルパス>")
        sys.exit(1)

    csv_path = sys.argv[1]

    if not os.path.isfile(csv_path):
        print(f"指定されたファイルが存在しません: {csv_path}")
        sys.exit(1)

    plot_csv_data(csv_path)