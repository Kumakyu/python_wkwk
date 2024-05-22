#水族館の入園料を計算しよう

#魔法の呪文
from datetime import date
import datetime
import sys
args = sys.argv

#入力部分
day = str(args[1])#日付 20000708
adult = int(args[2])#大人
children = int(args[3])#子供


# 入力された文章を数字、かつ年月日に変換
date = datetime.date(int(day[0:4]),int(day[4:6]),int(day[6:8]))

if date.strftime("%a") == "Sun" or  date.strftime("%a") ==  "Sat":
    sum = int(adult)*2400 + int(children)*1500

else:
    sum = int(adult)*2000 + int(children)*1200


print(int(sum),end="")


