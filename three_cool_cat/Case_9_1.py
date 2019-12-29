def print_D(dic):
    i=0
    try:
        len1=len(dic)
        while i<len1:
            print(dic.popitem())
            i=i+1
    except:
        print('传递数值错误!')
#=================================
print_D({1:'a',2:'b'})
print_D([1,2,3])
