from tkinter import * 
from tkinter import ttk

demo = Tk()
demo.geometry("400x400")
#images
quest_IMG = PhotoImage(file = "images/quest.png")
#canvas
canvas = Canvas(demo, width=400, height=400)
#font
font1 = ("Book Antiqua", 20, "bold")
font2 = ("Blackadder ITC", 35, "bold")

#global variables for display
name_label = Label(canvas, text="Please enter your name, traveller:", font=font1, height=8)
name_entry = Entry(canvas, bd=8, width=80)
strength_bar = Scale(demo, from_=0, to=100, orient=HORIZONTAL, width=40, length=1000, label="Strength", font=font1)
agility_bar = Scale(demo, from_=0, to=100, orient=HORIZONTAL, width=40, length=1000, label="Agility", font=font1)
dexterity_bar = Scale(demo, from_=0, to=100, orient=HORIZONTAL, width=40, length=1000, label="Dexterity", font=font1)
load_bar = ttk.Progressbar(mode="indeterminate")

#global data for user info
class player:
    def __init__(self, name="None", c_class="None", strength_stat=0, agility_stat=0, dexterity_stat=0):
        self.name = name
        self.c_class = c_class
        self.strength_stat = strength_stat
        self.agility_stat = agility_stat
        self.dexterity_stat = dexterity_stat

user = player()
name = "NA"
char_class = "NA"
strength = 0
agility = 0
dexterity = 0

#functions
def clear_canvas():
    canvas.delete('all')

def destroy_form():
    name_label.destroy()
    name_entry.destroy()

def destroy_scale():
    strength_bar.destroy()
    agility_bar.destroy()
    dexterity_bar.destroy()

def destroy_load_bar():
    load_bar.destroy()

def opening_title():
    canvas.pack(fill="both", expand=True)
    #canvas.create_image(0, 0, image=quest_IMG, anchor="nw")
    canvas.create_window(700, 400, anchor = "nw", window = button1) 

def enter_name():
    global name_entry, name_label
    clear_canvas()
    #canvas.create_image(0, 0, image=quest_IMG, anchor="nw")
    name_label.pack()
    name_entry.pack()
    canvas.create_window(700, 400, anchor = "nw", window = button2) 

def greetings():
    user.name = name_entry.get()
    destroy_form()
    clear_canvas()
    #canvas.create_image(0, 0, image=quest_IMG, anchor="nw")
    canvas.create_text(770, 250, text="Welcome,", font=font1)
    canvas.create_text(770, 300, text=user.name, font=font1)
    canvas.create_window(700, 400, anchor = "nw", window = button3)

def character_class():
    clear_canvas()
    #canvas.create_image(0, 0, image=quest_IMG, anchor="nw")
    canvas.create_text(750, 100, text="Please pick a character class", font=font1)
    canvas.create_window(200, 700, anchor = "nw", window = button4)
    canvas.create_window(600, 700, anchor = "nw", window = button5)
    canvas.create_window(900, 700, anchor = "nw", window = button6)
    canvas.create_window(1230, 700, anchor = "nw", window = button7)

def paladin():
    user.c_class = "Paladin"
    clear_canvas()
    #canvas.create_image(0, 0, image=quest_IMG, anchor="nw")
    character_class_widget()

def ranger():
    user.c_class = "Ranger"
    clear_canvas()
    #canvas.create_image(0, 0, image=quest_IMG, anchor="nw")
    character_class_widget()

def warlock():
    user.c_class = "Warlock"
    clear_canvas()
    #canvas.create_image(0, 0, image=quest_IMG, anchor="nw")
    character_class_widget()

def bard():
    user.c_class = "Bard"
    clear_canvas()
    #canvas.create_image(0, 0, image=quest_IMG, anchor="nw")
    character_class_widget()

def character_class_widget():
    canvas.create_text(770, 250, text="You have chosen", font=font1)
    canvas.create_text(770, 320, text=user.c_class, font=font2)
    canvas.create_window(700, 400, anchor = "nw", window = button8)

def stats():
    clear_canvas()
    #canvas.create_image(0, 0, image=quest_IMG, anchor="nw")
    canvas.create_text(770, 100, text="Please adjust your character stats", font=font1)
    canvas.create_window(700, 400, anchor = "nw", window = button9)
    strength_bar.pack(anchor = CENTER)
    agility_bar.pack()
    dexterity_bar.pack()

def show_stats():
    user.strength_stat = strength_bar.get()
    user.agility_stat = agility_bar.get()
    user.dexterity_stat = dexterity_bar.get()
    destroy_scale()
    clear_canvas()
    canvas.create_text(770, 50, text="-Character Stats-", font=font1)
    canvas.create_text(770, 150, text="Strength: " + str(user.strength_stat), font=font1)
    canvas.create_text(770, 250, text="Agility: " + str(user.agility_stat), font=font1)
    canvas.create_text(770, 350, text="Dexterity: " + str(user.dexterity_stat), font=font1)
    canvas.create_window(700, 400, anchor = "nw", window = button12)

def start_quest():
    clear_canvas()
    #canvas.create_image(0, 0, image=quest_IMG, anchor="nw")
    canvas.create_text(800, 300, text="Character design complete...", font=font1)
    canvas.create_window(700, 400, anchor = "nw", window = button10)

def end_of_demo():
    clear_canvas()
    #canvas.create_image(0, 0, image=quest_IMG, anchor="nw")
    load_bar.place(x=685, y=500, width=200)
    load_bar.start()
    canvas.create_window(1335, 40, anchor = "nw", window = button11)

#buttons
button1 = Button(demo, text = "Start", font = font1, command=enter_name)
button2 = Button(demo, text = "Submit", font = font1, command=greetings)
button3 = Button(demo, text = "Continue", font = font1, command=character_class)
button4 = Button(demo, text = "Paladin", font = font1, command=paladin)
button5 = Button(demo, text = "Ranger", font = font1, command=ranger)
button6 = Button(demo, text = "Warlock", font = font1, command=warlock)
button7 = Button(demo, text = "Bard", font = font1, command=bard)
button8 = Button(demo, text = "Continue", font = font1, command=stats)
button9 = Button(demo, text = "Submit", font = font1, command=show_stats)
button10 = Button(demo, text = "Start Quest", font = font1, command=end_of_demo)
button11 = Button(demo, text = "End Demo", font = font1, command=demo.destroy)
button12 = Button(demo, text = "Continue", font = font1, command=start_quest)

#game start
opening_title()

demo.mainloop()