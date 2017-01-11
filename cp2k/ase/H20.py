#!/usr/bin/python
from ase.calculators.cp2k import CP2K
from ase.structure import molecule
calc = CP2K(debug=True)
atoms = molecule('H2O', calculator=calc)
atoms.center(vacuum=2.0)
print(atoms.get_potential_energy())
