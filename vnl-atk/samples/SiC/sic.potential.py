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
# Analysis from File
# -------------------------------------------------------------
path = u'C:/Users/usuario/Documents/code/nanosciencecourse/vnl-atk/samples/SiC/sic.nc'
configuration = nlread(path, object_id='gID000')[0]

# -------------------------------------------------------------
# Electrostatic Difference Potential
# -------------------------------------------------------------
electrostatic_difference_potential = ElectrostaticDifferencePotential(bulk_configuration)
nlsave('C:/Users/usuario/Documents/code/nanosciencecourse/vnl-atk/samples/SiC/sic.nc', electrostatic_difference_potential)

# -------------------------------------------------------------
# Density Of States
# -------------------------------------------------------------
kpoint_grid = MonkhorstPackGrid(
    na=11,
    nc=11,
    )

density_of_states = DensityOfStates(
    configuration=bulk_configuration,
    kpoints=kpoint_grid,
    energy_zero_parameter=FermiLevel,
    bands_above_fermi_level=None,
    )
nlsave('C:/Users/usuario/Documents/code/nanosciencecourse/vnl-atk/samples/SiC/sic.nc', density_of_states)
nlprint(density_of_states)