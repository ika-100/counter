count = 0

while True:
    user_input = input("数字を入力してください(終了するには文字を入力): ")

# 数字が入力された回数をカウントするプログラム

    try:
        int(user_input)
        count += 1
        print(f"成功回数: {count}")
    except ValueError:
        print("数字ではありません。")
        print(f"最終的な成功回数: {count}")
        break