# エラー
# name: str = "Taro"
# def greet(name: str) -> str:
#     return "こんにちは、" + name + "！"

# print(greet(20))

# listの型ヒント
numbers: list[int] = [1, 2, 3]
names: list[str] = ["Alice", "Bob", "Charlie"]

# dictの型ヒント
age_map: dict[str, int] = {"Alice": 30, "Bob": 25, "Charlie": 35}

# tupleの型ヒント
coordinate: tuple[int, int] = (10, 20)
person: tuple[str, int, str] = ("Alice", 30, "Engineer")

# setの型ヒント
unique_numbers: set[int] = {1, 2, 3, 2, 1}