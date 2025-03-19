class Student:
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if value!='男'and value!='女':
            print('性别有误')
            self.__gender='男'
        else:
            self.__gender = value


stu=Student('赵高','男')
print(stu.name,'的性别是：',stu.gender)

# stu.gender='男'AttributeError: property 'gender' of 'Student' object has no setter
stu.gender='女'#调用@gender.setter
print(stu.name,'的性别是：',stu.gender)#调用@gender.setter之后调用@property