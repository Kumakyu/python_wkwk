from decimal import Decimal, ROUND_HALF_UP

def calcsalary(a):
    #１００万円以上なら税率が２０%
    if a > 1000000:
        tax_amount = (a - 1000000) * 0.2 + 100000
        tax_amount = Decimal(str(tax_amount)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)

    #それ以外なら税率が１０%  
    else:
        tax_amount = a*0.1
        tax_amount = Decimal(str(tax_amount)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)

    pay_amount = a - tax_amount

    print("支給額:" + str(pay_amount)+"、税額:" + str(tax_amount))


