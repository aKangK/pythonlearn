prompt='If you tell us who you are, we can personalize the messages you see.\nWhat is you first name? '
name=input(prompt)
print('Hello, ' + name + '!')

num=input('press a numver: ')
print(type(num))
if num.isdigit():
    print(int(num)+1)
else:
    print('press a number!')

message=''
while message!='quit':
    message=input()
    if message!='quit':
        print(message)

while True:
    city=input()
    if city=='quit':
        break
    else:
        print(city)
#break的使用

current_number=0
while current_number<10:
    current_number=current_number+1
    if current_number % 2 == 0:
        continue
    print(current_number)


unconfirmed_users=['alice','brian','candace']
confirmed_users=[]
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print('Verifying user: ' + current_user.title())
    confirmed_users.append(current_user)
print('\nThe following users have been confirmed: ')
for confirmed_user in confirmed_users:
    print(confirmed_user)
#列表间移动元素

pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
#删除列表中某元素

responses={}
polling_active=True
while polling_active:
    name=input('\nWhats your name? ')
    response=input('Whice mountain would you like to climb someday? ')
    responses[name]=response
    repeat=input('Would you like to let another person respond?(yes/no)')
    if repeat=='no':
        polling_active=False
print('\n=====Poll Results====')
for name,response in responses.items():
    print(name + ' would like to climb ' + response)
#利用循环填充字典