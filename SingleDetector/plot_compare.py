import matplotlib.pyplot as plt
import numpy as np
import sys

fig = plt.figure()

for name in sys.argv[1:]:
	source = open(name , 'r')
	data = []
	for line in source:
		data.append(float(line))


	zenith_hit = data[0]
	norm_data = [x/zenith_hit for x in data]
	deg = np.linspace(0,90,num=len(norm_data))
	ax = fig.add_subplot(111)
	line, = ax.plot(deg,norm_data)
	line.set_label(name)
	source.close()
ax.legend()
plt.show()

