import numpy as np, matplotlib.pyplot as plt, matplotlib.font_manager as fm,os
from numpy import pi, sin, linspace, array, gradient, cos, tan
from scipy.integrate import odeint
from mpl_toolkits.mplot3d.axes3d import Axes3D

g = 9.806 #Gravitational acceleration
l0 = 1 #Natural length of spring is 1
k = 2 #K value for spring is 2
OA = 2 #Length OA is 2
m = 1 #Mass of the particles is 1

d2r = (pi)/180
initial_state = [30*d2r,60*d2r,1,0,0,0]
a = 4
time_points = np.linspace(0, 10, 1000)

def my_system(current_state, t):
    x1, y1, z1, x2, y2, z2 = current_state
    Fs = -k*(z1-l0)
    Tn = m*(x1**2)*OA + m*g*cos(x1) + Fs*cos(y1-x1)

    x2dot = (Fs*sin(y1-x1) - m*g*sin(x1))/(m*OA)
    y2dot = (-g*sin(y1) - y2*z2 - OA*x2dot*cos(y1-x1) - (x2**2)*OA*sin(y1-x1))/z1
    z2dot = x2dot*OA*sin(y1-x1) + (x2**2)*OA*cos(y1-x1) - Fs + g*cos(y1) + (y2**2)*z1

    return [x2, y2, z2, x2dot, y2dot, z2dot]

xyz = odeint(my_system, initial_state, time_points)

x = xyz[:,0]
y = xyz[:,1]
z = xyz[:,2]

xp = np.gradient(x)
yp = np.gradient(y)
zp = np.gradient(z)

# Plot the trajectories
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set(xlim=(-0.1, 10.1), ylim=(-6, 4))

plt.plot(time_points, x.T)
plt.plot(time_points, y.T)
plt.plot(time_points, z.T)
plt.plot(time_points, xp.T)
plt.plot(time_points, yp.T)
plt.plot(time_points, zp.T)

plt.xlabel('t')
plt.title('Simple pendulum (point mass)')
plt.legend(['Theta1','Theta2','r','Theta1-dot','Theta2-dot','r-dot'])
plt.grid('on')
plt.show()
