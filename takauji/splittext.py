import sys
args = sys.argv
#第二引数に英文の指定
text = str(args[1])

#第三引数に何語目を取り出したいかを指定
word_number = int(args[2])

#第三引数で指定した番号の単語を出力する
a =text.split()
print(a[word_number -1],end="")