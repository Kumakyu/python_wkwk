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
animallist[num] = name
print(animallist, end="")
#2番の問題
# del animallist[4]
# print(animallist, end="")
# #3番の問題
# list_asc = animallist.sort()
# print(animallist, end="")

