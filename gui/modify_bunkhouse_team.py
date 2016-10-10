from Tkinter import *
import tkMessageBox
from controller.bunkhouse import Bunkhouse
from controller.team import Team

root = None
teams_capacity_tb = None
bunkhouses_capacity_tb = None

def update_bt_handler():
    try:
        teams_capacity = int(teams_capacity_tb.get())
        bunkhouses_capacity = int(bunkhouses_capacity_tb.get())
    except:
        tkMessageBox.showinfo(title="message",message="Teams and Bunkhouses Capacity must be numbers")
        return
    else:
        Bunkhouse.update_bunkhouses_num(bunkhouses_capacity)
        Team.update_teams_num(teams_capacity)
        cancel_bt_handler()

def cancel_bt_handler():
    root.destroy()

def modify_bunkhouse_team_start():
    global root, teams_capacity_tb, bunkhouses_capacity_tb
    root = Tk()
    root.title("modify bunkhouse team Capacity")
    root.minsize(width=400, height=400)

    teams_capacity_label = Label(root, text = "Teams Capacity")
    teams_capacity_label.pack()

    teams_capacity_tb = Entry(root, width=20)
    teams_capacity_tb.pack(expand=True)

    bunkhouses_capacity_label = Label(root, text = "Bunkhouses Capacity")
    bunkhouses_capacity_label.pack()

    bunkhouses_capacity_tb = Entry(root, width=20)
    bunkhouses_capacity_tb.pack(expand=True)

    update_bt = Button(root, text="Update", width=30, command = update_bt_handler)
    update_bt.pack(expand=True)

    cancel_bt = Button(root, text="Cancel", width=30, command = cancel_bt_handler)
    cancel_bt.pack(expand=True)

    root.mainloop()
