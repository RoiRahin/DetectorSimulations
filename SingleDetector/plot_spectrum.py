import glob
import sys
import matplotlib.pyplot as plt 
import numpy as np 

source = open(sys.argv[1] , 'r')

data = []
for line in source:
	data.append(float(line))

bins = np.linspace(0,1000,1000)
plt.hist(data , bins  , histtype = 'step')
plt.yscale('log')
plt.xscale('log')
fig = plt.show()