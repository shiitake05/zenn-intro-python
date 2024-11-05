try:
    # エラーが発生する可能性のあるコード
    number = int(input("数値を入力してください: "))
    print("入力された数値は", number, "です。")
except ValueError:
    # ValueErrorが発生したときの処理
    print("数値以外が入力されました。")