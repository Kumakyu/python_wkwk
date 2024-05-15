import sys
args = sys.argv

#タプルに世界人口ランキングを定義
country =("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

#数値を入力
num = int(args[1])

#入力数値のインデックス番号に対応する国名を表示
print(country[num-1], end="")
