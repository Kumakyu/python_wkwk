import sys
args = sys.argv

#羊の数を入力
sheep_count = int (args[1])

#入力された羊の数だけ、羊の数をカウントする
for i in range (sheep_count):
    print ("ひつじが" + sheep_count +"匹")