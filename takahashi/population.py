#世界の人口ランキングのプログラム
#引数のためのモジュールをインポート
import sys
args = sys.argv
#順位の入力
rank = int(args[1])
#リストの定義
country_tuple = ("China","India","U.S.A","Indonesia",
               "Pakistan","Brazil","Nigeria","Bangladesh","Russia","Mexico")
#順位の出力
contry_rank = country_tuple[rank -1]
print(contry_rank)
