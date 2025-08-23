import csv
import os
import sys

def linear_interpolation(x, x0, x1, y0, y1):
    """線形補間を行う関数"""
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

def map_and_interpolate(csv_path1, csv_path2, output_csv_path):
    # データ列番号を直接指定

    # CSVファイルを読み込む
    with open(csv_path1, mode='r') as file1, open(csv_path2, mode='r') as file2:
        reader1 = csv.DictReader(file1)
        reader2 = csv.DictReader(file2)

        # ②のデータをリストに格納
        data2_rows = list(reader2)

        # 出力ファイルを作成
        with open(output_csv_path, mode='w', newline='') as outfile:
            fieldnames = ["%time", f"opos", f"force"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            # ①の各行に対して処理
            past_id = 0
            for row1 in reader1:
                time1 = int(row1["%time"])
                field_data0_1 = row1[data_column]

                # ②の時刻に基づいて線形補間
                for i in range(past_id, len(data2_rows) - 1):
                    time2_0 = int(data2_rows[i]["%time"])
                    time2_1 = int(data2_rows[i + 1]["%time"])

                    if time2_0 <= time1 <= time2_1:
                        value2_0 = float(data2_rows[i][data_column])
                        value2_1 = float(data2_rows[i + 1][data_column])
                        interpolated_value = linear_interpolation(time1, time2_0, time2_1, value2_0, value2_1)

                        # 結果をCSVに書き込む
                        writer.writerow({
                            "%time": time1,
                            f"opos": field_data0_1,
                            f"force": interpolated_value
                        })
                        past_id = i
                        break

    print(f"結果を {output_csv_path} に保存しました。")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使用方法: python opos_force_mapping.py <CSVファイル1> <CSVファイル2>")
        sys.exit(1)

    csv_path1 = sys.argv[1]
    csv_path2 = sys.argv[2]

    if not os.path.isfile(csv_path1) or not os.path.isfile(csv_path2):
        print("指定されたCSVファイルが存在しません。")
        sys.exit(1)

    data_column = f"field.data{csv_path1[-13:-12]}"

    output_csv_path = os.path.join(os.path.dirname(csv_path1), f"mapped_interpolated-{data_column}.csv")
    map_and_interpolate(csv_path1, csv_path2, output_csv_path)