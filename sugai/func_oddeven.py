import sys
args = sys.argv

print(args)

def calcvalue(num):
    if int(num)%2 == 0:
        print(str(num)+"は偶数")
    else:
        print(str(num)+"は奇数")

for i in range(1, len(args)):
    input_num = args[i]
    calcvalue(input_num)

