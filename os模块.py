import random
import os
import os.path
def create_filename():
    filename_lst=[]
    lst=['水果','烟酒','粮油','肉蛋','蔬菜']
    code=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    for i in range(1,3001):
        filename=''
        if i<10:
            filename+='000'+str(i)
        elif i<100:
            filename+='00'+str(i)
        elif i<1000:
            filename+='0'+str(i)
        else:
            filename+=str(i)
        filename+='_'+random.choice(lst)
        s=''
        for j in range(9):
            s+=random.choice(code)
        filename+='_'+s
        filename_lst.append(filename)
    return filename_lst

def create_file(filename):
    with open(filename,'w') as file:
        pass
if __name__ == '__main__':
    path='./data'
    if not os.path.exists(path):
        os.mkdir(path)
    lst=create_filename()
    for item in lst:
        create_file(os.path.join(path,item))