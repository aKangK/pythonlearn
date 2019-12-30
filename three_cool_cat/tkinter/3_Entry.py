import tkinter as tk

window1=tk.Tk()

window1.title("My Window!")
window1.geometry('500x300')

et1=tk.Entry(window1,show=None,font=('Arial',12))    #显示明文
et2=tk.Entry(window1,show='*',font=('Arial',12))     #显示密文

et1.pack()
et2.pack()

window1.mainloop()