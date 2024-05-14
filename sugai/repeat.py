import sys
args = sys.argv

#変数の定義
sum = 0
num = int(args[1])

#引数で渡した整数を繰り返し足し算
while True:
    #足し算の結果が100以上になるまで継続
    if sum < 100:
        sum = sum + num
        print(sum)
        continue
    elif sum == 100:
        print("Just 100", end="")
        break
    elif sum > 100:
        print("Over!")
        break
