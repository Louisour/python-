class Student():
    def __init__(self, name, age, gender):
        self._name = name
        self.__age = age
        self.gender = gender
    def _fun1(self):
        print('子类及本身可以访问')

    def __fun2(self):#私有的
        print('只有定义的类可以访问')

    def show(self):
        self._fun1()
        self.__fun2()
        print(self._name)
        print(self.__age)

stu=Student('赵高',2000,'男')
#类的外部
print(stu._name)
# print(stu.__age)
stu._fun1()
# stu.__fun2()
print(stu._Student__age)

stu._Student__fun2()

print(dir(stu))

