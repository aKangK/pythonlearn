place=['beijing','qingdao','qiqihaer','wudi','alibaba','foreign']
#建立列表

print(place)
print(sorted(place))
print(place)
print(sorted(place,reverse=True))
print(place)
#sorted相关应用

place.reverse()
print(place)
place.reverse()
print(place)
#reverse相关应用

place.sort()
print(place)
place.sort(reverse=True)
print(place)
#sort应用

print(len(place))
#len应用

print(place[2])
print(place[-1])
#位置应用

place.append('house')
print(place)
#末尾添加元素

place[-1]='home'
print(place)
#更改元素

place.insert(2,'faraway')
print(place)
#任意位置插入元素

del place[-2]
print(place)
#删除任意位置元素

pop_place=place.pop(1)
print(place)
print(pop_place)
#弹出元素

place.remove('foreign')
print(place)