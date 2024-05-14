#給与計算プログラム
#四捨五入のための、モジュールをインポート
from decimal import Decimal, ROUND_HALF_UP
#引数のための、モジュールをインポート
import sys
args = sys.argv
#金額の入力
salary = int(args[1])
#支給額の計算
if salary > 1000000:
    #税額の計算
     tax = (salary - 1000000)*0.20 + 100000
     #四捨五入の計算
     tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
else:
     tax = salary*0.10
     #四捨五入の計算
     tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
pay_amount = salary - tax
#結果の表示
print("支給額:", pay_amount, "、税額", tax)


