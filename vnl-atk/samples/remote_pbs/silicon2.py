# -------------------------------------------------------------
# Bulk Configuration
# -------------------------------------------------------------

# Set up lattice
lattice = FaceCenteredCubic(5.4306*Angstrom)

# Define elements
elements = [Silicon, Silicon]

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
numerical_accuracy_parameters = NumericalAccuracyParameters(
    k_point_sampling=(5, 5, 5),
    )

calculator = LCAOCalculator(
    numerical_accuracy_parameters=numerical_accuracy_parameters,
    )

bulk_configuration.setCalculator(calculator)
nlprint(bulk_configuration)
bulk_configuration.update()
nlsave('Silicon_alpha.nc', bulk_configuration)
