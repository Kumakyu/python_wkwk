#魔法の呪文
import sys
args = sys.argv

#引数を変数に代入
hm_class = args[1]              #値下げ対象の種別
price_down = int(args[2])   #値下げ額

#品目（品名と価格）を辞書型で定義
hinmoku = {
    "リンゴ":80 , "みかん":198, "バナナ":150,
 "ビール":360, "日本酒":580,
  "ラーメン":380, "うどん":128, "パスタ":258}

#区分ごとの定義
fruits = ("リンゴ", "みかん", "バナナ")     #果物類をタプルで定義
alcohol = ("ビール", "日本酒")              #酒類をタプルで定義
noodles = ("ラーメン", "うどん", "パスタ")   #麺類をタプルで定義

#値下げした後の金額を計算する
#果物

hinmoku[fruits] -price_down

hinmoku[fruits] -price_down

hinmoku[fruits] -price_down


#計算できたものを出力する
print