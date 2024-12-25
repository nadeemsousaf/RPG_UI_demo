from tkinter import *


demo = Tk()
demo.geometry("400x400")
#images
quest_IMG = PhotoImage(file = "images/quest.png")
#canvas
canvas = Canvas(demo, width=400, height=400)
#font
font1 = ("Impact", 20)

#global data for user info
name_label = Label(canvas, text="Please enter your name:", font=font1)
name_entry = Entry(canvas)
name = "NA"

#functions
def clear_canvas():
    canvas.delete('all')

def destroy_form():
    name_label.after(1000, name_label.destroy())
    name_entry.after(1000, name_entry.destroy())

def opening_title():
    canvas.pack(fill="both", expand=True)
    #canvas.create_image(0, 0, image=quest_IMG, anchor="nw")
    canvas.create_window(750, 400, anchor = "nw", window = button1) 

def enter_name():
    global name_entry, name_label
    clear_canvas()
    canvas.create_text(750, 300, text="Hello, traveller.", font=font1)
    name_label.pack()
    name_entry.pack()
    canvas.create_window(750, 400, anchor = "nw", window = button2) 

def greetings():
    global name
    name = name_entry.get()
    destroy_form()
    clear_canvas()
    canvas.create_text(750, 300, text=name, font=font1)

#buttons
button1 = Button(demo, text = "Start", font = font1, command=enter_name)
button2 = Button(demo, text = "Submit", font = font1, command=greetings)

#game start
opening_title()

demo.mainloop()