from pymysql import *
from tkinter import *
from tkinter import messagebox

page = Tk()
page.geometry('400x400')
page.title("Login form")

con = connect(user = 'root' , password = 'Aadhi@745' , host = 'localhost' , port = 3306 , db = 'Aadhityaa')
cur = con.cursor()

def check():
    un = uname.get()
    pwd = password.get()
    
    cur.execute("select * from gmailsignup")
    for cr in cur:
        if cr[2]==un and cr[3]==pwd :
            msg = messagebox.showinfo("Success","Logged in successfully")
            break
    else:
         msg = messagebox.showerror("Error","User does not exist")

pwd = StringVar()
            
heading = Label(page, text = 'Login Form')
heading.place(x = 200 , y = 20)

label1 = Label(page, text = 'User Name : ',)
label1.place(x = 20 , y = 55)

label2 = Label(page, text = 'Password : ', )
label2.place(x = 20 , y = 85)

uname = Entry(page, )
uname.place(x = 100 , y = 55)

password = Entry(page, textvariable = pwd , show ="*",)
password.place(x = 100,y = 85)

submit = Button(page, text = 'Submit' , command = check)
submit.place(x = 150, y = 120)
              
