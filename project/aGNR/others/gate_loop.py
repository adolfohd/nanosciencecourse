#read in the old configuration
device_configuration = nlread("z-a-z-6-6.nc",DeviceConfiguration)[0]
calculator = device_configuration.calculator()
metallic_region0 = device_configuration.metallicRegions()[0]
# Define gate_voltages
gate_voltage_list=numpy.linspace(-2.0,2.0,17)*Volt
for gate_voltage in gate_voltage_list:
    # set the gate potential
    device_configuration.setMetallicRegions(
        [metallic_region0(value = gate_voltage)] )
    # make a copy of the calculator and attach it to the configuration
    # restart from the previous scf state
    device_configuration.setCalculator(calculator(),
        initial_state=device_configuration)
    #Analysis
    filename= 'gatescan-6-6.nc'
    electron_density = ElectronDifferenceDensity(device_configuration)
    nlsave(filename, electron_density,object_id='dens'+str(gate_voltage))
    electrostatic_potential = ElectrostaticDifferencePotential(device_configuration)
    nlsave(filename, electrostatic_potential, object_id='pot'+str(gate_voltage))
    transmission_spectrum = TransmissionSpectrum(
        configuration=device_configuration,
        energies=numpy.linspace(-2,2,200)*eV,
        )
    nlsave(filename, transmission_spectrum,object_id='trans'+str(gate_voltage))
    nlprint(transmission_spectrum)
