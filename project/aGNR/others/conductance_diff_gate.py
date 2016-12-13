#conf
carbon_body = '60'
fin = 'Device T_11_9_11_12_'+carbon_body+'_Grande_calcAJB.nc'
#specify the filename for the netcdf data file
filename= 'gatescan_' + carbon_body + '.nc'


#make list of relevant temperatures
temperature_list=numpy.linspace(250,350,11)*Kelvin

#make list of relevant gate voltages
gate_voltage_list=numpy.linspace(-2.0,2.0,17)*Volt

#make list to hold the conductance calculations
conductance_list=numpy.zeros(len(gate_voltage_list)*len(temperature_list))
conductance_list=conductance_list.reshape(len(gate_voltage_list),
                                          len(temperature_list))
#loop through the gate voltages
for n in range(len(gate_voltage_list)):
    transmission_spectrum=nlread(filename,
        object_id="trans"+str(gate_voltage_list[n]))[0]
    #loop through the temperature list
    for i in range(len(temperature_list)):
        conductance_list[n,i]=transmission_spectrum.conductance(
            electrode_temperatures=(temperature_list[i],temperature_list[i]))
#plot the conductance as function of gatevoltage
import pylab
pylab.figure()
# make curve for each temperature
for i in range(len(temperature_list)):
    pylab.semilogy(gate_voltage_list,conductance_list[:,i],label=temperature_list[i])
pylab.xlabel("Gate Voltage (V)")
pylab.ylabel("Conductance (S)")
pylab.legend(loc="lower left")
pylab.show()
