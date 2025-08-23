import csv
import os
import sys

def calculate_relative_values(input_csv_path):
    # 入力CSVのディレクトリとファイル名を取得
    input_dir = os.path.dirname(input_csv_path)
    output_csv_path = os.path.join(input_dir, "opos_relative.csv")

    # CSVを読み込む
    with open(input_csv_path, mode='r') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        data_fields = [field for field in fieldnames if field.startswith("field.data")]

        # 全データを読み込む
        rows = list(reader)

        # 各列の基準値を取得 (列の最初の値)
        base_values = {field: int(rows[0][field]) for field in data_fields}

        # 新しいCSVを作成
        with open(output_csv_path, mode='w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in rows:
                # 各列の相対値を計算
                for field in data_fields:
                    row[field] = int(row[field]) - base_values[field]
                writer.writerow(row)

    print(f"相対値を計算した結果を {output_csv_path} に保存しました。")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方法: python opos_relative.py <入力CSVファイルパス>")
        sys.exit(1)

    input_csv_path = sys.argv[1]
    if not os.path.isfile(input_csv_path):
        print(f"指定されたファイルが存在しません: {input_csv_path}")
        sys.exit(1)

    calculate_relative_values(input_csv_path)