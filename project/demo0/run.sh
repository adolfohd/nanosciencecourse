#!/bin/bash

rm -rf dump.new.* # erase all previous dump files
lammps -in in.graphene # run simmulation
./vmd.script.sh # generate list of dump files
# python -i ../../lib/pizza-9Oct15/src/pizza.py -f script.py # intended to generate graphene.xyz, which we already have generated
