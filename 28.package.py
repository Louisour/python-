import admin.my_admin as a
a.info()
print('-'*40)
from admin import  my_admin as b
b.info()
print('-'*40)
from admin.my_admin import info#form 包名。模块名。 import 函数/变量等
info()

print('-'*40)
from admin.my_admin import *#所有属性和方法
print(name)