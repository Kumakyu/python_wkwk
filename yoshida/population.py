import sys
args = sys.argv

#
input1 = int(args[1])

#タプル作成
Population_tuple = ("China","India","U.S.A","Indonesia","Pakistan","Brazil","Nigeria","Bangladesh","Russia","Mexico")
a =Population_tuple[input1 -1]

#出力
print(a,end="")