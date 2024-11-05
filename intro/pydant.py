# PydanticはPythonでのデータ構造化を容易にするライブラリ
# Userという名前のモデルを作成

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

user = User(name="Taro", age=20, email="taro@example.com")
# user = User(name="Taro", age="二十歳", email="taro@example.com")  # ageでエラー

print(user.name)
print(user.email)