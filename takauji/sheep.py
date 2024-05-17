import sys
args = sys.argv

#羊の数を入力
sheep_count = int(args[1])

#入力された羊の数だけ、羊の数をカウントする
for i in range (1,sheep_count):
sheep = i 
    print ("ひつじが",sheep,"匹",end="")