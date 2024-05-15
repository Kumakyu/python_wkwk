#新幹線の駅間を計算するプログラム

#引数のためのモジュールをインポート
import sys
args = sys.argv

#辞書型の定義
station_distance = {'東京': 0, '品川': 6.78, '新横浜': 25.54, '名古屋': 342.02, '京都': 476.31, '新大阪': 515.35}

#引数の入力
station1 = args[1]
station2 = args[2]

#駅間の距離の計算
distance = abs(station_distance[station1] - station_distance[station2])

#結果の表示
print(distance)