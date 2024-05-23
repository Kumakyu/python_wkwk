#引数のためのモジュール
import sys
from datetime import date

#データベース「Holiday」をインポート
from database import session
from tables import Holiday

# 来場日、大人の人数、子供の人数を入力
day = str(sys.argv[1])  # 来場日（YYYYMMDD）
adult = int(sys.argv[2])  # 大人
children = int(sys.argv[3])  # 子供

#土日祝日料金
adult_high_fee = 2400
children_high_fee = 1500

#平日料金
adult_low_fee = 2000
children_low_fee = 1200

#来場日を文字型→数値に変換
input_date = date(int(day[0:4]), int(day[4:6]), int(day[6:8]))


# 土曜、日曜日の場合
if input_date.strftime("%a") in ["Sun", "Sat"]:
    total = adult * adult_high_fee + children * children_high_fee

#平日の場合
else:
    holiday = session.query(Holiday.holi_date).filter_by(holi_date=input_date).first()
    if holiday is None:
        total = adult * adult_low_fee + children * children_low_fee
    #「Holiday」の祝日と入力した日付が重複している場合
    else:
        total = adult * adult_high_fee + children * children_high_fee

#合計金額を出力
print(total)