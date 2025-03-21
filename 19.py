class Person():
    def eat(self):
        print('人吃五谷杂粮')

class Cat():
    def eat(self):
        print('猫喜欢吃鱼')

class Dog():
    def eat(self):
        print('狗喜欢啃骨头')

def fun(obj):
    obj.eat()

person = Person()
cat = Cat()
dog = Dog()

fun(person)
fun(cat)
fun(dog)