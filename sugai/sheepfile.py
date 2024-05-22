import sys
args = sys.argv

#表示回数を入力
num = int(args[1])


#sheep.txtに数えた結果を書き込む
with open("sheep.txt", mode="w", encoding="utf-8") as s:
    #指定回数だけひつじのカウントを実行
    for i in range(1, num+1):
        s.write("ひつじが" + str(i) + "匹\n")
    print(s.read())
    
        

