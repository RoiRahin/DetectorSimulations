import numpy as np 
import sys
import matplotlib.pyplot as plt
import math

# based on Band et al. 1993
# Note: The burst will not be normalized because normalization is set by the cosima simulation anyway
if (len(sys.argv) < 4):
	print "usage: GenerateBurst.py <low energy photon spectral index> <high energy photon spectral index> <Peak energy>"
	quit()

alpha = -float(sys.argv[1])
beta = -float(sys.argv[2])
Ep = float(sys.argv[3])

if (alpha > 0 or beta > 0 or alpha < beta or Ep < 0):
	print "Impossible values. All inputs must be positive and the absolute value of high energy photon index must be higher than the absolute value of low energy photon index"
	quit()

E0 = Ep / (2 + alpha)

low_energies = np.arange(10 , (alpha - beta) * E0, 1)
high_energies = np.arange((alpha - beta) * E0,1000,1)

low_energy_flux_power = np.power(low_energies , alpha)
low_energy_flux_exp = np.exp(np.multiply(low_energies , -1/E0))
low_energy_flux = np.multiply(low_energy_flux_power , low_energy_flux_exp)

high_energy_flux_power = np.power(high_energies , beta)
high_energy_const = math.exp(beta-alpha) * (((alpha - beta) * E0) ** (alpha - beta))
high_energy_flux = np.multiply(high_energy_flux_power , high_energy_const)
energies = np.append(low_energies , high_energies)
total_flux = np.append(low_energy_flux , high_energy_flux)

filename = "Burst_" + str(-alpha)+"_" + str(-beta) + "_" + str(Ep) + ".flux"
fluxfile = open(filename , 'w')
fluxfile.write("IP\tLIN\n")
for (e,f) in zip (energies , total_flux):
	fluxfile.write("DP\t" + str(e) + '\t' + str(f) + '\n')


plt.loglog(energies , total_flux)
plt.show()
