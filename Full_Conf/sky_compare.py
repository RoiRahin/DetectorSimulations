import glob
import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate
from mpl_toolkits.mplot3d import Axes3D

min_energy = int(sys.argv[1])
max_energy = int(sys.argv[2])
flux = float(sys.argv[3])
maxdeg = 90
if (len(sys.argv) > 4):
	maxdeg = float(sys.argv[4])

if (len(sys.argv) == 6):
	location = sys.argv[5]
	files = glob.glob(location +"*.burst.out")
	matsize = len(files)
	angular_dependency = np.zeros([matsize , 7])
	row = 0
	filesleft = len(files)
	for sourcefile in files: 
		print filesleft
		filesleft -= 1
		source = open(sourcefile , 'rb')
		theta = int(sourcefile.split(".")[-3].split("_")[-2])
		phi = int(sourcefile.split(".")[-3].split("_")[-1])
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
		for i in range(2,7):
			angular_dependency[row,i] = float(hit_data[i - 2])
		angular_dependency[row,0] = theta
		angular_dependency[row,1] = phi
		row += 1
	angular_dependency = angular_dependency[angular_dependency[:,1].argsort()]
	angular_dependency = angular_dependency[angular_dependency[:,0].argsort()]
	# angular_dependency[:,1:] = np.array([row/np.sum(row) for row in angular_dependency[:,1:]])
	# Aeff = np.array([x/flux/45.6 for x in np.sum(angular_dependency[:,2:] , axis = 1)])
	# print Aeff
	# Aeff_sin_t = Aeff*np.sin(angular_dependency[:,0])
	np.save("angular_dependency.npy",angular_dependency)
else:
	angular_dependency=np.load("angular_dependency.npy")
Aeff_mat = np.zeros((19 ,72))
for row in angular_dependency:
	if (row[0] <= maxdeg):
		theta = row[0]*np.pi/180
		phi = row[1]*np.pi/180
		Aeff = np.sum(row[2:]/flux/45.6) * np.sin(theta)
		Aeff_mat[int(row[0]/5) , int(row[1]/5)] = Aeff

Aeff_mat[0,:] = Aeff_mat[0,0]
dt =  5*np.pi/180
grasp =  integrate.simps(integrate.simps(Aeff_mat , dx = dt), dx = dt)
print grasp
print grasp/(1-np.cos(maxdeg*np.pi/180))/2/np.pi

grasp_no_wall = integrate.simps(integrate.simps(Aeff_mat[:,18:54] , dx = dt), dx = dt)

print grasp_no_wall

grasp_wall = grasp - grasp_no_wall

print grasp_wall 

coincidence = np.zeros((19,73,5))

for row in angular_dependency:
	theta = row[0]*np.pi/180
	phi = row[1]*np.pi/180
	coincidence[int(row[0]/5) , int(row[1]/5),:] = (row[2:]/flux/45.6>0.33).astype(int)

coincidence[0,:,:] = coincidence[0,0,:]

coincidence = (np.sum(coincidence,axis = 2) > 1).astype(int)
print coincidence
X1,X2 = np.meshgrid(np.arange(0,361,5),np.arange(0,91,5))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X1,X2,coincidence,cmap="coolwarm")
plt.show()
