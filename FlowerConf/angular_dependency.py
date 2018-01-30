import glob
import sys
import matplotlib.pyplot as plt
import numpy as np
import itertools

flower_size = int(sys.argv[1])
min_energy = float(sys.argv[2])
max_energy = float(sys.argv[3])
matsize = len(glob.glob(str(flower_size) + "*.burst.out"))
angular_dependency = np.zeros([matsize , flower_size + 1])
row = 0
for sourcefile in glob.glob(str(flower_size) + "*.burst.out"): 
	source = open(sourcefile , 'rb')
	theta = int(sourcefile.split(".")[0].split("_")[2])
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
	for i in range(1,flower_size + 1):
		angular_dependency[row,i] = float(hit_data[i - 1])
	angular_dependency[row,0] = theta
	row += 1
angular_dependency = angular_dependency[angular_dependency[:,0].argsort()]
angular_relations = np.zeros([matsize , (flower_size * (flower_size-1))/2 + 1])
angular_relations[: , 0] = angular_dependency[:,0]
for i in range (0, matsize):
	angular_relations[i , 1:] = np.array([a/b for a,b in itertools.combinations(angular_dependency[i , range(1,flower_size + 1)] , 2)])

source = open(str(flower_size) + "_flower_test.angle.tst" , 'r')
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

det_relations =  np.array([float(a)/float(b) for a,b in itertools.combinations(hit_data[:flower_size] , 2)])

mse = 1000
deg = -1
for row in angular_relations:
	error = np.sum((det_relations - row[1:])**2)
	print error
	if (error < mse):
		mse = error
		deg = row[0]

print mse
print deg


# for i in range (0,matsize):
# 	angular_relations[0 , i] = angular_dependency[0,i]
# 	angular_relations[1,] = 



# plt.plot(angular_relations[:,0] , angular_relations[: , 1:])
# plt.show()
# # # 