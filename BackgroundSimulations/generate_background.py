import sys
import numpy as np
import matplotlib.pyplot as plt

low_energies = np.arange(3 , 60 , 1)
high_energies = np.arange(60,1001,1)

low_energy_flux_power = np.power(low_energies , -1.29)
low_energy_flux_exp = np.exp(np.multiply(low_energies , -1/41.13))
low_energies_flux_non_norm = np.multiply(low_energy_flux_exp , low_energy_flux_power)
low_energies_flux = [7.877 * x for x in low_energies_flux_non_norm]

high_energies_flux_one = np.power(np.multiply(high_energies , 3.2936/60) , -6.5)
high_energies_flux_two = np.power(np.multiply(high_energies , 6.3759/60) , -2.58)
high_energies_flux_three = np.power(np.multiply(high_energies , 41.5821/60) , -2.05)
high_energies_flux = np.add(high_energies_flux_one , high_energies_flux_two)
high_energies_flux = np.add(high_energies_flux , high_energies_flux_three)
energies = np.append(low_energies , high_energies)
total_flux = np.append(low_energies_flux , high_energies_flux)

output = open("background.input" , 'w')
output.write("IP\tLIN\n")
for (e,f) in zip (energies , total_flux):
	output.write("DP\t" + str(e) + '\t' + str(f) + '\n')

output.write("EN")
output.close()

plt.loglog(energies , total_flux)
plt.show()
