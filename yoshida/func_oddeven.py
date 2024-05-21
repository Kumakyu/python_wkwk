#魔法の呪文
import sys
args = sys.argv

#関数を定義＝偶数奇数判定
def calcvalue(a):
    if a%2 == 1:
        print(str(a),"は","奇数",end="")
    else:
        print(str(a),"は","偶数",end="")

#関数を使用して判定（複数の値を入力可）
print(calcvalue(2))

