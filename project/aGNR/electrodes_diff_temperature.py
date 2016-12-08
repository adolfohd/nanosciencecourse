# Read first transmission spectra from file device.nc and z-a-z-20-6.nc
transmission_spectrum6 = nlread("device.nc",TransmissionSpectrum)[0]
transmission_spectrum20 = nlread("z-a-z-20-6.nc",TransmissionSpectrum)[0]
#make list of temperatures
temperature_list=numpy.linspace(0,2000,21)*Kelvin
#make list for holding current
current_list6=numpy.zeros(len(temperature_list))
current_list20=numpy.zeros(len(temperature_list))
#fix the temperature in the left electrode
temperature_left=300*Kelvin
for i in range(len(temperature_list)):
    current_list6[i]=transmission_spectrum6.current(
        electrode_temperatures=(temperature_left,temperature_list[i]) )
    current_list20[i]=transmission_spectrum20.current(
        electrode_temperatures=(temperature_left,temperature_list[i]) )
#plot the current as function of temperature in right electrode
import pylab
pylab.figure()
pylab.plot(temperature_list,current_list6,label="short junction")
pylab.plot(temperature_list,current_list20,label="long junction")
pylab.xlabel("Right Electrode Temperature (K)")
pylab.ylabel("Current (A)")
pylab.legend(loc="lower left")
pylab.grid(True)
pylab.show()
