#!/bin/bash

# filepath: /home/sskr3/bags/ros1/make_csv.sh

# 引数の確認
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <bag_file>"
    exit 1
fi

# 引数からbagファイル名を取得
bag_file="$1"

# bagファイル名からディレクトリ名を作成
dir_name="${bag_file%.bag}"

# ディレクトリ作成
mkdir -p "$dir_name"

# bagファイルをディレクトリに移動
mv "$bag_file" "$dir_name/"

# 作業ディレクトリに移動
cd "$dir_name" || exit 1

# rostopic echoでCSVファイルを作成
rostopic echo -b "$bag_file" -p /force/input/tension > "${bag_file}_f.csv"
rostopic echo -b "$bag_file" -p /sensor/motor/input/position > "${bag_file}_ipos.csv"
rostopic echo -b "$bag_file" -p /sensor/motor/output/position > "${bag_file}_opos.csv"

echo "CSV files created in $dir_name:"
echo "${bag_file}_f.csv"
echo "${bag_file}_ipos.csv"
echo "${bag_file}_opos.csv"