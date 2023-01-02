from tkinter import *
from tkinter import ttk
from pymysql import connect
from tkinter import messagebox

con = connect(user='root',password='Aadhi@745',host='localhost',port=3306,db='Aadhityaa')
cur = con.cursor()

page = Tk()
page.geometry('800x800')
page.title('Registration Form')

gender = IntVar()
cb1 = IntVar()
cb2 = IntVar()
cb3 = IntVar()
cb4 = IntVar()
cb5 = IntVar()
cb6 = IntVar()

def save():
    try:
        stName = name.get()
        stAge = age.get()
        stAdd = address.get(1.0,END)
        hob = [cb1.get(),cb2.get(),cb3.get(),cb4.get(),cb5.get(),cb6.get()]
        val = ['Game','Reading','Fishing','Quiz','Stamp','Coin']
        fname = FName.get()
        gen = gender.get()
        dob = dateOfBirth.get()
        ph = phone.get()
        em = Email.get()
        nt = Nation.get()

        hobbies = ""
        i = 0
        while i<len(hob):
            if hob[i]==1:
                hobbies+=val[i]+" "
            i+=1
        if gen==1:
            gr = 'Male'
        else:
            gr = "Female"

        li = [stName,stAge,stAdd,hobbies,fname,gr,dob,ph,em,nt]

        for a in li:
            if a=="":
                ms = messagebox.showerror("Error","Enter all the fields")
                break
        else:
            ph = int(ph)
            stAge = int(stAge)
            query = 'insert into registration_form values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cur.execute(query,li)
            con.commit()
            ms = messagebox.showinfo('Success','Successfully Registered Student Data')
            
    except:
        ms = messagebox.showerror("Error",'Something Went Wrong. Try Again Later')
    
def clear():
    name.delete(0,END)
    age.delete(0,END)
    address.delete(1.0,END)
    cb1.set(0)
    cb2.set(0)
    cb3.set(0)
    cb4.set(0)
    cb5.set(0)
    cb6.set(0)
    gender.set(0)
    dateOfBirth.delete(0,END)
    FName.delete(0,END)
    phone.delete(0,END)
    Email.delete(0,END)
    Nation.delete(0,END)
    
def cancel():
    page.destroy()
    
heading = Label(page , text = 'Registration Form ').place(x = 350 , y = 15 )

Label1 = Label (page , text = 'Name :')
Label1.place(x = 20 , y = 60)

name = Entry (page , )
name.place(x = 80 , y =60)

Label2 = Label (page , text = 'Age    :')
Label2.place(x = 20 , y = 100)

age = Entry (page , )
age.place(x = 80 , y = 100 , width = 60 , height = 20)

Label3 = Label (page , text = 'Address :')
Label3.place(x = 20 , y = 140)

address = Text(page , )
address.place(x = 80 , y = 140 , width = 300 , height = 130)

Label4 = Label (page , text = 'Hobbies :')
Label4.place(x = 20 , y = 300)

game = Checkbutton (page , text = 'Game',variable=cb1)
game.place(x = 80 , y =300)

reading = Checkbutton (page , text = 'Reading',variable=cb2)
reading.place(x = 150 , y = 300)

fishing = Checkbutton (page , text = 'Fishing',variable=cb3)
fishing.place(x = 230 , y = 300)

quiz = Checkbutton (page , text = 'Quiz',variable=cb4)
quiz.place(x = 80 , y = 330)

stamp = Checkbutton (page , text = 'Stamp',variable=cb5)
stamp.place(x = 150 , y = 330)

coin = Checkbutton (page , text = 'Coin',variable=cb6)
coin.place(x = 230 , y = 330)

Label5 = Label (page , text = 'Father Name :')
Label5.place(x = 20 , y = 370)

FName = Entry (page ,)
FName.place(x = 120 , y = 370)

Label6 = Label (page , text = 'Sex :')
Label6.place(x = 420 , y = 60) 

S1 = Radiobutton (page , text = 'Male' , value = 1 , variable = gender)
S1.place(x = 480 , y = 60)

S2 = Radiobutton (page , text = 'Female' ,value = 2 , variable = gender)
S2.place(x= 560 , y = 60)

Label7 = Label (page , text = 'DOB :')
Label7.place(x = 420 , y = 100)

dateOfBirth = Entry(page,)
dateOfBirth.place(x=480, y=100)

Label8 = Label (page , text = 'Phone :')
Label8.place(x = 420 , y = 140)

phone = Entry ( page , )
phone.place(x = 480 , y = 140)

Label9 = Label (page , text = 'E-Mail : ')
Label9.place(x = 420 , y = 300)

Email = Entry( page, )	
Email.place(x = 480 , y = 300 , width = 200)

Label10 = Label (page , text = 'Nation : ')
Label10.place(x = 420 , y = 370)

Nation = ttk.Combobox(page , values = ["India ", "Australia" , "USA" , "UK ", "Germany" , "Canada"])
Nation.place(x = 480 , y = 370)

submit = Button (page , text = "Submit",command=save)
submit.place(x = 260 , y = 460,width=80)

clear = Button(page,text='Clear',command=clear)
clear.place(x=360,y=460,width=80)

cancel = Button (page , text = "Cancel",command=cancel)
cancel.place(x = 460 , y = 460,width=80)

page.mainloop()


