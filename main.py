from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.pyplot import *
import numpy as np
import mysql.connector as sqltor
import tkinter as tk
from tkinter import *
import pywhatkit
import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo, showerror


def closee():
    root.after(1000, lambda: root.destroy())


def clicked():
    Remove_Buttons(button)


def raise_frame(frame):
    frame.tkraise()
    command = clicked


root = tk.Tk()
root.geometry("15000x700")
root.title("dreams come true")
root.configure()
Staffop3 = tk.Frame(root)
Home = tk.Frame(root)
facilities = tk.Frame(root, width=1300, height=1400,
                      relief='raised', borderwidth=10)
about = tk.Frame(root, width=300, height=400, relief='raised', borderwidth=10)
fulfiller = tk.Frame(root, width=300, height=400,
                     relief='raised', borderwidth=10)
# wish=tk.Frame(root,width=700,height=900,relief='raised',borderwidth=10)
flogin = tk.Frame(root, width=700, height=900, relief='raised', borderwidth=10)
wlogin = tk.Frame(root, width=700, height=900, relief='raised', borderwidth=10)
ORG = tk.Frame(root, width=700, height=900, relief='raised', borderwidth=10)
f = tk.Frame(root)
cus2 = tk.Frame(root)

delete = tk.Frame(root, width=300, height=400, borderwidth=10)

weightpg = tk.Frame(root)

truckalert = tk.Frame(root)
f2 = tk.Frame(root, width=300, height=400, borderwidth=10)
organiser = tk.Frame(root)
Home = tk.Frame(root)


# PAGEOFCUSTOMER
cus = tk.Frame(root)
Cop1 = tk.Frame(root)

Cop2 = tk.Frame(root)

# truck=tk.Frame(root)


C = Canvas(Home, bg="blue", height=1, width=1)
filename = PhotoImage(file=r"C:\Users\lenovo\Pictures\garbage.png")
background_label = Label(Home, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()
for frame in (Home, facilities, about, fulfiller, cus2, flogin, wlogin, organiser, Staffop3, delete, f, f2, ORG, truckalert, cus, weightpg, Cop1, Cop2):  # truck):
    frame.grid(row=1, column=0, sticky='new')


"""Efficient waste collection system which has separated bins of collection for wet and dry waste
Waste segregation at source will enable the efficient recovery of resources from recyclables and through waste-to-energy recovery
The widespread introduction of vehicles and transportation enables the collection of waste from metropolitan cities, towns, and local villages.
Education of waste collectors on the mode of collection, types of waste, the value of recyclables and non-recyclables in the waste collected
Mechanization of waste sorting at landfills and DRCCs
Properly managed engineered landfills reduce the interaction between
Most important of all is the urgent need for a collaborative approach from the Urban Local Bodies (ULBs), state-level, and national-level authorities.

In conclusion, community awareness and responsible management create a sustainable waste management chain. This will ensure there is an optimal use of resources and the protection of the environment.
"""

title_label = tk.Label(facilities, text='PROCESS',
                       font=('calibre', 15, 'bold'))
title_label.pack(padx=5, pady=0)
intr_label = tk.Label(
    facilities, text='Notifies the individual about the collection truck when it is near the house.', font=('calibre', 10))
intr_label.pack(padx=5, pady=0)

# img4a =tk.PhotoImage(file=r"C:\Users\lenovo\Pictures\building - Copy (2).png")
# pimg4=img4a.subsample(0,0)
# button40=tk.Button(facilities,image=img4a,compound='left',width='0',height='0',font="Times 23 bold",activeforeground='black').pack(padx=5,pady=5)#

intr1_label = tk.Label(
    facilities, text='Waste segregation at source will enable the efficient recovery of resources from ', font=('calibre', 10))
intr1_label.pack(padx=6, pady=0)
intr2_label = tk.Label(
    facilities, text='recyclables and through waste-to-energy recovery.The truck comes once within a ', font=('calibre', 10))
intr2_label.pack(padx=7, pady=0)
intr3_label = tk.Label(
    facilities, text='fixed period of time at a pre-specified place.Waste is collected, segregated and points ', font=('calibre', 10))
intr3_label.pack(padx=9, pady=0)
intr4_label = tk.Label(
    facilities, text='are allocated to the members as per the rate specified per kg of the waste collected.', font=('calibre', 10))
intr4_label.pack(padx=10, pady=0)
intr5_label = tk.Label(
    facilities, text='The points are credited in the form of money to the linked bank account of user.', font=('calibre', 10))
intr5_label.pack(padx=11, pady=0)


intr7_label = tk.Label(
    facilities, text='The collected waste is segregated and supplied to various industries on demand. ', font=('calibre', 10))
intr7_label.pack(padx=12, pady=0)
intr8_label = tk.Label(
    facilities, text='These industries reuse the waste material or recycle it to produce new products.', font=('calibre', 10))
intr8_label.pack(padx=12, pady=0)

# img5a =tk.PhotoImage(file=r"C:\Users\lenovo\Pictures\reception - Copy (3).png")
# pimg5=img5a.subsample(0,0)
# button50=tk.intr6_label = tk.Label(facilities, text = 'To further encourage their admirable work, their workspace is designed to offer a collaborative and engaging work environment surrounded by flexible and supportive coworkers creating a heathy and interactive atmosphere.  ', font=('calibre',10))
# intr6_label.pack(padx=11,pady=0)
# img6a =tk.PhotoImage(file=r"C:/Users/lenovo/Pictures/office,.png")
# pimg6=img6a.subsample(0,0)
buttonX = tk.Button(facilities, text='back', width='0', height='0', activebackground='SlateGray1',
                    bg='SlateGray1', font="Times 23 bold", activeforeground='black', command=lambda: raise_frame(Home))
buttonX.pack(side='bottom')
# button60=tk.Button(facilities,image=img6a,compound='left',width='0',height='0',font="Times 23 bold",activeforeground='black').pack(padx=7,pady=5)#
button = tk.Button(Home, text='GARGO', width='0', height='0', activebackground='Pink1', bg='azure',
                   font="Times 30 bold", activeforeground='black').pack(side="top", expand=True, padx=0, pady=0)
button = tk.Button(Home, text='     ABOUT   ', width='0', height='0', activebackground='SlateGray1', bg='SlateGray1',
                   font="Times 23 bold", activeforeground='black', command=lambda: raise_frame(about)).pack(side="top", padx=10, pady=10)

button = tk.Button(Home, text='   THE PROCESS  ', width='0', height='0', activebackground='SlateGray1', bg='SlateGray1',
                   font="Times 23 bold", activeforeground='black', command=lambda: raise_frame(facilities)).pack(side="top", expand=True, padx=0, pady=10)
button = tk.Button(Home, text='REGISTER', width='0', height='0', activebackground='SlateGray1', bg='SlateGray1', font="Times 23 bold",
                   activeforeground='black', command=lambda: raise_frame(fulfiller)).pack(side="top", expand=True, padx=20, pady=10)
# buttond=tk.Button(Home,text='MAKE A WISH',width='0',height='0',activebackground='SlateGray1',bg='SlateGray1',font="Times 23 bold",activeforeground='black',command=lambda:raise_frame(wish)).pack(side="top",expand=True,padx=20,pady=10)
# LLOGIN AS FULFILLER
buttone = tk.Button(Home, text='EVENTS', width='0', height='0', activebackground='SlateGray1', bg='SlateGray1', font="Times 23 bold",
                    activeforeground='black', command=lambda: raise_frame(f)).pack(side="top", expand=True, padx=20, pady=10)
# buttond=tk.Button(Home,text='LOGIN AS WISHMAKER/TO ENTER AMT OF WASTE',width='0',height='0',activebackground='SlateGray1',bg='SlateGray1',font="Times 23 bold",activeforeground='black',command=lambda:raise_frame(wlogin)).pack(side="top",expand=True,padx=20,pady=10)
# ORGANISER
buttond = tk.Button(Home, text='LOGIN AS STAFF', width='0', height='0', activebackground='SlateGray1', bg='SlateGray1',
                    font="Times 23 bold", activeforeground='black', command=lambda: raise_frame(ORG)).pack(side="top", expand=True, padx=20, pady=10)
buttond = tk.Button(Home, text='LOGIN AS CUSTOMER', width='0', height='0', activebackground='SlateGray1', bg='SlateGray1',
                    font="Times 23 bold", activeforeground='black', command=lambda: raise_frame(wlogin)).pack(side="top", expand=True, padx=20, pady=10)
buttond = tk.Button(Home, text='EXIT', width='0', height='0', activebackground='SlateGray1', bg='SlateGray1',
                    font="Times 23 bold", activeforeground='black', command=closee).pack(side="top", expand=True, padx=20, pady=10)

buttonA = tk.Button(fulfiller, text='back', width='0', height='0', activebackground='SlateGray1',
                    bg='SlateGray1', font="Times 23 bold", activeforeground='black', command=lambda: raise_frame(Home))
buttonA.grid(row=20, column=0)
mycon = sqltor.connect(host="localhost", user="root",
                       passwd="123456", database='dreams_come_true1')
a = b = c = d = 0
cursor = mycon.cursor()
cursor.execute("select * from make_a_wish")
data = cursor.fetchall()
count = cursor.rowcount
for row in data:
   if row[3] < 12:
      a = a+1
   elif row[3] > 12 and row[3] <= 17:
      b = b+1
   elif row[3] < 65 and row[3] > 18:
      c = c+1
   else:
      d = d+1
z = [a, b, c, d]
Age = ['<12', '12-17', '18+', '>65']
values = [a, b, c, d]
actualFigure = figure(figsize=(2, 2))
actualFigure.suptitle("Age wise distribution", fontsize=10)
explode = list()
for k in Age:
    explode.append(0.1)
title_label = tk.Label(about, text='ABOUT', font=('calibre', 15, 'bold'))
title_label.pack(padx=5, pady=0)
# intro1_label = tk.Label(about, text = '"Dreams Come True" is a locally based wish granting organisation dedicated to using the power of a dream to bring hope and joy to every citizen battling with a physical disability.', font=('calibre',10))
# intro1_label.pack(padx=10,pady=0)


"""intro1_label = tk.Label(about, text = '"Dreams Come True" is a locally based wish granting organisation dedicated to using the power of a dream to bring hope and joy to every citizen battling with a physical disability.', font=('calibre',10))
intro1_label.pack(padx=10,pady=0)
intro2_label=tk.Label(about,text='Dreams come in all shapes and sizes, serving as a momentary reprieve from the doctors tests, medical treatments and hospital visits.', font=('calibre',10))
intro2_label.pack(padx=10,pady=0)
intro3_label=tk.Label(about,text='They go a long way in inspiring courage to battle every hardship coming our way, spreading positivity and in keeping the flames of hope glowing warm and strong as we strive to become the best versions of ourselves.',font=('calibre',10))
intro3_label.pack(padx=10,pady=0)
intro4_label=tk.Label(about,text='Heres to celebrating the Dreamer and Believer in each one of us.',font=('calibre',10))
intro4_label.pack(padx=10,pady=0)
chart_label=tk.Label(about,text="Statistics of development of organisation in the past decade",font=('calibre',15,"bold"))
chart_label.pack(padx=10,pady=0)
chart1_label=tk.Label(about,text="Dreams Come True has dedicated its efforts towards fulfilling dreams of individuals of every age group likewise owing to our firm belief in the ageless and limitless power of dreaming and believing",font=('calibre',10))
chart1_label.pack(padx=10,pady=0)"""

intro2_label = tk.Label(
    about, text='The world generates 2.1 billion tonnes of municipal solid waste annually with', font=('calibre', 10))
intro2_label.pack(padx=10, pady=0)
intro3_label = tk.Label(
    about, text='average waste generated per person per day being 0.74 kilograms. There has', font=('calibre', 10))
intro3_label.pack(padx=10, pady=0)
intro4_label = tk.Label(
    about, text='arisen a conscious need to control waste production and to manage the generated', font=('calibre', 10))
intro4_label.pack(padx=10, pady=0)
chart_label = tk.Label(
    about, text="waste efficiently. One of the ways include proper collection, segregation and", font=('calibre', 15, "bold"))
chart_label.pack(padx=10, pady=0)


pie = pie(values, labels=Age, explode=explode, shadow=True)
gender_label = tk.Label(
    about, text='<12:children, 12-17:teenagers, 18+:adults,+65:seniors', font=('calibre', 10, 'bold'))
canvas = FigureCanvasTkAgg(actualFigure, about)
# canvas.get_tk_widget().pack(padx=1,pady=0)
# canvas.draw()
# gender_label.pack(padx=2,pady=2)
team_label = tk.Label(about, text='NOTE FROM THE DIRECTOR',
                      font=('calibre', 15, 'bold'))
team_label1 = tk.Label(
    about, text='Reuse the past, Recycle the present, Save the future.', font=('calibre', 10, 'bold'))
team_label.pack(padx=5, pady=0)
# img4 =tk.PhotoImage(file=r"C:/Users/lenovo/Pictures/mickey mousea.png")
# pimg4=img4.subsample(0,0)
# button4=tk.Button(about,image=img4,compound='left',justify='right',width='0',height='0',font="Times 23 bold",activeforeground='black').pack(padx=5,pady=5)#
team_label1.pack(padx=7, pady=0)
button = tk.Button(about, text='back', width='0', height='0', activebackground='SlateGray1', bg='turquoise1', font="Times 23 bold",
                   activeforeground='black', command=lambda: raise_frame(Home)).pack(side="top", expand=True, padx=20, pady=20)
cursor = mycon.cursor()
first_name_var = tk.StringVar()
last_name_var = tk.StringVar()
address_var1 = tk.StringVar()
dob_var24 = tk.StringVar()
age_var = tk.StringVar()
phone_number_var11 = tk.IntVar()
amount_willing_to_pay_var = tk.IntVar()
gender_var = tk.StringVar()

team_label3 = tk.Label(f, text='Upcoming Events', font=('calibre', 15, 'bold'))
team_label3.pack(padx=5, pady=0)


team_label3 = tk.Label(f, text='Poster Making Competition',
                       font=('calibre', 15, 'bold'))
team_label3.pack(padx=5, pady=0)

# The form stuff


def submit():
   first_name = first_name_entry.get()
   first_name_var.set("")
   last_name = last_name_entry.get()
   last_name_var.set("")
   address1 = address_entry1.get()
   address_var1.set("")
   dob24 = dob_entry24.get()
   dob_var24.set("")
   age = age_entry.get()  # gaddress
   age_var.set("")
   phone_number11 = phone_number_entry11.get()
   phone_number_var11.set("")
   # amount_willing_to_pay=amount_willing_to_pay_entry.get()
   # amount_willing_to_pay_var.set("")
   gender = gender_entry.get()
   gender_var.set("")

   st = "insert into customer(Name,address,email,CID,Password,phoneno,GAdd) values('{}','{}','{}','{}','{}',{},'{}')".format(
       first_name, address1, dob24, last_name, gender, phone_number11, age)

   cursor.execute(st)
   mycon.commit()


first_name_label = tk.Label(fulfiller, text='Name',
                            font=('calibre', 10, 'bold'))
first_name_entry = tk.Entry(
    fulfiller, textvariable=first_name_var, font=('calibre', 10, 'normal'))
last_name_label = tk.Label(fulfiller, text='Username',
                           font=('calibre', 10, 'bold'))
last_name_entry = tk.Entry(
    fulfiller, textvariable=last_name_var, font=('calibre', 10, 'normal'))
address_label1 = tk.Label(fulfiller, text='Address',
                          font=('calibre', 10, 'bold'))
address_entry1 = tk.Entry(
    fulfiller, textvariable=address_var1, font=('calibre', 10, 'normal'))
dob_label24 = tk.Label(fulfiller, text='Email', font=('calibre', 10, 'bold'))
dob_entry24 = tk.Entry(fulfiller, textvariable=dob_var24,
                       font=('calibre', 10, 'normal'))
age_label = tk.Label(fulfiller, text='G.Address', font=('calibre', 10, 'bold'))
age_entry = tk.Entry(fulfiller, textvariable=age_var,
                     font=('calibre', 10, 'normal'))
phone_number_label11 = tk.Label(
    fulfiller, text='Phone Number', font=('calibre', 10, 'bold'))
phone_number_entry11 = tk.Entry(
    fulfiller, textvariable=phone_number_var11, font=('calibre', 10, 'normal'))
# amount_willing_to_pay_label = tk.Label(fulfiller, text = 'Amount Paid', font=('calibre',10,'bold'))
# amount_willing_to_pay_entry = tk.Entry(fulfiller, textvariable = amount_willing_to_pay_var,font=('calibre',10,'normal'))
gender_label = tk.Label(fulfiller, text='Password',
                        font=('calibre', 10, 'bold'))
gender_entry = tk.Entry(fulfiller, textvariable=gender_var,
                        font=('calibre', 12, 'normal'))
sub_btn = tk.Button(fulfiller, text='Submit', command=submit)
welcome_label = tk.Label(
    fulfiller, text='  WELCOME TO GARGO', font=('calibre', 15))
welcome1_label = tk.Label(
    fulfiller, text=', KINDLY ENTER YOUR CREDENTIALS CAREFULLY', font=('calibre', 15))
thank_label = tk.Label(fulfiller, text='THANK YOU ', font=('calibre', 15))
thank1_label = tk.Label(
    fulfiller, text='WE ARE DEEPLY GRATEFUL FOR YOUR SUPPORT', font=('calibre', 15))
thank2_label = tk.Label(fulfiller, text='', font=('calibre', 15))
first_name_label.grid(row=1, column=0)
first_name_entry.grid(row=1, column=1, padx=0, pady=15)
last_name_label.grid(row=2, column=0)
last_name_entry.grid(row=2, column=1, padx=0, pady=15)
address_label1.grid(row=3, column=0)
address_entry1.grid(row=3, column=1, ipadx=120, ipady=15)
dob_label24.grid(row=5, column=0)
dob_entry24.grid(row=5, column=1, padx=0, pady=15)
age_label.grid(row=6, column=0)
age_entry.grid(row=6, column=1, padx=0, pady=15)
phone_number_label11.grid(row=7, column=0)
phone_number_entry11.grid(row=7, column=1, padx=0, pady=15)
# amount_willing_to_pay_label.grid(row=8,column=0)
# amount_willing_to_pay_entry.grid(row=8,column=1,padx=0, pady=15)
gender_label.grid(row=9, column=0)
gender_entry.grid(row=9, column=1, padx=0, pady=15)
sub_btn.grid(row=10, column=1)
welcome_label.grid(row=0, column=0)
welcome1_label.grid(row=0, column=1)
thank_label.grid(row=11, column=0)
thank1_label.grid(row=11, column=1)
thank2_label.grid(row=12, column=0)


def submit3():  # loginpage
   username21 = username_entry21.get()
   username21_var.set("")
   password21 = password_entry21.get()
   password21_var.set("")
   print(username21)
   print(password21)
   st = "select * from customer where CID='{}' and Password='{}' ".format(
       username21, password21)
   cursor.execute(st)
   e = cursor.fetchall()
   print(e)
   print('z')
   for row in e:
       print(row)
       z = tk.Label(flogin, text=row)
       z.grid(row=3, column=0)
   mycon.commit()


username21_var = tk.StringVar()
password21_var = tk.StringVar()
username_label21 = tk.Label(flogin, text='Username',
                            font=('calibre', 10, 'bold'))
username_entry21 = tk.Entry(
    flogin, textvariable=username21_var, font=('calibre', 10, 'normal'))
password_label21 = tk.Label(flogin, text='Password',
                            font=('calibre', 10, 'bold'))
password_entry21 = tk.Entry(
    flogin, textvariable=password21_var, font=('calibre', 10, 'normal'))
sub_btnA = tk.Button(flogin, text='Submit', command=submit3)
username_label21.grid(row=0, column=0)
username_entry21.grid(row=0, column=1)
password_label21.grid(row=1, column=0)
password_entry21.grid(row=1, column=1)
sub_btnA.grid(row=10, column=1)


def Coppg():
   Qs = "select BD from customer where CID='{}' and Password='{}'".format(
       cusername1, cpassword1)
   cursor.execute(Qs)
   Qd = cursor.fetchall()
   # tHIS IS SUPPOSED TO BE THE AMOUNT THATS ALREADY LYING THERE.
   Qa = Qd[0][0]
   print("hi1")
   print(Qa)
   z = tk.Label(
       Cop1, text="The total waste(Biodegrable) contributed by you is")
   z.grid(row=3, column=0)
   w = tk.Label(Cop1, text=Qa)
   w.grid(row=6, column=0)

   Qs1 = "select NBD from customer where CID='{}' and Password='{}'".format(
       cusername1, cpassword1)
   cursor.execute(Qs1)
   Qd1 = cursor.fetchall()
   # tHIS IS SUPPOSED TO BE THE AMOUNT THATS ALREADY LYING THERE.
   Qa1 = Qd1[0][0]
   print("hi1")
   print(Qa1)
   y = tk.Label(
       Cop1, text="The total waste(NONBiodegrable) contributed by you is")
   y.grid(row=8, column=0)
   x = tk.Label(Cop1, text=Qa1)
   x.grid(row=12, column=0)

   As = "select WILMB from customer where CID='{}' and Password='{}'".format(
       cusername1, cpassword1)
   cursor.execute(As)
   Ad = cursor.fetchall()
   # tHIS IS SUPPOSED TO BE THE AMOUNT THATS ALREADY LYING THERE.
   Aa = Ad[0][0]
   print("hi1")
   print(Aa)
   Az = tk.Label(
       Cop2, text="The total waste(Biodegrable) contributed by you(latest month) is")
   Az.grid(row=3, column=0)
   Aw = tk.Label(Cop2, text=Aa)
   Aw.grid(row=6, column=0)

   As1 = "select WILMNB from customer where CID='{}' and Password='{}'".format(
       cusername1, cpassword1)
   cursor.execute(As1)
   Ad1 = cursor.fetchall()
   # tHIS IS SUPPOSED TO BE THE AMOUNT THATS ALREADY LYING THERE.
   Aa1 = Ad1[0][0]
   print("hi1")

   Ay = tk.Label(
       Cop2, text="The total waste(NONBiodegrable) contributed by you(latest month) is")
   Ay.grid(row=7, column=0)
   Ax = tk.Label(Cop2, text=Aa1)
   Ax.grid(row=13, column=0)


def submit4():  # the customerlogin
   global cusername1
   global cpassword1
   cusername1 = username1_entry.get()
   username1_var.set("")
   cpassword1 = password1_entry.get()
   password1_var.set("")

   st = "select * from customer where CID='{}' and Password='{}' ".format(
       cusername1, cpassword1)
   cursor.execute(st)
   d = cursor.fetchall()
   for row in d:
       print(row)
       z = tk.Label(wlogin, text=row)
       z.grid(row=3, column=0)

   if d != []:
      buttonf1 = tk.Button(wlogin, text='GOO', width='0', height='0', activebackground='SlateGray1',
                           bg='SlateGray1', font="Times 23 bold", activeforeground='black', command=lambda: raise_frame(cus2))
      buttonf1.grid()
      Coppg()
   mycon.commit()


username1_var = tk.StringVar()
password1_var = tk.StringVar()
username1_label = tk.Label(wlogin, text='Username.',
                           font=('calibre', 10, 'bold'))
username1_entry = tk.Entry(
    wlogin, textvariable=username1_var, font=('calibre', 10, 'normal'))
password1_label = tk.Label(wlogin, text='Password',
                           font=('calibre', 10, 'bold'))
password1_entry = tk.Entry(
    wlogin, textvariable=password1_var, font=('calibre', 10, 'normal'))
sub_btn = tk.Button(wlogin, text='Submit', command=submit4)
username1_label.grid(row=0, column=0)
username1_entry.grid(row=0, column=1)
password1_label.grid(row=1, column=0)
password1_entry.grid(row=1, column=1)

sub_btn.grid(row=10, column=1)

# new page to view stuff
# have a gooo button

#


def cash():
    s = "select WILMB from CUSTOMER where CID='{}'".format(username1)
    cursor.execute(s)
    e = cursor.fetchall()


# sub_btn=tk.Button(cus2,text = 'View CASH earned', command = cash)#submit6)#VIEW THE CASH YOUR GETTING/GOT RECENTLY AND OVERALL CASH TOO#View table grant a wish'
# sub_btn1.grid(row=0,column=0,ipadx=12,ipady=12)
sub_btnaa = tk.Button(cus2, text='Total overall waste collected',
                      command=lambda: raise_frame(Cop1))  # submit7)#VIEW WHERE TRUCK IS
sub_btnaa.grid(row=0, column=0, ipadx=12, ipady=12)
sub_btn2 = tk.Button(cus2, text='View Amount Earned in the latest month',
                     command=lambda: raise_frame(Cop2))
# sub_btn1=tk.Button(cus2,text = 'Update table make a wish',command=lambda:raise_frame(f2))
buttonz = tk.Button(cus2, text='Back To Home Page', width='0', height='0',
                    font="Times 23 bold", activeforeground='black', command=lambda: raise_frame(Home))
sub_btn2.grid(row=7, column=0, ipadx=12, ipady=12)
sub_btn.grid(row=5, column=0, ipadx=12, ipady=12)
buttonz.grid(row=100, column=0)


sub_btn.grid(row=10, column=1)
sub_btn2 = tk.Button(organiser, text='Update for the month ',
                     command=lambda: raise_frame(delete))  # pdate table grant a wish
# sub_btn1=tk.Button(organiser,text = 'Update table make a wish',command=lambda:raise_frame(f2))
buttonz = tk.Button(organiser, text='Back To Home Page', width='0', height='0',
                    font="Times 23 bold", activeforeground='black', command=lambda: raise_frame(Home))
sub_btn2.grid(row=7, column=0, ipadx=12, ipady=12)
# sub_btn1.grid(row=5,column=0,ipadx=12,ipady=12)
buttonz.grid(row=100, column=0)

# This function is for updating the Biodegradble Waste Amount of The ongoing month


def updatewater():
    # For biodegradable
    st1 = "update customer set WB='{}' where CID='{}'".format(
        bdw, username_staff_weight1)
    cursor.execute(st1)
    mycon.commit()
    # For non biodegrable
    st2 = "update customer set WNB='{}' where CID='{}'".format(
        nbdw, username_staff_weight1)
    cursor.execute(st2)
    mycon.commit()


# FIRST BUTTON OF STAFF LOGIN

def submitwt():

   # THE USERNAME
   global username_staff_weight1
   username_staff_weight1 = username_staff_weight_entry.get()
   print(username_staff_weight1)
   username_staff_weight.set("")

   # B11 IS THE PASSWORD
   b11 = b1_entry.get()
   print(b11)
   b1.set("")

   s = "select WB from customer where CID='{}' and Password='{}'".format(
       username_staff_weight1, b11)
   cursor.execute(s)

   d = cursor.fetchall()
   print(d)

   if len(d) == 0:
       d.append(0)
   a = d[0][0]  # tHIS IS SUPPOSED TO BE THE AMOUNT THATS ALREADY LYING THERE.
   print("hi1")
   print(a)

   s2 = "select WNB from customer where CID='{}' and Password='{}'".format(
       username_staff_weight1, b11)
   cursor.execute(s2)
   d2 = cursor.fetchall()
   # tHIS IS SUPPOSED TO BE THE AMOUNT THATS ALREADY LYING THERE.
   a2 = d2[0][0]
   print("hi2")
   print(a2)

   global bdw
   global nbdw

   # NON BIODEGRABLE WASTE
   nbdw = float(username_entry1Z.get())+a2

   # THIS IS THE BIODEGRADABLE AMOUNT
   bdw = float(username_entryY.get())+a

   updatewater()


username_staff_weight = tk.StringVar()
b1 = tk.StringVar()
username_varR = tk.DoubleVar()
username_var2Z = tk.DoubleVar()


username_label = tk.Label(
    weightpg, text='Weight of Biodegradable waste', font=('calibre', 10, 'bold'))
username_entryY = tk.Entry(
    weightpg, textvariable=username_varR, font=('calibre', 10, 'normal'))

username_label1 = tk.Label(
    weightpg, text='Weight of Non Biodegradable waste', font=('calibre', 10, 'bold'))
username_entry1Z = tk.Entry(
    weightpg, textvariable=username_var2Z, font=('calibre', 10, 'normal'))

username_staff_weight_label = tk.Label(
    weightpg, text='Username', font=('calibre', 10, 'bold'))
# USERNAME OD CUSTOMER TO MATH WITH DB AND ADD TO ADDING MONTHLY username_staff_weight
username_staff_weight_entry = tk.Entry(
    weightpg, textvariable=username_staff_weight, font=('calibre', 10, 'normal'))

b1_label = tk.Label(weightpg, text='Password', font=('calibre', 10, 'bold'))
b1_entry = tk.Entry(weightpg, textvariable=b1, font=('calibre', 10, 'normal'))


username_label.grid(row=7, column=0)
username_entryY.grid(row=7, column=1)

username_label1.grid(row=8, column=0)
username_entry1Z.grid(row=8, column=1)

username_staff_weight_label.grid(row=9, column=0)
username_staff_weight_entry.grid(row=9, column=1)

b1_label.grid(row=10, column=0)
b1_entry.grid(row=10, column=1)

sub_btn40 = tk.Button(weightpg, text='Submit', command=submitwt)
sub_btn40.grid(row=11, column=1, ipadx=12, ipady=12)

# Submit -then goes to update water and updates current records

# This is to send messages


def submit7():
  global areaname
  global aa
  global bb
  areaname = areaname_entry2.get()
  areaname_var2.set("")
  print("Enters function")

  st1 = "select phoneno from customer where GAdd='{}'".format(areaname)
  List = []
  cursor.execute(st1)
  aa = cursor.fetchall()
  print("alert")
  l = len(aa)
  print(aa)
  for i in range(0, l):

      phno = aa[i]
      List.append(("+91"+str(phno)))  # List of phone numbers

  print(List)
  print("YUYU")

  from twilio.rest import Client

  sid = 'AC7c25870346804f371b04d1d8a9eb89a2'
  auth_token = '245478beb51cf2ee5420c57162752bd1'

  dtr = '+919035548234'

  client = Client(sid, auth_token)
  resp = client.messages.create(
      body='Truck is here', from_='+17087878617', to=dtr)

  print(resp.sid)


areaname_var2 = tk.StringVar()
areaname_label2 = tk.Label(
    truckalert, text='Enter Area Name', font=('calibre', 10, 'bold'))
areaname_entry2 = tk.Entry(
    truckalert, textvariable=areaname_var2, font=('calibre', 10, 'normal'))

areaname_label2.grid(row=7, column=0)
areaname_entry2.grid(row=7, column=1)

sub_btn4111 = tk.Button(truckalert, text='Submit', command=submit7)
sub_btn4111.grid(row=10, column=1, ipadx=12, ipady=12)
# Submit sends a message


sub_btn = tk.Button(organiser, text='Enter the amount of kgs of waste',
                    command=lambda: raise_frame(weightpg))  # iew table grant a wish/
sub_btn.grid(row=0, column=0, ipadx=12, ipady=12)
sub_btnaa = tk.Button(organiser, text='Alert system',
                      command=lambda: raise_frame(truckalert))
sub_btnaa.grid(row=1, column=0, ipadx=12, ipady=12)  # view make a wish


def close_window():
    organiser.destroy()


def submit1():
   username = username_entry2.get()
   username_var2.set("")
   sname = s_entry.get()
   s_var.set("")

   st1 = "update make_a_wish set status='{}' where email='{}'".format(
       sname, username)
   cursor.execute(st1)
   mycon.commit()


s_var = tk.StringVar()
username_var2 = tk.IntVar()
username_label2 = tk.Label(f2, text='Email', font=('calibre', 10, 'bold'))
username_entry2 = tk.Entry(
    f2, textvariable=username_var2, font=('calibre', 10, 'normal'))
# sub_btn1=tk.Button(f2,text = 'update a record',command=submit1)
username_label2.grid(row=7, column=0)
username_entry2.grid(row=7, column=1)
Status = tk.Label(f2, text='New Status', font=('calibre', 10, 'bold'))
s_entry = tk.Entry(f2, textvariable=s_var, font=('calibre', 10, 'normal'))
blank_label = tk.Label(f2, text='', font=('calibre', 10, 'bold'))
blank_label.grid(row=13, column=0)
blank_label2 = tk.Label(f2, text='', font=('calibre', 10, 'bold'))
blank_label2.grid(row=14, column=0)
blank_label3 = tk.Label(f2, text='', font=('calibre', 10, 'bold'))
blank_label3.grid(row=25, column=0)
blank_label4 = tk.Label(f2, text='', font=('calibre', 10, 'bold'))
blank_label4.grid(row=30, column=0)
blank_label5 = tk.Label(f2, text='', font=('calibre', 10, 'bold'))
blank_label5.grid(row=34, column=0)
blank_label6 = tk.Label(f2, text='', font=('calibre', 10, 'bold'))
blank_label6.grid(row=40, column=0)
blank_label7 = tk.Label(f2, text='', font=('calibre', 10, 'bold'))
blank_label7.grid(row=52, column=0)
sub_btn411 = tk.Button(f2, text='Submit', command=submit1)
sub_btn411.grid(row=10, column=1, ipadx=12, ipady=12)
Status.grid(row=9, column=0)
s_entry.grid(row=9, column=1, ipadx=0, ipady=15)
button = tk.Button(f2, text='Back to Organisers page', width='0', height='0',
                   font="Times 23 bold", activeforeground='black', command=lambda: raise_frame(organiser))
button.grid(row=16, column=1, ipadx=1, ipady=1)


# This is the update for the month window
def submit8():

   global username_v
   username_v = username_value.get()
   print(username_v)
   # username_staff_weight.set("")

   global password_v
   password_v = password_value.get()
   print(password_v)
   # username_staff_weight.set("")

   st = "select * from customer where CID='{}' and Password='{}' ".format(
       username_v, password_v)
   cursor.execute(st)
   d = cursor.fetchall()
   for row in d:
       print(row)
       z = tk.Label(delete, text=row)
       z.grid(row=3, column=0)

   if d != []:
      buttonf1 = tk.Button(delete, text='UPDATE RECORDS', width='0', height='0', activebackground='SlateGray1',
                           bg='SlateGray1', font="Times 23 bold", activeforeground='black', command=lambda: raise_frame(Staffop3))
      buttonf1.grid()
   mycon.commit()


username_value = tk.StringVar()
username_value_label = tk.Label(
    delete, text='Username', font=('calibre', 10, 'bold'))
# USERNAME OD CUSTOMER TO MATH WITH DB AND ADD TO ADDING MONTHLY username_staff_weight
username_value_entry = tk.Entry(
    delete, textvariable=username_value, font=('calibre', 10, 'normal'))
username_value_label.grid(row=9, column=0)
username_value_entry.grid(row=9, column=1)


password_value = tk.StringVar()
password_value_label = tk.Label(
    delete, text='password', font=('calibre', 10, 'bold'))
# password OD CUSTOMER TO MATH WITH DB AND ADD TO ADDING MONTHLY password_staff_weight
password_value_entry = tk.Entry(
    delete, textvariable=password_value, font=('calibre', 10, 'normal'))
password_value_label.grid(row=15, column=0)
password_value_entry.grid(row=15, column=1)

sub_btn4 = tk.Button(delete, text='Submit', command=submit8)
sub_btn4.grid(row=20, column=1)


# STAFFLOGIN
def submit5():
   username212 = username_entry212.get()
   username212_var.set("")
   password212 = password_entry212.get()
   password212_var.set("")
   st = "select * from company where username='{}'and password='{}' ".format(
       username212, password212)
   cursor.execute(st)
   e = cursor.fetchall()
   if e != []:
      buttonf1 = tk.Button(ORG, text='ORGANISER', width='0', height='0', activebackground='SlateGray1',
                           bg='SlateGray1', font="Times 23 bold", activeforeground='black', command=lambda: raise_frame(organiser))
      buttonf1.grid()
   mycon.commit()


username212_var = tk.StringVar()
password212_var = tk.StringVar()
username_label212 = tk.Label(
    ORG, text='Username', font=('calibre', 10, 'bold'))
username_entry212 = tk.Entry(
    ORG, textvariable=username212_var, font=('calibre', 10, 'normal'))
password_label212 = tk.Label(
    ORG, text='Password', font=('calibre', 10, 'bold'))
password_entry212 = tk.Entry(
    ORG, textvariable=password212_var, font=('calibre', 10, 'normal'))
sub_btnA = tk.Button(ORG, text='Submit', command=submit5)
username_label212.grid(row=0, column=0)
username_entry212.grid(row=0, column=1)
password_label212.grid(row=1, column=0)
password_entry212.grid(row=1, column=1)
sub_btnA.grid(row=10, column=1)

# Staffop3


def settozero():
    # For biodegradable
    zero = 0
    st1 = "update customer set WB='{}' where CID='{}'".format(zero, username_v)
    cursor.execute(st1)
    mycon.commit()
    # For non biodegrable
    st2 = "update customer set WNB='{}' where CID='{}'".format(
        zero, username_v)
    cursor.execute(st2)
    mycon.commit()


def updateyearly():

    st1 = "update customer set BD='{}' where CID='{}'".format(ya, username_v)
    cursor.execute(st1)
    mycon.commit()
    # For non biodegrable
    st2 = "update customer set NBD='{}' where CID='{}'".format(ya1, username_v)
    cursor.execute(st2)
    mycon.commit()


def setyearly():
   global ys
   global ys1
   global ya
   global ya1
   s = "select BD from customer where CID='{}' and Password='{}'".format(
       username_v, password_v)
   cursor.execute(s)
   d = cursor.fetchall()
   # tHIS IS SUPPOSED TO BE THE AMOUNT THATS ALREADY LYING THERE.
   ya = d[0][0]+float(ma)

   s1 = "select NBD from customer where CID='{}' and Password='{}'".format(
       username_v, password_v)
   cursor.execute(s1)
   d1 = cursor.fetchall()
   # tHIS IS SUPPOSED TO BE THE AMOUNT THATS ALREADY LYING THERE.
   ya1 = d1[0][0]+float(ma1)

   updateyearly()


def setnewmonthly():
    st1 = "update customer set WILMB='{}' where CID='{}'".format(
        da, username_v)
    cursor.execute(st1)
    mycon.commit()
    # For non biodegrable
    st2 = "update customer set WILMNB='{}' where CID='{}'".format(
        da1, username_v)
    cursor.execute(st2)
    mycon.commit()


def submit90():
    # The on going waste collection value is stored
    # The on going waste collection value becomes 0
    # The month value is stored AND we SHOW AMOUNT IS CALCULATED SO AND SO FOR THIS KG
    # The on going value is made month value(The month for which they will earn money)
    # Yearly value we update

    # username_v
    # password_v
   global da
   global da1

   s = "select WB from customer where CID='{}' and Password='{}'".format(
       username_v, password_v)
   cursor.execute(s)
   d = cursor.fetchall()

   print(d)
   print(d[0])
   da = d[0][0]  # THIS IS SUPPOSED TO BE THE AMOUNT THATS ALREADY LYING THERE.

   s1 = "select WNB from customer where CID='{}' and Password='{}'".format(
       username_v, password_v)
   cursor.execute(s1)
   d1 = cursor.fetchall()
   # THIS IS SUPPOSED TO BE THE AMOUNT THATS ALREADY LYING THERE.
   da1 = d1[0][0]

   blabel1 = tk.Label(Staffop3, text='The Total amount which will be received by the cutomer is for __ amount of kgs(Biodegrable)', font=(
       'calibre', 10, 'bold'))
   blabel2 = tk.Label(Staffop3, text=da, font=('calibre', 10, 'bold'))

   blabel11 = tk.Label(Staffop3, text='The Total amount which will be received by the cutomer is for __ amount of kgs(NonBiodegrable)', font=(
       'calibre', 10, 'bold'))
   blabel22 = tk.Label(Staffop3, text=da1, font=('calibre', 10, 'bold'))

   blabel1.grid(row=10, column=1)
   blabel2.grid(row=12, column=1)
   blabel11.grid(row=14, column=1)
   blabel22.grid(row=16, column=1)

   settozero()

   global ma
   global ma1
   ms = "select WILMB from customer where CID='{}' and Password='{}'".format(
       username_v, password_v)
   cursor.execute(ms)
   md = cursor.fetchall()
   # tHIS IS SUPPOSED TO BE THE OLD MONTH AMOUNT THATS ALREADY LYING THERE.
   ma = md[0][0]

   ms1 = "select WILMNB from customer where CID='{}' and Password='{}'".format(
       username_v, password_v)
   cursor.execute(ms1)
   md1 = cursor.fetchall()
   # tHIS IS SUPPOSED TO BE THE OLD MONTHAMOUNT THATS ALREADY LYING THERE.
   ma1 = md1[0][0]

   setyearly()
   setnewmonthly()


sub_btn555 = tk.Button(
    Staffop3, text='CONFIRM Update AND SEND AMOUNT TO CUSTOMER', command=submit90)
sub_btn555.grid(row=10, column=1)
