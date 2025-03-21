class Person(object):
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return "Name: %s, Age: %d" % (self.name, self.age)


per=Person('zhang',18)
print(per)
print(type(per))
print(per.__str__())