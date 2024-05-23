import sys
args = sys.argv

#入力する繰り返し回数を引数に設定
input = int(args[1])

#入力した回数分繰り返し
for sheep in range(1,input + 1):
    print("ひつじが" +str(sheep)+"匹")