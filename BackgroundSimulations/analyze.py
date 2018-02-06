import numpy as np
import matplotlib.pyplot as plt
import sys

source = open(sys.argv[1] , 'rb')
data = []
for line in source:
    data.append(float(line))

comp_data=[]
for point in data:
	if (point < 1000 and point > 500) :
		comp_data.append(point)
print len(data)/100.0
print len(comp_data)/100.0
bins = np.linspace(0,1000,1000)
weights = [1/100.0] * len(data)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(data , bins , weights = weights , histtype = 'step')
plt.yscale('log')
plt.xscale('log')
ax.set_title('GBM background signal')
ax.set_xlabel(r'E [KeV]')
ax.set_ylabel(r'Photon $s^{-1}$')
fig = plt.show()
