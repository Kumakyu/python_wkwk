import sys
args = sys.argv

#入力する整数を引数に設定
input = int(args[1])
sum = 0

#
while sum < 100:
    sum = sum + input

if sum >= 101:
    print("Over!",end="")

elif sum == 100:
    print("Just 100!",end="")


