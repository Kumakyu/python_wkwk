# クラスの生成
class Intro:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def name_out(self):
        nametxt = "私の名前は、" + self.name + "です"
        return nametxt
    def age_out(self):
        agetxt = "年齢は、" + self.age + "歳です"
        return agetxt