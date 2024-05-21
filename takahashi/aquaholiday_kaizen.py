# 水族館の料金のプログラム
from datetime import date
#import datetime    #モジュールごとのimportする記述
import sys
#mysqlDB接続、テーブル
from database import session
from tables import Holiday

args = sys.argv

# 引数の入力 → 引数に変数を入力
input_days = str(args[1])
adult = int(args[2])
child = int(args[3])

# 文字列のスライス
year = int(input_days[0:4])
month = int(input_days[4:6])
day = int(input_days[6:8])

# 曜日・日にちの取得
t = date(year, month, day)
weekday = t.strftime("%a")
dt = t.strftime('%Y/%m/%d')

# 曜日の判定
if weekday == "Sat" or weekday == "Sun": #土日の判定
    amount = 2400 * adult + 1500 * child
else:
    get_date = session.query(Holiday.holi_date).filter_by(holi_date = dt).first() #祝日の日にちと同じ日を取得
    if get_date is None: #平日
        amount = 2000 * adult + 1200 * child
    else: #祝日
        amount = 2400 * adult + 1500 * child