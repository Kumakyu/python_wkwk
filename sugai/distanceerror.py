import sys
args = sys.argv

#辞書型に新幹線駅名と東京駅からの距離を定義
distance = {'東京' : 0.00, '品川' : 6.78, '新横浜': 25.54, '名古屋':342.02, '京都':476.31, '新大阪':515.35}

#新幹線駅名を2つ入力
input_station1 = str(args[1])
input_station2 = str(args[2])

#入力した2つの駅間の距離を表示
try:
    print(round(abs(distance[input_station1] - distance[input_station2]), 2), end="")
except:
    print("のぞみの停車駅を引数に設定してください", end="")
