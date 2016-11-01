#!/bin/bash

echo $1
echo $2
# lmp_serial.exe -in in.Al2
lammps < $1 > $2

grep "length, pressure =" log.lammps > l
grep -v "print" l > l1
sed -e 's/Length, Energy (eV and kcal\/mol), pressure = //g' l1 > l2
sort -k1n l2 > eos
rm l l1 l2
# python murnaghan.py eos