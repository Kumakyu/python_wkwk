#四捨五入のための、モジュールをインポート
from decimal import Decimal, ROUND_HALF_UP

# 関数の定義
def calcsalary(salary):
    if salary > 1000000:
    #税額の計算
     tax = (salary - 1000000)*0.20 + 100000
     #四捨五入の計算
     tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    else:
     tax = salary*0.10
     #四捨五入の計算
     tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    #支給額の計算
    pay_amount = salary - tax
    # print("給与:" + str(salary) + "、支給額:" + str(pay_amount) + 
    #       "、税額:" + str(tax))
    return [pay_amount,tax]