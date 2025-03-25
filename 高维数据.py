import json
lst=[
    {'name':'赵高','age':2000,'score':100},
    {'name':'张','age':2001,'score':10},
    {'name':'cheng','age':2002,'score':101},
]
s=json.dumps(lst,ensure_ascii=False,indent=4)
print(type(s))
print(s)
print('-'*40)

lst2=json.loads(s)
print(type(lst2))
print(lst2)
print('-'*40)

with open('student.txt','w',encoding='utf-8') as file:
    json.dump(lst,file,ensure_ascii=False,indent=4)

with open('student.txt','r',encoding='utf-8') as file:
    lst3=json.load(file)
    print(type(lst3))
    print(lst3)
