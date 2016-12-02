#!/bin/bash

# for i in $(ls -1v dump*) ; do printf "mol addfile %s waitfor all\n" $i ; done > script.tcl

for i in $(ls -1v dump*) ; do printf "mol addfile %s waitfor all type lammpstrj\n" $i ; done > script.tcl
