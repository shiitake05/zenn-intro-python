# TODO
# これから実装されるべき機能や、コードの改善点、追加すべきテストなど、まだ完了していないタスクを示すために使用

def calculate_average(scores):
    # TODO: ゼロ除算を考慮するエラーハンドリングを追加する
    return sum(scores) / len(scores)


# NOTE
#コードの特定の部分について、追加の情報や説明を提供する場合に使用

def calculate_average(scores):
    # NOTE: 平均点は全点数の合計を点数の数で割ることで求められます。
    total = sum(scores)  # 全点数の合計を計算
    count = len(scores)  # 点数の数
    average = total / count  # 平均点を計算
    return average


# FIXME
# コードにバグがあるか、あるいは期待通りに動作していない部分がある場合に使用

def calculate_discount(price, discount):
    # FIXME: 割引率が負の値の場合に正しく計算されない
    return price - (price * discount)


# XXX
# 注意を要するコードの部分を指摘する場合に使用

# XXX: この関数は非常に大きなデータセットで遅くなる可能性があります
def sort_data(data):
    return sorted(data)


# HACK
# 一時的な解決策や回避策をコードに適用した場合に使用

# HACK: APIが空のリストを返すバグを回避する一時的な修正
def get_data():
    result = api_call()
    if result is None:
        return []  # 空のリストを返す
    return result

