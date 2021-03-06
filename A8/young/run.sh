#!/bin/bash
rm fit.log
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

# latex young.tex

evince young.pdf &
#  young.dvi &
# rm youn.tex young.log l l1 fit.log

rm l l1 log.lammps fit.log 
# python murnaghan.py eos

# rm out*
# rm l
# rm l1