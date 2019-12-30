import tkinter as tk

window1=tk.Tk()

window1.title('my window')
window1.geometry('500x300')

label1=tk.Label(window1,text='你好！This is tkinter!',fg='red',bg='green',font=('Arial',12),width=30,height=2)

label1.pack()

window1.mainloop()