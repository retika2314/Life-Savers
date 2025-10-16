import tkinter.messagebox
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import random as rd
import datetime
import mysql.connector as sqltor  
from tkinter import PhotoImage
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

con=sqltor.connect(host="localhost",user="root",password="admin")
cur=con.cursor()
cur = con.cursor(buffered=True) 
cur.execute("create database if not exists hospital_management")

cur.execute("use hospital_management")

cur.execute("create table if not exists details"
            "("
            "idno varchar(12) primary key,"
            "name char(50),"
            "age char(3),"
            "gender char(40),"
            "phone varchar(20),"
            "bg varchar(30))")




# Message for registration
def entry():
    global e1, e2, e3, gender_dropdown, gender_var, blood_group_var, e5, e6
    
    p1 = e1.get()
    p2 = e2.get()
    p3 = e3.get()
    p4 = gender_var.get()
    p5 = e5.get()
    p6 = blood_group_var.get()

    if not p1 or not p2 or not p3 or not p5 or not p6 or not p4:
        tkinter.messagebox.showwarning("Error", "Please fill in all the required fields.")
        return 

    

    cur.execute('insert into details values(%s,%s,%s,%s,%s,%s)', (p1, p2, p3, p4, p5, p6,))
    con.commit()
    tkinter.messagebox.showinfo("DONE", "YOU HAVE BEEN REGISTERED")
    

def validate_phone(new_value):
    if len(new_value) >10 :
        messagebox.showerror("Error", "Phone number must be exactly 10 digits")
        return False
    else:
        return True


   
def focus_next_entry(event):
    event.widget.tk_focusNext().focus()  


#  For registration 
def register():
    global e1, e2, e3, gender_dropdown, gender_var, blood_group_var, e5, e6
    global photo_image

    root1=Tk()
    root1.title("REGISTERATION")
    label=Label(root1,text="REGISTER YOURSELF",font='Gabriola 40 bold',bg="black",fg="white",width="70",height="1")
    label.pack()
    frame=Frame(root1,height=800,width=1400)
    frame.pack()
    l1=Label(root1,text="PATIENT ID",font='Gabriola 25 bold',bg="grey69")
    l1.place(x=500,y=130)
    e1=tkinter.Entry(root1,width=22,font='ariel 15')
    e1.place(x=700,y=150)
    l2=Label(root1,text="NAME",font='Gabriola 25 bold',bg="grey69")
    l2.place(x=500,y=200)

  
    def is_valid_name(new_value):
        if new_value.isalpha() or new_value == "":
            return True
        else:
            messagebox.showerror("Error", "Please enter valid name !")
            return False

    validation = root1.register(is_valid_name)

    e2 = tkinter.Entry(root1, width=22, font='ariel 15', validate="key", validatecommand=(validation, "%P"))
    e2.place(x=700,y=220)

    l3=Label(root1,text="AGE",font='Gabriola 25 bold',bg="grey69")
    l3.place(x=500,y=270)
    def is_valid_age(new_value):
        if new_value.isdigit() or new_value == "":
            return True
        else:
            messagebox.showerror("Error", "Please enter age in numbers !")
            return False
    validation = root1.register(is_valid_age)
    e3 = tkinter.Entry(root1, width=22, font='ariel 15', validate="key", validatecommand=(validation, "%P"))
    e3.place(x=700,y=290)
    l4=Label(root1,text="GENDER ",font='Gabriola 25 bold',bg="grey69")
    l4.place(x=500,y=340)
    gender_options = ['Male', 'Female']  
    gender_var = tkinter.StringVar(root1)  
    gender_dropdown = ttk.Combobox(root1, textvariable=gender_var, values=gender_options, font='ariel 15')
    gender_dropdown.place(x=700, y=360)
    l5 = Label(root1, text="PHONE", font='Gabriola 25 bold', bg="grey69")
    l5.place(x=500, y=410)
    validation = root1.register(validate_phone)
    e5 = tkinter.Entry(root1, width=22, font='ariel 15', validate="key", validatecommand=(validation, "%P"))
    e5.place(x=700, y=430)
    blood_group_options = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    blood_group_var = tkinter.StringVar(root1)
    blood_group_dropdown = ttk.Combobox(root1, textvariable=blood_group_var, values=blood_group_options, font='ariel 15')
    blood_group_dropdown.place(x=700, y=500)
    l6 = Label(root1, text="BLOOD GROUP", font='Gabriola 25 bold', bg="grey69")
    l6.place(x=500, y=480)
    b1=Button(root1,text="SUBMIT",width=10,height=1,font=("ariel",16),bd=5,bg='lightseagreen',command=entry)
    b1.place(x=630,y=600)

    e1.bind("<Return>", focus_next_entry) 
    e2.bind("<Return>", focus_next_entry)
    e3.bind("<Return>", focus_next_entry)
    gender_dropdown.bind("<Return>", focus_next_entry)  
    e5.bind("<Return>", focus_next_entry)
    blood_group_dropdown.bind("<Return>", focus_next_entry)
    
    root1.geometry("1366x768")
    root1.resizable(False,False)
    frame.configure(bg="grey69")
    root1.configure(bg="grey69")
    root1.mainloop()

#  Message for appointment
def apo_details():
     global x2
     p1=x2.get()    
     if int(p1)==1:
         i=("Dr. Varun \n\nRoom no:- 201")
         j=("Dr. Kausalya \n\nRoom no:- 202")
         q=(i,j)
         h=rd.choice(q) 
         u=(23,34,12,67,53,72)
         o=rd.choice(u)        
         det=("Your appointment is fixed with",h,"\n\nDate:-",datetime.date.today() + datetime.timedelta(days=3),'\n\nAppointmnet no:-',o)
         tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)
     
     elif int(p1)==2:
         i=("Dr. Sidharth \n\nRoom no. 207")
         j=("Dr. Abhishek \n\nRoom no. 208")
         q=(i,j)
         h=rd.choice(q) 
         u=(23,34,12,67,53,72)
         o=rd.choice(u)        
         det=("Your appointment is fixed with",h,"\n\nDate:-",datetime.date.today() + datetime.timedelta(days=5),'\n\nAppointmnet no:-',o)
         tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)
     
     elif int(p1)==3:
         i=("Dr. Divya\n\nRoom no. 203")
         j=("Dr. Keerthi \n\nRoom no. 204")
         q=(i,j)
         h=rd.choice(q) 
         u=(23,34,12,67,53,72)
         o=rd.choice(u)        
         det=("Your appointment is fixed with",h,"\n\nDate:-",datetime.date.today() + datetime.timedelta(days=3),'\n\nAppointmnet no:-',o)
         tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)

     elif int(p1)==4:
         i=("Dr. Naresh, \n\nRoom no. 209")
         j=("Dr. Ashok \n\nRoom no. 200")
         q=(i,j)
         h=rd.choice(q) 
         u=(23,34,12,67,53,72)
         o=rd.choice(u)        
         det=("Your appointment is fixed with",h,"\n\nDate:-",datetime.date.today() + datetime.timedelta(days=6),'\n\nAppointmnet no:-',o)
         tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)

     elif int(p1)==5:
         i=("Dr. William \n\nRoom no. 205")
         j=("Dr. Patrick\n\nRoom no. 206")
         q=(i,j)
         h=rd.choice(q) 
         u=(23,34,12,67,53,72)
         o=rd.choice(u)        
         det=("Your appointment is fixed with",h,"\n\nDate:-",datetime.date.today() + datetime.timedelta(days=4),'\n\nAppointmnet no:-',o)
         tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)   

     elif int(p1)==6:
         i=("Dr. Ashwin \n\nRoom no. 001")
         j=("Dr. John \n\nRoom no. 002")
         k=("Dr. Vikram \n\nRoom no. 003")
         l=("Dr. Irfan\n\nRoom no. 004")
         q=(i,j,k,l)
         h=rd.choice(q) 
         u=(23,34,12,67,53,72)
         o=rd.choice(u)        
         det=("Your appointment is fixed with",h,"\n\nDate:-",datetime.date.today() + datetime.timedelta(days=1),'\n\nAppointmnet no:-',o)
         tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)   
 
     else:
          tkinter.messagebox.showwarning('WRONG INPUT','PLEASE ENTER VALID VALUE')
        

#  For appointment
def get_apoint():
    global x1,x2
    p1=x1.get()  
    cur.execute('select * from details where idno=(%s)',(p1,))
    dat=cur.fetchall()
    a=[]
    for i in dat:
        a.append(i)   
    if len(a)==0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
        root3=Tk()
        root3.title("APPOINTMENT")
        label=Label(root3,text="APPOINTMENT",font='Gabriola 30 bold',bg="black",fg="white",width="50",height="1")
        label.pack()
        frame=Frame(root3,height=700,width=800)
        frame.pack()
        if i[3]=='Male':
                x="Mr."
                name2=Label(root3,text=i[1],font='Gabriola 20 bold',bg="grey69")
                name2.place(x=200,y=98)
        elif i[3]=='Female':
                x="Mrs/Ms."
                name2=Label(root3,text=i[1],font='Gabriola 20 ',bg="grey69")
                name2.place(x=250,y=98)
        else:
            name2=Label(root3,text=i[1],font='Gabriola 20 ',bg="grey69")
            name2.place(x=250,y=98)
        for i in dat:
            name=Label(root3,text='WELCOME',font='Gabriola 20 bold',bg="grey69")
            name.place(x=50,y=100)
            name1=Label(root3,text=x,font='verdana 16',bg="grey69")
            name1.place(x=160,y=110)
            age=Label(root3,text='AGE:',font='Gabriola 20 bold',bg="grey69")
            age.place(x=50,y=140)
            age1=Label(root3,text=i[2],font='verdana 16',bg="grey69")
            age1.place(x=99,y=150)
            phone=Label(root3,text='PHONE:',font='Gabriola 20 bold ',bg="grey69")
            phone.place(x=50,y=180)
            phone1=Label(root3,text=i[4],font='verdana 16',bg="grey69")
            phone1.place(x=128,y=190)
            bg=Label(root3,text='BLOOD GROUP:',font='Gabriola 20 bold ',bg="grey69")
            bg.place(x=50,y=220)
            bg1=Label(root3,text=i[5],font='verdana 16',bg="grey69")
            bg1.place(x=210,y=230)


        L=Label(root3,text='DEPARTMENTS',font='Gabriola 20 bold ',bg="grey69")
        L.place(x=50,y=300)
        L1=Label(root3,text="1.Cardiologist ",font='Gabriola 20 ',bg="grey69")
        L1.place(x=50,y=350)
        L2=Label(root3,text='2.Rheumatologist',font='Gabriola 20 ',bg="grey69")
        L2.place(x=50,y=400)
        L3=Label(root3,text='3.Psychitrist',font='Gabriola 20 ',bg="grey69")
        L3.place(x=50,y=450)
        L4=Label(root3,text='4.Neurologist',font='Gabriola 20 ',bg="grey69")
        L4.place(x=50,y=500)
        L5=Label(root3,text='5.Otolaryngonologist',font='Gabriola 20 ',bg="grey69")
        L5.place(x=50,y=550)
        L6=Label(root3,text='6.MI Room',font='Gabriola 20 ',bg="grey69")
        L6.place(x=50,y=600)
        L7=Label(root3,text='Enter',font='Gabriola 25 bold ',bg="grey69")
        L7.place(x=100,y=683)
        x2=tkinter.Entry(root3,bd=5,width=9,font='verdana 15')
        x2.place(x=200,y=700)        
        B1=Button(root3,text='Submit',width=10,height=1,font=("verdana",16),bd=5,bg='lightseagreen',command=apo_details)
        B1.place(x=550,y=700)   
        root3.resizable(False,False)
        frame.configure(bg="grey69")
        root3.configure(bg="grey69")
        root3.mainloop()

#  For id input
def apoint():
    global x1
    root2=Tk()
    root2.title("APPOINTMENT")
    label=Label(root2,text="APPOINTMENT",font="Gabriola 20 bold",bg="black",fg="white",width="50",height="1")
    label.pack()
    frame=Frame(root2,height=350,width=400)
    frame.pack()
    l1=Label(root2,text=" PATIENT ID",font='Gabriola 25 bold',bg="grey69")
    l1.place(x=70,y=130)
    x1=tkinter.Entry(root2,bd=5,width=18,font='verdana 15')
    x1.place(x=250,y=140)
    b1=Button(root2,text='Submit',width=10,height=1,font=("verdana",16),bd=5,bg='lightseagreen',command=get_apoint)
    b1.place(x=370,y=270)
    root2.resizable(False,False)
    root2.configure(bg="grey69")
    frame.configure(bg="grey69")
    root2.mainloop()
    
#  List of doctors
def lst_doc():
    root4=Tk()
    root4.title("LIST OF DOCTORS")
    
    l=["Dr. Varun","Dr.Kausalya ","Dr.Keerthi","Dr.Divya","Dr.William ","Dr.Patrick","Dr. Sidharth","Dr. Abhishek","Dr. Naresh","Dr. Vikram",'Dr. Irfan','Dr. John','Dr. Ashwin','Dr. Ashok']
    m=["Cardiologist","Cardiologist","Psychitrist","Psychitrist","Otolaryngonologist","Otolaryngonologist","Rheumatologist","Rheumatologist","Neurologist","Neurologist",'MI room','MI room','MI room','MI room']
    n=[201,202,203,204,205,206,207,208,209,200,401,402,403,404]

    frame=Frame(root4,height=700,width=700)
    frame.configure(bg="grey69")
    frame.pack()
    
    
    l1=Label(root4,text='NAME OF DOCTORS',font='Gabriola 25 bold',bg="grey69") 
    l1.place(x=20,y=10)
    count=20
    for i in l:
       count=count+40
       l=Label(root4,text=i,font='verdana 15',bg="grey69")
       l.place(x=20,y=count)

    l2=Label(root4,text='DEPARTMENT',font='Gabriola 25 bold',bg="grey69")
    l2.place(x=300,y=10)
    count1=20
    for i in m:
       count1=count1+40
       l3=Label(root4,text=i,font='verdana 15',bg="grey69")
       l3.place(x=300,y=count1)

    l4=Label(root4,text='ROOM NO',font='Gabriola 25 bold',bg="grey69")
    l4.place(x=520,y=10)
    count2=20
    for i in n:
       count2=count2+40
       l5=Label(root4,text=i,font='verdana 15',bg="grey69")
       l5.place(x=520,y=count2)
    root.resizable(False,False)
    root4.mainloop()

def ser_avail():
    root5=Tk()
    root5.title("SERVICES AVAILABLE")
    frame=Frame(root5,height=600,width=900)
    frame.configure(bg="grey69")
    frame.pack()
    l1=Label(root5,text='SERVICES AVAILABLE',font='Gabriola 25 bold',bg="grey69")
    l1.place(x=20,y=10)
    f=["X-Ray","MRI","CT Scan","Endoscopy","Dialysis","Ultrasound ","EEG","ENMG","ECG"]
    count1=20
    for i in f:
       count1=count1+40
       l3=Label(root5,text=i,font='verdana 15',bg="grey69")
       l3.place(x=20,y=count1)
    l2=Label(root5,text='ROOM NO.',font='Gabriola 25 bold',bg="grey69")
    l2.place(x=400,y=10)
    g=[101,102,103,104,105,301,302,303,304]
    count2=20
    for i in g:
       count2=count2+40
       l4=Label(root5,text=i,font='verdana 15',bg="grey69")
       l4.place(x=400,y=count2)
    l5=Label(root5,text='To avail any of these please contact on our nos.:- 80506 11470 / 94887 26364',font='Gabriola 25 bold',bg="grey69")
    l5.place(x=20,y=440)
    root5.resizable(False,False)
    root5.configure(bg="grey69")
    root5.mainloop()

def mod_sub():
    global x3
    root7=Tk()
    root7.title("MODIFICATION")
    label=Label(root7,text="MODIFICATION",font="Gabriola 20 bold",bg="black",fg="white",width="50",height="1")
    label.pack()
    frame=Frame(root7,height=350,width=400)
    frame.pack()
    l1=Label(root7,text="PATIENT ID",font='Gabriola 20 bold',bg="grey69")
    l1.place(x=70,y=130)
    x3=tkinter.Entry(root7,bd=5,width=18,font='verdana 15')
    x3.place(x=200,y=140)
    b1=Button(root7,text='Submit',width=10,height=1,font=("verdana",16),bd=5,bg='lightseagreen',command=modify)
    b1.place(x=370,y=270)
    root7.configure(bg="grey69")
    frame.configure(bg="grey69")
    root7.resizable(False,False)
    root7.mainloop()
     



def modify():
    def mod():
        new_value = x5.get()  
        p1 = x3.get()       
        choice = x4.get()     
        
        if choice == '1':
            cur.execute("UPDATE details SET name = %s WHERE idno = %s", (new_value, p1))
        elif choice == '2':
            cur.execute("UPDATE details SET age = %s WHERE idno = %s", (new_value, p1))
        elif choice == '3':
            cur.execute("UPDATE details SET gender = %s WHERE idno = %s", (new_value, p1))
        elif choice == '4':
            cur.execute("UPDATE details SET phone = %s WHERE idno = %s", (new_value, p1))
        elif choice == '5':
            cur.execute("UPDATE details SET bg = %s WHERE idno = %s", (new_value, p1))
        else:
            tkinter.messagebox.showwarning("Invalid Choice", "Please enter a valid choice.")

        con.commit()  
        tkinter.messagebox.showinfo("MODIFIED", "Patient details have been modified successfully.")


    p1=x3.get()
    cur.execute('select * from details where idno=(%s)',(p1,))
    dat=cur.fetchall()
    a=[]
    for i in dat:
        a.append(i)   
    if len(a)==0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND !!!")
    else: 
      root6=Tk()
      root6.title("DATA MODIFICATION")
      frame=Frame(root6,height=800,width=1100)
      frame.pack()
      label=Label(root6,text='DATA MODIFICATION',font="Gabriola 30 bold",bg="black",fg="white",width="70",height="1")
      label.pack()
      l2=Label(root6,text='WHAT DO YOU WANT TO CHANGE',font='Gabriola 25 bold',bg="grey69")
      l2.place(x=50,y=340)
      l3=Label(root6,text='1.NAME',font='verdana 15',bg="grey69")
      l3.place(x=50,y=440)
      l4=Label(root6,text='2.AGE',font='verdana 15',bg="grey69")
      l4.place(x=50,y=480)
      l5=Label(root6,text='3.GENDER',font='verdana 15',bg="grey69")
      l5.place(x=50,y=520)
      l6=Label(root6,text='4.PHONE',font='verdana 15',bg="grey69")
      l6.place(x=50,y=560)
      l7=Label(root6,text='5.BLOOD GROUP',font='verdana 15',bg="grey69")
      l7.place(x=50,y=600)
      x2=Label(root6,text='ENTER YOUR CHOICE',font='Gabriola 23 bold',bg="grey69")
      x2.place(x=150,y=630)
      x4=tkinter.Entry(root6,bd=5,width=7,font='verdana 15')
      x4.place(x=480,y=640)
      for i in dat:
            name=Label(root6,text='NAME:-',font='verdana 15',bg="grey69")
            name.place(x=50,y=140)
            name1=Label(root6,text=i[1],font='verdana 15',bg="grey69")
            name1.place(x=150,y=140)
            age=Label(root6,text='AGE:-',font='verdana 15',bg="grey69")
            age.place(x=50,y=180)
            age1=Label(root6,text=i[2],font='verdana 15',bg="grey69")
            age1.place(x=150,y=180)
            gen=Label(root6,text='GENDER:-',font='verdana 15',bg="grey69")
            gen.place(x=50,y=220)
            gen1=Label(root6,text=i[3],font='verdana 15',bg="grey69")
            gen1.place(x=150,y=220)
            pho=Label(root6,text='PHONE NO.:-',font='verdana 15',bg="grey69")
            pho.place(x=50,y=260)
            pho1=Label(root6,text=i[4],font='verdana 15',bg="grey69")
            pho1.place(x=200,y=260)
            bg=Label(root6,text='BLOOD GROUP:-',font='verdana 15',bg="grey69")
            bg.place(x=50,y=300)
            bg1=Label(root6,text=i[5],font='verdana 15',bg="grey69")
            bg1.place(x=230,y=300)
      b=Button(root6,text='Submit',width=10,height=1,font=("verdana",16),bd=5,bg='lightseagreen',command=mod)
      b.place(x=900,y=684)
      L1=Label(root6,text='OLD DETAILS',font="Gabriola 30 bold",bg="grey69")
      L1.place(x=50,y=50)
      L2=Label(root6,text='ENTER NEW DETAIL',font="Gabriola 23 bold ",bg="grey69")
      L2.place(x=150,y=680)
      x5=tkinter.Entry(root6,bd=5,width=18,font='verdana 15')
      x5.place(x=480,y=690)
      root6.geometry("1366x768")
      root6.configure(bg="grey69")
      frame.configure(bg="grey69")
      
      

      root6.resizable(False,False)
      root6.mainloop()


def generate_report():
    cur.execute("SELECT age FROM details")
    age_data = cur.fetchall()
    
    # Extract ages as a list
    ages = [age[0] for age in age_data]

    # Define age categories
    categories = ["Under 18", "19-30", "31-65", "66-80", "Above 80"]
    category_counts = [0, 0, 0, 0, 0]

    # Categorize the ages
    for age in ages:
        if int(age) < 18:
            category_counts[0] += 1
        elif 19 <= int(age) <= 30:
            category_counts[1] += 1
        elif 31 <= int(age) <= 65:
            category_counts[2] += 1
        elif 66 <= int(age) <= 80:
            category_counts[3] += 1
        else:
            category_counts[4] += 1

    # Create a pie chart to visualize the distribution of age categories
    plt.figure(figsize=(6, 6))
    labels = categories
    sizes = category_counts
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Age Category Distribution of Patients')

    # Display the pie chart within a Tkinter window
    report_window = tkinter.Toplevel(root)
    report_window.title("Age Category Distribution Report")
    canvas = FigureCanvasTkAgg(plt.gcf(), master=report_window)
    canvas.get_tk_widget().pack()
    canvas.draw()



    # Make the window non-resizable
    report_window.resizable(False, False)



root = Tk()
root.geometry("1366x768")
root.resizable(False, False)
root.title("HOSPITAL MANAGEMENT")
##
##bg_image = PhotoImage(file="C:/Users/user/Desktop/CS/bg.png")  
##bg_label = Label(root, image=bg_image)
##bg_label.place(relwidth=1, relheight=1)

label = Label(root, text="NEW LIFE HOSPITAL", font="Gabriola 50 bold", bg="black", fg="white", width="60", height="1")
label.pack()
b1 = Button(text="Registration", font="verdana 20", bg='indianred1', bd=6, command=register)
b1.place(x=40,y=250)
b2 = Button(text="Appointment", font="verdana 20 ", bg='indianred1', bd=6, command=apoint)
b2.place(x=40,y=550)
b3 = Button(text="List of Doctors", font="verdana 20 ", bg='indianred1', bd=6, command=lst_doc)
b3.place(x=40,y=400)
b4 = Button(text="Services available", font='verdana 20 ', bg='indianred1', bd=6, command=ser_avail)
b4.place(x=1070,y=250)
b5 = Button(text="Modify data", font='verdana 20 ', bg='indianred1', bd=6, command=mod_sub)
b5.place(x=1150,y=400)
b6 = Button(text="Exit", font='verdana 20 ', command=root.destroy, bg='indianred1', bd=6)
b6.place(x=1250,y=550)
b7 = tkinter.Button(text="Report", font="verdana 20", bg='indianred1', bd=6, command=generate_report)
b7.place(x=630, y=650)


root.mainloop()  
