import matplotlib.pyplot as plt
import numpy as np
import sys

source = open("single_det_32.out" , 'rb')
data = []
for line in source:
    data.append(float(line))
source.close()

zenith_hit = data[0]
norm_data = [x/zenith_hit for x in data]
deg = np.linspace(0,90,num=len(norm_data))
fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot(deg,norm_data , 'b')
line.set_label('32 KeV no silicon')

source = open("single_det_32_sil.out" , 'rb')
data = []
for line in source:
    data.append(float(line))
source.close()
# zenith_hit = data[0]
norm_data = [x/zenith_hit for x in data]
line, = ax.plot(deg,norm_data , 'r')
line.set_label('32 KeV with silicon')
ax.legend()

source = open("single_det_32_wall.out" , 'rb')
data = []
for line in source:
    data.append(float(line))
source.close()
# zenith_hit = data[0]
norm_data = [x/zenith_hit for x in data]
line, = ax.plot(deg,norm_data , 'g')
line.set_label('32 KeV with wall')
ax.legend()
ax.set_ylabel(r'Normalized photon count (relative to $\theta$ = 0, no silicon or wall)')
ax.set_xlabel(r'$\theta$')

source = open("single_det_662.out" , 'rb')
data = []
for line in source:
    data.append(float(line))
source.close()

zenith_hit = data[0]
norm_data = [x/zenith_hit for x in data] 
fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot(deg,norm_data)
line.set_label('662 KeV no silicon')

source = open("single_det_662_sil.out" , 'rb')
data = []
for line in source:
    data.append(float(line))
source.close()
# zenith_hit = data[0]
norm_data = [x/zenith_hit for x in data]
line, = ax.plot(deg,norm_data , 'r')
line.set_label('662 KeV with silicon')
ax.legend()

source = open("single_det_662_wall.out" , 'rb')
data = []
for line in source:
    data.append(float(line))
source.close()
# zenith_hit = data[0]
norm_data = [x/zenith_hit for x in data]
line, = ax.plot(deg,norm_data , 'g')
line.set_label('662 KeV with wall')
ax.legend()
ax.set_ylabel(r'Normalized photon count (relative to $\theta$ = 0, no silicon or wall)')
ax.set_xlabel(r"$\theta$")
plt.show()