import sys
import numpy as np
from scipy import interpolate
from full_conf_background import get_background

flower_size = 5
min_energy = int(sys.argv[1])
max_energy = int(sys.argv[2])
orig_theta = int(sys.argv[3])
orig_phi = int(sys.argv[4])
angular_dependency=np.load("angular_dependency_"+str(min_energy)+"_"+str(max_energy)+".npy")

angular_dependency = angular_dependency[angular_dependency[:,0].argsort()]

angular_dependency[:,2:] = np.array([row/np.sum(row) for row in angular_dependency[:,2:]])
angular_dep_mat = np.zeros((19,72,5))
theta_vec = set([])
phi_vec = set([])
for row in angular_dependency:
	theta_vec.add(row[0])
	phi_vec.add(row[1])
	angular_dep_mat[int(row[0]/5) , int(row[1]/5),:] = row[2:]


angular_dep_mat[0,:,:] = angular_dep_mat[0,0,:]
theta_vec = np.array(list(theta_vec))
theta_vec.sort()
phi_vec = np.array(list(phi_vec))
phi_vec.sort()
interp_theta = np.arange(0,90.1,0.1)
interp_phi = np.arange(0,360,0.1)
interp_dep_f = [[],[],[],[],[]]
for i in range(0,5):
	interp_dep_f[i] = interpolate.RectBivariateSpline(theta_vec , phi_vec, angular_dep_mat[:,:,i])


testfile = (sys.argv[5])
source = open(testfile, 'r')
data = []
for line in source:
    data.append(line.split(";"))
source.close()
hit_data=[0 , 0 , 0 , 0 , 0]
for hit in data:
	if (float(hit[3]) >= min_energy and float(hit[3]) <= max_energy):
		if (float(hit[1]) > 7) :
			hit_data[0] += 1
		elif (float(hit[1]) < -7) :
			hit_data[2] += 1		
		elif (float(hit[0]) > 7) :
			hit_data[3] += 1
		elif (float(hit[0]) < -7) :
			hit_data[1] += 1
		else :
			hit_data[4] += 1
measurement = np.array([float(a) for a in hit_data[:flower_size]])
background = get_background(min_energy,max_energy)
measurement_m_background = measurement - 2*background
total_hits = np.sum(measurement)
total_hits_m_background = np.sum(measurement_m_background)
mesh_theta , mesh_phi = np.meshgrid(interp_theta , interp_phi , indexing='ij')
mse = 1000000
deg = -1

interp_dep = np.zeros((len(interp_theta) , len(interp_phi) , flower_size))
for i in range(0,5):
	interp_dep[:,:,i] = interp_dep_f[i](interp_theta,interp_phi)

meas_mat = np.ones_like(interp_dep)*measurement_m_background
chi_square = np.sum((meas_mat - interp_dep * total_hits_m_background)**2 / measurement , axis = 2)
output = np.array([mesh_theta[np.unravel_index(np.argmin(chi_square), chi_square.shape)] , mesh_phi[np.unravel_index(np.argmin(chi_square), chi_square.shape)]])
print np.append(np.array([orig_theta,orig_phi]),a)