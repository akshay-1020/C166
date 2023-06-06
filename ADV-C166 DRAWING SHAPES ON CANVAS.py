from tkinter import *
from tkinter import ttk

# I tried this project, the place function doesn't work for some reason. I get the concept, though.

root = Tk()
root.geometry("1000x800")
root.title("Scibbled Canvas")

canvas = Canvas(root, width=995, height=500, bg="darkgrey", highlightbackground = "black")
canvas.pack(pady=10, padx=10)

colorlbl = Label(root, text="Chose Color: ")
colors = ["red", "green", "blue", "yellow", "purple", "orange", "black"]
colorcombo = ttk.Combobox(root, state="readonly", values=colors, width=10)
colorlbl.pack()
colorcombo.pack()

startxlbl = Label(root, text="Chose the startx: ")
xvalues = [10,50,100,200,300,400,500,600,800,900]
startxcombo = ttk.Combobox(root, state="readonly", values=colors, width=10)
startxlbl.place(relx=200, rely=400, anchor=CENTER)
startxcombo.place(relx=250, rely=400, anchor=CENTER)

root.mainloop()