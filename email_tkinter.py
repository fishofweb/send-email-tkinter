from tkinter import *
import tkinter.messagebox as tmsg
import smtplib
from tkinter import messagebox  


conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
root = Tk()
root.geometry("400x400")
root.title("send email")


def send_email():
    sendr = sender.get()
    recievr = reciever.get()
    passw_ = passw.get()
    subjct = subject.get()
    body = message.get("1.0",END)
    msg = f'Subject:{subjct}\n\n{body}'
    conn.login(sendr, passw_)
    conn.sendmail(sendr,recievr,msg)
    
    conn.quit()
    messagebox.showinfo("confirm","Email sent ")  





Label(root, text="Sender Email", font="comicsansms 13 bold").pack()
sender = Entry(root, width=30)
sender.pack()

Label(root, text="Reciever Email", font="comicsansms 13 bold").pack()
reciever = Entry(root,  width=30)
reciever.pack()

Label(root, text="Password", font="comicsansms 13 bold").pack()
passw = Entry(root , width=30)
passw.pack()

Label(root, text="Subject", font="comicsansms 13 bold").pack()
subject = Entry(root , width=30)
subject.pack()

Label(root, text="Message", font="comicsansms 13 bold").pack()

message = Text(root, height= 10, width=50)

message.pack()

send = Button(root, text = "send", command= send_email)
send.pack()


root.mainloop()