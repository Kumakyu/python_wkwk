# 動物の名前のリストのプログラム
#引数のためのモジュールをインポート
import sys
args = sys.argv
# リストの作成
animallist = ["giraffe","tiger","zebra","elephant", "lion"]
#1番の問題
#引数の入力
num = int(args[1])
name = args[2]
#動物名の挿入
animallist.insert(num,name)
#2番の問題
del animallist[5]
#3番の問題
animallist.sort()
print(animallist)

