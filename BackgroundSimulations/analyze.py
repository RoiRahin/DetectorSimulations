import numpy as np
import matplotlib.pyplot as plt
import sys

source = open(sys.argv[1] , 'rb')
data = []
for line in source:
    data.append(float(line))

comp_data=[]
for point in data:
	if (point < 300 and point > 50) :
		comp_data.append(point)

print len(comp_data)/100
bins = np.linspace(0,1000,1000)
weights = [1/100.0] * len(data)
plt.hist(data , bins , weights = weights , histtype = 'step')
plt.yscale('log')
plt.xscale('log')
fig = plt.show()
