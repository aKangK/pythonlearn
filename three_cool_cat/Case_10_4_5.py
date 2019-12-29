import os
print(os.path.abspath(os.path.curdir))
print(os.path.exists(r'C:\Users\二花\Desktop\python.test\t1.txt'))
print(os.path.isfile(r'C:\Users\二花\Desktop\python.test\t1.txt'))
print(os.path.isdir(r'C:\Users\二花\Desktop\python.test'))
print(os.path.exists(r'C:\Users\二花\Desktop\python.test'))
os.makedirs(r'C:\Users\二花\Desktop\python.test\test1')
print('新文件夹"test1"建立完成！')
