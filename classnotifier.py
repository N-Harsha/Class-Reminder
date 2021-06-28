from win10toast import ToastNotifier
import pandas as p
from datetime import datetime
# from datetime import timedelta
import calendar
import time

hr = ToastNotifier()
hr.show_toast("Notice","Python reminder is at your service....")
f = p.read_excel("TT/Book3.xlsx", index_col=0)
k = ('I', 'II', 'III', 'IV', 'LUNCH', 'V', 'VI', 'VII')
s = datetime.now()
w = calendar.day_name[s.weekday()]
if w == "Sunday":
    hr.show_toast("Sunday", "There are no classes today.")
    exit(0)

d = {}
l=[]    
for i in k:
    s = f[i]['day']
    d[s[0:s.index('-')]] = i
    l.append(s[0:s.index('-')])
# print(l)
# s=datetime.now();

while True:
    s = datetime.now()
    h = s.strftime("%H:%M")
    # h = "14:00"
    # w = "Thursday"
    if h in d:
        if f[d[h]][w] == "BREAK" or "LAB" in f[d[h]][w]:
            hr.show_toast("Class", "Now it's time for your "+f[d[h]][w], duration=10)
        else:
            hr.show_toast("Class", "Now it's time for your " + f[d[h]][w]+" class", duration=10)
        if h == "15:40":
            exit(0)
        time.sleep(2934)
    else:
        k = s.strftime("%H:%M")
        for i in range(len(l)):
            if l[i] < k < l[i + 1]:
                time.sleep((s.strptime(l[i+1],'%H:%M')-s.strptime(k,"%H:%M")).total_seconds()-6)

