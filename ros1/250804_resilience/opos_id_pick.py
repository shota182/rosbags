import csv
import os
import sys

def compare_and_extract(csv_path):
    # 入力CSVのディレクトリを取得
    input_dir = os.path.dirname(csv_path)
    output_csv_data2 = os.path.join(input_dir, "data2_greater.csv")
    output_csv_data3 = os.path.join(input_dir, "data3_greater.csv")

    # CSVファイルを読み込む
    with open(csv_path, mode='r') as infile:
        reader = csv.DictReader(infile)

        # フィールド名を取得
        fieldnames = reader.fieldnames

        # 出力ファイルを作成
        with open(output_csv_data2, mode='w', newline='') as file_data2, open(output_csv_data3, mode='w', newline='') as file_data3:
            writer_data2 = csv.DictWriter(file_data2, fieldnames=fieldnames)
            writer_data3 = csv.DictWriter(file_data3, fieldnames=fieldnames)

            # ヘッダーを書き込む
            writer_data2.writeheader()
            writer_data3.writeheader()

            # 行を比較して抽出
            for row in reader:
                data2 = float(row["field.data2"])
                data3 = float(row["field.data3"])

                if data2 < 0:
                    writer_data2.writerow(row)
                else:
                    writer_data3.writerow(row)

    print(f"data2が大きい行を {output_csv_data2} に保存しました。")
    print(f"data3が大きい行を {output_csv_data3} に保存しました。")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方法: python opos_id_pick.py <CSVファイルパス>")
        sys.exit(1)

    csv_path = sys.argv[1]

    if not os.path.isfile(csv_path):
        print(f"指定されたファイルが存在しません: {csv_path}")
        sys.exit(1)

    compare_and_extract(csv_path)