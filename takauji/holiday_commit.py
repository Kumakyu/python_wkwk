from datetime import date
from database import session
from tables import Holiday
import sys
args = sys.argv
 
#数字を入力させる（この時点だと八桁の数）
day = str(args[1])

#八桁の数から年、月、日付ごとに取り出す
date = (int(day[0:4]),int(day[4:6]),int(day[6:8]))
print (date)
 
# データを取得する
holidaylist=session.query(Holiday).all()
 
for holiday in holidaylist:
    print(holiday.holi_date,holiday.holi_text)

