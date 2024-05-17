# モジュールの取り込み
from func_salary import calcsalary

# 引数のためのモジュールの取り込み
import sys
args = sys.argv

for i in range(1,len(args)):
    salary = int(args[i])
    # 結果の表示
    # calcsalary(salary)
    result = calcsalary(salary)
    print("給与:" + str(salary) + "、支給額:" + str(result[0]) + 
          "、税額:" + str(result[1]))