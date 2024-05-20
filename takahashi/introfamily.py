# クラスの作成
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
    
class IntroFam(Intro):
    def __init__(self, name, age, cat_name) -> None:
        super().__init__(name, age)
        self.cat_name = cat_name

    def cat_out(self):
        familytxt = "飼い猫の名前は、" + self.cat_name + "です"
        return familytxt