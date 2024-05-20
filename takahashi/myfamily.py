# 引数のためのモジュール
import sys
args = sys.argv

# 引数の入力
name = str(args[1])
age= str(args[2])
cat_name = str(args[3])

#取り込む
from introfamily import *

intro = IntroFam(name, age, cat_name)
print(intro.name_out())
print(intro.age_out())
print(intro.cat_out())
