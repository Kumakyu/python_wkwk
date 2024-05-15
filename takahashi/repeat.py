#永遠の足し算のプログラム
#日数のためのモジュールをインポート
import sys
args = sys.argv
#引数の入力
number = int(args[1])
#合計の初期値
sum = 0
#繰り返しの始まり
while True:
    if sum < 100:
        sum += number
    elif sum == 100:
        print("Just 100!")
        break
    else:
        print("Over!") 
        break