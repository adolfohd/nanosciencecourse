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

```
memory 250 mb

molecule h2o {
  O 
  H 1 0.96
  H 1 0.96 2 180
}

set basis cc-pVDZ

op, wfn = optimize('hf', return_wfn=True, molecule=h2o)

molden(wfn, "op.molden", density_a=wfn.Da())
```

## Methodology

```
psi4 -i h2.dat -o h2.out

```


```
./psi4ex.py h2.out 
```
This generated a file named *geoms.xyz*. Next, to visualize all optimization steps in Molden:

```
$MOLDEN_PATH geoms.xyz 
```



```
gifsicle --delay=100 --loop moldenfiles*.gif > images/filename.gif
```

## Results



### Basis set: cc-pVDZ 

![][h2.cc-pvdz.movie]
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

![][h2.dzp.gif]
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

# Water

The initial and resulting optimization geometries are:

```
3
           O          0.000000000000     0.000000000000     0.000000000000    15.994914619560
           H          0.000000000000     0.000000000000     0.960000000000     1.007825032070
           H          0.000000000000     0.000000000000    -0.960000000000     1.007825032070
3
           O          0.000000000000     0.000000000000     0.000000000000    15.994914619560
           H          0.000000000000     0.000000000000     0.921033029773     1.007825032070
           H          0.000000000000     0.000000000000    -0.921033029773     1.007825032070
3

           O          0.000000000000     0.000000000000     0.000000000000    15.994914619560
           H          0.000000000000     0.000000000000     0.925290203181     1.007825032070
           H          0.000000000000     0.000000000000    -0.925290203181     1.007825032070
3

           O          0.000000000000     0.000000000000     0.000000000000    15.994914619560
           H          0.000000000000     0.000000000000     0.924748954405     1.007825032070
           H          0.000000000000     0.000000000000    -0.924748954405     1.007825032070
```
An animation of this steps is shown next:

![][h2o.gif]

Although the previous result would greatly differ from the experimentally measured geometry, at least in terms of the angle:


![][realh2o]

This happens because the calculator detected a symmetry in the geomtry we provided. We can fin a better approximation if we nudge one of the hydrogen atoms just a little bit, so the angle is not 180°:

```
memory 250 mb

molecule h2o {
  O 
  H 1 0.96
  H 1 0.96 2 179.9
}

set basis cc-pVDZ

op, wfn = optimize('hf', return_wfn=True, molecule=h2o)

molden(wfn, "op.molden", density_a=wfn.Da())
```

The resulting geometry, that approximates a lot better to the one shown in the previous image, is:

```
Final energy is    -76.0270327800673
	Final (previous) structure:
	Cartesian Geometry (in Angstrom)
	    O     0.0000000000   0.0000000000  -0.0647393695
	    H     0.0000000000  -0.7488413998   0.5137303870
	    H     0.0000000000   0.7488413998   0.5137303870
	Saving final (previous) structure.
			--------------------------
			 OPTKING Finished Execution 
			--------------------------

    Final optimized geometry and variables:
    Molecular point group: c2v
    Full point group: C2v

    Geometry (in Angstrom), charge = 0, multiplicity = 1:

    O
    H             1    0.946251
    H             1    0.946251      2  104.628807
```
A step by step animation of the optimization steps is shown next:

![][h2o.nudged]

**pending**: Angular energy

# Nitrogen molecule

## Input file

With the code shown next, I calculated the atomix energy of nytrogen and then the energy of a $N_2$ molecule.

```
memory 250 mb

molecule n {
  N
}
set basis dzp
set reference uhf
e_n=energy('scf', molecule=n)
print "Nitrogen atom's energy=",e_n


molecule n2 {
  N 
  N 1 1.45
}

set basis cc-pvdz
op, wfn = optimize('hf', return_wfn=True, molecule=n2)

molden(wfn, "n2.molden", density_a=wfn.Da())

e_n2 = energy('scf', molecule=n2)
print "Nitrogen molecule's energy=",e_n2

print "bond energy=", e_n2-2*e_n
```

## Results

When executing this code, the results are:

### Basis set: dzp

```
$ psi4 -i n2.dat -o n2.out 
Nitrogen atom's energy= -54.2591265885
Optimizer: Optimization complete!
Nitrogen molecule's energy= -108.955259424
bond energy= -0.437006247261
```
In literature, bond energy for nitrogen is reported as $226 \frac{kcal}{mol}$, which equals:

$226 \frac{kcal}{mol}=0.3602 Hartree$

So we have a different level. Let's try with other basis sets


### Basis set: cc-pvdz

```
$ psi4 -i n2.dat -o n2.out 

Nitrogen atom's energy= -54.2516556453
Optimizer: Optimization complete!
Nitrogen molecule's energy= -108.955259424
bond energy= -0.451948133562
```

### Basis set: cc-pwcv_tpd_z

```
$ psi4 -i n2.dat -o n2.out 
Nitrogen atom's energy= -54.2639929677
Optimizer: Optimization complete!
Nitrogen molecule's energy= -108.955259424
bond energy= -0.427273488756
```

## Conclusion


$error_{{DZP}}=\frac{0.437-0.3602}{0.3602}\approx 21\% $ 


# Linear VS planar estructures

# CO2

Given the next geometry

```
molecule co2 {
  C 
  O 1 0.96
  O 1 1.20 2 90
}
```

and after optimizing it, we have the next result:

```
    Geometry (in Angstrom), charge = 0, multiplicity = 1:

    C       
    O             1    1.297446
    O             1    1.297136      2   69.133888
```

```
molecule co2 {
  C 
  O 1 0.96
  O 1 1.20 2 60
}

    Geometry (in Angstrom), charge = 0, multiplicity = 1:

    C       
    O             1    1.297054
    O             1    1.297134      2   69.137257
```

```
molecule co2 {
  C 
  O 1 0.96
  O 1 1.20 2 120
}

    Geometry (in Angstrom), charge = 0, multiplicity = 1:

    C       
    O             1    1.140523
    O             1    1.140537      2  179.994584
```




# NH3

# BH3

# NH4+


[h2.cc-pVDZ]: psi4/images/h2.cc-pvdz.png
[h2.cc-pvdz.movie]: psi4/images/h2.cc-pvdz.gif


[h2.dzp]: psi4/images/h2.dzp.png
[h2.dzp.gif]: psi4/images/h2.dzp.gif

[h2.cc-pwcv_tpd_z]: psi4/images/h2.cc-pwcv_tpd_z.png
[h2o.gif]: psi4/images/h2o.gif

[realh2o]: psi4/images/Water-2D_angl_Wiki.png
[h2o.nudged]: psi4/images/h2o.nudged.gif
