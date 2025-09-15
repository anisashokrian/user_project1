from tkinter import *
import tkinter.messagebox as msg
from data_access.database_manager import save_user
from tools.validation import *


def save_button():
    try:
        user_name_validator(user_name.get())
        password_validator(password.get())
        nick_name_validator(nick_name.get())
        save_user(user_name.get(), password.get(),nick_name.get(),locked.get())
        msg.showinfo("saved",f"person saved")
        user_name.set("")
        password.set("")
        nick_name.set("")
    except Exception as e:
        msg.showerror("error",f"{e}")


window = Tk()


window.title("user:")
window.geometry("500x300")
#User_name

user_name = StringVar()
user_name.get()
Label(window, text= "User_name", bg="pink",fg="black",font=("LucidaConsole", 10)).place(x=20, y=20)
Entry(window, textvariable=user_name ).place(x=100, y=20)
#Password
password = StringVar()
Label(window, text= "Password", bg="pink",fg="black",font=("LucidaConsole", 10)).place(x=20, y=60)
Entry(window, show="*", textvariable=password).place(x=100, y=60)
#Nick_name
nick_name = StringVar()
Label(window, text= "Nick_name", bg="pink",fg="black",font=("LucidaConsole", 10)).place(x=20, y=100)
Entry(window,textvariable=nick_name).place(x=100, y=100)
#Locked
locked = BooleanVar()
Label(window, text="locked").place(x=20, y=140)
Checkbutton(window, variable=locked).place(x=100, y=140)
#save
Button(window, text="Save", width= 15, command=save_button).place(x=70, y=200)

person_list= []
#save_butten



window.mainloop()