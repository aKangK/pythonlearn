import tkinter as tk

window1=tk.Tk()

window1.title("My Window!")
window1.geometry('500x300')
#设置主窗口
#==========================
ety1=tk.Entry(window1,show=None)
ety1.pack()

def insert_point(): #在指针处插入
    var=ety1.get()
    t.insert('insert',var)
    
def insert_end():   #在文本框后面插入
    var=ety1.get()
    t.insert('end',var)

btn1=tk.Button(window1,text='insert point',width=10,height=2,command=insert_point)
btn1.pack()

btn2=tk.Button(window1,text='insert end',width=10,height=2,command=insert_end)
btn2.pack()

t=tk.Text(window1,height=3)
t.pack()

#==========================
#主窗口循环显示
window1.mainloop()