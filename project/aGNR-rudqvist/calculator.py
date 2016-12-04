# -------------------------------------------------------------
# Calculator
# -------------------------------------------------------------
#----------------------------------------
# Basis Set
#----------------------------------------
basis_set = [
    HoffmannHuckelParameters.Hydrogen_Basis,
    CerdaHuckelParameters.Carbon_graphite_Basis,
    ]

#----------------------------------------
# Numerical Accuracy Settings
#----------------------------------------
left_electrode_k_point_sampling = MonkhorstPackGrid(
    nc=50,
    )
left_electrode_numerical_accuracy_parameters = NumericalAccuracyParameters(
    k_point_sampling=left_electrode_k_point_sampling,
    )

right_electrode_k_point_sampling = MonkhorstPackGrid(
    nc=50,
    )
right_electrode_numerical_accuracy_parameters = NumericalAccuracyParameters(
    k_point_sampling=right_electrode_k_point_sampling,
    )

device_k_point_sampling = MonkhorstPackGrid(
    nc=50,
    )
device_numerical_accuracy_parameters = NumericalAccuracyParameters(
    k_point_sampling=device_k_point_sampling,
    )

#----------------------------------------
# Iteration Control Settings
#----------------------------------------
left_electrode_iteration_control_parameters = IterationControlParameters()

right_electrode_iteration_control_parameters = IterationControlParameters()

device_iteration_control_parameters = IterationControlParameters()

#----------------------------------------
# Poisson Solver Settings
#----------------------------------------
left_electrode_poisson_solver = MultigridSolver(
    boundary_conditions=[[NeumannBoundaryCondition(),NeumannBoundaryCondition()],
                         [NeumannBoundaryCondition(),NeumannBoundaryCondition()],
                         [PeriodicBoundaryCondition(),PeriodicBoundaryCondition()]]
    )

right_electrode_poisson_solver = MultigridSolver(
    boundary_conditions=[[NeumannBoundaryCondition(),NeumannBoundaryCondition()],
                         [NeumannBoundaryCondition(),NeumannBoundaryCondition()],
                         [PeriodicBoundaryCondition(),PeriodicBoundaryCondition()]]
    )

device_poisson_solver = MultigridSolver(
    boundary_conditions=[[NeumannBoundaryCondition(),NeumannBoundaryCondition()],
                         [NeumannBoundaryCondition(),NeumannBoundaryCondition()],
                         [DirichletBoundaryCondition(),DirichletBoundaryCondition()]]
    )

#----------------------------------------
# Device Algorithm Settings
#----------------------------------------
initial_density_type = EquivalentBulk(
    electrode_constraint_length=10.0*Angstrom,
    )

device_algorithm_parameters = DeviceAlgorithmParameters(
    initial_density_type=initial_density_type,
    )

#----------------------------------------
# Electrode Calculators
#----------------------------------------
left_electrode_calculator = HuckelCalculator(
    basis_set=basis_set,
    numerical_accuracy_parameters=left_electrode_numerical_accuracy_parameters,
    iteration_control_parameters=left_electrode_iteration_control_parameters,
    poisson_solver=left_electrode_poisson_solver,
    )

right_electrode_calculator = HuckelCalculator(
    basis_set=basis_set,
    numerical_accuracy_parameters=right_electrode_numerical_accuracy_parameters,
    iteration_control_parameters=right_electrode_iteration_control_parameters,
    poisson_solver=right_electrode_poisson_solver,
    )

#----------------------------------------
# Device Calculator
#----------------------------------------
calculator = DeviceHuckelCalculator(
    basis_set=basis_set,
    numerical_accuracy_parameters=device_numerical_accuracy_parameters,
    iteration_control_parameters=device_iteration_control_parameters,
    poisson_solver=device_poisson_solver,
    device_algorithm_parameters=device_algorithm_parameters,
    electrode_calculators=
        [left_electrode_calculator, right_electrode_calculator],
    )

device_configuration.setCalculator(calculator)
nlprint(device_configuration)
device_configuration.update()
nlsave('device.nc', device_configuration)

# -------------------------------------------------------------
# Electron Difference Density
# -------------------------------------------------------------
electron_difference_density = ElectronDifferenceDensity(device_configuration)
nlsave('device.nc', electron_difference_density)

# -------------------------------------------------------------
# Electrostatic Difference Potential
# -------------------------------------------------------------
electrostatic_difference_potential = ElectrostaticDifferencePotential(device_configuration)
nlsave('device.nc', electrostatic_difference_potential)

# -------------------------------------------------------------
# Transmission Spectrum
# -------------------------------------------------------------
kpoint_grid = MonkhorstPackGrid()

transmission_spectrum = TransmissionSpectrum(
    configuration=device_configuration,
    energies=numpy.linspace(-2,2,200)*eV,
    kpoints=kpoint_grid,
    energy_zero_parameter=AverageFermiLevel,
    infinitesimal=1e-06*eV,
    self_energy_calculator=RecursionSelfEnergy(),
    )
nlsave('device.nc', transmission_spectrum)
nlprint(transmission_spectrum)
