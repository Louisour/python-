def copy(src,new_path):
    file1 = open(src,'rb')
    file2 = open(new_path,'wb')
    s=file1.read()
    file2.write(s)
    file2.close()
    file1.close()#先开后关

if __name__ == '__main__':
    src='./logo.png'#.表示当前目录
    new_path='../1/copy_logo.png'#..上一级目录
    copy(src,new_path)
    print('success')