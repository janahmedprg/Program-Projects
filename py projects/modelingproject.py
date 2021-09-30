import matplotlib.pyplot as plt
import numpy as np
import random

def dataPoints(p):
    x_data = list(range(1001))
    y_data = [100]

    for n in range(1000):
        newInfect = 0
        for i in range(1000-y_data[n]):
            if (y_data[n]-1) >= random.randint(0,999):
                newInfect += 1
        infected = y_data[n] + newInfect
        for i in range(infected):
            if (random.randint(1,100) <= p):
                infected -= 1
        y_data.append(infected)

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
for i in range(10):
    dataP = dataPoints(p)
    l = 'Curve %d' % (i+1)
    plt.plot(dataP[0],dataP[1],marker = ".",label=l)

plt.xlabel('Days')
plt.ylabel('Number of infected')
plt.title('Modeling project p = %d, N = 1000 and A = 100'%(p))
plt.legend()
# plt.savefig('Figure_%d_p%d'%(j,p))
plt.show()

print('Program has finished plotting graphs check Desktop/Program-Projects')
