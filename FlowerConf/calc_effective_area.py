import sys
import matplotlib.pyplot as plt 
import numpy as np 

if (len(sys.argv) < 2 or "help" in sys.argv or "-h" in sys.argv):
	print "usage: <total photons per cm^-2 used in simulation>"
	exit()


source = open("5_flower_count.burst.out", 'r')
flower_5 = []
for line in source:
	flower_5.append(float(line))

source.close()
source = open("4_flower_count.burst.out", 'r')
flower_4 = []
for line in source:
	flower_4.append(float(line))

flux = float(sys.argv[1])

Aeff_4 = [x/flux/45.6 for x in flower_4]
Aeff_5 = [x/flux/45.6 for x in flower_5]
deg = np.linspace(0,90, len(Aeff_4))

plt.plot(deg , Aeff_4)
plt.plot(deg, Aeff_5)
plt.show()
