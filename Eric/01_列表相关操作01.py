places=['beijing','qingdao','qiqihaer','wudi','alibaba','foreign']
#建立列表

print(places)
print(sorted(places))
print(places)
print(sorted(places,reverse=True))
print(places)
#sorted相关应用

places.reverse()
print(places)
places.reverse()
print(places)
#reverse相关应用

places.sort()
print(places)
places.sort(reverse=True)
print(places)
#sort应用

print(len(places))
#len应用

print(places[2])
print(places[-1])
#位置应用

places.append('house')
print(places)
#末尾添加元素

places[-1]='home'
print(places)
#更改元素

places.insert(2,'faraway')
print(places)
#任意位置插入元素

del places[-2]
print(places)
#删除任意位置元素

pop_place=places.pop(1)
print(places)
print(pop_place)
#弹出元素

places.remove('foreign')
print(places)
#删除特定元素

print('\n')
for place in places:
    print(place)