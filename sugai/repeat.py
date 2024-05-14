import sys
args = sys.argv

sum = 0
num = int(args[1])

while True:
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
