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
name_entry = Entry(canvas, bd=5, width=80)
strength_bar = Scale(demo, from_=0, to=100, orient=HORIZONTAL, width=40, length=1000, label="Strength", font=font1)
agility_bar = Scale(demo, from_=0, to=100, orient=HORIZONTAL, width=40, length=1000, label="Agility", font=font1)
dexterity_bar = Scale(demo, from_=0, to=100, orient=HORIZONTAL, width=40, length=1000, label="Dexterity", font=font1)
load_bar = ttk.Progressbar(mode="indeterminate")

#global data for user info
name = "NA"
char_class = "NA"

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
    global name
    name = name_entry.get()
    destroy_form()
    clear_canvas()
    #canvas.create_image(0, 0, image=quest_IMG, anchor="nw")
    canvas.create_text(770, 250, text="Welcome,", font=font1)
    canvas.create_text(770, 300, text=name, font=font1)
    canvas.create_window(700, 400, anchor = "nw", window = button3)

def character_class():
    clear_canvas()
    #canvas.create_image(0, 0, image=quest_IMG, anchor="nw")
    canvas.create_text(750, 100, text="Please pick a character class", font=font1)
    canvas.create_window(250, 700, anchor = "nw", window = button4)
    canvas.create_window(650, 700, anchor = "nw", window = button5)
    canvas.create_window(950, 700, anchor = "nw", window = button6)
    canvas.create_window(1250, 700, anchor = "nw", window = button7)

def paladin():
    global char_class
    char_class = "Paladin"
    clear_canvas()
    #canvas.create_image(0, 0, image=quest_IMG, anchor="nw")
    character_class_widget()

def ranger():
    global char_class
    char_class = "Ranger"
    clear_canvas()
    #canvas.create_image(0, 0, image=quest_IMG, anchor="nw")
    character_class_widget()

def warlock():
    global char_class
    char_class = "Warlock"
    clear_canvas()
    #canvas.create_image(0, 0, image=quest_IMG, anchor="nw")
    character_class_widget()

def bard():
    global char_class
    char_class = "Bard"
    clear_canvas()
    #canvas.create_image(0, 0, image=quest_IMG, anchor="nw")
    character_class_widget()

def character_class_widget():
    canvas.create_text(770, 250, text="You have chosen", font=font1)
    canvas.create_text(770, 320, text=char_class, font=font2)
    canvas.create_window(700, 400, anchor = "nw", window = button8)

def stats():
    clear_canvas()
    #canvas.create_image(0, 0, image=quest_IMG, anchor="nw")
    canvas.create_text(770, 100, text="Please adjust your character stats", font=font1)
    canvas.create_window(700, 400, anchor = "nw", window = button9)
    strength_bar.pack()
    agility_bar.pack()
    dexterity_bar.pack()

def start_quest():
    clear_canvas()
    destroy_scale()
    #canvas.create_image(0, 0, image=quest_IMG, anchor="nw")
    canvas.create_window(700, 400, anchor = "nw", window = button10)

def end_of_demo():
    canvas.create_text(650, 600, text="End of demo...", font=font2)
    load_bar.place(x=685, y=500, width=200)
    load_bar.start()

#buttons
button1 = Button(demo, text = "Start", font = font1, command=enter_name)
button2 = Button(demo, text = "Submit", font = font1, command=greetings)
button3 = Button(demo, text = "Continue", font = font1, command=character_class)
button4 = Button(demo, text = "Paladin", font = font1, command=paladin)
button5 = Button(demo, text = "Ranger", font = font1, command=ranger)
button6 = Button(demo, text = "Warlock", font = font1, command=warlock)
button7 = Button(demo, text = "Bard", font = font1, command=bard)
button8 = Button(demo, text = "Continue", font = font1, command=stats)
button9 = Button(demo, text = "Continue", font = font1, command=start_quest)
button10 = Button(demo, text = "Start Quest", font = font1, command=end_of_demo)

#game start
opening_title()

demo.mainloop()