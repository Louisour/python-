import random
random.seed(10)
print(random.random())#[0.0,1.0]
print(random.random())
print('-'*40)
random.seed(10)
print(random.randint(1,100))#[1,100]
print('-'*40)
for i in range(10):#[m,n)
    print(random.randrange(1,10,3))

print(random.uniform(1,100))#[a,b]随机小数
print('-'*40)
lst=[i for i in range(1,11)]
print(random.choice(lst))

print('-'*40)
random.shuffle(lst)
print(lst)
random.shuffle(lst)
print(lst)