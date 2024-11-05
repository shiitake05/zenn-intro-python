# 三項演算子
# 条件式
# 値1 if 条件 else 値2

x = 10
result = "偶数" if x % 2 == 0 else "奇数"
print(result)
# 使用しない例
# x = 20
# result = ""

# if x % 2 == 0:
#     result = "偶数"
# else:
#     result = "奇数"



# リスト内包表記
# リストを生成する際にループや条件文を簡潔に書く方法
# [式 for アイテム in イテラブル(リスト、タプル、辞書など)if 条件]

squares = [x**2 for x in range(10)]
print(squares)



# ラムダ式
# 無名関数を定義するための式
# lambda 引数: 式

add = lambda x, y: x + y
print(add(1, 2))
# 使用しない例
# def add(x: int, y: int) -> int:
#     return x + y