# 入力文字列を取得
input_string = input("文字列を入力してください: ")

# アルファベットの最後の出現インデックスを保持する辞書を作成
last_index_dict = {}

# 文字列の各文字を走査
for index, char in enumerate(input_string):
    if char.isalpha():  # アルファベットかどうかをチェック
        last_index_dict[char.lower()] = index  # 小文字に変換してインデックスを保持

# 結果を表示
for letter in 'abcdefghijklmnopqrstuvwxyz':
    if letter in last_index_dict:
        print(f"{letter}: {last_index_dict[letter]}")
