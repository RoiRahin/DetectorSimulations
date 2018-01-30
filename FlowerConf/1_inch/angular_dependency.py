import glob

for sourcefile in glob.glob("5*.burst.out"): 
	source = open(sourcefile , 'rb')
	theta = int(sourcefile.split(".")[0].split("_")[2])
	data = []
	for line in source:
	    data.append(line.split(";"))
	source.close()
	hit_data=[0 , 0 , 0 , 0 , 0]
	energy_data = [[],[],[],[],[]]
	for hit in data:
		if (float(hit[1]) == 7) :
			hit_data[0] += 1
			energy_data[0].append(hit[3])
		elif (float(hit[1]) == -7) :
			hit_data[2] += 1
			energy_data[2].append(hit[3])		
		elif (float(hit[0]) == 7) :
			hit_data[3] += 1
			energy_data[3].append(hit[3])
		elif (float(hit[0]) == -7) :
			hit_data[1] += 1
			energy_data[1].append(hit[3])
		else :
			hit_data[4] += 1
			energy_data[4].append(hit[3])

	print energy_data

