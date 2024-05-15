#羊の数を数えるプログラム
#引数のためのモジュールをインポート
import sys
args = sys.argv

#引数の入力
num = int(args[1])

#繰り返しの開始
for i in range(1,num + 1,1):
    print("ひつじが" + str(i) + "匹")
    i += 1 