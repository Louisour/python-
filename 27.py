from my_info import *
from introduce import *
#导入模块中具有同名变量和函数，后导入的会覆盖前面的
info()
#解决方案:直接使用模块名打点调用
import my_info
import introduce
my_info.info()
introduce.info()