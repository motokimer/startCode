import csv

# 'sample.csv' ファイルを読み取りモードで開く
with open('sample.csv', 'r') as csvfile:

# DictReaderを使用してCSVファイルを辞書形式で読み込む
    reader = csv.DictReader(csvfile)

    # 年齢の合計と人数を初期化
    total_age = 0
    num_people = 0

    # 各行を処理して年齢を合計し、人数をカウント
    for row in reader:
        total_age += int(row['age'])
        num_people += 1
    
    # 平均年齢を計算
    average_age = total_age / num_people

    # 平均年齢を表示（小数点以下2桁まで）
    print(f"平均年齢: {average_age:.2f} 歳")