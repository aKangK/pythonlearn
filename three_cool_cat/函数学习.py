def find_factor(nums):
    '''
    find_factor是一个自定义函数'''
    if type(nums)!=int:
        print('非法输入')
        return
    i=1
    str1=''
    print('%d的因数是：'%(nums))
    while i<=nums:
        if nums%i==0:
            str1=str1+' '+str(i)
        i=i+1
    return str1

#===================================自定义函数结束，开始函数调用
n=input('请输入一个整数')
if n.isdigit():
    n=int(n)
    print(find_factor(n))
    t=type(find_factor)
    print(t)
    help(find_factor)
else:
    print('非法输入')
