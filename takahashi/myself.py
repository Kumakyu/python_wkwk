# 引数のためのモジュール
import sys
args = sys.argv

# 引数の入力
name = str(args[1])
age= str(args[2])

#取り込む
from introduce import *

Name = Intro(name,age)
print(Name.name_out())
print(Name.age_out())