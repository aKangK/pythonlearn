txt=r'C:\Users\二花\Desktop\python.test\t2.txt'
#将路径修改为t1.txt，文件即可读取，正常运行
flag=False
try:
    f=open(txt,'r')
    print(f.read())
    flag=True
except:
    print('打开%s文件出错，请检查！'%(txt))
finally:
    if flag:
        f.close()
        print('文件做关闭处理')
    else:
        print('程序关闭！')
