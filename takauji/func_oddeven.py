#呪文
import sys
args = sys.argv


#関数

def calcvalue(a):
    if a %2==0:
        print(str(a) + "は偶数",end="")
    else:
        print(str(a) + "は奇数",end="")

#複数の引数を入力
for i in range (1,len(args)):
    a = int(args[i])
    calcvalue(a)


