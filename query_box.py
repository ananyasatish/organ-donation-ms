# Import the required library
import mysql.connector
from tkinter import *
from tkinter import ttk

conn_object=mysql.connector.connect(host="localhost",user="root",passwd="Hiddlesbatch@199",database="DBMS_PROJECT")

cur=conn_object.cursor()

# Create an instance of tkinter frame
win=Tk()

# Set the geometry
win.geometry("700x350")

def get_input():
    x=text.get(1.0, "end-1c")
    cur.execute(x)
    d=cur.fetchall()
    for i in d:
        label.insert(END, "\n" + str(i))
        conn_object.commit()

# Add a text widget
text=Text(win, width=80, height=15)
text.insert(END, "")
text.pack()

# Create a button to get the text input
b=ttk.Button(win, text="Print", command=get_input)
b.pack()

# Create a Label widget
label=Text(win, font=('Calibri 15'))
label.pack()

win.mainloop()