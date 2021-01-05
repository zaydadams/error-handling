from tkinter import *
from tkinter import messagebox as mb


root = Tk()
root.title("Authentication")
root.geometry("450x300")
root.config(bg="grey")


def gui():
    window = Tk()
    window.title("Exception handling")
    window.geometry("450x300")
    window.configure(bg="grey")

    amnt_lab = Label(window, text="Enter the amount in your account:")
    amnt_entry = Entry(window)
    amnt_lab.place(x=5, y=5)
    amnt_entry.place(x=5, y=30)

    def shw_amnt():
        if int(amnt_entry.get()) < 3000:
            mb.showerror("Message", "Please deposit more funds for this excursion.")
        if int(amnt_entry.get()) >= 3000:
            mb.showinfo("Message", "Congratulations. You qualify for the trip to Malaysia!!")

    amnt_btn = Button(window, text="check amount", command=shw_amnt)
    amnt_btn.place(x=50, y=60)

    window.mainloop()


user_lab = Label(root, text="Username:")
user_lab.place(x=190, y=30)

user_entry = Entry(root)
user_entry.place(x=150, y=50)

pass_lab = Label(root, text="Password:")
pass_entry = Entry(root, show="*")

pass_entry.place(x=150, y=110)
pass_lab.place(x=199, y=80)

log_btn = Button(root, text="Login", bg="pink", command=gui)
log_btn.place(x=200, y=150)

lab1 = Label(root, text="Please enter login details")
lab1.place(x=139, y=1)

root.mainloop()
