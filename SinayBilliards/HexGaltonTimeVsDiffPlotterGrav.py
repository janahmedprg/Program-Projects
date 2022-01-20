import numpy as np
import math
import matplotlib.pyplot as plt
import random
import csv

fig, ax = plt.subplots()
ax.set_aspect('equal')

r=(1/1.125)/(0.5/(-0.5**2+1)**0.5)*0.5
eta = 0
nXY=15
nAng=20
sumPosition=0
coeffVstime=[[],[],[]]
particles = nXY*nAng
gravity = 1
fname='galton('+str(round(r,2))+')_timeRange'+str(0)+'-'+str(17000)+'_particles'+str(particles)+'_eta'+str(0)+'_gravity'+str(gravity)


increment = 1000
timeCap = 0
while(timeCap<17000):
    sumPosition=0
    timeCap += increment
    csvName = r'D:\Users\janah\Desktop\Program-Projects\SinayBilliards\gdata_eta_0_particles300_grav1\gdata_'+'eta_'+str(eta)+'time_'+str(timeCap)+'_particles'+str(particles)+'_grav'+str(gravity)+'.csv'
    rf = open(csvName,'r')
    reader = csv.reader(rf)
    next(reader)
    endPoslist = []

    for row in reader:
        xFrame = float(row[0])
        yFrame = float(row[1])
        sumPosition+=abs(yFrame)
        # endPoslist.append((xFrame**2+yFrame**2)/timeCap)
    rf.close()
    # coeffVstime[2].append(np.std(endPoslist))
    average=sumPosition/(particles)
    coeffVstime[0].append(timeCap)
    coeffVstime[1].append(np.log(average)/np.log(timeCap))

################################################################################
######################### Ploting Trajctory Map ################################
################################################################################
# ax.plot(tabX, tabY,'k',linewidth=1)
# ax.plot(trajX, trajY,'k',linewidth=1)
# disperser=plt.Circle((0, 0), r, fill=False,color='k')
# ax.add_patch(disperser)
############################### Save of Show ###################################
# plt.show()
# plt.axis('off')
# plt.savefig(fname+'.eps',transparent=True)

################################################################################
######################### Ploting Stat Experiment###############################
################################################################################
# plt.errorbar(coeffVstime[0],coeffVstime[1],yerr=coeffVstime[2], linestyle='None', marker='o',capsize=2,color='black')
plt.scatter(coeffVstime[0],coeffVstime[1],s=1,c='black')
plt.xlabel('Time')
plt.ylabel('log(E(y))/log(t)')
plt.title('Eta=0')
ax.set_aspect(1.0/ax.get_data_ratio(), adjustable='box')
############################### Save of Show ###################################
# plt.show()
plt.savefig(fname+'.eps')
