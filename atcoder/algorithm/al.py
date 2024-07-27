# 入力文字列を取得
input_string = input("文字列を入力してください: ")

# アルファベットの出現回数をカウントする辞書を作成
count_dict = {}

# 文字列の各文字を走査
for char in input_string:
    if char.isalpha():  # アルファベットかどうかをチェック
        char_lower = char.lower()  # 小文字に変換
        if char_lower in count_dict:
            count_dict[char_lower] += 1
        else:
            count_dict[char_lower] = 1

# 結果を表示
for letter in 'abcdefghijklmnopqrstuvwxyz':
    if letter in count_dict:
        print(f"{letter}: {count_dict[letter]}")
