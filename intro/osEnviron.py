# 独自の環境変数を設定し、出力する

import os

os.environ['NEW_VAR'] = 'value'
my_variable = os.getenv('NEW_VAR')

print(my_variable)