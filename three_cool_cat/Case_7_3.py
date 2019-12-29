class Box1():
    '''求立方体的类'''
    def __init__(self,l1,w1,h1):
        self.l1=l1
        self.w1=w1
        self.h1=h1
    def volume(self):
        v=self.l1*self.w1*self.h1
        return v
#===============================
class Box2(Box1):
    def __init__(self,l1,w1,h1):
        super().__init__(l1,w1,h1)
        self.c='white'
        self.m='paper'
        self.t='fish'
    def area(self):
        re=(self.l1*self.w1+self.l1*self.h1+self.w1*self.l1)*2
        return re
    def volume(self,n=1):
        v=self.l1*self.w1*self.h1*n
        return v
#==============================
my_box1=Box1(10,20,30)
print('立方体1的体积为%d'%(my_box1.volume()))
my_box2=Box2(10,10,10)
print('5个立方体体积是%d'%(my_box2.volume(5)))
print('立方体表面积是%d'%(my_box2.area()))
print('立方体颜色%s，材质%s，类型%s'%(my_box2.c,my_box2.m,my_box2.t))
print(my_box2.area())
