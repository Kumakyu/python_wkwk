from datetime import date
import sys
args = sys.argv
 
#数字を入力させる（この時点だと八桁の数）
day = str(args[1])
count_adult = int(args[2])
count_child = int(args[3])

#八桁の数から年、月、日付ごとに取り出す
year = int(day[0:4])
month = int(day[4:6])
day = int(day[6:8])
 
#曜日を得る
import datetime
t = datetime.date(year,month,day)
dt= t.strftime("%a")

#平日か土日かを判定する
if dt == "Sat" or dt == "Sun":
    pay_adult = 2400 * count_adult
    pay_child = 1500 * count_child

else:
    pay_adult = 2000 * count_adult
    pay_child = 1200 * count_child

total_pay = pay_adult + pay_child

print(total_pay ,end="")