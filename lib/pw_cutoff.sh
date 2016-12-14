#! /bin/bash

## pw_cutoff
## Check the convergence of the wavefunction of a given
## pseudopotential in Quantum Espresso
##
##   By Julen Larrucea  julen@larrucea.eu
##

VERSION=1.1


PWD=$(pwd -P )
PSEUDO_DIR="."
USPP=false

while getopts f:x:m:p:s:v opt
do
   case "$opt" in
      f) PSP_ARG=$OPTARG;;
      x) BIN=$OPTARG;;
      m) MPI=$OPTARG;;
      p) PO="yes";;
      s) SP="yes";;
      v) echo "resend version " $VERSION; exit 1;; 
      \?) echo """   resend usage:
    -f  Name of the pseudopotential file in current directory
        or path to it.
    -x  path to the pw.x binary (if not in the \$PATH)
    -m  MPI driver with options (i.e. "mpirun -np 8")
    -p  Plot Only. It assumes the calculation is already done previously
    -s  Save picture
    -v  Print version
    -h  print this help 
   Example: pw_cutoff.sh -f ~/pwpsp/H.pz-rrkjus.UPF -x ~/QE/bin/pw.x -m "mpirun -np 8"
 """
     exit 1  ;;
   esac
done

echo "    pw_cutoff.sh v." $VERSION
echo "    -------------------" 

# Parse PSP file and path
if [ -z "$PSP_ARG" ]; then  
  echo "Provide a pseudopotential file name!"
  exit
else
  PSEUDO_DIR=$( dirname $PSP_ARG )"/"
  PSEUDO=$( basename $PSP_ARG ) 
fi

# Check for pw.x binary
PW_BIN=`which pw.x 2>/dev/null`

if [ "$BIN" ]; then
  PW_BIN=$BIN  
fi

if [ -z "$PW_BIN" ]; then
   echo " # ERROR: Provide a path to a pw.x binary."
   exit
fi

echo "pw.x executed as: " $MPI $PW_BIN

#parse element symbol (specie)
SP=$( echo $PSEUDO | cut -d"." -f1 ) 
if [[ ${#SP} -gt "2" ]]; then #parse 1st letter in case of non standard file name
  SP=${PSEUDO:0:1} 
fi

# Try to check whether it is ultrasoft
if [[ "$PSEUDO" == *us.* || "$PSEUDO" == *us_* || "$PSEUDO" == *us-* || "$PSEUDO" == *uspp* ]]; then
  USPP=true
elif [[ ! -z $( head -20 $PSP_ARG |grep -a "USPP" ) ]]; then
  USPP=true
fi

#Generate list of ecutwfc for normal and ultrasoft pseudopotentials
if $USPP ; then
  ecutwfc_list=`seq 20 10 60`
else
  ecutwfc_list=$(seq 30 10 120)
fi
echo "cutoff list: " $ecutwfc_list



if [[ -z $PO ]]; then    # if PO option present skip this part

rm -f out.ecut_wfc.$PSEUDO
for i in $ecutwfc_list; do
 echo "  calculating ecutwfc="$i " ... "

   # Generating a basic pw.x input
   cat > in << EOF
&CONTROL
  calculation  = "scf",
  prefix       = "SIM",
  pseudo_dir   = "$PSEUDO_DIR",
  outdir       = ".",
  verbosity = 'low',
  disk_io="none", 
/
&SYSTEM
  ibrav     = 1,
  celldm(1) = 30.0, 
  nat       = 1, 
  ntyp      = 1,
  ecutwfc   = $i,
  ecutrho   = 200.D0,
  occupations='smearing', smearing='gauss', degauss=0.02,
/
&ELECTRONS
  conv_thr    = 1.D-6,
/
/
ATOMIC_SPECIES
$SP 1.0 $PSEUDO
ATOMIC_POSITIONS (angstrom) 
$SP  0.000000000000 0.000000000000 0.000000000000
K_POINTS {automatic}
1 1 1 0 0 0
EOF
$MPI $PW_BIN < in >> out.ecut_wfc.$PSEUDO 2> /dev/null 

done  # loop for calculations

energies=$(grep -a "!    total energy              =" out.ecut_wfc.$PSEUDO | awk '{print $5}' )

# Write total energies obtained at different ecutwfc to energies.ecutwfc.PSEUDO
declare -a array_ecut
declare -a array_ener
array_ecut=(${ecutwfc_list// / })
array_ener=(${energies// / })
rm -f energies.ecutwfc.$PSEUDO
for i in `seq 0 ${#array_ecut[@]}`; do
  echo ${array_ecut[$i]} ${array_ener[$i]}  >> energies.ecutwfc.$PSEUDO
done

fi # end of PO section


# Plotting results with gnuplot

if [ -f energies.ecutwfc.$PSEUDO ]; then
gnuplot_bin=`which gnuplot 2>/dev/null`
if [ "$gnuplot_bin" != "" ]; then
  $gnuplot_bin -persist -e "set xlabel 'ecutwfc (Ry.)'; set ylabel 'E (a.u.)'; p 'energies.ecutwfc.$PSEUDO' u 1:2 w linespoints"
  $gnuplot_bin -e "set terminal png; set output 'fig.ecutwfc.$PSEUDO.png'; set xlabel 'ecutwfc (Ry.)'; set ylabel 'E (a.u.)'; p 'energies.ecutwfc.$PSEUDO' u 1:2 w linespoints"
else
d        $ECHO "No gnuplot in PATH. Results not plotted."
fi
else
 echo ' ' 
 echo ' # ERROR: There is no energy file (called "energies.ecutwfc.$PSEUDO"). Unable to plot.' 
fi  #end of plot lool

echo " - DONE! -"


