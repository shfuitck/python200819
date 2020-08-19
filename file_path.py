import os.path

if os.path.isfile('yee.txt'):
    print('存在')
    file=open('yee.txt','a')
    file.write('檔案94存在')
    file.close()
else :
    print('不存在')
    file=open('yee.txt','w')
    file.write('這是新檔案')
    file.close()