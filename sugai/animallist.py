#リスト操作プログラム_animal
import sys
args = sys.argv

#リストの作成
list = ["giraffe", "tiger", "zebra", "elephant", "lion"]

#引数の挿入
input_num = int(args[1])
input_animal = str(args[2])

#指定したインデックス位置に指定した動物名を挿入
list.insert(input_num, input_animal)
print(list)

#listの一番後ろの要素を削除
del list[-1]
print(list)

#listを昇順に並び替え
list.sort()
print(list)
