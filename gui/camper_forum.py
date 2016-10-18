from Tkinter import *
from controller.camper import Camper
import tkMessageBox
from datetime import date, datetime


root = None
name1_label = None
name1_tb = None
name2_label = None
name2_tb = None
date_of_birth_label = None
date_of_birth_tb = None
gender_label = None
gender_lb = None
address_label = None
address_lb = None
camper_id_global = 0

def is_valid_date(s):
    """
    take a string and check if this string follows this format(YYYY-MM-DD) or not, return bool
    """
    lst = s.split("-")
    if len(lst) != 3 or len(lst[0]) != 4 or len(lst[1]) != 2 or len(lst[2]) != 2:
        return False
    try:
        year = int(lst[0])
        month = int(lst[1])
        day = int(lst[2])
    except:
        return False
    return True

def validate_age_9_18(birth_date):
    tmp_lst = birth_date.split('-')
    date_of_birth = date(int(tmp_lst[0]), int(tmp_lst[1]), int(tmp_lst[2]))
    now = datetime.now()
    date_now = date(now.year, now.month, now.day)
    camper_age = (date_now - date_of_birth).days / 365
    return camper_age > 9 and camper_age < 18



def update_camper_bt_handler():
    try:
        x = gender_lb.get(gender_lb.curselection())
    except:
        tkMessageBox.showinfo(title="message",message="Gender is required.")
        return
    if name1_tb.get() == '':
        tkMessageBox.showinfo(title="message",message="First Name is required.")
    elif name2_tb.get() == '':
        tkMessageBox.showinfo(title="message",message="Last Name is required.")
    elif gender_lb.get(gender_lb.curselection()) == '':
        tkMessageBox.showinfo(title="message",message="Gender is required.")
    elif not is_valid_date(date_of_birth_tb.get()):
        tkMessageBox.showinfo(title="message",message="wrong date of birth.")
    elif not validate_age_9_18(date_of_birth_tb.get()):
        tkMessageBox.showinfo(title="message",message="Camper age must be between 9-18")
    else:
        tmp_camper = Camper(camper_id_global, name1_tb.get(), name2_tb.get(), date_of_birth_tb.get(), gender_lb.get(gender_lb.curselection()), address_lb.get())
        tmp_camper.update_camper()
        tkMessageBox.showinfo(title="message",message="record updated")
        cancel_camper_bt_handler()

def cancel_camper_bt_handler():
    global root
    #root.grab_release()
    root.destroy()

def submit_camper_bt_handler():
    try:
        x = gender_lb.get(gender_lb.curselection())
    except:
        tkMessageBox.showinfo(title="message",message="Gender is required.")
        return
    if name1_tb.get() == '':
        tkMessageBox.showinfo(title="message",message="First Name is required.")
    elif name2_tb.get() == '':
        tkMessageBox.showinfo(title="message",message="Last Name is required.")
    elif gender_lb.get(gender_lb.curselection()) == '':
        tkMessageBox.showinfo(title="message",message="Gender is required.")
    elif not is_valid_date(date_of_birth_tb.get()):
        tkMessageBox.showinfo(title="message",message="wrong date of birth.")
    elif not validate_age_9_18(date_of_birth_tb.get()):
        tkMessageBox.showinfo(title="message",message="Camper age must be between 9-18")
    else:
        tmp_camper = Camper(0, name1_tb.get(), name2_tb.get(), date_of_birth_tb.get(), gender_lb.get(gender_lb.curselection()), address_lb.get())
        tmp_camper.insert_camper()
        tkMessageBox.showinfo(title="message",message="record inserted")
        cancel_camper_bt_handler()

def init_camper_forum():
    global root, name1_label, name1_tb, name2_label, name2_tb, date_of_birth_label, date_of_birth_tb, gender_label, gender_lb, address_lb, address_label
    root = Tk()
    root.title("Add Camper")
    root.minsize(width=400, height=400)
    name1_label = Label(root, text = "First Name")
    name1_tb = Entry(root, width=20)
    name2_label = Label(root, text = "Last Name")
    name2_tb = Entry(root, width=20)
    date_of_birth_label = Label(root, text = "Date of Birth format(YYYY-MM-DD)")
    date_of_birth_tb = Entry(root, width=20)
    gender_label = Label(root, text = "Gender")
    gender_lb = Listbox(root, height=2, width=10)
    address_label = Label(root, text = "Address")
    address_lb = Entry(root, width=20)
    gender_lb.insert(1, "Male")
    gender_lb.insert(2, "Female")

def pack_elements():
    name1_label.pack()
    name1_tb.pack(expand=True)
    name2_label.pack()
    name2_tb.pack(expand=True)
    date_of_birth_label.pack()
    date_of_birth_tb.pack(expand=True)
    gender_label.pack()
    gender_lb.pack(expand=True)
    address_label.pack()
    address_lb.pack(expand=True)

def start_camper_forum():
    global root
    init_camper_forum()
    pack_elements()
    submit_camper = Button(root, text="submit", width=30, command = submit_camper_bt_handler)
    submit_camper.pack(expand=True)
    cancel_camper_bt = Button(root, text="Cancel", width=30, command = cancel_camper_bt_handler)
    cancel_camper_bt.pack(expand=True)
    root.mainloop()

def update_camper(camper_id):
    global root
    global name1_tb
    global name2_tb
    global date_of_birth_tb
    global gender_lb
    global camper_id_global, address_lb
    camper_id_global = camper_id
    current_camper = Camper(camper_id)
    data = current_camper.select_camper()
    if data == None:
        tkMessageBox.showinfo(title="message",message="Camper Not Found")
        return
    init_camper_forum()
    #init text boxes with data
    name1_tb.delete(0,END)
    name1_tb.insert(0, data[0])
    name2_tb.delete(0,END)
    name2_tb.insert(0, data[1])
    date_of_birth_tb.delete(0,END)
    date_of_birth_tb.insert(0, data[2])
    tmp = 0
    if data[3] == "Female":
        tmp =  1
    gender_lb.select_set(tmp)
    address_lb.delete(0,END)
    address_lb.insert(0, data[4])
    pack_elements()
    submit_camper = Button(root, text="update", width=30, command = update_camper_bt_handler)
    submit_camper.pack(expand=True)
    cancel_camper_bt = Button(root, text="Cancel", width=30, command = cancel_camper_bt_handler)
    cancel_camper_bt.pack(expand=True)
    root.mainloop()
