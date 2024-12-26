from tkinter import * 
from tkinter import ttk

demo = Tk()
demo.geometry("400x400")

#image
quest_text_IMG = PhotoImage(file = "images/quest_text2.png")
paladin_IMG = PhotoImage(file = "images/paladin.png")
warlock_IMG = PhotoImage(file = "images/warlock.png")
bard_IMG = PhotoImage(file = "images/bard.png")
ranger_IMG = PhotoImage(file = "images/ranger.png")
pen_IMG = PhotoImage(file = "images/pen.png")
castle_bg_IMG = PhotoImage(file = "images/castle_bg.png")
wizard_orb_pondering_IMG = PhotoImage(file = "images/wizard_orb_pondering.png")
sword_IMG = PhotoImage(file = "images/sword.png")
princess_IMG = PhotoImage(file = "images/princess.png")
arrow_IMG = PhotoImage(file = "images/arrow.png")


#canvas
canvas = Canvas(demo, width=400, height=400)

#font
font1 = ("Book Antiqua", 20, "bold")
font2 = ("Blackadder ITC", 35, "bold")
font3 = ("Blackadder ITC", 48, "bold")

#global variables for display
name_label = Label(canvas, text="Please enter your name, traveller:", font=font2, height=4)
name_entry = Entry(canvas, bd=8, width=80)
strength_bar = Scale(demo, from_=0, to=100, orient=HORIZONTAL, width=40, length=1000, label="Strength", font=font1)
agility_bar = Scale(demo, from_=0, to=100, orient=HORIZONTAL, width=40, length=1000, label="Agility", font=font1)
dexterity_bar = Scale(demo, from_=0, to=100, orient=HORIZONTAL, width=40, length=1000, label="Dexterity", font=font1)
load_bar = ttk.Progressbar(mode="indeterminate")
frame1 = Frame(demo, width=10, height=10)
frame2 = Frame(demo, width=10, height=10)
frame3 = Frame(demo, width=10, height=10)
frame4 = Frame(demo, width=10, height=10)
frame5 = Frame(demo, width=10, height=10)
frame6 = Frame(demo, width=10, height=10)
frame7 = Frame(demo, width=10, height=10)
frame8 = Frame(demo, width=10, height=10)
frame9 = Frame(demo, width=10, height=10)
paladin_icon = Label(frame1, image = paladin_IMG)
warlock_icon = Label(frame2, image = warlock_IMG)
bard_icon = Label(frame3, image = bard_IMG)
ranger_icon = Label(frame4, image = ranger_IMG)
wizard_orb_pondering_icon = Label(frame5, image = wizard_orb_pondering_IMG)
castle_bg_icon = Label(frame6, image = castle_bg_IMG)
sword_icon = Label(frame7, image = sword_IMG)
princess_icon = Label(frame8, image = princess_IMG)
arrow_icon = Label(frame9, image = arrow_IMG)


#data for user info
class player:
    def __init__(self, name="None", c_class="None", strength_stat=0, agility_stat=0, dexterity_stat=0):
        self.name = name
        self.c_class = c_class
        self.strength_stat = strength_stat
        self.agility_stat = agility_stat
        self.dexterity_stat = dexterity_stat

user = player() #user's character object

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

def destroy_frame(): #add global to keep track of active frames, then destroy all active- allows for reusal in multiple functions
    frame1.destroy()
    frame2.destroy()
    frame3.destroy()
    frame4.destroy()

def opening_title():
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=quest_text_IMG, anchor="nw")
    canvas.create_window(700, 400, anchor = "nw", window = button1)
    frame6.pack()
    frame6.place(relx=0.63, rely=0.45)
    castle_bg_icon.pack()

def enter_name():
    global name_entry, name_label
    clear_canvas()
    canvas.create_image(0, 0, image=pen_IMG, anchor="nw")
    name_label.pack()
    name_entry.pack()
    canvas.create_window(700, 400, anchor = "nw", window = button2) 

def greetings():
    user.name = name_entry.get()
    destroy_form()
    clear_canvas()
    #canvas.create_image(0, 0, image=clouds_IMG, anchor="nw")
    canvas.create_text(770, 250, text="Welcome,", font=font3)
    canvas.create_text(770, 300, text=user.name, font=font3)
    canvas.create_window(700, 400, anchor = "nw", window = button3)

def character_class():
    clear_canvas()
    frame6.destroy()
    canvas.create_text(750, 100, text="Please pick a character class", font=font3)
    canvas.create_window(220, 700, anchor = "nw", window = button4)
    canvas.create_window(600, 700, anchor = "nw", window = button5)
    canvas.create_window(900, 700, anchor = "nw", window = button6)
    canvas.create_window(1230, 700, anchor = "nw", window = button7)
    frame1.pack()
    frame1.place(relx=0.07, rely=0.2)
    paladin_icon.pack()
    frame2.pack()
    frame2.place(relx=0.5, rely=0.2)
    warlock_icon.pack()
    frame3.pack()
    frame3.place(relx=0.7, rely=0.2)
    bard_icon.pack()
    frame4.pack()
    frame4.place(relx=0.28, rely=0.2)
    ranger_icon.pack()

def paladin():
    user.c_class = "Paladin"
    clear_canvas()
    canvas.create_image(0, 0, image=paladin_IMG, anchor="nw")
    character_class_widget()

def ranger():
    user.c_class = "Ranger"
    clear_canvas()
    canvas.create_image(0, 0, image=ranger_IMG, anchor="nw")
    character_class_widget()

def warlock():
    user.c_class = "Warlock"
    clear_canvas()
    canvas.create_image(0, 0, image=warlock_IMG, anchor="nw")
    character_class_widget()

def bard():
    user.c_class = "Bard"
    clear_canvas()
    canvas.create_image(0, 0, image=bard_IMG, anchor="nw")
    character_class_widget()

def character_class_widget():
    destroy_frame()
    canvas.create_text(770, 250, text="You have chosen", font=font3)
    canvas.create_text(770, 320, text=user.c_class, font=font3)
    canvas.create_window(700, 400, anchor = "nw", window = button8)

def stats():
    clear_canvas()
    #canvas.create_image(0, 0, image=clouds_IMG, anchor="nw")
    canvas.create_text(770, 200, text="Please adjust your character stats", font=font3)
    canvas.create_window(700, 400, anchor = "nw", window = button9)
    strength_bar.pack()
    agility_bar.pack()
    dexterity_bar.pack()

def show_stats():
    user.strength_stat = strength_bar.get()
    user.agility_stat = agility_bar.get()
    user.dexterity_stat = dexterity_bar.get()
    destroy_scale()
    clear_canvas()
    #canvas.create_image(0, 0, image=clouds_IMG, anchor="nw")
    canvas.create_text(770, 35, text="===Character Stats===", font=font3)
    canvas.create_text(770, 125, text="Strength: " + str(user.strength_stat), font=font2)
    canvas.create_text(770, 225, text="Agility: " + str(user.agility_stat), font=font2)
    canvas.create_text(770, 325, text="Dexterity: " + str(user.dexterity_stat), font=font2)
    canvas.create_window(700, 400, anchor = "nw", window = button12)
    frame7.pack()
    frame7.place(relx=0.65, rely=0.30)
    sword_icon.pack()
    frame9.pack()
    frame9.place(relx=0.1, rely=0.1)
    arrow_icon.pack()

def start_quest():
    clear_canvas()
    #canvas.create_image(0, 0, image=castle_bg_IMG, anchor="nw")
    frame7.destroy()
    frame9.destroy()
    canvas.create_text(800, 300, text="Character design complete...", font=font3)
    appearing_button = lambda: canvas.create_window(700, 400, anchor = "nw", window = button10)
    demo.after(1000, appearing_button)
    frame8.pack()
    frame8.place(relx=0.74, rely=0.30)
    princess_icon.pack()

def end_of_demo():
    clear_canvas()
    frame8.destroy()
    #canvas.create_image(0, 0, image=clouds_IMG, anchor="nw")
    load_bar.place(x=580, y=600, width=350)
    load_bar.start()
    canvas.create_window(1335, 40, anchor = "nw", window = button11)
    frame5.pack()
    frame5.place(relx=0.3, rely=0.2)
    wizard_orb_pondering_icon.pack()

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