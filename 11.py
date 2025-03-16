def get_sum(num):
    s = 0
    for i in range(1,num+1):
        s+=i
    print(f'1到{num}之间的累加和为：{s}')

get_sum(10)

def happy_birthday(name,age):
    print('祝'+name+'生日快乐')
    print(str(age)+'岁生日快乐')

happy_birthday('中国','76')

happy_birthday(age=76,name='中国')
