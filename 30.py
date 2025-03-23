import time
now=time.time()
print(now)

obj=time.localtime()
print(obj)

obj2=time.localtime(60)
print(obj2)
print(obj2.tm_year)
print(time.ctime())

print(time.strftime('%Y-%m-%d %H:%M:%S', obj))

print(time.strptime('2008-08-08', '%Y-%m-%d'))
time.sleep(2)
print('hello world')
