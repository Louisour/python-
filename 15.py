class Student:
    school='湖南科技大学'
    def __init__(self,xm,age):
        self.name=xm
        self.age=age
    def show(self):
        print(self.name,self.age)
    # @staticmethod
    # def sm():
    #     #print(self.name)
    #     #self.show


stu=Student('csl',18)
print(stu.name,stu.age)
stu.show()
stu1=Student('hrb',19)
stu2=Student('sxn',21)
stu3=Student('hsb',22)
stu.gender='男'
lst=[stu,stu1,stu2,stu3]
print(stu.name,stu.age,stu.gender)
for i in lst:
    i.show()