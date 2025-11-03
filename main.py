from tkinter import*
from PIL import ImageTk
root = Tk()
root.wm_geometry('1280x700+0+0')
root.wm_resizable(False, False)
backgroundImage=ImageTk.PhotoImage(file='python.jpg')
bgLabel=Label(root,image=backgroundImage)
bgLabel.place(x=0,y=0)
loginFrame=Frame(root)
loginFrame.place(x=400,y=150)
logoImage=PhotoImage(file='logo.png')
logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0)
root.mainloop()