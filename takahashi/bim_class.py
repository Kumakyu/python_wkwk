# BMIを計算するクラス
class BMI:
    def __init__(self, weight, height) -> None:
        '''初期化'''
        self.weight = weight
        self.height = height
        self.calcBMI()

    def calcBMI(self):
        '''BMIを計算'''
        h = self.height / 100
        self.bmi = self.weight / (h ** 2)

    def printJudge(self):
        '''結果を表示'''
        print("---")
        print("BMI=",self.bmi)
        b = self.bmi
        if(b < 18.5): print("やせ型")
        elif(b < 25): print("標準")
        elif(b < 30): print("肥満（軽）")
        else: print("肥満（重）")

# 引数のためのモジュール
import sys
args = sys.argv
# 引数の入力
weight = int(args[1])
height = int(args[2])

person = BMI(weight,height)
person.printJudge()