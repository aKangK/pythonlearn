from Class_module import *
class FishBox(Box2):
    def __init__(self,l1,w1,h1):
        #对类中的部分数据进行初始化
        super().__init__(l1,w1,h1)
        self.price=0
        self.capacity=0
        self.type=('大礼盒','小礼盒')
        self.weight=0
        #对类中的部分数据进行初始化
    def countBoxNums(self,fish_nums,fish_type_index):
        #定义盒子数量相关方法
        if fish_type_index==0:
            self.capacity=20
        else:
            self.capacity=10
        if fish_nums%self.capacity==0:
            return fish_nums/self.capacity
        else:
            return fish_nums/self.capacity+1
    def total(self,box_nums,price):
    #定义总金额方法
        return box_nums*price

    

    
