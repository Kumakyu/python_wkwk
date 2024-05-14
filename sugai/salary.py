from decimal import Decimal, ROUND_HALF_UP
import sys
args = sys.argv

#変数一覧
salary = 0
pay_amount = 0
tax = 0
tax_rate = 0.1
tax_rate2 = 0.2
surplus_minutes = 0

#給与を入力
salary = int(args[1])

#給与に応じた条件分岐
if salary < 1000000:
    surplus_minutes = salary - 1000000
    tax = 1000000*tax_rate + a*tax_rate2
    tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
    pay_amount = salary - tax 
    print("支給額:" + str(pay_amount)+ "、税額:" + str(tax))
else:
    tax = salary * tax_rate
    tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
    pay_amount = salary -tax
    print("支給額:" + str(pay_amount)+"、税額:" + str(tax))



