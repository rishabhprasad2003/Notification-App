from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from plyer import notification
import time

t = Tk()
t.geometry('500x300')

# notifier app logo
im = Image.open('notifier_1.png')
tkimage = ImageTk.PhotoImage(im)
img_label = Label(t, image=tkimage).grid()

def button_click():
    get_title = e1.get()
    get_msg = e2.get()
    get_time = e3.get()

    if (get_msg == '') or (get_time == '') or (get_title == ''):
        messagebox.showwarning("WARNING!!", "Enter the values!")

    else:
        int_time = int(float(get_time))
        min_to_sec = int_time*60

        messagebox.showinfo("Notification", "Notifier set!!!")
        t.destroy()
        time.sleep(min_to_sec)

        notification.notify(
            title = get_title,
            message = get_msg,
            timeout = 10,
            app_icon = 'bell_icon_file.ico'
        )

#Label1
label1 = Label(t, text="Title to Notify")
label1.place(x=12,y=110)
#Entry 1
e1 = Entry(t, width=40)
e1.place(x=120,y=110)

#Label2
label2 = Label(t, text="Display Message")
label2.place(x=12,y=150)
#Entry2
e2 = Entry(t, width=60)
e2.place(x=120,y=150)

#Label3
label3 = Label(t, text="Set Time")
label3.place(x=12,y=190)
minlabel = Label(t, text="min").place(x=190,y=190)
#Entry3
e3 = Entry(t, width=10)
e3.place(x=120,y=190)

#Button
button = Button(t, text="SET NOTIFICATION",bg='blue',fg='white', command=button_click)
button.place(x=150,y=220)

t.mainloop()