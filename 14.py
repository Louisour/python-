lst=[54,56,77,4,567,34]
asc_lst=sorted(lst)
desc_lst=sorted(lst,reverse=True)
print(asc_lst)
print(desc_lst)

x=['a','b','c','d','e','f','g','h']
y=[10,20,30,40,50]
zipoj=zip(x,y)
print(type(zipoj))
print(list(zipoj))

def fun(num):
    return num%2==1
obj=filter(fun,range(10))
print(list(obj))
