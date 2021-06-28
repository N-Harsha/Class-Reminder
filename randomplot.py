import random as r
import matplotlib.pyplot as p
x=[]
y=[]
a=[]
b=[]

for i in range(0,20):
    x.append(r.random())
    y.append(r.random())
x.sort()
y.sort()
p.plot(x,y,label='l1',color='green')
p.xlabel("x-axis")
p.ylabel("y-axis")
for i in range(0,20):
    a.append(r.random())
    b.append(r.random())
a.sort()
b.sort()
p.plot(a,b,label="l2",color='red')
p.legend()
p.show()
