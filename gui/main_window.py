from Tkinter import *
import tkMessageBox

root = None

def camper_window_bt_handler():
    from camper_window import start_camper_window
    start_camper_window()

def camp_window_bt_handler():
    from camp_window import start_camp_window
    start_camp_window()

def payment_window_bt_handler():
    from payment_window import start_payment_window
    start_payment_window()

def check_in_bt_handler():
    from check_in_forum import start_check_in_forum
    start_check_in_forum()

def bunkhouse_bt_handler():
    from gui.bunkhouse_forum import start_bunkhouse_forum
    start_bunkhouse_forum()

def team_bt_handler():
    from gui.team_forum import start_team_forum
    start_team_forum()

def modify_bunkhouse_team_capacity_handler():
    from modify_bunkhouse_team import modify_bunkhouse_team_start
    modify_bunkhouse_team_start()

def assign_to_camp_bt_handler():
    from gui.assign_to_camp import start_assign_to_camp
    start_assign_to_camp()

def start_main_window():
    global root
    root = Tk()
    root.title("Main Window(Clerk)")
    root.minsize(width=400, height=500)

    camper_window_bt = Button(root, text="Camper", width=30, command = camper_window_bt_handler)
    camper_window_bt.pack(expand=True)

    camp_window_bt = Button(root, text="Camp", width=30, command = camp_window_bt_handler)
    camp_window_bt.pack(expand=True)

    payment_window_bt = Button(root, text="Payments", width=30, command = payment_window_bt_handler)
    payment_window_bt.pack(expand=True)

    bunkhouse_bt = Button(root, text="Bunkhouses", width=30, command = bunkhouse_bt_handler)
    bunkhouse_bt.pack(expand=True)

    team_bt = Button(root, text="Teams", width=30, command = team_bt_handler)
    team_bt.pack(expand=True)

    check_in_bt = Button(root, text="Check-in Forum", width=30, command = check_in_bt_handler)
    check_in_bt.pack(expand=True)

    assign_to_camp_bt = Button(root, text="Register Camper to Camp", width=30, command = assign_to_camp_bt_handler)
    assign_to_camp_bt.pack(expand=True)

    exit_main_bt = Button(root, text="Exit", width=30, command = exit)
    exit_main_bt.pack(expand=True)

    root.mainloop()

def start_main_window_admin():
    global root
    root = Tk()
    root.title("Main Window(Admin)")
    root.minsize(width=400, height=500)

    camper_window_bt = Button(root, text="Camper", width=30, command = camper_window_bt_handler)
    camper_window_bt.pack(expand=True)

    camp_window_bt = Button(root, text="Camp", width=30, command = camp_window_bt_handler)
    camp_window_bt.pack(expand=True)

    payment_window_bt = Button(root, text="Payments", width=30, command = payment_window_bt_handler)
    payment_window_bt.pack(expand=True)

    bunkhouse_bt = Button(root, text="Bunkhouses", width=30, command = bunkhouse_bt_handler)
    bunkhouse_bt.pack(expand=True)

    team_bt = Button(root, text="Teams", width=30, command = team_bt_handler)
    team_bt.pack(expand=True)

    check_in_bt = Button(root, text="Check-in Forum", width=30, command = check_in_bt_handler)
    check_in_bt.pack(expand=True)

    assign_to_camp_bt = Button(root, text="Register Camper to Camp", width=30, command = assign_to_camp_bt_handler)
    assign_to_camp_bt.pack(expand=True)

    #label,entry,button,button
    modify_bunkhouse_team_capacity = Button(root, text="Modify Capacity", width=30, command = modify_bunkhouse_team_capacity_handler)
    modify_bunkhouse_team_capacity.pack(expand=True)

    exit_main_bt = Button(root, text="Exit", width=30, command = exit)
    exit_main_bt.pack(expand=True)

    root.mainloop()
