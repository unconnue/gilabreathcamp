from Tkinter import *
import tkMessageBox
from controller.camper import Camper
from controller.camp import Camp
from controller.bunkhouse import Bunkhouse
from controller.team import Team

top = None
slepping_bag_CheckVar = None
pillow_CheckVar = None
blanket_CheckVar = None
spray_CheckVar = None
bathing_suit_CheckVar = None
sun_block_CheckVar = None
rain_coat_CheckVar = None
flashlight_CheckVar = None
camper_id_tb = None
camp_id_tb = None

def check_in_bt_handler():
    
    try:
        camper_id = int(camper_id_tb.get())
        camp_id = int(camp_id_tb.get())
    except:
        tkMessageBox.showinfo(title="message",message="camper and camp id must be nubmers")
        return
    checked_in_camper = Camper(camper_id)
    checked_in_camp = Camp(camp_id)
    if checked_in_camper.select_camper() == None:
        tkMessageBox.showinfo(title="message",message="camper not found")
        return
    if checked_in_camp.select_camp() == None:
        tkMessageBox.showinfo(title="message",message="camp not found")
        return
    #check if this camper is regestered in this camp
    data = Bunkhouse.select_camp_team_bunkhouse(camper_id)
    if not str(camp_id) in data[0]:
        tkMessageBox.showinfo(title="message",message="Sorry, You need to register in this camp before Check-in.")
        return
    
    str_buffer = ""
    if slepping_bag_CheckVar.get() == 0:
        str_buffer += "Slepping Bag, "
    if pillow_CheckVar.get() == 0:
        str_buffer += "Pillow, "
    if blanket_CheckVar.get() == 0:
        str_buffer += "Blanket, "
    if spray_CheckVar.get() == 0:
        str_buffer += "Insect Repellent Spray, "
    if bathing_suit_CheckVar.get() == 0:
        str_buffer += "Bathing Suit, "
    if sun_block_CheckVar.get() == 0:
        str_buffer += "Sun Blocking Lotion, "
    if rain_coat_CheckVar.get() == 0:
        str_buffer += "Raincoat, "
    if flashlight_CheckVar.get() == 0:
        str_buffer += "Flashlight, "
    if str_buffer != "":
        f = open("checkin.txt", 'w')
        f.write("Please bring in (" + str_buffer[:-2] + ")")
        f.close()
        import webbrowser
        webbrowser.open("checkin.txt")
        return
    
    Camp.camper_check_in(camper_id, camp_id)
    tkMessageBox.showinfo(title="message",message="you have checked_in")
    cancel_check_in_bt_handler()

def cancel_check_in_bt_handler():
    top.destroy()

def slepping_bag_CheckButton_handler():
    global slepping_bag_CheckVar
    if slepping_bag_CheckVar.get() == 0:
        slepping_bag_CheckVar.set(1)
    else:
        slepping_bag_CheckVar.set(0)

def pillow_CheckButton_handler():
    global pillow_CheckVar
    if pillow_CheckVar.get() == 0:
        pillow_CheckVar.set(1)
    else:
        pillow_CheckVar.set(0)

def blanket_CheckButton_handler():
    global blanket_CheckVar
    if blanket_CheckVar.get() == 0:
        blanket_CheckVar.set(1)
    else:
        blanket_CheckVar.set(0)

def spray_CheckButton_handler():
    global spray_CheckVar
    if spray_CheckVar.get() == 0:
        spray_CheckVar.set(1)
    else:
        spray_CheckVar.set(0)

def bathing_suit_CheckButton_handler():
    global bathing_suit_CheckVar
    if bathing_suit_CheckVar.get() == 0:
        bathing_suit_CheckVar.set(1)
    else:
        bathing_suit_CheckVar.set(0)

def sun_block_CheckButton_handler():
    global sun_block_CheckVar
    if sun_block_CheckVar.get() == 0:
        sun_block_CheckVar.set(1)
    else:
        sun_block_CheckVar.set(0)

def rain_coat_CheckButton_handler():
    global rain_coat_CheckVar
    if rain_coat_CheckVar.get() == 0:
        rain_coat_CheckVar.set(1)
    else:
        rain_coat_CheckVar.set(0)

def flashlight_CheckButton_handler():
    global flashlight_CheckVar
    if flashlight_CheckVar.get() == 0:
        flashlight_CheckVar.set(1)
    else:
        flashlight_CheckVar.set(0)

def start_check_in_forum():
    global top, slepping_bag_CheckVar, pillow_CheckVar, blanket_CheckVar, spray_CheckVar, bathing_suit_CheckVar, sun_block_CheckVar, rain_coat_CheckVar, flashlight_CheckVar
    global camper_id_tb, camp_id_tb

    top = Tk()
    top.title("Check-in Forum")
    top.minsize(width=400, height=400)

    slepping_bag_CheckVar = IntVar()
    pillow_CheckVar = IntVar()
    blanket_CheckVar = IntVar()
    spray_CheckVar = IntVar()
    bathing_suit_CheckVar = IntVar()
    sun_block_CheckVar = IntVar()
    rain_coat_CheckVar = IntVar()
    flashlight_CheckVar = IntVar()

    slepping_bag_CheckButton = Checkbutton(top, text = "Slepping Bag", variable  = slepping_bag_CheckVar, height=2, width = 20, command = slepping_bag_CheckButton_handler)
    pillow_CheckButton = Checkbutton(top, text = "Pillow", variable = pillow_CheckVar, height=2, width = 20, command = pillow_CheckButton_handler)
    blanket_CheckButton = Checkbutton(top, text = "Blanket", variable = blanket_CheckVar, height=2, width = 20, command = blanket_CheckButton_handler)
    spray_CheckButton = Checkbutton(top, text = "Insect Repellent Spray", variable = spray_CheckVar, height=2, width = 20, command = spray_CheckButton_handler)
    bathing_suit_CheckButton = Checkbutton(top, text = "Bathing Suit", variable = bathing_suit_CheckVar, height=2, width = 20, command = bathing_suit_CheckButton_handler)
    sun_block_CheckButton = Checkbutton(top, text = "Sun Blocking Lotion", variable = sun_block_CheckVar, height=2, width = 20, command = sun_block_CheckButton_handler)
    rain_coat_CheckButton = Checkbutton(top, text = "Raincoat", variable = rain_coat_CheckVar, height=2, width = 20, command = rain_coat_CheckButton_handler)
    flashlight_CheckButton = Checkbutton(top, text = "Flashlight", variable = flashlight_CheckVar, height=2, width = 20, command = flashlight_CheckButton_handler)

    check_in_bt = Button(top, text="Check-in Camper", width=30, command = check_in_bt_handler)
    cancel_check_in_bt = Button(top, text="Cancel", width=30, command = cancel_check_in_bt_handler)

    camper_id_label = Label(top, text = "Enter camper ID")
    camper_id_tb = Entry(top, width=20)
    camp_id_label = Label(top, text = "Enter Camp ID")
    camp_id_tb = Entry(top, width=20)

    camper_id_label.pack()
    camper_id_tb.pack(expand=True)
    camp_id_label.pack()
    camp_id_tb.pack(expand=True)
    
    slepping_bag_CheckButton.pack(expand=True)
    pillow_CheckButton.pack(expand=True)
    blanket_CheckButton.pack(expand=True)
    spray_CheckButton.pack(expand=True)
    bathing_suit_CheckButton.pack(expand=True)
    sun_block_CheckButton.pack(expand=True)
    rain_coat_CheckButton.pack(expand=True)
    flashlight_CheckButton.pack(expand=True)
    check_in_bt.pack(expand=True)
    cancel_check_in_bt.pack(expand=True)

    top.mainloop()
