#外部からインポートする関数
from decimal import Decimal,ROUND_HALF_UP

def calcsalary(a):
    if a > 1000000:

        tax = ((a - 1000000) * 0.2) + 100000
        #四捨五入の計算
        #変数「tax」を計算したのちに四捨五入を行う
        tax = Decimal(str(tax)).quantize(Decimal("0"),
        rounding=ROUND_HALF_UP)   
        payment = a - tax #総支給額
    else:
        tax = a * 0.1
        #四捨五入の計算
        #変数「tax」を計算したのちに四捨五入を行う
        tax = Decimal(str(tax)).quantize(Decimal("0"),
        rounding=ROUND_HALF_UP)   
        payment = a - tax #総支給額

    print("支給額:"+str(payment)+"、"+"税額:"+str(tax),end="")

     