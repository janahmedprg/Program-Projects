from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib import animation

fig, ax = plt.subplots()

def update_point(n, x, y, point):
    point.set_data(np.array([x[n], y[n]]))
    return point

def sysOde(state, t):
    V,Phi,X,Y = state
    return (-np.sin(Phi)-Alpha*(V**2),-np.cos(Phi)/V,V*np.cos(Phi),V*np.sin(Phi))

################################## Interactive #################################
grid = 1000
Alpha = 2.1
phiList = [70.48377777777777] #[10,30,45,60,70,80] #np.linspace(70.483,70.49,100)
xRange = 4.5
v0 = 26
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
    print((x[len(x)-1]*(v0**2))/9.80665, "x")
    print((time*v0)/9.80665,"time")
    print(((time*v0)/9.80665)*6, "rugby player at")
    print(Rmax,"Rmax")
    print(argMaxPhi,"argMaxPhi")
    print()
    # plt.plot(x,y)
    # plt.save(fname + ".png")
    rugbyPx = []
    rugbyPy = []
    for tt in t:
        rugbyPx.append(6*tt/v0)
        rugbyPy.append(0)

    def animate(i):
        ax.clear()
        ax.set_xlim(-0.05,0.95)
        ax.set_ylim(-0.05,1.7)
        line, = ax.plot(x[0:i], y[0:i], color = 'blue')
        line2, = ax.plot(rugbyPx[0:i], rugbyPy[0:i], color = 'red')
        point1, = ax.plot(x[i], y[i], marker='o', color='blue')
        point2, = ax.plot(rugbyPx[i], rugbyPy[i], marker='o', color='red')
        return line, line2, point1, point2
    anim1=animation.FuncAnimation(fig, animate, grid)
    plt.show()
    # writervideo = animation.FFMpegWriter(fps=60)
    # anim1.save('upAndUnder.mp4', writer=writervideo)

# print(bestPhi, "bestPhi") # 70.48377777777777
# print(bestError, "error in distance") # 1.3947084518406427e-05
print("(Rmax-R0)/R0 = "+str(round(abs(Rmax-1)*100,4))+"%")
