import sys
args = sys.argv

#入力
start = str (args[1])
goal = str (args[2])

#辞書型のデータを作成
dic = {'東京':0.00,'品川':6.78,'新横浜':25.54,'名古屋':342.02,'京都':476.31,'新大阪':515.35}

#距離の計算
distance = (round (abs(dic[start] - dic[goal]),2))

#出力
print(distance,end="")