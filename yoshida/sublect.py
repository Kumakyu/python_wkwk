import sys
args = sys.argv

#引数を変数に代入
input1 = args[1]
input2 = args[2]
input3 = args[3]

#
if (int(input1) >=70 and int(input2)  >=70 and int(input3) >= 70) or int(input1) + int(input2) +int(input3) >= 220 and (int(input1) > 50 and int(input2) > 50 and int(input3) > 50):
    print("合格",end="")
#（False）それ以外は偶数と表示
else:
    print("不合格",end="")