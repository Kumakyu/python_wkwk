# 動物の名前のリストのプログラム
# リストの作成
animallist = ["giraffe","tiger", "zebra","elephant", "lion"]
#1番の問題
animallist[2] = animallist[3]
print(animallist, end="")
#2番の問題
del animallist[4]
print(animallist, end="")
#3番の問題
list_asc = animallist.sort()
print(animallist, end="")

