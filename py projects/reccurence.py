import matplotlib.pyplot as plt
import numpy as np
import random


def dataPoints():
    x_data = list(range(5001))
    y_data = [0.1]
    a=0
    
    for n in range(5000):
        a = (2*y_data[n]-y_data[n]*y_data[n])*0.55
        y_data.append(a)
        
    return x_data,y_data

# From here the plotting starts
# for n in y_data:
#     print(n)

j=7

# for p in range (5,100,10):
# 
#     for i in range(10):
#         dataP = dataPoints(p)
#         l = 'Curve %d' % (i+1)
#         plt.plot(dataP[0],dataP[1],marker = ".",label=l)
# 
#     plt.xlabel('Days')
#     plt.ylabel('Number of infected')
#     plt.title('Modeling project p = %d, N = 1000 and A = 100'%(p))
#     plt.legend()
#     plt.savefig('Figure_%d_p%d'%(j,p))
#     plt.clf()

p=50
i=0
dataP = dataPoints()
plt.plot(dataP[0],dataP[1],marker = ".")

plt.xlabel('i')
plt.ylabel('a_i')
plt.title('Reccurency with p=0.5')
plt.legend()
# plt.savefig('Figure_%d_p%d'%(j,p))
plt.show()