#新幹線の駅間を計算するプログラムその2

#引数のためのモジュールをインポート
import sys
args = sys.argv

#辞書型の定義
station_distance = {'東京': 0, '品川': 6.78, '新横浜': 25.54, '名古屋': 342.02, '京都': 476.31, '新大阪': 515.35}

#引数の入力
station_name1 = str(args[1])
station_name2 = str(args[2])

#駅間の距離の計算
try:
    distance = round(abs(station_distance[station_name1] - station_distance[station_name2]),2)
    #結果の表示
    print(distance, end="")
except:
    print("のぞみの停車駅を引数に設定してください", end="")