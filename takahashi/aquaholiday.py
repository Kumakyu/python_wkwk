# 水族館の料金のプログラム
from datetime import date
#import datetime    #モジュールごとのimportする記述
import sys
#mysqlDB接続、テーブル
from database import session
from tables import Holiday


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
wday = t.strftime("%a")
dt = t.strftime('%Y/%m/%d')

# 曜日の判定
if wday == "Sat" or wday == "Sun":
    amount = 2400*adult + 1500*child
else:
    get_date = session.query(Holiday.holi_date).filter_by(holi_date = dt).first()
    if get_date is None:
        amount = 2000*adult + 1200*child
    else:
        amount = 2400*adult + 1500*child

# 結果の表示
print(amount, end="")