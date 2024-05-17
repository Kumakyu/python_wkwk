from decimal import Decimal, ROUND_HALF_UP
import sys
import func_salary
args = sys.argv

#変数一覧
salary = 0
pay_amount = 0
tax = 0
tax_rate = 0.1
tax_rate2 = 0.2
surplus_minutes = 0

#給与を入力
#salary = int(args[1])

for i in range(1, len(args)):
    func_salary.calcsalary(int(args[i]), 0.1, 0.2)