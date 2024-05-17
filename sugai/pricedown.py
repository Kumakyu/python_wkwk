"""
import sys
args = sys.argv

input1 = str(args[1])
input2 = int(args[2])

hinmoku = {"リンゴ":80, "みかん": 198, "バナナ":150, "ビール":360, 
           "日本酒": 580, "ラーメン":380, "うどん":128, "パスタ": 258}

hinmoku["果物"] = {"リンゴ":80, "みかん": 198, "バナナ":150}
hinmoku["酒類"] = {"ビール":360, "日本酒": 580}
hinmoku["麺類"] = {"ラーメン":380, "うどん":128, "パスタ": 258}

print(hinmoku[input1], end="")
a = hinmoku[input1]

if a==hinmoku["果物"]:
    hinmoku={"リンゴ":80-input2, "みかん": 198-input2, "バナナ":150-input2, "ビール":360, 
           "日本酒": 580, "ラーメン":380, "うどん":128, "パスタ": 258}
    print(hinmoku, end="")
elif a==hinmoku["酒類"]:
    hinmoku = {"リンゴ":80, "みかん": 198, "バナナ":150, "ビール":360-input2, 
           "日本酒": 580-input2, "ラーメン":380, "うどん":128, "パスタ": 258}
    print(hinmoku, end="")
elif a==hinmoku["麺類"]:
    hinmoku = {"リンゴ":80, "みかん": 198, "バナナ":150, "ビール":360, 
           "日本酒": 580, "ラーメン":380-input2, "うどん":128-input2, "パスタ": 258-input2}
    print(hinmoku, end="")
"""
import sys
args = sys.argv

#引数を変数に代入
#hm_class = args[1]              #値下げ対象の種別
#price_down = int(args[2])   #値下げ額

#品目（品名と価格）を辞書型で定義
hinmoku = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

#区分ごとの定義
fruits = ("リンゴ", "みかん", "バナナ")            #果物類をタプルで定義
alcohol = ("ビール", "日本酒")                         #酒類をタプルで定義
noodles = ("ラーメン", "うどん", "パスタ")   #麺類をタプルで定義

#ここ以降にプログラムを書く
input1 = str(args[1])
input2 = int(args[2])

hinmoku["果物類"] = {"リンゴ":80, "みかん": 198, "バナナ":150}
hinmoku["酒類"] = {"ビール":360, "日本酒": 580}
hinmoku["麺類"] = {"ラーメン":380, "うどん":128, "パスタ": 258}

#print(hinmoku[input1], end="")
a = hinmoku[input1]

if a==hinmoku["果物類"]:
    hinmoku={"リンゴ":max(80-input2, 1), "みかん": max(198-input2, 1), "バナナ":max(150-input2, 1), "ビール":360, 
           "日本酒": 580, "ラーメン":380, "うどん":128, "パスタ": 258}
elif a==hinmoku["酒類"]:
    hinmoku = {"リンゴ":80, "みかん": 198, "バナナ":150, "ビール":max(360-input2,1), 
           "日本酒": max(580-input2,1), "ラーメン":380, "うどん":128, "パスタ": 258}
elif a==hinmoku["麺類"]:
    hinmoku = {"リンゴ":80, "みかん": 198, "バナナ":150, "ビール":360, 
           "日本酒": 580, "ラーメン":max(380-input2,1), "うどん":max(128-input2,1), "パスタ": max(258-input2,1)}
print(hinmoku, end="")