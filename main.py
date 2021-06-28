import numpy as np
import matplotlib.pyplot as m
x=[]
y=[]

for i in np.arange(-50,50,0.01):
    for j in np.arange(-50,50,0.01):
        if int(4*(i**2) - 9*(j**2))==36:
            x.append(i)
            y.append(j)
print(x,y)
m.plot(x,y)
m.xlabel("x-axis")
m.ylabel("y-axis")
m.title("hyperbola")

m.show()