import sys
args = sys.argv

#表示回数を入力
num = int(args[1])

#指定回数だけひつじのカウントを実行
for i in range(1, num+1):
    print("ひつじが" + str(i) + "匹")