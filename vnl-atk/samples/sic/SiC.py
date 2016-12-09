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
nlsave('/media/fito/Windows/Users/fitoh/Documents/code/nanosciencecourse/vnl-atk/samples/sic/SiC.nc', bulk_configuration)

# -------------------------------------------------------------
# Electron Density
# -------------------------------------------------------------
electron_density = ElectronDensity(
    configuration=bulk_configuration,
    )
nlsave('/media/fito/Windows/Users/fitoh/Documents/code/nanosciencecourse/vnl-atk/samples/sic/SiC.nc', electron_density)