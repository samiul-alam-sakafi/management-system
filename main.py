from tkinter import*
from PIL import ImageTk
root = Tk()
root.wm_geometry('1280x700+0+0')
root.wm_resizable(False, False)
backgroundImage=ImageTk.PhotoImage(file='python.jpg')
bgLabel=Label(root,image=backgroundImage)
bgLabel.place(x=0,y=0)
loginFrame=Frame(root,bg='tan')
loginFrame.place(x=0,y=0)
loginFrame.place(x=0,y=0)
loginFrame.place(x=400,y=150)
logoImage=PhotoImage(file='logo.png')
logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)
usernameImage=PhotoImage(file='user.png')
usernameLabel=Label(loginFrame,image=usernameImage,text='Username',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)
usernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=3,fg='royalblue')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)

passwordImage=PhotoImage(file='password.png')
passwordLabel=Label(loginFrame,image=passwordImage,text='Password',compound=LEFT
                    ,font=('times new roman',20,'bold'),bg='white')
passwordLabel.grid(row=2,column=0,pady=10,padx=20)
passwordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=3,fg='royalblue')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)

loginButton=Button(loginFrame,text='Login',font=('times new roman',14,'bold')
                   ,width=15,fg='white',bg='cornflowerblue',activebackground='cornflowerblue'
                   ,activeforeground='white',cursor='hand2')
loginButton.grid(row=3,column=1,pady=10,padx=20)

root.mainloop()