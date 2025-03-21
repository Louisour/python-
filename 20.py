class Person(object):
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name, self.age)

per=Person('赵高',2000)

print(dir(per))
print(per)