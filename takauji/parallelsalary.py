import sys
import func_salary

#給料を入力
args = sys.argv
for i in range(1,len(args)):
    num = int(args[i])
    func_salary.calcsalary(num)


