#3つの整数の足し算プログラム
import sys
args = sys.argv
#3つの整数の入力
input1 = int(args[1])
input2 = int(args[2])
input3 = int(args[3])
#足し算の実行
sum = input1 + input2 + input3
#結果の表示
print(sum, end="")
