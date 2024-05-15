#世界の人口ランキングのプログラム
#引数のためのモジュールをインポート
import sys
args = sys.argv
#順位の入力
rank = int(args[1])
#リストの定義
countrylist = ("China","India","U.S.A","Indonesia","Pakistan","Brazil","Nigeria","Bangladesh","Russia","Mexico")
#順位の出力
contry_rank = countrylist[rank]
print(contry_rank)


