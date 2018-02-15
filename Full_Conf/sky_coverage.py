import glob
import sys
import matplotlib.pyplot as plt
import numpy as np

min_energy = int(sys.argv[1])
max_energy = int(sys.argv[2])
filename1 = sys.argv[3] + "full_conf_*_0.burst.out"
filename2 = sys.argv[3] + "full_conf_*_180.burst.out"
files = glob.glob(filename1) + glob.glob(filename2)
matsize = len(files)
angular_dependency = np.zeros([matsize , 6])
row = 0
for sourcefile in files: 
	source = open(sourcefile , 'rb')
	print sourcefile.split(".")[-3]
	theta = int(sourcefile.split(".")[-3].split("_")[-2])
	phi = int(sourcefile.split(".")[-3].split("_")[-1])
	if (phi == 0):
		theta = -theta
	data = []
	for line in source:
	    data.append(line.split(";"))
	source.close()
	hit_data=[0 , 0 , 0 , 0 , 0]
	# energy_data = [[],[],[],[],[]]
	for hit in data:
		if (float(hit[3]) >= min_energy and float(hit[3]) <= max_energy):
			if (float(hit[1]) > 7) :
				hit_data[0] += 1
				# energy_data[0].append(hit[3])
			elif (float(hit[1]) < -7) :
				hit_data[2] += 1
				# energy_data[2].append(hit[3])		
			elif (float(hit[0]) > 7) :
				hit_data[3] += 1
				# energy_data[3].append(hit[3])
			elif (float(hit[0]) < -7) :
				hit_data[1] += 1
				# energy_data[1].append(hit[3])
			else :
				hit_data[4] += 1
				# energy_data[4].append(hit[3])
	for i in range(1,6):
		angular_dependency[row,i] = float(hit_data[i - 1])
	angular_dependency[row,0] = theta
	row += 1
angular_dependency = angular_dependency[angular_dependency[:,0].argsort()]
# angular_dependency[:,1:] = np.array([row/np.sum(row) for row in angular_dependency[:,1:]])
plt.plot(angular_dependency[:,0] , angular_dependency[:,1:]/1000)
plt.plot(angular_dependency[:,0] , np.sum(angular_dependency[:,1:]/1000 , axis = 1))
plt.legend(['detector 1' ,'detector 2','detector 3','detector 4','detector 5' , 'total'])
plt.xlabel(r'$\theta$')
plt.title('sky coverage for energy band ['+str(min_energy) + " "+str(max_energy)+"] KeV")
plt.ylabel(r'count rate Counts/Second')
plt.show() 
