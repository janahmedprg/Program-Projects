import numpy as np
x = 1-0.1
for i in range(0,1000):
    print(i,x)
    x = (x**3)/(-5/2+0.7)+(2*x)/(-5/2+0.7)-3/(-5/2+0.7)+x
