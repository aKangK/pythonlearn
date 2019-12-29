nums=['one','two','three','four','five','six']
txt=r'C:\Users\二花\Desktop\python.test\t1.txt'
t=open(txt,'a')
for one in nums:
    t.write(one+'\n')
t.close()
print('连续写入完成')

t1=open(txt,'r')
dd=1
while dd:
    dd=t1.readline()
    print(dd)
t1.close()

t2=open(txt,'r')
L_s=t2.readlines()
print(L_s)
t2.close()

f=open(txt,'r')
print(f.readline(2))
print(f.readline())
print(f.readline(4))
print(f.readline(4))
print(f.tell())
print(f.read(1))
print(f.tell())

