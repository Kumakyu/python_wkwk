#英文のn番目の単語に関するプログラム

#引数のためのモジュールをインポート
import sys
args = sys.argv

#引数の入力
sentence = args[1]
num = int(args[2])

word = sentence.split()

#結果の表示
print(word[num])