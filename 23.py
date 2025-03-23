class CPU():
    pass
class Disk():
    pass
class Computer():
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

cpu=CPU()
disk=Disk()

com=Computer(cpu,disk)
com1=com
print(com)
print(com1)


print('-'*40)
import copy
com2=copy.copy(com)
print(com,com.cpu,com.disk)
print(com2,com2.cpu,com2.disk)


print('-'*40)
com3=copy.deepcopy(com)
print(com,com.cpu,com.disk)
print(com3,com3.cpu,com3.disk)


