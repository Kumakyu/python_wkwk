import sys
args = sys.argv

#知りたい順位の値を入力
input1 = int (args[1])

#国名リストを指定
country_list = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")
country_name = country_list[input1 -1]

#出力
print(country_name,end="")