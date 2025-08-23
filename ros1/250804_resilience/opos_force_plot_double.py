import os
import csv
import matplotlib.pyplot as plt

def plot_csv_data(csv_path1, csv_path2, csv_path3):
    times = []
    data2_1 = []
    data2_2 = []
    data3_1 = []
    data3_2 = []
    data4_1 = []
    data4_2 = []

    # CSVファイルを読み込む
    with open(csv_path1, mode='r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            times.append(int(row["%time"]))
            data2_1.append(float(row["opos"]))
            data2_2.append(float(row["force"]))

    with open(csv_path2, mode='r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            times.append(int(row["%time"]))
            data3_1.append(float(row["opos"]))
            data3_2.append(float(row["force"]))

    with open(csv_path3, mode='r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            times.append(int(row["%time"]))
            data4_1.append(float(row["opos"]))
            data4_2.append(float(row["force"]))

    # プロット
    plt.figure(figsize=(10, 6))
    plt.plot(data2_1, data2_2, label="force-opos", lw=0.5, color='blue')
    plt.plot(data3_1, data3_2, label="force-opos", lw=0.5, color='red')
    plt.plot(data4_1, data4_2, label="force-opos", lw=0.5, color='green')
    plt.xlabel("opos")
    plt.ylabel("force")
    plt.title("opos force plot")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("使用方法: python opos_force_plot_double.py <CSVファイルパス> <CSVファイルパス> <CSVファイルパス>")
        sys.exit(1)

    csv_path1 = sys.argv[1]
    csv_path2 = sys.argv[2]
    csv_path3 = sys.argv[3]

    if not os.path.isfile(csv_path1):
        print(f"指定されたファイルが存在しません: {csv_path1}")
        sys.exit(1)
    if not os.path.isfile(csv_path2):
        print(f"指定されたファイルが存在しません: {csv_path2}")
        sys.exit(1)
    if not os.path.isfile(csv_path3):
        print(f"指定されたファイルが存在しません: {csv_path3}")
        sys.exit(1)

    plot_csv_data(csv_path1, csv_path2, csv_path3)