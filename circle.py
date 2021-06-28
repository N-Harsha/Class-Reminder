import numpy as np
import matplotlib.pyplot as m
x=[]
y=[]
c=0
r=int(input("enter the radius of required circle : "))
for i in np.arange(-r,r,0.001):
    for j in np.arange(-r,r,0.001):
        c+=1
        if int((i**2) + (j**2))==r**2 or int((i**2) + (j**2))==r**2-1 :
            x.append(i)
            y.append(j)
print(x,y)
m.plot(x,y,color='black')
m.xlabel("x-axis")
m.ylabel("y-axis")
m.title("circle")
m.show()
print(f"no.of repetitions : {c}")
