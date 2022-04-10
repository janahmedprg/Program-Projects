from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt
import math

def sysOde(state, t):
    V,Phi,X,Y = state
    return (-np.sin(Phi)-Alpha*(V**2),-np.cos(Phi)/V,V*np.cos(Phi),V*np.sin(Phi))

################################## Interactive #################################
grid = 1000000
Alpha = 1.8
phiList = [10,30,45,60,70,80] #np.linspace(70.483,70.49,100)
xRange = 1.5
v0 = 1
################################################################################

Rmax = -1
argMaxPhi = -1
bestError = 10000
bestPhi = -1
for phi in phiList:
    time = 0
    fname = "traj_alpha" + str(round(Alpha,3)) + "_phi" + str(phi) + "_grid"+ str(grid)
    initialCond = np.array([v0,math.radians(phi),0,0])
    t = np.linspace(0,xRange,grid)
    states = integrate.odeint(sysOde,initialCond,t)
    # print(states)
    x = []
    y = []
    for i in range(grid):
        if states[i][3]<=0 and i!=0:
            time = t[i]
            break
        x.append(states[i][2])
        if Rmax<states[i][2]:
            Rmax = states[i][2]
            argMaxPhi = phi
        y.append(states[i][3])

    if (abs((time*v0)/9.80665)*6-(x[len(x)-1]*(v0**2))/9.80665) < bestError:
        bestError = abs(((time*v0)/9.80665)*6-(x[len(x)-1]*(v0**2))/9.80665)
        bestPhi = phi

    print(y[len(y)-1], "Y(T_f)")
    print(phi, "Phi")
    # print((x[len(x)-1]*(v0**2))/9.80665, "x")
    # print((time*v0)/9.80665,"time")
    # print(((time*v0)/9.80665)*6, "rugby player at")
    print(Rmax,"Rmax")
    print(argMaxPhi,"argMaxPhi")
    print()
    plt.plot(x,y)
    # plt.save(fname + ".png")
    plt.show()

# print(bestPhi, "bestPhi") # 70.48377777777777
# print(bestError, "error in distance") # 1.3947084518406427e-05
print("(Rmax-R0)/R0 = "+str(round(abs(Rmax-1)*100,4))+"%")
