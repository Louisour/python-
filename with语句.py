def write_fun():
    with open('aa.txt', 'w',encoding='utf-8') as file:
        file.write('2022北京东奥会欢迎你')

def read_fun():
    with open('aa.txt', 'r',encoding='utf-8') as file:
        print(file.read())

def copy(src_file,target_file):
    with open(src_file,'r',encoding='utf-8') as file:
        with open(target_file,'w',encoding='utf-8') as file2:
            file2.write(file.read())

if __name__ == '__main__':
    write_fun()
    read_fun()
    copy('./aa.txt','./dd.txt')