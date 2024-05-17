#奇数、偶数判定プログラム

#引数のためのモジュール
import sys
args = sys.argv

# 関数の定義
def calcvalue(num):
    if num %2 == 0:
        return True #偶数
    else:
        return False #奇数

# 引数の入力
for i in range(1,len(args)):
    num = int(args[i])
    # 結果の表示
    if calcvalue(num):
        print(str(num) + "は偶数")
    else:
        print(str(num) + "は奇数")