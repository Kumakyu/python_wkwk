import sys
args = sys.argv
from decimal import Decimal, ROUND_HALF_UP
#給料を入力
salary = int(args[1])


#１００万円以上なら税率が２０%
if salary > 1000000:
   tax_amount = (salary - 1000000) * 0.2 + 100000

#それ以外なら税率が１０%  
else:
    tax_amount = salary*0.1

tax_amount = Decimal(str(tax_amount)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)

pay_amount = salary - tax_amount

print("支給額:" + str(pay_amount)+"、税額:" + str(tax_amount), end="")



