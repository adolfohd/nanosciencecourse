#!/bin/bash

echo $1
echo $2
# lmp_serial.exe -in in.Al2
lammps < $1 > $2
grep "length, pre" log.lammps | grep -v "print" > l  


# grep "length, pressure =" log.lammps > l
# grep -v "print" l > l1
sed -e 's/length, pressure = //g' l > l1
sort -k1n l1 > eos

gnuplot -e "load 'plot.p'"


evince young.pdf
# rm l l1 l2
# python murnaghan.py eos

# rm out*
# rm l
# rm l1