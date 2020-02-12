magicians=['alice','david','carolina']
for magician in magicians:
    print(magician.title()+",that was a great trick!")
    print('I cant wait to see your next trick,' + magician.title() + '\n')
print('Thank you, everyone. That was a great magic show!\n5')

for value in range(1,6):
    print(value)

nums=list(range(1,10,2))
print(nums)
#range函数转化为列表

squares=[]
for value in range(1,6):
    squares.append(value**2)
print(squares)
#输出平方数

digits=[1,2,3,5,4,6,7,8,9]
print(digits)
digits.sort()
print(digits)
#数字排序试验

print(min(digits))
print(max(digits))
print(sum(digits))
print('\n')
#数字列表统计

squares2=[num**2 for num in range(1,11)]
print(squares2)
#列表解析

my_words=['a','b','c']
his_words=my_words[:]
print(my_words)
print(his_words)
my_words.append('d')
his_words.append('z')
print(my_words)
print(his_words)
#复制列表成功

my_words=['a','b','c']
his_words=my_words
print(my_words)
print(his_words)
my_words.append('d')
his_words.append('z')
print(my_words)
print(his_words)
#复制列表失败，未进行切片处理
for eword in my_words:
    print(eword)

