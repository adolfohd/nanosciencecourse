# -*- coding: utf-8 -*-
# -------------------------------------------------------------
# Bulk Configuration
# -------------------------------------------------------------

# Set up lattice
lattice = FaceCenteredCubic(4.348*Angstrom)

# Define elements
elements = [Silicon, Carbon]

# Define coordinates
fractional_coordinates = [[ 0.  ,  0.  ,  0.  ],
                          [ 0.25,  0.25,  0.25]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

# -------------------------------------------------------------
# Calculator
# -------------------------------------------------------------
#----------------------------------------
# Exchange-Correlation
#----------------------------------------
exchange_correlation = MGGA.TB09LDA

k_point_sampling = MonkhorstPackGrid(
    na=5,
    nb=5,
    nc=5,
    )
numerical_accuracy_parameters = NumericalAccuracyParameters(
    k_point_sampling=k_point_sampling,
    )

calculator = LCAOCalculator(
    exchange_correlation=exchange_correlation,
    numerical_accuracy_parameters=numerical_accuracy_parameters,
    )

bulk_configuration.setCalculator(calculator)
nlprint(bulk_configuration)
bulk_configuration.update()
nlsave('C:/Users/usuario/Documents/code/nanosciencecourse/vnl-atk/samples/SiC/sic.nc', bulk_configuration)

# -------------------------------------------------------------
# Density Of States
# -------------------------------------------------------------
kpoint_grid = MonkhorstPackGrid(
    na=6,
    nb=6,
    nc=6,
    )

density_of_states = DensityOfStates(
    configuration=bulk_configuration,
    kpoints=kpoint_grid,
    energy_zero_parameter=FermiLevel,
    bands_above_fermi_level=None,
    )
nlsave('C:/Users/usuario/Documents/code/nanosciencecourse/vnl-atk/samples/SiC/sic.nc', density_of_states)
nlprint(density_of_states)

# -------------------------------------------------------------
# Electrostatic Difference Potential
# -------------------------------------------------------------
electrostatic_difference_potential = ElectrostaticDifferencePotential(bulk_configuration)
nlsave('C:/Users/usuario/Documents/code/nanosciencecourse/vnl-atk/samples/SiC/sic.nc', electrostatic_difference_potential)