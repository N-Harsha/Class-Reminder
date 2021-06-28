from tkinter import *

r1 = Tk()
r1.title("Class reminder")
def action():
    t1.configure(text=time_frame())
    t1.configure(state=DISABLED)
b1 = Button(r, text="CHECK", padx=30, pady=5, bg="pink",command=action)
b1.grid(row=0, column=0, padx=20, pady=10)
def b_exit():
    r.destroy()
b2 = Button(r, text="EXIT", padx=30, pady=5, bg="cyan", command=b_exit)
b2.grid(row=0, column=1, padx=20, pady=10)
# r1=Radiobutton(r,text="Auto")
# r1.pack()
# r2=Radiobutton(r,text="Manual")
# r2.pack()
t1 = Text(r, height=13, width=50)
t1.insert(INSERT, "Welcome...")
# t1.configure(state=DISABLED)
t1.grid(row=1, column=0, columnspan=2, pady=10, padx=10)
# r.geometry("250x250")
r.resizable(False, False)
r.mainloop()
