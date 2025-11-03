from itertools import count
from tkinter import *
import time
import ttkthemes
from tkinter import ttk
#functionality part
count=0
text=''
def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    sliderLabel.configure(text=text)
    count+=1
    sliderLabel.after(300,slider)
def clock():
    date=time.strftime("%d/%m/%Y")
    currenttime=time.strftime("%H:%M:%S")
    datetimeLabel.config(text=f'  Date: {date}\nTime:  {currenttime}')
    datetimeLabel.after(1000,clock)

#GUI part
window=ttkthemes.ThemedTk()
window.get_themes()
window.set_theme('smog')
window.geometry('1174x680+0+0')
window.resizable(0,0)
window.title('Employee Management System')
datetimeLabel=Label(window,text='Date and Time',font=('Times New Roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()

s='Employee Management System'
sliderLabel=Label(window,text=s,font=('arial',28,'italic bold'),width=30)
sliderLabel.place(x=200,y=0)
slider()
connectButton=ttk.Button(window,text='Connect to Database')
connectButton.place(x=980,y=0)
leftFrame=Frame(window)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='candidates.png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0,padx=10,pady=10)
addemployeeeButton=ttk.Button(leftFrame,text='Add Employee',width=15)
addemployeeeButton.grid(row=1,column=0,padx=10,pady=10)
searchemployeeeButton=ttk.Button(leftFrame,text='Search Employee',width=15)
searchemployeeeButton.grid(row=2,column=0,padx=10,pady=10)
deleteemployeeeButton=ttk.Button(leftFrame,text='Delete Employee',width=15)
deleteemployeeeButton.grid(row=3,column=0,padx=10,pady=10)
updateemployeeeButton=ttk.Button(leftFrame,text='Update Employee',width=15)
updateemployeeeButton.grid(row=4,column=0,padx=10,pady=10)
showemployeeeButton=ttk.Button(leftFrame,text='Show Employee',width=15)
showemployeeeButton.grid(row=5,column=0,padx=10,pady=10)
exportemployeeeButton=ttk.Button(leftFrame,text='Export Data',width=15)
exportemployeeeButton.grid(row=6,column=0,padx=10,pady=10)
exitButton=ttk.Button(leftFrame,text='Exit',width=15)
exitButton.grid(row=7,column=0,pady=20)
rightFrame=Frame(window)
rightFrame.place(x=350,y=80,width=820,height=600)


window.mainloop()