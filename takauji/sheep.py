import sys
args = sys.argv

#羊の数を入力
sheep_count=int(args[1])

#入力された羊の数だけ、羊の数をカウントする 
for i in range (1,sheep_count+1):#１から、引数で渡した数字＋1回数える→これがIに入る
    #sheep = i 
    print ("ひつじが"+str(i)+"匹")