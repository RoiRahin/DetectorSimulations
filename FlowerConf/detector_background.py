import sys
import matplotlib.pyplot as plt
import numpy as np


flower_size = int(sys.argv[1])
min_energy = float(sys.argv[2])
max_energy = float(sys.argv[3])
source = open(str(sys.argv[4]) + str(flower_size) +"_flower.background.out" ,'r')
data = []
for line in source:
    data.append(line.split(";"))
source.close()
hit_data=[0 , 0 , 0 , 0 , 0]
# energy_data = [[],[],[],[],[]]
for hit in data:
	if (float(hit[3]) >= min_energy and float(hit[3]) <= max_energy):
		if (float(hit[1]) == 7) :
			hit_data[0] += 1
			# energy_data[0].append(hit[3])
		elif (float(hit[1]) == -7) :
			hit_data[2] += 1
			# energy_data[2].append(hit[3])		
		elif (float(hit[0]) == 7) :
			hit_data[3] += 1
			# energy_data[3].append(hit[3])
		elif (float(hit[0]) == -7) :
			hit_data[1] += 1
			# energy_data[1].append(hit[3])
		else :
			hit_data[4] += 1
			# energy_data[4].append(hit[3])

background = np.array(hit_data[:flower_size])

plt.title(str(flower_size) + " detector configuration background")
plt.xlabel("detector number")
plt.ylabel("Counts/Second")
plt.bar(range(1,flower_size + 1), background/100.0)
plt.xticks(range(1,flower_size + 1))
plt.show()