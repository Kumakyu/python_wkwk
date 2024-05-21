#魔法の呪文
import sys
args = sys.argv

#文字を入力
input1 = str(args[1])
input2 = int(args[2])

#スプリット
a = input1.split()

print(a[input2 -1],end="")

