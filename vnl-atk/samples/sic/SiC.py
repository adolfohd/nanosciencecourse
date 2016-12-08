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
nlsave('SiC.nc', bulk_configuration)

# -------------------------------------------------------------
# Bandstructure
# -------------------------------------------------------------
bandstructure = Bandstructure(
    configuration=bulk_configuration,
    route=['G', 'X', 'W', 'L', 'G', 'K', 'X', 'U', 'W', 'K', 'L'],
    points_per_segment=100,
    bands_above_fermi_level=All
    )
nlsave('SiC.nc', bandstructure)

# -------------------------------------------------------------
# Electron Density
# -------------------------------------------------------------
electron_density = ElectronDensity(
    configuration=bulk_configuration,
    )
nlsave('SiC.nc', electron_density)