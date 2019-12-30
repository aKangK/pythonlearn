import tkinter as tk

window1=tk.Tk()

window1.title("My Window!")
window1.geometry('500x300')

var=tk.StringVar()
lb1=tk.Label(window1,textvariable=var,bg='green',fg='white',font=('Arial',12),width=30,height=2)
lb1.pack()

on_hit=False
def hit_me():
    global on_hit
    if on_hit==False:
        on_hit=True
        var.set("you hit me!")
    else:
        on_hit=False
        var.set(' ')

btn1=tk.Button(window1,text='hit me!',font=('Arial',12),width=10,height=1,command=hit_me)
btn1.pack()

btn1.bind("<Button-1>",hit_me)

window1.mainloop()

