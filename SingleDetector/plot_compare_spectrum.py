import matplotlib.pyplot as plt
import numpy as np
import sys

fig = plt.figure()

for name in sys.argv[1:]:
	source = open(name , 'r')

	data = []
	for line in source:
		data.append(float(line))

	bins = np.linspace(0,1000,10)
	weights = [1/2.0] * len(data)
	ax = fig.add_subplot(111)
	ax.hist(data , bins  ,weights = weights, histtype = 'step' , label = name)
	plt.yscale('log')
	plt.xscale('log')
	source.close()
ax.legend()
ax.set_ylabel(r'Photon $s^{-1}$')
ax.set_xlabel(r'E[Kev]')
plt.show()

