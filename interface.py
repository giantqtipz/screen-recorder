from tkinter import *
from PIL import ImageTk
from app import start_application
from utils.utils import set_duration_focus, upload_prompt

root = Tk()

root.title(string='UMG - Screen Recorder')

canvas = Canvas(root, width=900, height=400)
canvas.pack()

background_logo = ImageTk.PhotoImage(file='./assets/umg-logo.png')
background_logo_label = Label(root, image=background_logo)
background_logo_label.place(relwidth=1, relheight=1)

frame = Frame(root, bg='white')
frame.place(relx=.5, rely=.7, relwidth=.9, relheight=0.1, anchor='n')

upload_button = Button(frame, text='Upload File', command=lambda:upload_prompt(root, display_filename))
upload_button.place(relx=0, relheight=1, relwidth=0.20)

display_filename = Label(frame, font='Raleway', bg='white', fg='black', text='no file selected')
display_filename.place(relx=0.225, relheight=1)

set_duration = Entry(frame, bg='white', fg='black', justify='center')
set_duration.insert(0, "duration (s)")
set_duration.bind('<1>', lambda event, arg=set_duration: set_duration_focus(set_duration))
set_duration.place(relx=.60, relwidth=0.10,relheight=1)

start_button = Button(frame, text='Start Recording', command=lambda:start_application(root.filename, set_duration.get()))
start_button.place(relx=.8, relwidth=0.20, relheight=1)

root.mainloop()