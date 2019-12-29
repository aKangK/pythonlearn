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
#================================
class SHost():
    name='Tom'
    age=20
    address='china'
    call='12345678'
