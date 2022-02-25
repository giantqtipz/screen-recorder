import os
from tkinter import filedialog

def upload_prompt(root, display_filename):
    root.filename = filedialog.askopenfilename(title='Upload an Excel file', filetypes=(('excel files', '*.xlsx'), ('all files', '*.*')))
    basename = os.path.basename(root.filename)
    display_filename.configure(text=basename, fg='black')

def set_duration_focus(set_duration):
    set_duration.delete(0, 'end')