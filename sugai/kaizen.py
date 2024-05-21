#
#各モジュールのインストール 
import sys
from datetime import date
from database import session
from tables import Holiday

#条件入力(日付、大人の人数、子供の人数)
args = sys.argv
input_date=str(args[1])
input_adults=int(args[2])
input_children=int(args[3])

#input_dateの入力値からyear, month, dayに対応する部分を抜き出す
year = int(input_date[0:4])
month = int(input_date[4:6])
day = int(input_date[6:8])

#入力日のデータを取得
dt = date(year, month, day)

#条件分岐
#まずは入力日が土日かどうか判断
if dt.strftime("%a") == "Sat" or dt.strftime("%a") == "Sun":
    pay_sum=2400*input_adults + 1500*input_children

else:
    #平日のうち、休日かそうでないかを判断
    x = session.query(Holiday.holi_date).filter_by(holi_date = dt).first()
    if x is None:
        pay_sum=2000*input_adults + 1200*input_children
    else:
        pay_sum=2400*input_adults + 1500*input_children
#出力
print(pay_sum, end="")

