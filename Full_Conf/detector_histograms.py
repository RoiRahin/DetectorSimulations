import sys
import matplotlib.pyplot as plt
import numpy as np

theta = int(sys.argv[1])
phi = int(sys.argv[2])
location = sys.argv[3]
source = open(location + "full_conf_"+str(theta)+"_"+str(phi)+".burst.out" , 'rb')
data = []
for line in source:
    data.append(line.split(";"))
energy_data = [[],[],[],[],[]]
for hit in data:
	if (float(hit[1]) > 7) :
		energy_data[0].append(float(hit[3]))
	elif (float(hit[1]) < -7) :
		energy_data[2].append(float(hit[3]))		
	elif (float(hit[0]) > 7) :
		energy_data[3].append(float(hit[3]))
	elif (float(hit[0]) < -7) :
		energy_data[1].append(float(hit[3]))
	else :
		energy_data[4].append(float(hit[3]))
energy_data = np.array(energy_data)
bins = np.linspace(0,1000,100)
fig = plt.figure()
ax = fig.add_subplot(111)
for i in range (0,5):
	weights = [1/1000.0] * len(energy_data[i])
	ax.hist(energy_data[i],bins,weights = weights,histtype = 'step')
plt.yscale('log')
plt.xscale('log')
plt.legend(['detector 1' ,'detector 2','detector 3','detector 4','detector 5'])
plt.show()