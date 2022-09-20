# Importing Modules
from tkinter import messagebox
from tkinter import *
from tkinter import colorchooser
import tkinter.scrolledtext as tkst
from PIL import ImageTk, Image

note_color = []

""" note creation button and functions """
def add_note():

    """ confirmation alert to delete note """
    def delete_note():
        if messagebox.askokcancel("Delete Note", "Do you want to delete this note?", parent=note_window):
            note_window.destroy()

    """ close the app """
    def exit_system():
        if messagebox.askokcancel("Close", "Do you want to close the app?", parent=note_window):
                    window.destroy()

    global note_color
    
    choose_color()
    color = note_color[1]
    note_window = Toplevel()
    note_window.title("My Note")
    note_window.resizable(False, False)
    mainarea = tkst.ScrolledText(note_window, width=20,  height=10 ,bg = color, font=('Comic Sans MS', 14, 'italic'), relief = 'flat')
    mainarea.pack(fill=BOTH, expand=True)
    note_window.attributes('-topmost', 'true')
    note_window.protocol("WM_DELETE_WINDOW", delete_note)
    window.protocol("WM_DELETE_WINDOW", exit_system)

""" set the color of the note """
def choose_color():
    global note_color
    # variable to store hexadecimal code of color
    note_color = colorchooser.askcolor(title ="Choose color")

# Main window settings
window = Tk()
window.title("Post it Note")
window.config(width=1025, height=685)
window.resizable(width=False, height=False)
canvas = Canvas(window, width=1025, height=685)
bg_image = ImageTk.PhotoImage(Image.open("pano.jpeg"), master=window)
canvas.create_image(0,0, anchor=NW,image=bg_image)
canvas.place(x=0,y=0)
add_note_button = Button(text="+", command=add_note)
add_note_button.place(x=20, y=20)

window.mainloop()

