#make list of relevant temperatures
temperature_list=numpy.linspace(0,2000,21)*Kelvin
#make list of relevant gate voltages
voltage_list=numpy.linspace(0.0,2.0,9)*Volt
#make list to hold the current calculations
current_list=numpy.zeros(len(voltage_list)*len(temperature_list))
current_list=current_list.reshape(len(voltage_list),len(temperature_list))
#specify the filename for the netcdf data file
filename="ivscan.nc"
#loop through the gate voltages
for n in range(len(voltage_list)):
    transmission_spectrum=nlread(filename, object_id="trans"+str(voltage_list[n]))[0]
    #loop through the temperature list
    for i in range(len(temperature_list)):
        current_list[n,i]=transmission_spectrum.current(
            electrode_temperatures=(temperature_list[i],temperature_list[i]))
#plot the current as function of voltage
import pylab
pylab.figure()
# make curve for each temperature
for i in range(len(temperature_list)):
    #    print temperature_list[i]
    pylab.plot(voltage_list,current_list[:,i],label=temperature_list[i])
pylab.xlabel("Bias (V)")
pylab.ylabel("Current (A)")
pylab.legend(loc='lower left')
pylab.show()
