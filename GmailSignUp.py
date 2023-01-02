from tkinter import *
from pymysql import *
from tkinter import messagebox

con = connect(user='root', password='Aadhi@745', host='localhost', port=3306, db='Aadhityaa')
cur = con.cursor()

mainpage = Tk()
mainpage.geometry('700x700')
mainpage.title('Gmail Sign Up')

def submit():
    try:
        firstname = FName.get()
        lastname = LName.get()
        username = UName.get()
        pwd = Password.get()
        cpwd =  CPassword.get()

        cur.execute('select * from gmailsignup')
        for a in cur:
            if a[2]==username:
                ms = messagebox.showerror('Error','User Already Exists')
                break
        else:
            if pwd==cpwd:
                li = [firstname,lastname,username,pwd]
                query = 'insert into gmailsignup values(%s,%s,%s,%s)'
                cur.execute(query,li)
                con.commit()
                if messagebox.showinfo("Success","Signed Up Successfully"):
                    FName.delete(0,END)
                    LName.delete(0,END)
                    UName.delete(0,END)
                    Password.delete(0,END)
                    CPassword.delete(0,END)
            else:
                msg = messagebox.showerror("Error","Enter password correctly")
        
    except:
        msg = messagebox.showerror("Error","Something went wrong.Check!")
        
def clear():
    FName.delete(0,END)
    LName.delete(0,END)
    UName.delete(0,END)
    Password.delete(0,END)
    CPassword.delete(0,END)

def cancel():
    mainpage.destroy()

password = StringVar()
cpassword = StringVar()

Heading = Label(mainpage, text = 'Gmail Sign Up')
Heading.place(x = 340 , y = 25)

Label1 = Label(mainpage, text ='FName : ',)
Label1.place(x = 90 , y = 70)

Label2 = Label(mainpage, text = 'LName : ',)
Label2.place(x = 90 , y = 110)

Label3 = Label(mainpage, text = 'UName : ',)
Label3.place(x = 90 , y = 150)

Label4 = Label(mainpage, text = 'Password : ',)
Label4.place(x= 90 , y = 190)

Label5 = Label(mainpage, text = 'CPassword : ',)
Label5.place(x = 90 , y =230)

FName = Entry(mainpage , )
FName.place(x =180, y = 70)

LName = Entry(mainpage , )
LName.place(x = 180, y = 110)

UName = Entry(mainpage,)
UName.place(x = 180, y = 150)

Password = Entry(mainpage, textvariable=password, show="*" )
Password.place(x = 180, y = 190)

CPassword = Entry(mainpage, textvariable=cpassword, show="*")
CPassword.place(x = 180, y = 230)

Submit = Button(mainpage, text = 'Submit', command = submit)
Submit.place(x = 250, y = 270 , )

Clear = Button(mainpage, text = 'Clear', command = clear)
Clear.place(x = 310, y = 270, )

Cancel = Button(mainpage, text = 'Cancel', command = cancel)
Cancel.place(x = 360, y = 270, )

mainpage.mainloop()
