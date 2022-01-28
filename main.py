from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re
import csv


class Reservation:
    total_seats = 20
    flag = False
    seats = 0

    def __init__(self, root):
        self.root = root
        self.root.title = 'BUS TICKET BOOKING'
        self.root.geometry('1120x610+0+0')
        self.root.configure(background='gainsboro')

        db = sqlite3.connect('tickets_db.sqlite')
        cursor = db.cursor()
        Reservation.flag = False

        try:
            cursor.execute(''' create table tickets(
                name text,
                email text,
                gender text,
                aadhar text,
                contact text,
                address text,
                class text,
                arrival text,
                destination text,
                seats integer)
            ''')
        except:
            pass

        # ----------------------------------------------------------------FRAMES---------------------------------------------------------------------#
        MainFrame = Frame(self.root, bd=10, width=1350, height=800, bg='dark green', relief=RIDGE)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=10, width=1340, height=100, bg='light green', relief=RIDGE)
        TitleFrame.grid()
        MenuFrame = Frame(MainFrame, bd=10, width=1340, height=600, bg='dark green', relief=RIDGE)
        MenuFrame.grid()

        f1 = Frame(MenuFrame, width=900, height=500, relief=RIDGE)  # left partition
        f1.grid(row=1, column=0)

        f2 = Frame(MenuFrame, width=420, height=500, pady=2, relief=RIDGE)  # right partition
        f2.grid(row=1, column=1)

        f2Top = Frame(f2, width=404, height=510, bd=5, relief=RIDGE)  # Ticketing Receipt
        f2Top.pack(side=TOP)

        f2Buttons = Frame(f2, width=408, height=50, pady=15, relief=RIDGE)  # Buttons pady=10
        f2Buttons.pack(side=BOTTOM)

        f2Bottom = Frame(f2, width=408, height=50, bd=5, pady=15, relief=RIDGE)  # Buttons pady=10
        f2Bottom.pack(side=BOTTOM)

        f1Left = Frame(f1, width=450, height=610, bd=5, pady=12, relief=RIDGE)  # Frame For Tax, SubTotal and Total
        f1Left.pack(side=LEFT)

        title = Label(TitleFrame, font=('arial', 40, 'bold'), text='BUS TICKET BOOKING', width=20, justify='center')
        title.grid(row=0, column=0)

        ticket_preview = Label(f2Top, font=('arial', 18, 'bold'), text='TICKET PREVIEW', width=28, padx=4,justify='center')
        ticket_preview.grid(row=0, column=0)

        # ------------------------------------------------------------------------------------------------------------------------------------------#

        name_input = StringVar()
        email_input = StringVar()
        gender_input = StringVar()
        aadhar_input = StringVar()
        contact_input = StringVar()
        address_input = StringVar()
        class_input = StringVar()
        arrival_input = StringVar()
        dest_input = StringVar()
        seats_input = IntVar()
        arrival_entry = StringVar()
        dest_entry = StringVar()
        flag_mf = IntVar()
        var1 = IntVar()

        name_input.set('')
        email_input.set('')
        aadhar_input.set('')
        class_input.set('')
        arrival_input.set('')
        dest_input.set('')
        seats_input.set('')
        flag_mf.set(0)
        var1.set(0)

        # -----------------------------------------------------------PREVIEW----------------------------------------------------------------------- #
        name_p = Label(f2Bottom, font=('arial', 14, 'bold'), text="NAME", width=20, relief='sunken', justify='center')
        name_p.grid(row=2, column=0)
        name_pt = Label(f2Bottom, font=('arial', 14, 'bold'), width=20, relief='sunken', textvariable=name_input,justify='center')
        name_pt.grid(row=2, column=1)

        email_p = Label(f2Bottom, font=('arial', 14, 'bold'), text="EMAIL", width=20, relief='sunken', justify='center')
        email_p.grid(row=3, column=0)
        email_pt = Label(f2Bottom, font=('arial', 14, 'bold'), width=20, relief='sunken', textvariable=email_input,justify='center')
        email_pt.grid(row=3, column=1)

        gender_p = Label(f2Bottom, font=('arial', 14, 'bold'), text="GENDER", width=20, relief='sunken',justify='center')
        gender_p.grid(row=4, column=0)
        gender_pt = Label(f2Bottom, font=('arial', 14, 'bold'), width=20, relief='sunken', textvariable=gender_input,justify='center')
        gender_pt.grid(row=4, column=1)

        aadhar_p = Label(f2Bottom, font=('arial', 14, 'bold'), text="AADHAR", width=20, relief='sunken', justify='center')
        aadhar_p.grid(row=5, column=0)
        aadhar_pt = Label(f2Bottom, font=('arial', 14, 'bold'), width=20, relief='sunken', textvariable=aadhar_input,justify='center')
        aadhar_pt.grid(row=5, column=1)

        contact_p = Label(f2Bottom, font=('arial', 14, 'bold'), text="CONTACT", width=20, relief='sunken',justify='center')
        contact_p.grid(row=6, column=0)
        contact_pt = Label(f2Bottom, font=('arial', 14, 'bold'), width=20, relief='sunken', textvariable=contact_input,justify='center')
        contact_pt.grid(row=6, column=1)

        address_p = Label(f2Bottom, font=('arial', 14, 'bold'), text="AADHAR", width=20, relief='sunken',justify='center')
        address_p.grid(row=7, column=0)
        address_pt = Label(f2Bottom, font=('arial', 14, 'bold'), width=20, relief='sunken', textvariable=address_input,justify='center')
        address_pt.grid(row=7, column=1)

        class_p = Label(f2Bottom, font=('arial', 14, 'bold'), text="CLASS", width=20, relief='sunken', justify='center')
        class_p.grid(row=8, column=0)
        class_pt = Label(f2Bottom, font=('arial', 14, 'bold'), width=20, relief='sunken', textvariable=class_input,justify='center')
        class_pt.grid(row=8, column=1)

        arrival_p = Label(f2Bottom, font=('arial', 14, 'bold'), text="ARRIVAL", width=20, relief='sunken',justify='center')
        arrival_p.grid(row=9, column=0)
        arrival_pt = Label(f2Bottom, font=('arial', 14, 'bold'), width=20, relief='sunken', textvariable=arrival_input,justify='center')
        arrival_pt.grid(row=9, column=1)

        dest_p = Label(f2Bottom, font=('arial', 14, 'bold'), text="DESTINATION", width=20, relief='sunken', justify='center')
        dest_p.grid(row=10, column=0)
        dest_pt = Label(f2Bottom, font=('arial', 14, 'bold'), width=20, relief='sunken', textvariable=dest_input,justify='center')
        dest_pt.grid(row=10, column=1)

        seats_p = Label(f2Bottom, font=('arial', 14, 'bold'), text="SEATS", width=20, relief='sunken', justify='center')
        seats_p.grid(row=11, column=0)
        seats_pt = Label(f2Bottom, font=('arial', 14, 'bold'), width=20, relief='sunken', textvariable=seats_input,justify='center')
        seats_pt.grid(row=11, column=1)

        # ------------------------------------------SPACE---------------------------------------------------------------------------------#
        space = Label(f2Bottom, font=('arial', 14, 'bold'), width=20, height=1, relief='sunken', bg='light grey')
        space.grid(row=12, column=0)
        space = Label(f2Bottom, font=('arial', 14, 'bold'), width=20, height=1, relief='sunken', bg='light grey')
        space.grid(row=12, column=1)

        # -----------------------------------------INPUT---------------------------------------------------------------------------------#
        name_label = Label(f1Left, font=('arial', 14, 'bold'), text="NAME : ",width=15)
        name_label.grid(row=0, column=0)
        name_entry = Entry(f1Left, width=30)
        name_entry.grid(row=0, column=1)

        email_label = Label(f1Left, font=('arial', 14, 'bold'), text="EMAIL : ",width=10)
        email_label.grid(row=1, column=0)
        email_entry = Entry(f1Left, width=30)
        email_entry.grid(row=1, column=1)

        gender_label = Label(f1Left, font=('arial', 14, 'bold'), text="    GENDER :",bd=2).grid(row=2, column=0,sticky=W)
        Radiobutton(f1Left, font=('arial', 14, 'bold'), text="MALE", variable=flag_mf, value=1).grid(row=2,column=1, sticky=W)
        Radiobutton(f1Left, font=('arial', 14, 'bold'), text="FEMALE", variable=flag_mf, value=2).grid(row=2, column=2,sticky=W)

        aadhar_label = Label(f1Left, font=('arial', 14, 'bold'), text="AADHAR : ",width=10)
        aadhar_label.grid(row=3, column=0)
        aadhar_entry = Entry(f1Left, width=30)
        aadhar_entry.grid(row=3, column=1)

        contact_label = Label(f1Left, font=('arial', 14, 'bold'), text="CONTACT : ",width=10)
        contact_label.grid(row=4, column=0)
        contact_entry = Entry(f1Left, width=30)
        contact_entry.grid(row=4, column=1)

        add_label = Label(f1Left, font=('arial', 14, 'bold'), text="ADDRESS : ",width=10)
        add_label.grid(row=5, column=0)
        add_entry = Entry(f1Left, width=30)
        add_entry.grid(row=5, column=1)


        class_label = Label(f1Left, font=('arial', 14, 'bold'), text="     CLASS :", bd=8).grid(row=6, column=0)
        tick_standard = Radiobutton(f1Left, font=('arial', 14, 'bold'), text="STANDARD", variable=var1, value=1).grid(row=6, column=1,sticky=W)
        tick_economy = Radiobutton(f1Left, font=('arial', 14, 'bold'), text="ECONOMY", variable=var1, value=2).grid(row=7, column=1, sticky=W)
        tick_fclass = Radiobutton(f1Left, font=('arial', 14, 'bold'), text="FIRST CLASS", variable=var1,value=3).grid(row=8, column=1,sticky=W)

        arrival_label = Label(f1Left,font=('arial', 14, 'bold'),text="     ARRIVAL :", bd=8).grid(row=9, column=0, sticky=W)
        arrival_dropdown = ttk.Combobox(f1Left, textvariable= arrival_entry, font=('arial', 14, 'bold'), state='readonly',width=20)
        arrival_dropdown['value'] = (' ', 'Jamshedpur', 'Ahmedabad', 'Jaipur', 'Bangalore')
        arrival_dropdown.current(0)
        arrival_dropdown.grid(row=9, column=1)

        dest_label = Label(f1Left, font=('arial', 14, 'bold'), text="     DESTINATION :", bd=8).grid(row=10, column=0,sticky=W)
        dest_dropdown = ttk.Combobox(f1Left, textvariable = dest_entry, font=('arial', 14, 'bold'), state='readonly',width=20)
        dest_dropdown['value'] = (' ', 'Kanpur', 'Vizag', 'Varanasi', 'Aurangabad')
        dest_dropdown.current(0)
        dest_dropdown.grid(row=10,column=1)

        seats_label = Label(f1Left, font=('arial', 14, 'bold'), text="SEATS : ", width=10)
        seats_label.grid(row=11, column=0)
        seats_entry = Entry(f1Left, width=30)
        seats_entry.grid(row=11, column=1)

        seats_count_label = Label(f1Left, font=('arial', 14, 'bold'), text="SEATS AVAILABLE : ", width=18)
        seats_count_label.grid(row=12, column=0)
        seats_count = Label(f1Left, font=('arial', 14, 'bold'), text=str(Reservation.total_seats), width=10)
        seats_count.grid(row=12, column=1)

        # ------------------------------------------------------FUNCTIONS---------------------------------------------------------------------------#
        data = []

        def exit_app():
            exit_ = tkinter.messagebox.askyesno("Bus Ticketing System", "Confirm if you want to exit")
            if exit_ > 0:
                cursor.close()
                db.close()
                root.destroy()
                return

        def check_name(name):
            s = name.replace(' ','')
            return s.isalpha()

        def check_email(email):
            regex = '\S+@\S+'
            return re.search(regex,email)

        def check_aadhar(aadhar):
           return aadhar.isdigit() and len(aadhar) == 12

        def check_contact(contact):
            return  contact.isdigit() and len(contact) == 10


        def preview_app():
            data.clear()
            Reservation.flag = True

            name = name_entry.get()
            email = email_entry.get()
            aadhar = aadhar_entry.get()
            contact = contact_entry.get()
            address = add_entry.get()
            Reservation.seats = seats_entry.get()
            class_ = str()
            gender = str()
            arrival = arrival_entry.get()
            dest = dest_entry.get()

            # get gender
            if flag_mf.get() == 1:
                gender = "Male"
            elif flag_mf.get() == 2:
                gender = "Female"

            if var1.get() == 1:
                class_ = "Standard"
            elif var1.get() == 2:
                class_ = "Economy"
            elif var1.get() == 3:
                class_ = "First Class"

            warning = ''
            if not check_name(name):
                warning += 'Invalid Name\n'
            if not  check_email(email):
                warning += 'Invalid Email\n'
            if not check_aadhar(aadhar):
                warning += 'Invalid Aadhar\n'
            if not check_contact(contact):
                warning += 'Invalid Contact\n'
            if len(gender) == 0:
                warning += 'Not selected Gender\n'
            if len(class_) == 0:
                warning += 'Not selected Class\n'
            if len(arrival) == 1:
                warning += 'Not selected Arrival\n'
            if len(dest) == 1:
                warning += 'Not selected Destination\n'
            if Reservation.seats == '':
                warning += 'Not specified seats\n'
            if len(warning) != 0:
                tkinter.messagebox.showerror("Error", warning)
                return

            # get seats
            if Reservation.total_seats <= int(Reservation.seats):
                tkinter.messagebox.showerror("Error", "Not enough seats!")
                return

            name_input.set(name)
            email_input.set(email)
            gender_input.set(gender)
            aadhar_input.set(aadhar)
            contact_input.set(contact)
            address_input.set(address)
            class_input.set(class_)
            seats_input.set(Reservation.seats)
            arrival_input.set(arrival)
            dest_input.set(dest)

            l = [name, email, gender, aadhar, contact, address, class_, arrival, dest, int(Reservation.seats)]
            data.extend(l)
            print(data)
            cursor.execute('insert into tickets values(?,?,?,?,?,?,?,?,?,?)', data)
            db.commit()
            seats_count = Label(f1Left, font=('arial', 14, 'bold'), text=str(Reservation.total_seats), width=10)
            seats_count.grid(row=12, column=1)

        def book_send_mail():
            if Reservation.flag:

                if Reservation.total_seats >= int(Reservation.seats):
                    Reservation.total_seats = Reservation.total_seats - int(Reservation.seats)
                else:
                    tkinter.messagebox.showerror("Error", "Not enough seats!")
                    return

                message = MIMEMultipart()
                message["Subject"] = "Booking Confirmation: Ticket"
                message["From"] = "Railways"

                # username and password
                username = 'dummy.org.123@gmail.com'
                password = 'dummy@123'
                print("in book mail: ", data)
                receiver = data[1]

                body = '''
                <h1> BOOKING CONFIRMATION  <h1>
                <h2> TICKET DETAILS  </h2>
                <p> Name : ''' + data[0] + '''  </p>
                <p> Gender : ''' + data[2] + '''  </p>
                <p> Aadhar : ''' + data[3] + '''  </p>
                <p> Contact Info : ''' + data[4] + '''  </p>
                <p> Address : ''' + data[5] + '''  </p>
                <p> Class : ''' + data[6] + '''  </p>
                <p> Arrival : ''' + data[7] + '''  </p>
                <p> Destination : ''' + data[8] + '''  </p>
                <p> Seats booked : ''' + str(data[9]) + '''  </p>

                <h2> Wish You Safe And Happy Travels !!! <h2>
                '''
                seats_count = Label(f1Left, font=('arial', 14, 'bold'), text=str(Reservation.total_seats), width=10)
                seats_count.grid(row=12, column=1)

                txt = MIMEText(body, 'html')
                message.attach(txt)

                server = smtplib.SMTP("smtp.gmail.com", "587")
                server.starttls()
                print("Connected")

                server.login(username, password)
                print("Login Successfull")

                server.sendmail(username, receiver, message.as_string())
                print("Mail sent successfully")

                tkinter.messagebox.showinfo("", "Mail Sent Successfully !")

                cursor.execute('select * from tickets')
                print(cursor.fetchall())
                file = open("tickets_info.csv",'a+')
                obj = csv.writer(file)
                obj.writerow(data)

                file.close()
                print(data)
                data.clear()
            else:
                tkinter.messagebox.showerror("Error", "Must Preview Before Booking !")
                return

        # -----------------------------------------BUTTON---------------------------------------------------------------------------------#
        btn_book = Button(f2Buttons, font=('arial', 14, 'bold'), text='BOOK AND SEND', width=18, height=1, padx=2, pady=6, bd=2, command= lambda: book_send_mail())
        btn_book.grid(row=13, column=0)

        btn_preview = Button(f2Buttons, font=('arial', 14, 'bold'), text='PREVIEW', width=8, height=1, padx=2, pady=6, bd=2, command= lambda: preview_app())
        btn_preview.grid(row=13, column=1)

        btn_exit = Button(f2Buttons, font=('arial', 14, 'bold'), text='EXIT', width=8, height=1, padx=2, pady=6, bd=2, command=lambda: exit_app())
        btn_exit.grid(row=13, column=3)


if __name__ == '__main__':
    root = Tk()
    application = Reservation(root)
    root.mainloop()
