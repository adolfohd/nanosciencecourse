#!/bin/sh -f
#SBATCH -n 8                    # Number of cores
#SBATCH -N 1                    # Ensure that all cores are on one machine
#SBATCH -t 10-00:00              # Runtime in D-HH:MM
#SBATCH -p full       # Partition to submit to
### SBATCH --mem=100               # Memory pool for all cores (see also --mem-per-cpu)
#SBATCH -o hydra_%j.out      # File to which STDOUT will be written
#SBATCH -e hydra_%j.err      # File to which STDERR will be written
#SBATCH --mail-type=END         # Type of email notification- BEGIN,END,FAIL,ALL
#SBATCH --mail-user=adolfo.hoyos@javerianacali.edu.co # Email to which notifications will be sent

case "$1" in
    "1")  echo "running: GNR device";
        mpirun -np 8 atkpython DeviceGNR.py
        exit 0;;
    "2")  echo "running: GNR + glucose"
        mpirun -np 8 atkpython device.glucose.script.py
        exit 0;;
    "3")  echo "running: Non customized GNR "
        mpirun -np 8 atkpython device.script.nocustom.py
        exit 0;;
    "4")  echo "running: Non customized GNR + glucose (far?)"
        mpirun -np 8 atkpython device.glucose.script_nocustom.py
        exit 0;;
    *)
        echo "error, select an ATK script to run"
        exit 2;;
esac