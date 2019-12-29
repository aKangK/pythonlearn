from Class_module import *
my_box1=Box1(10,20,30)
print('立方体1的体积为%d'%(my_box1.volume()))
my_box2=Box2(10,10,10)
print('5个立方体2体积是%d'%(my_box2.volume(5)))
print('立方体2表面积是%d'%(my_box2.area()))
print('立方体2颜色%s，材质%s，类型%s'%(my_box2.c,my_box2.m,my_box2.t))
print(my_box2.area())
