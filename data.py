from idlelib import query
from itertools import count
from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox
import pymysql


#functionality part

def search_employee():
    def search_data():
        query='select * from employee where id=%s or name=%s or phone=%s or email=%s or salary=%s or address=%s or gender=%s or dob=%s'
        mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),salaryEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get()))
        employeeTable.delete(*employeeTable.get_children())
        fetched_data=mycursor.fetchall()
        for data in fetched_data:
            employeeTable.insert('', END, values=data)
    search_root = Toplevel()
    search_root.title('Search Employee')
    search_root.grab_set()
    idLabel = Label(search_root, text='ID', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15)
    idEntry = Entry(search_root, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, padx=15, pady=10)

    nameLabel = Label(search_root, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15)
    nameEntry = Entry(search_root, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, padx=15, pady=10)

    phoneLabel = Label(search_root, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15)
    phoneEntry = Entry(search_root, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, padx=15, pady=10)

    emailLabel = Label(search_root, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15)
    emailEntry = Entry(search_root, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, padx=15, pady=10)

    salaryLabel = Label(search_root, text='Salary', font=('times new roman', 20, 'bold'))
    salaryLabel.grid(row=4, column=0, padx=30, pady=15)
    salaryEntry = Entry(search_root, font=('roman', 15, 'bold'), width=24)
    salaryEntry.grid(row=4, column=1, padx=15, pady=10)

    addressLabel = Label(search_root, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=5, column=0, padx=30, pady=15)
    addressEntry = Entry(search_root, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=5, column=1, padx=15, pady=10)

    genderLabel = Label(search_root, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=6, column=0, padx=30, pady=15)
    genderEntry = Entry(search_root, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=6, column=1, padx=15, pady=10)

    dobLabel = Label(search_root, text='Date of Birth', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=9, column=0, padx=30, pady=15)
    dobEntry = Entry(search_root, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=9, column=1, padx=15, pady=10)

    search_employee_button = ttk.Button(search_root, text='SEARCH', command=search_data)
    search_employee_button.grid(row=10, columnspan=2, pady=15)

def add_employee():
    def add_data():
        if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()=='' or salaryEntry.get()== '' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
            messagebox.showerror('Error','All Field Are Required!',parent=add_root)
        else:
            date = time.strftime("%d/%m/%Y")
            currenttime = time.strftime("%H:%M:%S")
            query = 'insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),salaryEntry.get(),addressEntry.get(),genderEntry.get(),date,
                currenttime,dobEntry.get()))
            con.commit()
            result=messagebox.askyesno('Confirm','Data added Successfully. Do you want to clean the form?')
            if result:
                idEntry.delete(0,END)
                nameEntry.delete(0, END)
                phoneEntry.delete(0, END)
                emailEntry.delete(0, END)
                salaryEntry.delete(0, END)
                addressEntry.delete(0, END)
                genderEntry.delete(0, END)
                dobEntry.delete(0, END)


                query='select * from employee'
                mycursor.execute(query)
                fetched_data=mycursor.fetchall()
                employeeTable.delete(*employeeTable.get_children())
                for data in fetched_data:
                    employeeTable.insert('',END,values=data)


    add_root=Toplevel()
    add_root.grab_set()
    idLabel=Label(add_root,text='ID',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15)
    idEntry=Entry(add_root,font=('roman',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,padx=15,pady=10)

    nameLabel = Label(add_root, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15)
    nameEntry = Entry(add_root, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, padx=15, pady=10)

    phoneLabel = Label(add_root, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15)
    phoneEntry = Entry(add_root, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, padx=15, pady=10)

    emailLabel = Label(add_root, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15)
    emailEntry = Entry(add_root, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, padx=15, pady=10)


    salaryLabel = Label(add_root, text='Salary', font=('times new roman', 20, 'bold'))
    salaryLabel.grid(row=4, column=0, padx=30, pady=15)
    salaryEntry = Entry(add_root, font=('roman', 15, 'bold'), width=24)
    salaryEntry.grid(row=4, column=1, padx=15, pady=10)

    addressLabel = Label(add_root, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=5, column=0, padx=30, pady=15)
    addressEntry = Entry(add_root, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=5, column=1, padx=15, pady=10)

    genderLabel = Label(add_root, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=6, column=0, padx=30, pady=15)
    genderEntry = Entry(add_root, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=6, column=1, padx=15, pady=10)

    dobLabel = Label(add_root, text='Date of Birth', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=9, column=0, padx=30, pady=15)
    dobEntry = Entry(add_root, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=9, column=1, padx=15, pady=10)

    add_employee_button=ttk.Button(add_root,text='ADD EMPLOYEE',command=add_data)
    add_employee_button.grid(row=10,columnspan=2,pady=15)


def connect_database():
    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(host='localhost',user='root',password='1111')
            mycursor=con.cursor()

        except:
            messagebox.showerror('Error','Please enter correct username and password',parent=connectRoot)
            return
        try:
            query='create database employeemanagementsystem'
            mycursor.execute(query)
            query='use employeemanagementsystem'
            mycursor.execute(query)
            query='create table employee(id int not null primary key,name varchar(30),mobile varchar(10),email varchar(30),salary varchar(10),address varchar(100),gender varchar(20),date varchar(50),time varchar(50),dob varchar(20))'
            mycursor.execute(query)
        except:
            query='use employeemanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database Connection is Successful', parent=connectRoot)
        connectRoot.destroy()
        addemployeeeButton.config(state='normal')
        searchemployeeeButton.config(state='normal')
        updateemployeeeButton.config(state='normal')
        deleteemployeeeButton.config(state='normal')
        exportemployeeeButton.config(state='normal')
        showemployeeeButton.config(state='normal')


    connectRoot=Toplevel()
    connectRoot.grab_set()
    connectRoot.geometry('470x250+730+230')
    connectRoot.title('Database Connection')
    connectRoot.resizable(0,0)

    hostnameLabel=Label(connectRoot,text='Hostname',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=10,pady=10)

    hostEntry=Entry(connectRoot,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=10,pady=10)

    usernameLabel = Label(connectRoot, text='Username', font=('arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=10, pady=10)

    usernameEntry =Entry(connectRoot,font=('roman',15,'bold'),bd=2)
    usernameEntry.grid(row=1, column=1, padx=10, pady=10)

    passwordLabel = Label(connectRoot, text='password', font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=10, pady=10)

    passwordEntry = Entry(connectRoot, font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=10, pady=10)

    connectButton=ttk.Button(connectRoot,text='Connect',command=connect)
    connectButton.grid(row=3,columnspan=2,padx=10,pady=10)

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
connectButton=ttk.Button(window,text='Connect to Database',command=connect_database)
connectButton.place(x=980,y=0)
leftFrame=Frame(window)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='candidates.png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0,padx=10,pady=10)
addemployeeeButton=ttk.Button(leftFrame,text='Add Employee',width=15,command=add_employee)
addemployeeeButton.grid(row=1,column=0,padx=10,pady=10)
searchemployeeeButton=ttk.Button(leftFrame,text='Search Employee',width=15,command=search_employee)
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
scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)
employeeTable=ttk.Treeview(rightFrame,columns=('ID','Name','Mobile No.','Email','Salary','Address'
                                     ,'Gender','Added Date','Added Time','Date of Birth')
                           ,xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set
             ,show='headings')
scrollBarX.config(command=employeeTable.xview)
scrollBarY.config(command=employeeTable.yview)
scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)
employeeTable.pack(fill='both',expand=True)

employeeTable.heading('ID',text='ID')
employeeTable.heading('Name',text='Name')
employeeTable.heading('Mobile No.',text='Mobile No.')
employeeTable.heading('Email',text='Email')
employeeTable.heading('Salary',text='Salary')
employeeTable.heading('Address',text='Address')
employeeTable.heading('Gender',text='Gender')
employeeTable.heading('Added Date',text='Added Date')
employeeTable.heading('Added Time',text='Added Time')
employeeTable.heading('Date of Birth',text='Date of Birth')


window.mainloop()