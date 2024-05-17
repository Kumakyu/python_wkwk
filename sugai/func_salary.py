from decimal import Decimal, ROUND_HALF_UP
import sys
#給料を入力として支給額、税額を返す関数
def calcsalary(salary, tax_rate, tax_rate2):
    if salary > 1000000:
        surplus_minutes = salary - 1000000
        tax = 1000000*tax_rate + surplus_minutes*tax_rate2
        tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
        pay_amount = salary - tax 
    else:
        tax = salary * tax_rate
        tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
        pay_amount = salary -tax
    print("支給額:" + str(pay_amount)+"、税額:" + str(tax))