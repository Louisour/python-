class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name, self.age)

class Student(Person):
    def __init__(self, name,age,stuno):
        super().__init__(name,age)#调用父类的初始化方法
        self.stuno = stuno


class Doctor(Person):
    def __init__(self, name,age,department):
        super().__init__(name,age)
        self.department = department
#第一个子类对象
stu=Student('赵高',2000,'1001')


doctor=Doctor('张一一',32,'外科')
doctor.show()