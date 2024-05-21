import sys
#import introduce
#introduce.pyをインポート
from introfamily import *

args = sys.argv

#名前と年齢を入力
input_name = args[1]
input_age = args[2]
input_catname = args[3]

intro = Intro(input_name, input_age)
print(intro.name_out())
print(intro.age_out())

introfam = IntroFam(input_catname)
print(introfam.cat_out())