# Read first transmission spectrum from file device.nc
transmission_spectrum = nlread("ivscan.nc",TransmissionSpectrum)[0]
#make list of temperatures
temperature_list=numpy.linspace(0,2000,21)*Kelvin
#make list for holding conductance
conductance_list=numpy.zeros(len(temperature_list))
#calculate the conductance for each temperature in the temperature list
for i in range(len(temperature_list)):
    conductance_list[i]=transmission_spectrum.conductance(
        electrode_temperatures=(temperature_list[i], temperature_list[i]))
#plot the conductance as function of temperature
import pylab
pylab.figure()
pylab.semilogy(temperature_list,conductance_list)
pylab.xlabel("Temperature (K)")
pylab.ylabel("Conductance (S)")
pylab.show()
