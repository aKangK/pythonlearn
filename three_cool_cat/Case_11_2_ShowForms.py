import tkinter
def turn_property(event):
    event.widget["activeforeground"]="red"
    event.widget["text"]="小仙女~"
    event.widget["bg"]="green"

MainForm=tkinter.Tk()
MainForm.geometry("500x300")
MainForm.title("刘肉饼！")
MainForm.iconbitmap(r'C:\Users\二花\Desktop\Python编程从零基础到项目实战\Python编程从零基础到项目实战-源代码\第11章\McuSDKTool.ico')
MainForm['background']='LightSlateGray'

btn1=tkinter.Button(MainForm,text="刘肉饼是什么？",fg="black")
btn1.config(fg='red',bg='blue')
btn1.pack()

btn1.bind("<Button-1>",turn_property)
MainForm.mainloop()

