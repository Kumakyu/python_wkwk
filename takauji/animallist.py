import sys
args = sys.argv

#入力
input1 = int (args[1])
input2 = str (args[2])

#リストを作成
animal_list = ["giraffe","tiger","zebra","elephant","lion"]

#第2引数で設定したインデックスの位置に第三引数の動物名を挿入する
animal_list.insert(input1,input2)

#リストの最後の要素を削除する
del animal_list[-1]

#リストを昇順に並べ替える
animal_list.sort()

#リストを出力する
print(animal_list,end="")