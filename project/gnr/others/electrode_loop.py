# Read in the old configuration
device_configuration = nlread("device.nc",DeviceConfiguration)[0]
calculator = device_configuration.calculator()
# Output filename
filename = 'ivscan.nc'
# Define bias voltages
voltage_list=numpy.linspace(0.0,2.0,9)*Volt
for voltage in voltage_list:
    # Set new calculator with modified electrode voltages on the configuration
    # use the self consistent state of the old calculation as starting input.
    device_configuration.setCalculator(
    calculator(electrode_voltages=(-0.5*voltage,0.5*voltage)),
               initial_state=device_configuration)
    #Analysis
    electron_density = ElectronDifferenceDensity(device_configuration)
    nlsave(filename, electron_density, object_id='dens'+str(voltage))
    electrostatic_potential = ElectrostaticDifferencePotential(device_configuration)
    nlsave(filename, electrostatic_potential, object_id='pot'+str(voltage))
    transmission_spectrum = TransmissionSpectrum(
        configuration=device_configuration,
        energies=numpy.linspace(-2,2,200)*eV)
    nlsave(filename, transmission_spectrum, object_id='trans'+str(voltage))
    nlprint(transmission_spectrum)
