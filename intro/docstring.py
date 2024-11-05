# DocStringはコードブロックが何をするのかの説明
# 三重クォートで囲んでDocStringを記述する

def add(a: int, b: int) -> int:
    """
    二つの数値を加算します。

    Args:
        a (int): 数値1
        b (int): 数値2

    Returns:
        int: aとbの合計
    """
    return a + b