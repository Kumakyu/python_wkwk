import sys
args = sys.argv

input_name = args[1]
input_age = args[2]

class intro:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name_out(self):
        nametxt = "私の名前は、" + self.name + "です"
        return nametxt
    
    def age_out(self):
        agetxt = "年齢は、" +self.age +"歳です"
        return agetxt
    
a = intro(input_name, input_age)
print(a.name_out())
print(a.age_out())



        