import matplotlib.pyplot as plt
import numpy as np
import sys

source = open("single_det2_32_1.out" , 'rb')
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
line.set_label('32 KeV 1 inch')

source = open("single_det2_32_0.5.out" , 'rb')
data = []
for line in source:
    data.append(float(line))
source.close()
# zenith_hit = data[0]
norm_data = [x/zenith_hit for x in data]
line, = ax.plot(deg,norm_data , 'r')
line.set_label('32 KeV 0.5 inch')
ax.legend()
deg_rad = np.multiply(deg , np.pi/180)
theo_32_1 = np.multiply(np.add(np.multiply(np.cos(deg_rad) , np.pi * ((1.5 * 2.54)**2)) , np.multiply(np.sin(deg_rad) , 3 * 2.54 * 2.54)) , 1/(np.pi * ((1.5 * 2.54)**2)))
theo_32_05 = np.multiply(np.add(np.multiply(np.cos(deg_rad) , np.pi * ((1.5 * 2.54)**2)) , np.multiply(np.sin(deg_rad) , 3 * 2.54 * 2.54 * 0.5)) , 1/(np.pi * ((1.5 * 2.54)**2)))
line, = ax.plot(deg,theo_32_1 , 'b--')
line.set_label('32 KeV 1 inch theoretical')
line, = ax.plot(deg,theo_32_05 , 'r--')
line.set_label('32 KeV 0.5 inch theoretical')
ax.legend()


source = open("single_det2_662_1.out" , 'rb')
data = []
for line in source:
    data.append(float(line))
source.close()

zenith_hit = data[0]
norm_data = [x/zenith_hit for x in data] 
fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot(deg,norm_data)
line.set_label('662 KeV 1 inch')

source = open("single_det2_662_0.5.out" , 'rb')
data = []
for line in source:
    data.append(float(line))
source.close()
# zenith_hit = data[0]
norm_data = [x/zenith_hit for x in data]
line, = ax.plot(deg,norm_data , 'r')
line.set_label('662 KeV 0.5 inch')
ax.legend()
plt.show()


