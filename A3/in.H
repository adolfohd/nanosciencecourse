&CONTROL
  calculation  = "relax",
  prefix       = "H",
  pseudo_dir   = "pseudo/"
  outdir       = "log/"
/
&SYSTEM
  ibrav     = 0,
  nat       = 1,
  ntyp      = 1,
  ecutwfc   = 24.D0,
  ecutrho   = 144.D0,
  occupations="smearing"
  smearing  = "gaussian"
  degauss   = 0.01
/
&ELECTRONS
  conv_thr    = 1.D-7,
  mixing_beta = 0.7D0,
/
&IONS
/
CELL_PARAMETERS cubic
12.0  0.0  0.0
 0.0 12.0  0.0
 0.0  0.0 12.0
ATOMIC_SPECIES
H 1.00 H.coulomb-ae.UPF

K_POINTS {Gamma}

ATOMIC_POSITIONS {bohr}
H 0 0 0

