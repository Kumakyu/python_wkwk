import sys
args = sys.argv

#引数の設定
score_math=int(args[1])
score_japanese=int(args[2])
score_english=int(args[3])

#合格の条件
if (score_math >=70 and score_japanese >=70 and score_english >=70 )or (score_math + score_japanese + score_english >=220)and (score_math >=50 and score_japanese >=50 and score_english >=50):
    print("合格",end="")

#不合格の条件
else:
    print("不合格",end="")
