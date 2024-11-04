# .append()を使ってリストの末尾に要素を追加
# .insert()を使って特定の位置に要素を挿入
# .remove()で最初に見つかった要素を削除
# delキーワードや.pop()で特定のインデックスの要素を削除

my_list = [1, "Python", 3.14, [2, 4, 6]]

#1.リストの作成
my_list = ["apple", "banana", "cherry"]
print(f"1.リストの作成: {my_list}")

#2.要素へアクセス
print(f"2.要素へアクセス: {my_list[1]}")

#3.要素の追加
my_list.append("orange")
print(f"2.要素へアクセス: {my_list}")

#4.要素の削除
my_list.remove("banana")
print(f"4.要素の削除: {my_list}")

#「f」は、文字列内で変数や式の値を直接埋め込んで利用できるようにするもの