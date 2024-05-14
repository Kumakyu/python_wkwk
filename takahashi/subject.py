#テスト結果の判定
#引数のためのモジュールをインポート
import sys
args = sys.argv
#引数の入力
Japanese = int(args[1])
Math = int(args[2])
English = int(args[3])
#変数の設定
sum = Japanese + Math + English
#判定開始
if ((Japanese >= 70 and Math >= 70 and English >= 70) or (sum >= 220)) and (Japanese >=50 and Math >=50 and English >= 50):
    print("合格", end="")
else:
    print("不合格", end="")