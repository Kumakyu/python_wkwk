#魔法の呪文
import sys
args = sys.argv#これはリスト

#関数を定義＝偶数奇数判定
def calcvalue(input):
    if input%2 == 1:
        print(str(input),"は","奇数")
    else:
        print(str(input),"は","偶数")

#入力する整数
#リストの中の個数を数える（=len

for i in range(1,len(args)):
    input = int(args[i])#入力する個数分
    calcvalue(input)

    

#関数を使用して判定（複数の値を入力可）


