from tkinter import *
from PIL import Image,ImageTk
import tkinter as tk
from tkinter import ttk
import math,random
class Flight_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Flight Booking System")
        title = Label(self.root,text="AIR-ASIA FLIGHTS",font=("times new roman",30,"bold"),pady=2,fg="white",bg="#FF7700",bd=7,relief=GROOVE).pack(fill=X)

        Frame1 = LabelFrame(self.root,text="Customer Booking Details",font=("times new roman",20,"bold"),fg="blue",bg="white")
        Frame1.place(x=0,y=70,width=800,height=370)
        '''load = Image.open("icon.png")
        render = ImageTk.PhotoImage(load)
        img = Label(Frame1,image=render)
        img.grid(row=0,column=0,padx=2,pady=2)'''
        #=======================================Variables========================================
        self.passenger_name = StringVar()
        self.pfrom = StringVar()
        self.pto = StringVar()
        self.flight_N = StringVar()
        self.seat_no = IntVar()
        seatno = random.randint(1,200)
        self.seat_no.set(str(seatno))
        self.gate_no = IntVar()
        gateno = random.randint(1,4)
        self.gate_no.set(str(gateno))
        self.fdate = StringVar()
        self.ftime = StringVar()
        self.fair = StringVar()


        # =======================================#=======================================

        cname_lbl = Label(Frame1,text="Customer's Name:",font=("times new roman",15,"bold"),fg="blue",bg="white",justify=LEFT).grid(row=0,column=0,pady=10)
        cname_txt = Entry(Frame1,width=20,font=("Arial",15),bd=3,textvariable=self.passenger_name,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        cfrom_lbl = Label(Frame1, text="From:", font=("times new roman", 15, "bold"), fg="blue", bg="white",justify=LEFT).grid(row=1, column=0, pady=10)
        cfrom_txt = Entry(Frame1, width=20, font=("Arial", 15), bd=3, textvariable=self.pfrom,relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)
        '''n = tk.StringVar()
        place1chosen=ttk.Combobox(Frame1,width=18,textvariable=n,font=("Arial",15))
        place1chosen['values']=('Chennai','Bombay','Hyderabad','Banglore','Pune','Chandigarh','Trivandrum','Cochin','Goa','Jaipur','Nashik','Vijaywada','Dehradun','Shilong','Aurangabad')
        place1chosen.grid(row=1,column=1)
        place1chosen.current()'''


        cdes_lbl = Label(Frame1, text="Destination:", font=("times new roman", 15, "bold"), fg="blue", bg="white",justify=LEFT).grid(row=2, column=0, pady=10)
        cdes_txt = Entry(Frame1, width=20, font=("Arial", 15), bd=3, textvariable=self.pto,relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)
        '''n1 = tk.StringVar()
        place2chosen = ttk.Combobox(Frame1, width=18, textvariable=n1, font=("Arial", 15))
        place2chosen['values'] = (
        'Chennai', 'Bombay', 'Hyderabad', 'Banglore', 'Pune', 'Chandigarh', 'Trivandrum', 'Cochin', 'Goa', 'Jaipur',
        'Nashik', 'Vijaywada', 'Dehradun', 'Shilong', 'Aurangabad')
        place2chosen.grid(row=2, column=1)
        place2chosen.current()'''


        cclass_lbl = Label(Frame1, text="Class:", font=("times new roman", 15, "bold"), fg="blue", bg="white",justify=LEFT).grid(row=3, column=0, pady=10)
        n2 = tk.StringVar()
        classchosen = ttk.Combobox(Frame1, width=18, textvariable=n2, font=("Arial", 15))
        classchosen['values'] = (
            'Standard', 'Imperial', 'Premium')
        classchosen.grid(row=3, column=1)
        classchosen.current()

        cflight_lbl = Label(Frame1, text="Flight No:", font=("times new roman", 15, "bold"), fg="blue", bg="white",justify=LEFT).grid(row=4, column=0, pady=10)
        cflight_txt = Entry(Frame1, width=20, font=("Arial", 15), bd=3,textvariable=self.flight_N, relief=SUNKEN).grid(row=4, column=1, padx=10,pady=10)

        btn_book = Button(Frame1, text="Book Flight", width=18, font=("times new roman", 15, "bold"),command=self.manage_flight, fg="white",bg="#FF7700", relief=GROOVE, bd=7).grid(row=5, column=1,pady=10)

        cseat_lbl = Label(Frame1, text="Seat:", font=("times new roman", 15, "bold"), fg="blue", bg="white",justify=LEFT).grid(row=0, column=5, pady=10,padx=10)
        cseat_txt = Entry(Frame1, width=20, font=("Arial", 15), bd=3,textvariable=self.seat_no, relief=SUNKEN).grid(row=0, column=6, padx=10,pady=10)

        cdate_lbl = Label(Frame1, text="Date:", font=("times new roman", 15, "bold"), fg="blue", bg="white",justify=LEFT).grid(row=1, column=5, pady=10,padx=10)
        cdate_txt = Entry(Frame1, width=20, font=("Arial", 15),textvariable=self.fdate, bd=3, relief=SUNKEN).grid(row=1, column=6, padx=10,pady=10)

        cgate_lbl = Label(Frame1, text="Gate:", font=("times new roman", 15, "bold"), fg="blue", bg="white",justify=LEFT).grid(row=2, column=5, pady=10,padx=10)
        cgate_txt = Entry(Frame1, width=20, font=("Arial", 15), bd=3,textvariable=self.gate_no, relief=SUNKEN).grid(row=2, column=6, padx=10,pady=10)

        ctime_lbl = Label(Frame1, text="Time:", font=("times new roman", 15, "bold"), fg="blue", bg="white",justify=LEFT).grid(row=3, column=5, pady=10,padx=10)
        ctime_txt = Entry(Frame1, width=20, font=("Arial", 15), bd=3,textvariable=self.ftime, relief=SUNKEN).grid(row=3, column=6, padx=10,pady=10)




        btn_pass = Button(Frame1, text="Alot Pass", width=18, font=("times new roman", 15, "bold"), fg="white",bg="#FF7700", command=self.pass_area ,relief=GROOVE, bd=7).grid(row=5, column=6, pady=10)
        pass_frame =LabelFrame(self.root,text="Flight Pass:", font=("times new roman", 20, "bold"), fg="blue",bg="white")
        pass_frame.place(x=0, y=440, width=1000, height=370)
        '''load1 = Image.open("ticket1.jpg")
        self.render = ImageTk.PhotoImage(load1)
        img1 = Label(pass_frame, image=self.render)
        img1.grid(row=0, column=0, padx=20, pady=2)'''
        bill_title = Label(pass_frame, text="BOARDING PASS:", bd=7, font="arial 15 bold", relief=GROOVE, bg="#FF7700",fg="white").pack(fill=X)
        scrol_y = Scrollbar(pass_frame, orient=VERTICAL)
        self.ttxtarea = Text(pass_frame, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.ttxtarea.yview)
        self.ttxtarea.pack(fill=BOTH, expand=1)

        self.welcome_pass()

        if self.pfrom!="" and self.pto!="":
            self.manage_flight()

        scheduleframe = LabelFrame(self.root, relief=GROOVE, bd=3,bg="white",text="Flight Schedules:",font=("times new roman",20,"bold"),fg="blue")
        scheduleframe.place(x=801, y=70, width=720, height=370)
        bill_title = Label(scheduleframe, text="Schedules", bd=7, font="arial 15 bold", relief=GROOVE,bg="#FF7700",fg="white").pack(fill=X)
        scrol_y = Scrollbar(scheduleframe, orient=VERTICAL)
        self.txtarea = Text(scheduleframe, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        self.schedule_area()

    def manage_flight(self):
        if self.pfrom.get() == 'Chennai' and self.pto.get() == 'Bombay':
            self.flight_N.set("CB1001")
            self.fdate.set("15/4/21")
            self.ftime.set("9:30 AM")
            self.fair.set("Rs.2600")
        if self.pfrom.get() == 'Pune' and self.pto.get() == 'Aurangabad':
            self.flight_N.set("PA1023")
            self.fdate.set("15/4/21")
            self.ftime.set("11:00 AM")
            self.fair.set("Rs.600")
        if self.pfrom.get() == 'Bombay' and self.pto.get() == 'Trivandrum':
            self.flight_N.set("BT2345")
            self.fdate.set("15/4/21")
            self.ftime.set("01:30 PM")
            self.fair.set("Rs.2800")
        if self.pfrom.get() == 'Bangalore' and self.pto.get() == 'Chennai':
            self.flight_N.set("BC2657")
            self.fdate.set("15/4/21")
            self.ftime.set("2:15 PM")
            self.fair.set("Rs.1600")
        if self.pfrom.get() == 'Hyderabad' and self.pto.get() == 'Pune':
            self.flight_N.set("HP2354")
            self.fdate.set("15/4/21")
            self.ftime.set("04:00 PM")
            self.fair.set("Rs.3200")
        if self.pfrom.get() == 'Cochin' and self.pto.get() == 'Shilong':
            self.flight_N.set("CS1234")
            self.fdate.set("17/4/21")
            self.ftime.set("3:00 AM")
            self.fair.set("Rs.4500")
        if self.pfrom.get() == 'Dehradun' and self.pto.get() == 'Nashik':
            self.flight_N.set("DC0098")
            self.fdate.set("17/4/21")
            self.ftime.set("5:30 AM")
            self.fair.set("Rs.8600")
        if self.pfrom.get() == 'Vijaywada' and self.pto.get() == 'Chandigarh':
            self.flight_N.set("VC4562")
            self.fdate.set("17/4/21")
            self.ftime.set("7:15 AM")
            self.fair.set("Rs.3700")
        if self.pfrom.get() == 'Bangalore' and self.pto.get() == 'Pune':
            self.flight_N.set("BP3465")
            self.fdate.set("17/4/21")
            self.ftime.set("12:40 PM")
            self.fair.set("Rs.3400")
        if self.pfrom.get() == 'Shilong' and self.pto.get() == 'Mumbai':
            self.flight_N.set("SM9890")
            self.fdate.set("19/4/21")
            self.ftime.set("4:14 PM")
            self.fair.set("Rs.4600")
        if self.pfrom.get() == 'Nashik' and self.pto.get() == 'Dehradun':
            self.flight_N.set("ND2134")
            self.fdate.set("19/4/21")
            self.ftime.set("8:45 AM")
            self.fair.set("Rs.6200")
        if self.pfrom.get() == 'Chandigarh' and self.pto.get() == 'Mumbai':
            self.flight_N.set("CM9043")
            self.fdate.set("19/4/21")
            self.ftime.set("11:15 AM")
            self.fair.set("Rs.5200")
        if self.pfrom.get() == 'Pune' and self.pto.get() == 'Aurangabad':
            self.flight_N.set("PA6745")
            self.fdate.set("19/4/21")
            self.ftime.set("1:00 PM")
            self.fair.set("Rs.6100")
        if self.pfrom.get() == 'Mumbai' and self.pto.get() == 'Bombay':
            self.flight_N.set("MB1200")
            self.fdate.set("20/4/21")
            self.ftime.set("6:10 PM")
            self.fair.set("Rs.3000")

    def schedule_area(self):
        self.txtarea.insert(END,f"\t\t\t****** Welcome to Air Asia Flights *****\n")
        self.txtarea.insert(END,"====================================================================================")
        self.txtarea.insert(END,"\nFlight no.\t\tFrom \t\tDestination \t\t\tDate \t\tTime")
        self.txtarea.insert(END, "\n====================================================================================")
        self.txtarea.insert(END, "\nCB1001\t\tChennai \t\tBombay \t\t\t15/4/21 \t\t09:30 AM")
        self.txtarea.insert(END, "\nPA1023\t\tPune \t\tAurangabad \t\t\t15/4/21 \t\t11:00 AM")
        self.txtarea.insert(END, "\nBT2345\t\tBombay \t\tTrivandrum \t\t\t15/4/21 \t\t01:30 PM")
        self.txtarea.insert(END, "\nBC2657\t\tBangalore \t\tChennai \t\t\t15/4/21 \t\t02:15 PM")
        self.txtarea.insert(END,"\nHP2354\t\tHyderabad \t\tPune \t\t\t15/4/21\t\t04:00 PM")
        self.txtarea.insert(END, "\nCS1234\t\tCochin \t\tShilong \t\t\t17/4/21 \t\t03:00 AM")
        self.txtarea.insert(END, "\nDC0098\t\tDehradun \t\tNashik \t\t\t17/4/21 \t\t05:30 AM")
        self.txtarea.insert(END, "\nVC4562\t\tVijaywada \t\tChandigarh \t\t\t17/4/21 \t\t07:15 AM")
        self.txtarea.insert(END, "\nBP3465\t\tBangalore \t\tPune \t\t\t17/4/21 \t\t12:40 PM")
        self.txtarea.insert(END, "\nSM9890\t\tShilong \t\tMumbai \t\t\t19/4/21 \t\t04:14 AM")
        self.txtarea.insert(END, "\nND2134\t\tNashik \t\tDehradun \t\t\t19/4/21 \t\t08:45 AM")
        self.txtarea.insert(END, "\nCM9043\t\tChandigarh \t\tMumbai \t\t\t19/4/21 \t\t11:15 AM")
        self.txtarea.insert(END, "\nPA6745\t\tPune \t\tAurangabad \t\t\t19/4/21 \t\t01:00 PM")
        self.txtarea.insert(END, "\nMB1200\t\tMumbai \t\tBombay \t\t\t20/4/21 \t\t06:10 PM")

        logo_frame = LabelFrame(self.root, font=("times new roman", 20, "bold"), fg="blue",bg="white")
        logo_frame.place(x=1001, y=440, width=520, height=370)
        load1 = Image.open("28logo9.jpg")
        self.render = ImageTk.PhotoImage(load1)
        img1 = Label(logo_frame, image=self.render)
        img1.grid(row=0, column=0, padx=0, pady=2)

    def welcome_pass(self):
        self.ttxtarea.delete('1.0', END)
        self.ttxtarea.insert(END, f"\t\t\t****** Thanks for Choosing Air Asia Flights *****\n")
        self.ttxtarea.insert(END, "====================================================================================")



    def pass_area(self):
        self.welcome_pass()
        self.ttxtarea.insert(END, f"\n\n\n\tNAME OF PASSENGER:  {self.passenger_name.get()} ")
        self.ttxtarea.insert(END, f"\n\tFROM:  {self.pfrom.get()} ")
        self.ttxtarea.insert(END, f"\n\tTO:  {self.pto.get()}")
        self.ttxtarea.insert(END, f"\n\n\tFLIGHT:{self.flight_N.get()}\t\tSEAT: {self.seat_no.get()} ")
        self.ttxtarea.insert(END, f"\n\n\tDATE:  {self.fdate.get()}\t\tGATE:{self.gate_no.get()}\t\tTIME:{self.ftime.get()}")
        self.ttxtarea.insert(END, f"\n\tFAIR:  {self.fair.get()} ")

