class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name ,age ):
        self.name = name
        self.age = age
a=A()
b=B()
c=C('John',23)

print(a.__dict__)
print(b.__dict__)
print(c.__dict__)

print(a.__class__)
print(b.__class__)
print(c.__class__)

print(A.__bases__)
print(B.__bases__)
print(C.__bases__)

print(A.__base__)
print(B.__base__)
print(C.__base__)

print(A.__mro__)
print(B.__mro__)
print(C.__mro__)

print(A.__subclasses__())
print(B.__subclasses__())
print(C.__subclasses__())