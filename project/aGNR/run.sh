#!/bin/bash
#SBATCH -n 8                    # Number of cores
#SBATCH -N 1                    # Ensure that all cores are on one machine
#SBATCH -t 10-00:05              # Runtime in D-HH:MM
#SBATCH -p serial_requeue       # Partition to submit to
#SBATCH --mem=100               # Memory pool for all cores (see also --mem-per-cpu)
#SBATCH -o hydra_%j.out      # File to which STDOUT will be written
#SBATCH -e hydra_%j.err      # File to which STDERR will be written
#SBATCH --mail-type=END         # Type of email notification- BEGIN,END,FAIL,ALL
#SBATCH --mail-user=adolfo.hoyos@javerianacali.edu.co # Email to which notifications will be sent

mpirun -np 8 atkpython DeviceGNR.py
