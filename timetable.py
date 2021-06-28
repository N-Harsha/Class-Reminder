import pandas as p
from datetime import datetime
import calendar

s = datetime.now()
f = p.read_excel("TT/Book2.xlsx", index_col=0)
l = ['I', 'II', 'III', 'IV', 'LUNCH', 'V', 'VI', 'VII']


def other_case(h, m):
    l1 = []
    for i in range(0, len(l)):
        u = f[l[i]]['day']
        for k in u.split('-'):
            for j in k.split(':'):
                l1.append(int(j))
        h1, m1, h2, m2 = l1
        l1.clear()
        if h1 <= h <= h2:
            if m1 >= m2:
                if m in range(m1, 60) or m in range(0, m2 + 1):
                    if h == h2:
                        if m not in range(0, m2 + 1):
                            pass
                        else:
                            return l[i], True
                    else:
                        return l[i], True
            elif m1 < m2:
                if m in range(m1, m2):
                    return l[i], True


def time_frame():
    h = int(s.strftime("%H"))
    m = int(s.strftime("%M"))
    h = 10
    m = 59
    if h <= 9:
        if h == 9 and m < 30:
            return "it's too early for this...", False
        elif h < 9:
            return "it's too early for this...", False
        else:
            return other_case(h, m)
    elif h >= 16:
        if h == 16 and m > 30:
            return "class are over enjoy...", False
        elif h > 16:
            return "class are over enjoy...", False
        else:
            return other_case(h, m)

    elif 9 < h < 16:
        return other_case(h, m)


print("Date : {} , {}".format(s.strftime("%d-%m-%y"), calendar.day_name[s.weekday()]))
print("Time : ", s.strftime("%H : %M"))
o = list(time_frame())
if o[1] is False:
    print(o[0])
else:
    d = calendar.day_name[s.weekday()]
    # d='Wednesday'
    if d == 'Sunday':
        print("HOLIDAY")
    else:
        print("Now it's time for your {}".format(f[o[0]][d]),end='')
        if f[o[0]][d] == 'BREAK':
            pass
        else:
            print(" class.",end='')
        try:
            if f[l[l.index(o[0]) + 1]][d]=="BREAK":
                print("\nAfter this period its time for your Lunch Break")
            else:
                print(f"\n{f[l[l.index(o[0]) + 1]][d]} is your next class.")
        except:
                print("\nthere is no class next")