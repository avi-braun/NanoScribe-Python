
import math as m, math
import numpy as np
import matplotlib.pyplot as plt
import os.path

ns_path = 'C:\Users\Avi Braun\Dropbox\LAB B014\NaNoscribe\Structures\8 Kings\Bridges'
r = 30  # arc radius in um
dteta = 50e-3  # differential angel in radians
steps = int(m.pi/dteta)  # number of writing steps


teta = -m.pi  #strating point
posxV = []
poszV = []

for i in range(0, steps):
    x = m.cos(teta)*r
    z = m.sin(-teta)*r
    posxV.append(x+r)
    poszV.append(z)
    print "%.2f %.2f %.2f" %(x,0,z)
    teta=teta+dteta
    x=r
    z=0

print "%.2f %.2f %.2f" % (x, 0, z)
posxV.append(x+r)
poszV.append(z)
posyV=np.zeros(len(posxV))
posxyzV=np.array([posxV,posyV,poszV]).transpose()

name_of_file='pos_'+str(r)+'_.gwl'
completeName = os.path.join(ns_path,name_of_file)
np.savetxt(completeName,posxyzV,fmt='%.3f')

plt.plot(posxV,poszV,'bo')
plt.show()


