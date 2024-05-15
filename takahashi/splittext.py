#英文のn番目の単語に関するプログラム

#引数のためのモジュールをインポート
import sys
args = sys.argv

#文章の入力
sentence = args[1]
#番号の入力
num = int(args[2])

#指定したn番目の単語
word = sentence.split()

#結果の表示
print(word[num])