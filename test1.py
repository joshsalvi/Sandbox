import math as m
import numpy as num
import matplotlib.pyplot as p

x = num.linspace(0,10,10000)
y = num.sin(x)

p.plot(x,y)
p.show()