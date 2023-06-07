from tkinter import *
from tkinter import ttk

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
startxcombo = ttk.Combobox(root, state="readonly", values=xvalues, width=10)
startxlbl.place(relx=.092, rely=.8, anchor=CENTER)
startxcombo.place(relx=.18, rely=.8, anchor=CENTER)

startylbl = Label(root, text="Chose the starty: ")
yvalues = [10,50,100,200,300,400,450]
startycombo = ttk.Combobox(root, state="readonly", values=yvalues, width=10)
startylbl.place(relx=0.33, rely=.8, anchor=CENTER)
startycombo.place(relx=.42, rely=.8, anchor=CENTER)

endxlbl = Label(root, text="Chose the endx: ")
exvalues = [10,50,100,200,300,400,500,600,800,900]
endxcombo = ttk.Combobox(root, state="readonly", values=exvalues, width=10)
endxlbl.place(relx=0.55, rely=.8, anchor=CENTER)
endxcombo.place(relx=.66, rely=.8, anchor=CENTER)

endylbl = Label(root, text="Chose the endy: ")
eyvalues = [10,50,100,200,300,400,450]
endycombo = ttk.Combobox(root, state="readonly", values=eyvalues, width=10)
endylbl.place(relx=0.77, rely=.8, anchor=CENTER)
endycombo.place(relx=.88, rely=.8, anchor=CENTER)

root.mainloop()