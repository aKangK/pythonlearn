alien_0={'color':'green'}
print('The alien is ' + alien_0['color'] + '.')

alien_0['color']='yellow'
print('The alien is now ' + alien_0['color'] + '.')
#字典值变化

alien_1={'x_position':0, 'y_position':25, 'speed':'medium'}
print('Original x positon: ' + str(alien_1['x_position']))
if alien_1['speed']=='slow':
    x_increment=1
elif alien_1['speed']=='medium':
    x_increment=2
else:
    x_increment=3
alien_1['x_position']=alien_1['x_position']+x_increment
print('New x position: ' + str(alien_1['x_position']))

alien_1['speed']='fast'
if alien_1['speed']=='slow':
    x_increment=1
elif alien_1['speed']=='medium':
    x_increment=2
else:
    x_increment=3
alien_1['x_position']=alien_1['x_position']+x_increment
print('New x position: ' + str(alien_1['x_position']))
#外星人位移

alien_2={'color':'green','point':5}
print(alien_2)
del alien_2['point']
print(alien_2)
#删除键值对

users_0={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
    }
for key, value in users_0.items():
    print('\nKey: ' + key)
    print('Value: ' + value)
print('')

favorite_laguages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
    }
friends=['phil','sarah']
for name in favorite_laguages.keys():
    print(name.title())
    if name in friends:
        print('Hi ' + name + ', I see your favorite language is ' + favorite_laguages[name].title() + '!')
if 'erin' not in favorite_laguages.keys():
    print('Erin, please take our poll!')
for name in sorted(favorite_laguages.keys()):
    print(name.title() + ', thank you for taking the poll')
print('\nThe following languages have been mentioned:')
for language in favorite_laguages.values():
    print(language)
print('\nThe following languages have been mentioned:')
for language in set(favorite_laguages.values()):
    print(language)

print('')
a={'a':'abc','b':[1,2,3]}
print(a['b'][1])




























