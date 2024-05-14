#奇数、偶数判定プログラム
import sys
args = sys.argv
#数字の入力
number = int(args[1])
#判定
if number % 2 == 1:
    print("奇数です")
else:
    print("偶数です", end="")

    
