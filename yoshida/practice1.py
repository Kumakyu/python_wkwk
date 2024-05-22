#魔法の呪文
import sys
args = sys.argv
sum = 0

#for文を使って1~10まで連続して足すプログラム

for i in range(1,11): #i=range（iがとりうる値の範囲を設定している＝だからiはこない）
    sum = sum + i

#合計を印刷
print(sum)