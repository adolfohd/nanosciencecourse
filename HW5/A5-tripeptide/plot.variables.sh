#!/bin/bash


python -i /home/fito/code/nanosciencecourse/lib/pizza-9Oct15/src/pizza.py -f plot.variables.py
gnuplot -e "set style circle radius 1; set terminal pdf;set output 'plot2ii.pdf'; plot 'tempData' using 1:8 with lines"
rm tempData
