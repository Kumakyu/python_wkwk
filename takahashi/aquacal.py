# 水族館の料金のプログラム

# 引数のためのモジュール
import sys
args = sys.argv
# 引数の入力
days = str(args[1])
adult = int(args[2])
child = int(args[3])

# 文字列のスライス
year = int(days[0:4])
month = int(days[4:6])
day = int(days[6:8])

# 曜日を得る
import datetime
t = datetime.date(year,month,day)
dt = t.strftime("%a")

# 曜日の判定
if dt == "Sat" or dt == "Sun":
    amount = 2400*adult + 1500*child
else:
    amount = 2000*adult + 1200*child

# 結果の表示
print(amount, end="")