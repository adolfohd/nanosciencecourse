#!/bin/bash

echo $1

# lmp_serial.exe -in in.Al2
lammps -in $1

grep "Length, Energy " log.lammps > l
grep -v "print" l > l1
sed -e 's/Length, Energy (eV and kcal\/mol), pressure = //g' l1 > l2
sort -k1n l2 > eos
rm l l1 l2
python murnaghan.py eos