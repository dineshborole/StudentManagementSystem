from tkinter import *
import ttkthemes
from tkinter import ttk,messagebox
import pymysql

####functionality part
def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

###########
def toplevel_data(title,button_text,command):
    global idEntry,phoneEntry,nameEntry,classEntry,addressEntry,genderEntry,dobEntry,screen

    screen=Toplevel()
    screen.title(title)
    idLable=Label(screen,text='Id',font=('times new roman',20,'bold'))
    idLable.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,padx=10,pady=15)

    nameLable=Label(screen,text='Name',font=('times new roman',20,'bold'))
    nameLable.grid(row=1,column=0,padx=20,pady=15,sticky=W)
    nameEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,padx=10,pady=15)

    classLable=Label(screen,text='Class',font=('times new roman',20,'bold'))
    classLable.grid(row=2,column=0,padx=20,pady=15,sticky=W)
    classEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    classEntry.grid(row=2,column=1,padx=10,pady=15)

    phoneLable=Label(screen,text='Phone',font=('times new roman',20,'bold'))
    phoneLable.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    phoneEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    phoneEntry.grid(row=3,column=1,padx=10,pady=15)

    addressLable=Label(screen,text='Address',font=('times new roman',20,'bold'))
    addressLable.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    addressEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    addressEntry.grid(row=4,column=1,padx=10,pady=15)

    genderLable=Label(screen,text='Gender',font=('times new roman',20,'bold'))
    genderLable.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    genderEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    genderEntry.grid(row=5,column=1,padx=10,pady=15)

    dobLable=Label(screen,text='D.O.B',font=('times new roman',20,'bold'))
    dobLable.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    dobEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    dobEntry.grid(row=6,column=1,padx=10,pady=15)

    student_button=ttk.Button(screen,text=button_text,command=command)
    student_button.grid(row=7,columnspan=2,pady=15)


    if title=='Update Student':
        indexing = studentTable.focus()
        content = studentTable.item(indexing)
        listdata = content['values']

        idEntry.insert(0, listdata[0])
        nameEntry.insert(0, listdata[1])
        classEntry.insert(0,listdata[2])
        phoneEntry.insert(0, listdata[3])
        addressEntry.insert(0, listdata[4])
        genderEntry.insert(0, listdata[5])
        dobEntry.insert(0, listdata[6])

######UPDATE Student
def update_data():
    query='update student set name=%s,class=%s,mobile_no=%s,address=%s,gender=%s,dob=%s where id=%s'
    mycursor.execute(query,(nameEntry.get(),classEntry.get(),phoneEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),idEntry.get()))
    con.commit()
    messagebox.showinfo('Success',f'Id {idEntry.get()} is modified successfully')
    screen.destroy()
    show_student()

######showing students
def show_student():
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)

######DELETE Student
def delete_student():
    indexing=studentTable.focus()
    print(indexing)
    content=studentTable.item(indexing)
    # print(content)
    content_id=content['values'][0]
    query='delete from student where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'ID {content_id} is deleted successfully')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)

######Search Student
def search_data():
    query='select * from student where id=%s or name=%s or class=%s or gender=%s or dob=%s or address=%s'
    mycursor.execute(query,(idEntry.get(),nameEntry.get(),classEntry.get(),genderEntry.get(),dobEntry.get(),addressEntry.get()))
    studentTable.delete(*studentTable.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('',END,values=data)

###########ADD NEW STUDENT
def add_data():
    if idEntry.get()=='' or nameEntry.get()=='' or classEntry.get()=='' or phoneEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
        messagebox.showerror('Error','All Feilds are required',parent=screen)
    else:
        # try:
        query='insert into student values(%s,%s,%s,%s,%s,%s,%s)'
        mycursor.execute(query,(idEntry.get(),nameEntry.get(),classEntry.get(),phoneEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get()))
        con.commit()
        result=messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?',parent=screen)
        # print(result)
        if result:
            idEntry.delete(0,END)
            nameEntry.delete(0,END)
            classEntry.delete(0,END)
            phoneEntry.delete(0,END)
            addressEntry.delete(0,END)
            genderEntry.delete(0,END)
            dobEntry.delete(0,END)
        else:
            pass
        # except:
        #     messagebox.showerror('Error','Id cannot be repeated',parent=add_window)
        #     return

    query='select *from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    # print(fetched_data)
    for data in fetched_data:
        studentTable.insert('',END,values=data)

def connect_database():
    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(user=userEntry.get(),password=passwordEntry.get())
            mycursor=con.cursor()
            
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return
        
        try:
            query='Create Database studentmanagementsystem'
            mycursor.execute(query)
            query='use studentmanagementsystem'
            mycursor.execute(query)
            query='create table student(id int not null primary key,name varchar(30),class varchar(10),mobile_no varchar(10),address varchar(20),gender varchar(10),dob varchar(10))'
            mycursor.execute(query)
        except:
                query='use studentmanagementsystem'
                mycursor.execute(query)
        messagebox.showinfo('Success','Database Connection is Successful',parent=connectWindow)
        connectWindow.destroy()
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)


    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+750+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)# for hight and width cannot be maximize

    usernameLable=Label(connectWindow,text='User Name',font=('arial',20,'italic bold'))
    usernameLable.grid(row=1,column=0,padx=20)

    userEntry=Entry(connectWindow,font=('Helvetica',15,'bold'),bd=2)
    userEntry.grid(row=1,column=1,padx=40,pady=20)

    passwordLable=Label(connectWindow,text='Password',font=('arial',20,'italic bold'))
    passwordLable.grid(row=2,column=0,padx=20)

    passwordEntry=Entry(connectWindow,font=('Helvetica',15,'bold'),bd=2,show='*')
    passwordEntry.grid(row=2,column=1,padx=40,pady=20)

    connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)

#GUI part
root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry('1180x680+0+0')#'1174x680+0+0'
root.resizable(0,0)
root.title('Student Management System')

# datetimeLable=Label(root,font=('times new roman',18,'bold'))
# datetimeLable.place(x=5,y=5)

s='Student Management System'
sliderLabel=Label(root ,text=s,font=('arial',28,'italic bold'),width=30)
sliderLabel.place(x=200,y=0)

connectButton=ttk.Button(root,text='Connect To Database',command=connect_database) ## connect button
connectButton.place(x=980,y=0)

leftFrame=Frame(root)       #creating frame using frame class
leftFrame.place(x=50,y=80,width=300,height=600)

###########################Buttons###################
addstudentButton=ttk.Button(leftFrame,text='Add Student',width=15,state=DISABLED,command= lambda:toplevel_data('Add Student','Add',add_data))
addstudentButton.grid(row=1,column=0,pady=15)

searchstudentButton=ttk.Button(leftFrame,text='Search Student',width=15,state=DISABLED,command= lambda: toplevel_data('Search Student','Search',search_data))
searchstudentButton.grid(row=2,column=0,pady=15)

deletestudentButton=ttk.Button(leftFrame,text='Delete Student',width=15,state=DISABLED,command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=15)

updatestudentButton=ttk.Button(leftFrame,text='Update Student',width=15,state=DISABLED,command=lambda:toplevel_data('Update Student','Update',update_data))
updatestudentButton.grid(row=4,column=0,pady=15)

showstudentButton=ttk.Button(leftFrame,text='Show Student',width=15,state=DISABLED,command=show_student)
showstudentButton.grid(row=5,column=0,pady=15)

exitButton=ttk.Button(leftFrame,text='Exit',command=iexit)
exitButton.grid(row=7,column=0,pady=15)
##################################################

rightFrame=Frame(root)
rightFrame.place(x=250,y=80,width=930,height=500)

# scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Class','Mobile No','Address','Gender','D.O.B'), yscrollcommand=scrollBarY.set)#, xscrollcommand=scrollBarX.set
scrollBarY.config(command=studentTable.yview)
scrollBarY.pack(side=RIGHT,fill=Y) #pack is used when u have to place any thing at top, bottom,left,right

studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Class',text='Class')
studentTable.heading('Mobile No',text='Mobile No')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('D.O.B',text='D.O.B')


studentTable.column('Id',width=50,anchor=CENTER)
studentTable.column('Name',width=100,anchor=CENTER)
studentTable.column('Class',width=80,anchor=CENTER)
studentTable.column('Mobile No',width=100,anchor=CENTER)
studentTable.column('Address',width=150,anchor=CENTER)
studentTable.column('Gender',width=80,anchor=CENTER)
studentTable.column('D.O.B',width=100,anchor=CENTER)

style=ttk.Style()
style.configure('Treeview', rowheight=40,font=('arial', 12, 'bold'), fieldbackground='white', background='white')
style.configure('Treeview.Heading',font=('arial', 14, 'bold'),foreground='red')

studentTable.config(show='headings')
root.mainloop()