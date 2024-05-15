import sys
args = sys.argv

#数字を入力
number = int(args[1])
calculation_result = 0

#計算結果が100を超えない場合は足し算を繰り返す
while calculation_result < 100:
    calculation_result = calculation_result + int(args[1])

#計算結果が丁度100になった場合はJust 100！を表示
if calculation_result == 100:
    print("Just 100!",end="")

#計算結果が100を超えた場合はOver！を表示
elif calculation_result >100:
    print("Over!", end="")
