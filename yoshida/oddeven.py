import sys
args = sys.argv

#引数を変数に代入
number = args[1]
number = int(number) 

#（True）奇数ならば奇数と表示
if number%2 == 1:
    print("奇数",end="")
#（False）それ以外は偶数と表示
else:
    print("偶数",end="")