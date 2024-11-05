from dotenv import load_dotenv
import os

load_dotenv()

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')

print(f"DBホスト: {db_host}, ユーザー: {db_user}, パスワード: {db_pass}")