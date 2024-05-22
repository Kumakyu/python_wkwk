import sys
args = sys.argv

#引数を変数に代入
hm_class = args[1]              #値下げ対象の種別
price_down = int(args[2])   #値下げ額

#品目（品名と価格）を辞書型で定義
hinmoku = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

#区分ごとの定義
fruits = ("リンゴ", "みかん", "バナナ")            #果物類をタプルで定義
alcohol = ("ビール", "日本酒")                         #酒類をタプルで定義
noodles = ("ラーメン", "うどん", "パスタ")   #麺類をタプルで定義

#ここ以降にプログラムを書く
if hm_class=="果物類":
    cate = fruits
elif hm_class =="酒類":
    cate =alcohol
elif hm_class=="麺類":
    cate=noodles

print(hinmoku[cate[0]])

hinmoku = {
    '果物類':{'リンゴ':80,'みかん':198,'バナナ':150},
    '酒類':{'ビール':360, '日本酒':580},
    '麺類':{'ラーメン':380,'うどん':128,'パスタ':258}}

#print(hinmoku['果物類'][cate[0]])

for i in range(0, int(len(cate))):
    max(hinmoku[hm_class][cate[i]] - price_down, 1)

print(hinmoku)

#値下げの処理と結果の表示
if hm_class == "果物類":
    for item in fruits:
        hinmoku[item] = max(hinmoku[item] - price_down, 1)
    print(hinmoku,end="")
elif hm_class == "酒類":
    for item in alcohol:
        hinmoku[item] = max(hinmoku[item] - price_down, 1)
    print(hinmoku,end="")
elif hm_class == "麺類":
    for item in noodles:
        hinmoku[item] = max(hinmoku[item] - price_down, 1)
    print(hinmoku,end="")
