import sys
args = sys.argv

#
input1 = int(args[1])#数字
input2 = str(args[2])#動物名

#アニマルリストを作成
animal_list = ["giraffe","tiger","zebra","elephant","lion"]

#input2の場所にinput3の動物名をいれる
animal_list.insert(input1,input2)

#リストの最後の要素を削除する
del animal_list[-1]

#リストを昇順に並べ替える
animal_list.sort()

#出力
print(animal_list,end="")