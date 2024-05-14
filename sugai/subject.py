import sys
args = sys.argv

math = int(args[1])
japanese = int(args[2])
english = int(args[3])

if ((math+japanese+english >= 220) or (math>= 70 and japanese>= 70 and english >= 70)) and (math >= 50 and japanese >= 50 and english >= 50):
    print("合格", end="")
else:
    print("不合格",end="")



