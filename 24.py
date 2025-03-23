import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2
    def perimeter(self):
        return 2 * 3.14*self.radius

r=eval(input('请输入圆的半径：'))
c=Circle(r)
print(c.area())
print(c.perimeter())



class Student(object):
    def __init__(self, name,age,gender,score):
        self.name = name
        self.age = age
        self.gender=gender
        self.score = score


    def info(self):
        print(self.name, self.age,self.gender,  self.score)


print('请输入5位学生信息：(姓名#年龄#性别#分数)')
lst=[]
for i in range(1,6):
    s=input(f'请输入第{i}位学生信息及成绩')
    s_lst=s.split('#')
    stu=Student(s_lst[0],s_lst[1],s_lst[2],s_lst[3])
    lst.append(stu)

for item in lst:
    item.info()

