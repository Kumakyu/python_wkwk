from decimal import Decimal,ROUND_HALF_UP

import sys
import fanc_salary
args = sys.argv


for i in range(1,len(args)):
    num = int(args[i])
    fanc_salary.calcsalary(num)#ファンクサラリーのかるくサラリーの関数を使う
    