import sys
#import introduce
#introduce.pyをインポート
from introduce import *

args = sys.argv

#名前と年齢を入力
input_name = args[1]
input_age = args[2]

#class introより関数を参照
a = intro(input_name, input_age)
print(a.name_out())
print(a.age_out())