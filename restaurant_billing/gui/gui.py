from tkinter import *
from reporting import view_reports  # if it's in a separate file

def launch_gui(db_connection):
    root = Tk()
    root.title("Restaurant Billing Software")

    # Other GUI elements...

    report_btn = Button(root, text="📊 View Reports", command=lambda: view_reports(db_connection))
    report_btn.pack(pady=10)

    root.mainloop()
