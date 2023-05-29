from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='Dinesh' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Welcome')

        window.destroy()
        import test2

    else:
        messagebox.showerror('Error','Invalid Username and Password')


window=Tk() 

window.geometry('1280x700+0+0')
window.title('Login System of Student Management System')

window.resizable(False,False)#  disable minimize and maximize window

backgroundImage=ImageTk.PhotoImage(file='bg.jpg')

bgLable=Label(window,image=backgroundImage)
bgLable.place(x=0,y=0)#,columnspan=2


loginFrame=Frame(window,bg='white')
loginFrame.place(x=400,y=150)

logoImage=ImageTk.PhotoImage(file='logo.jpg')

logoLable=Label(loginFrame,image=logoImage)
logoLable.grid(row=0,column=0,columnspan=2,pady=10)

usernameImage=ImageTk.PhotoImage(file='user.jpg')

usernameLable=Label(loginFrame,image=usernameImage,text='Username',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
usernameLable.grid(row=1,column=0,pady=10,padx=10)

usernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
usernameEntry.grid(row=1,column=1,pady=10,padx=10)
##################

passwordImage=ImageTk.PhotoImage(file='password.jpg')

passwordLable=Label(loginFrame,image=passwordImage,text='Password',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
passwordLable.grid(row=2,column=0,pady=10,padx=10)

passwordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
passwordEntry.grid(row=2,column=1,pady=10,padx=10)

loginButton=Button(loginFrame,text='Login',font=('times new roman',15,'bold'),width=15,fg='white',bg='cornflowerblue',activebackground='cornflowerblue',activeforeground='white',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,padx=10)


window.mainloop()