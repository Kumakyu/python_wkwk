import sys
args = sys.argv

#四捨五入のためにモジュールをインポート
from decimal import Decimal, ROUND_HALF_UP

#入力する給与を引数に設定
salary =int(args[1]) 

#100万円以上なら20%の税率をかけて＋10万円する
if salary >1000000 :
    tax=((salary-1000000)*0.2)+100000

#それ以外は10%の税率をかける
else:
    tax=((salary)*0.1)

#四捨五入の計算
#変数「tax」を計算したのちに四捨五入を行う
tax = Decimal(str(tax)).quantize(Decimal("0"),
rounding=ROUND_HALF_UP)    

payment = salary - tax 

print("支給額:"+str(payment)+"、"+"税額:"+str(tax),end="")

