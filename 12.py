def calc(a,b):
    return a+b
print(calc(1,2))
s=lambda a,b:a+b
print(type(s))
print(s(10,20))


lst=[1,2,3,4,5,6,7,8,9]
for i in range(len(lst)):
    result=lambda x:x[i]
    print(result(lst))

student_scores=[
    {'name':'A','score':90},
    {'name':'B','score':80},
    {'name':'C','score':70},
    {'name':'D','score':60}
]
student_scores.sort(key=lambda x:x.get('score'),reverse=True)
print(student_scores)