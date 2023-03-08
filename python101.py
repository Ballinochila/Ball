from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมบันทึกลาคา')
GUI.geometry('500x400')

L1 = Label(GUI,text='โปแกรมบันทึกลาคา',font=('Angsana New',30),fg='green')
L1.place(x=60,y=20)

def Button2():
    text = '10 bath'
    messagebox.showinfo('เปับชี้ลาคา',text,)

FB1 = Frame(GUI)
FB1.place(x=100,y=80)
B2 = ttk.Button(FB1,text='เปับชี้ลาคากีบาท',command=Button2)
B2.pack(ipadx=20,ipady=20)




GUI.mainloop()
