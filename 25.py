class Instrument():
    def make_sound(self):
        pass
class Erhu(Instrument):
    def make_sound(self):
        print('二胡在弹奏')

class Piano(Instrument):
    def make_sound(self):
        print('钢琴在弹奏')

class Violin(Instrument):
    def make_sound(self):
        print('小提琴在演奏')

def play(obj):
    obj.make_sound()

erhu = Erhu()
piano = Piano()
violin = Violin()
play(erhu)
play(piano)
play(violin)

class Car():
    def __init__(self,type,no):
        self.type = type
        self.no = no
    def start(self):
        print('我是车，我能启动')
    def stop(self):
        print('我是车，我可以停止')

class Taxi(Car):
    def __init__(self,type,no,company):
        super().__init__(type,no)
        self.company = company

    def start(self):
        print('乘客你好！')
        print(f'我是{self.company}出租车公司，我的车牌是：{self.no}，您要去哪里？')

    def stop(self):
        print('目的地到达')

class FamilyCar(Car):
    def __init__(self,type,no,name):
        super().__init__(type,no)
        self.name = name

    def start(self):
        print(f'我是{self.name}，我的轿车我做主')

    def stop(self):
        print('目的地到达')

taxi=Taxi('上海大众','京A8888','长城')
taxi.start()
taxi.stop()
print('-'*40)
family_car=FamilyCar('广汽丰田','京B6666','赵高')
family_car.start()
family_car.stop()
