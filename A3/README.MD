# Assignment #3

Los ejercicios que quiero que vayan adelantando con sus respectivas selecciones de programa para el cálculos al nivel de mecánica cuántica (e.g. NWChem, QEspresso, etc. [https://en.wikipedia.org/wiki/List_of_quantum_chemistry_and_solid-state_physics_software](https://en.wikipedia.org/wiki/List_of_quantum_chemistry_and_solid-state_physics_software) https://en.wikipedia.org/wiki/List_of_quantum_chemistry_and_solid-state_physics_software) serían:

# Questions

1. Compute the total energy of the hydrogen atom.
	- How does it change with different basis sets?
2. Now compute the optimized structure and energy of the H2 molecule.
	- How does the binding energy change with basis set?
	- How does the optimized H—H distance change with basis set?
	- Calculate and plot the electron density
	- Visualicen la geometría con Molden en función del cambio de energía sufrido durante minimización. Reporten lo observado.
3. Now let’s do water.
	- What did you choose for the spin state of both H2O and the O atom?
	- What is the computed O—H distance and binding energy?
	- What is the computed H-O-H angle?
	- Can you estimate the angle energy? if yes, do so.
	- Do your results agree with experiment? Why or why not?
4. N2 is one of the strongest bonds in nature.
	- How strong is it?
	- How does it compare with the CO bond in CO2?
5. Which are linear and which are straight/planar: 
	- CO2
	- NH3
	- BH3
	- NH4+

# Hydrogen Atom

## Input File

```
molecule h {
  H
}

# set basis cc-pvdz
set basis dzp
# set basis cc-pwcv_tpd_z
set reference uhf
energy('scf')  # on H
```

## Results


### Basis Set: dzp

```
  ==> Primary Basis <==

  Basis Set: DZP
    Number of shells: 3
    Number of basis function: 5
    Number of Cartesian functions: 5
    Spherical Harmonics?: false
    Max angular momentum: 1

  ==> Iterations <==

                           Total Energy        Delta E     RMS |[F,P]|

   @DF-UHF iter   1:    -0.49407722562233   -4.94077e-01   1.61112e-02 
   @DF-UHF iter   2:    -0.49728383016970   -3.20660e-03   5.08424e-03 DIIS
   @DF-UHF iter   3:    -0.49763724462701   -3.53414e-04   8.12527e-17 DIIS
   @DF-UHF iter   4:    -0.49763724462701    0.00000e+00   2.03132e-17 DIIS

  ==> Post-Iterations <==

   @Spin Contamination Metric:   0.000000000E+00
   @S^2 Expected:                7.500000000E-01
   @S^2 Observed:                7.500000000E-01
   @S   Expected:                5.000000000E-01
   @S   Observed:                5.000000000E-01

   => Energetics <=

    Nuclear Repulsion Energy =              0.0000000000000000
    One-Electron Energy =                  -0.4976372446270106
    Two-Electron Energy =                  -0.0000000000000001
    DFT Exchange-Correlation Energy =       0.0000000000000000
    Empirical Dispersion Energy =           0.0000000000000000
    PCM Polarization Energy =               0.0000000000000000
    EFP Energy =                            0.0000000000000000
    Total Energy =                         -0.4976372446270107
```


### Basis Set: cc-pvdz

```
  ==> Primary Basis <==

  Basis Set: CC-PVDZ
    Number of shells: 3
    Number of basis function: 5
    Number of Cartesian functions: 5
    Spherical Harmonics?: true
    Max angular momentum: 1
  ==> Iterations <==

                           Total Energy        Delta E     RMS |[F,P]|

   @DF-UHF iter   1:    -0.49927002321515   -4.99270e-01   6.38560e-04 
   @DF-UHF iter   2:    -0.49927729076367   -7.26755e-06   2.32679e-04 DIIS
   @DF-UHF iter   3:    -0.49927840341958   -1.11266e-06   4.07205e-17 DIIS
   @DF-UHF iter   4:    -0.49927840341958    0.00000e+00   4.07205e-17 DIIS

  ==> Post-Iterations <==

   @Spin Contamination Metric:   0.000000000E+00
   @S^2 Expected:                7.500000000E-01
   @S^2 Observed:                7.500000000E-01
   @S   Expected:                5.000000000E-01
   @S   Observed:                5.000000000E-01

    => Energetics <=

    Nuclear Repulsion Energy =              0.0000000000000000
    One-Electron Energy =                  -0.4992784034195830
    Two-Electron Energy =                   0.0000000000000000
    DFT Exchange-Correlation Energy =       0.0000000000000000
    Empirical Dispersion Energy =           0.0000000000000000
    PCM Polarization Energy =               0.0000000000000000
    EFP Energy =                            0.0000000000000000
    Total Energy =                         -0.4992784034195830

```

### Basis set: 

```

  ==> Primary Basis <==

  Basis Set: CC-PWCV_TPD_Z
    Number of shells: 6
    Number of basis function: 14
    Number of Cartesian functions: 15
    Spherical Harmonics?: true
    Max angular momentum: 2

  ==> Iterations <==

                           Total Energy        Delta E     RMS |[F,P]|

    Occupation by irrep:
             Ag   B1g   B2g   B3g    Au   B1u   B2u   B3u 
    DOCC [     0,    0,    0,    0,    0,    0,    0,    0 ]
    SOCC [     1,    0,    0,    0,    0,    0,    0,    0 ]

   @DF-UHF iter   1:     1.23325821703274    1.23326e+00   1.51567e-01 
   @DF-UHF iter   2:    -0.47420084802653   -1.70746e+00   1.33259e-02 DIIS
   @DF-UHF iter   3:    -0.49588247211565   -2.16816e-02   5.24527e-03 DIIS
   @DF-UHF iter   4:    -0.49980907054834   -3.92660e-03   8.63121e-05 DIIS
   @DF-UHF iter   5:    -0.49980980920812   -7.38660e-07   7.88566e-06 DIIS
   @DF-UHF iter   6:    -0.49980981130007   -2.09195e-09   2.14571e-07 DIIS

  ==> Post-Iterations <==

   @Spin Contamination Metric:   0.000000000E+00
   @S^2 Expected:                7.500000000E-01
   @S^2 Observed:                7.500000000E-01
   @S   Expected:                5.000000000E-01
   @S   Observed:                5.000000000E-01

      => Energetics <=

    Nuclear Repulsion Energy =              0.0000000000000000
    One-Electron Energy =                  -0.4998098113000718
    Two-Electron Energy =                  -0.0000000000000001
    DFT Exchange-Correlation Energy =       0.0000000000000000
    Empirical Dispersion Energy =           0.0000000000000000
    PCM Polarization Energy =               0.0000000000000000
    EFP Energy =                            0.0000000000000000
    Total Energy =                         -0.4998098113000719
```

# Hydrogen Molecule

## Input file


## Results



### Basis set: cc-pVDZ 

![][h2.cc-pvdz]

```
=> Energetics <=

    Nuclear Repulsion Energy =              0.7071319318497025
    One-Electron Energy =                  -2.4919532844360299
    Two-Electron Energy =                   0.6560744341303761
    DFT Exchange-Correlation Energy =       0.0000000000000000
    Empirical Dispersion Energy =           0.0000000000000000
    PCM Polarization Energy =               0.0000000000000000
    EFP Energy =                            0.0000000000000000
    Total Energy =                         -1.1287469184559513
```





### Basis set: dzp

![][h2.dzp]

```
=> Energetics <=
	Nuclear Repulsion Energy =              0.7222609384611225
    One-Electron Energy =                  -2.5184653046305803
    Two-Electron Energy =                   0.6649544618924614
    DFT Exchange-Correlation Energy =       0.0000000000000000
    Empirical Dispersion Energy =           0.0000000000000000
    PCM Polarization Energy =               0.0000000000000000
    EFP Energy =                            0.0000000000000000
    Total Energy =                         -1.1312499042769963
```


### Basis Set: cc-pwcv_tpd_z

![][h2.cc-pwcv_tpd_z]

```
=> Energetics <=

    Nuclear Repulsion Energy =              0.7205946813745386
    One-Electron Energy =                  -2.5143129880085149
    Two-Electron Energy =                   0.6607201636904894
    DFT Exchange-Correlation Energy =       0.0000000000000000
    Empirical Dispersion Energy =           0.0000000000000000
    PCM Polarization Energy =               0.0000000000000000
    EFP Energy =                            0.0000000000000000
    Total Energy =                         -1.1329981429434868
```






[h2.cc-pVDZ]: psi4/images/h2.cc-pvdz.png
[h2.dzp]: psi4/images/h2.dzp.png
[h2.cc-pwcv_tpd_z]: psi4/images/h2.cc-pwcv_tpd_z.png