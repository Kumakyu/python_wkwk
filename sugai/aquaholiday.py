from datetime import date 
import sys
from datetime import date
from database import session
from tables import Holiday

args = sys.argv

#条件入力
input1=str(args[1])
input2=int(args[2])
input3=int(args[3])

#input１の入力値からyear, month, dayに対応する部分を抜き出し
year = int(input1[0:4])
month = int(input1[4:6])
day = int(input1[6:8])

#入力日のデータを取得
dt = date(year, month, day)

#入力が祝日かどうかを判断するプログラム
holidaylist=session.query(Holiday).all()
a = []
for holiday in holidaylist:
    a.append(holiday.holi_date)
    print(a)
if dt in a:
    pay_sum=2400*input2 + 1500*input3
     #曜日が土、日かそれ以外で条件分岐
elif dt.strftime("%a") == "Sat" or dt.strftime("%a") == "Sun":
    pay_sum=2400*input2 + 1500*input3
else:
    pay_sum=2000*input2 + 1200*input3
#出力
print(pay_sum, end="")