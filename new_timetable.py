import pandas as p
from datetime import datetime
import calendar
from tkinter import *
from tkinter import font
import re

s = datetime.now()
f = p.read_excel("TT/Book3.xlsx", index_col=0)
l = ['I', 'II', 'III', 'IV', 'LUNCH', 'V', 'VI', 'VII']
h = s.strftime("%H:%M")

# h = "12:20"


def time_frame():
    s = datetime.now()
    if calendar.day_name[s.weekday()] == "Sunday":
        return "Today is a holiday...\ncuz it is a SUNDAY...-_-\n"
    if h < "09:30":
        return f"it's too early for this...\nclasses start at 9:30 \nnext class is {f['I'][calendar.day_name[s.weekday()]]}"
    elif h > '16:30':
        return "classes are over,\nyou can enjoy now..."
    else:
        for j in l:
            k = f[j]['day'].split('-')
            if k[0] <= h <= k[1]:
                if f[j][calendar.day_name[s.weekday()]] == "BREAK":
                    return f"it's time for your {f[j][calendar.day_name[s.weekday()]]}...[{f[j]['day']}]\nyour next class is your {f[l[l.index(j) + 1]][calendar.day_name[s.weekday()]]}...[{f[l[l.index(j) + 1]]['day']}]\n"
                elif l.index(j) + 1 >= len(l):
                    return f"it's time for your {f[j][calendar.day_name[s.weekday()]]}...[{f[j]['day']}]\nAfter this your classes will be over...\nThis is your last period...\n"
                elif f[l[l.index(j) + 1]][calendar.day_name[s.weekday()]] == "BREAK":
                    return f"it's time for your {f[j][calendar.day_name[s.weekday()]]} class...[{f[j]['day']}]\nAfter this class your can have your {f[l[l.index(j) + 1]][calendar.day_name[s.weekday()]]}...[{f[l[l.index(j) + 1]]['day']}]\n"
                return f"it's time for your {f[j][calendar.day_name[s.weekday()]]} class...[{f[j]['day']}]\nyour next class is your {f[l[l.index(j) + 1]][calendar.day_name[s.weekday()]]}...[{f[l[l.index(j) + 1]]['day']}]\n"


r = Tk()
r.title("Class reminder")


def action():
    # y="Time : "+s.strftime("%H : %M")
    t1.configure(state=NORMAL)
    s = datetime.now()
    t1.delete("1.0", END)
    x1 = "Date : {} , {}".format(s.strftime("%d-%m-%y"), calendar.day_name[s.weekday()]) + "\nTime : " + s.strftime(
        "%H : %M : %S") + "\n"
    if x.get() == 1:
        x1 += time_frame()
    elif x.get() == 2:
        if c2.get() == "Sunday":
            x1 += "Today is a holiday...\ncuz it is a SUNDAY...-_-\n"
        if f[c1.get()][c2.get()] != "BREAK":
            if l.index(c1.get()) + 1 >= len(l):
                x1 += f"it's time for your {f[c1.get()][c2.get()]}...\nAfter this your classes will be over...\nThis is your last period...\n"
            elif f[l[l.index(c1.get()) + 1]][c2.get()] != "BREAK":
                x1 += f"It's time for your {f[c1.get()][c2.get()]} class...\nNext will be your {f[l[l.index(c1.get()) + 1]][c2.get()]} class...\n"
            else:
                x1 += f"It's time for your {f[c1.get()][c2.get()]} class...\nAfter this class you can take your BREAK ...\n"
        else:
            x1 += f"Now it's time for your BREAK...\nYour next class will be {f[l[l.index(c1.get()) + 1]][c2.get()]}\n"
    bold_font = font.Font(t1, t1.cget("font"))
    bold_font.configure(family="cascadia mono semibold", size=15)
    larger = font.Font(t1, t1.cget("font"))
    larger.configure(size=10, family="cascadia mono light")
    # t1.configure(font=larger)
    t1.insert(INSERT, x1)
    sub = re.findall(r'[A-Z]?[-]?[A-Z][&]?[A-Z]{1,5}', x1)
    print(sub)
    # print(x1.count("\n",0,x1.index("CO")))
    lines = [m.start() for m in re.finditer("\n", x1)]
    # for i in range(len(lines)-1):
    #     print(x1[lines[i]:lines[i+1]])
    # print(x1[lines[1]:lines[2]].index("CO"))
    # print(x1[lines[2]:lines[3]].index("M-II"))
    t1.tag_add("b2", "1.0", "10.100")
    t1.tag_configure("b2", font=larger)
    print(lines)
    d = {}
    for k in range(0, len(sub) // 2):
        d[sub[k]] = 0
    for i in sub:
        if x1.count(i) == 1:
            n1 = x1.count('\n', 0, x1.index(i))
        else:
            # print(d)
            n1 = x1.count('\n', 0, x1.index(i)) + d[i]
            d[i] += 1

        s1 = f"{n1 + 1}.{x1[lines[n1 - 1]:lines[n1]].index(i) - 1}"
        s2 = f"{n1 + 1}.{x1[lines[n1 - 1]:lines[n1]].index(i) + len(i) - 1}"
        # s2=f"{n1+1}.{lines[n1]-x1.index(i)+len(i)-5}"
        print(s1, s2)  # "1.22","1.23"
        t1.tag_add("b1", s1, s2)
        t1.tag_configure("b1", font=bold_font)
    t1.configure(state=DISABLED)
    # print(x1)
    # print(re.findall(r"[^I[a-z]]{2,10}",x1))
    # print(re.findall(r"[A-Z]{1,2}[-&]?[A-Z]{0,5}",x1))
    # print()

    # print(x1.index("\n"))


b1 = Button(r, text="CHECK", padx=30, pady=5, bg="pink", command=action)
b1.grid(row=2, column=0, padx=20, pady=10)


def b_exit():
    r.destroy()


b2 = Button(r, text="EXIT", padx=30, pady=5, bg="cyan", command=b_exit)
b2.grid(row=2, column=3, padx=20, pady=10)
x = IntVar()
x.set(1)


def dis():
    op.configure(state=DISABLED)
    op1.configure(state=DISABLED)


def en():
    op.configure(state=NORMAL)
    op1.configure(state=NORMAL)


Radiobutton(r, text="Auto", variable=x, value=1, command=dis).grid(row=0, column=0)
Radiobutton(r, text="Manual", variable=x, value=2, command=en).grid(row=0, column=1)
c1 = StringVar()
c1.set(l[0])
wd = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
c2 = StringVar()
c2.set(wd[0])
op = OptionMenu(r, c1, *l)
Label(r, text="period : ").grid(row=1, column=0)
op.grid(row=1, column=1)
Label(r, text="weekday : ").grid(row=1, column=2)
op1 = OptionMenu(r, c2, *wd)
op1.grid(row=1, column=3)
op.configure(state=DISABLED)
op1.configure(state=DISABLED)

t1 = Text(r, height=13, width=50)
t1.insert(INSERT, "Welcome...\n")
t1.configure(state=DISABLED)
t1.grid(row=3, column=0, columnspan=4, pady=10, padx=10)
r.resizable(False, False)
r.mainloop()
