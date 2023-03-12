from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)

def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file)
        data = list(fr)
    return data

GUI = Tk()
GUI.title('โปรแกรมบันทึกลาคา')
GUI.geometry('800x400')


L1 = Label(GUI,text='โปรแกรมบันทึก',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)

def Button2():
    text = 'I Have 3300 Bath'
    messagebox.showinfo('I Have',text)

FB1 = Frame(GUI)
FB1.place(x=100,y=80)
B2 = ttk.Button(FB1,text='I Have',command=Button2)
B2.pack(ipadx=20,ipady=20)

LF1 = ttk.LabelFrame(GUI,text='write')
LF1.place(x=400,y=50)

v_data = StringVar()
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Angsana New',25))
E1.pack(ipadx=10,ipady=10)

from datetime import datetime

def SaveData():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data.get()
    text = [data]
    writecsv(text)
    v_data.set('')
    

B4 = ttk.Button(LF1,text='บันทึก',command=SaveData)
B4.pack(ipadx=20,ipady=20)

LF2 = ttk.LabelFrame(GUI,text='data.csv')
LF2.place(x=500,y=250)

def ReadData():
    
    datacsv = readcsv()
    messagebox.showinfo('data.csv',datacsv)

B5 = ttk.Button(LF2,text='อ่าน',command=ReadData)
B5.pack(ipadx=50,ipady=20)

GUI.mainloop()
