import numpy as np

def get_background(min_energy , max_energy):
	source = open("full_conf.background" ,'r')
	data = []
	for line in source:
	    data.append(line.split(";"))
	source.close()
	hit_data=[0.0 , 0.0 , 0.0 , 0.0 , 0.0]

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

	background = np.array(hit_data)
	return background/1000

