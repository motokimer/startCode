import csv

search_name = input("検索する名前を入力してください: ")

with open('sample.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    found = False
    for row in reader:
        if row['name'] == search_name:
            print(f"{search_name} は {row['city']} に住んでいます。")
            found = True
            break
    
    if not found:
        print(f"{search_name} は見つかりませんでした。")


#やっとできた
