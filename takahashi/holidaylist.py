from datetime import date
from database import session
from tables import Holiday

# データを取得する
holidaylist=session.query(Holiday.holi_date).filter_by(holi_text = "憲法記念日").all()
 
for holiday in holidaylist:
    print(holiday.holi_date, holiday.holi_text)

#INSERT処理
session.add(holiday)
#コミット
session.commit()