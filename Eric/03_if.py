current_users=['admin','Tom','John','Jack','Jerry','Carry','Venom','Masix']
if current_users:
    for user in current_users:
        if user=='admin':
            print('Hello ' + user + ', would you like to see a status report?')
        else:
            print('Hello ' + user + ', thank you for logging in again!')
else:
    print('we need to find some users!')
print('')
new_users=['aaa','JAck','bbb','ccc','carry']
for new_user in new_users:
    if new_user.title() in current_users:
        print('Sorry, ' + new_user + ' was registed, Please change your name!')
    else:
        print('Hello ' + new_user + '! wellcom to the YTS')
        current_users.append(new_user)
print(current_users)