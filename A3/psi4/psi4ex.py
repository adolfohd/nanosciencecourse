#!/usr/bin/python
import sys

"""
usage: psi4ex.py <psi4 output>

writes optimization log file (xyz, energy, grms) suitable for molden.
Can be used for quickly checking running jobs
"""

# set output file name
outfile='geoms.xyz'

if len(sys.argv) > 1:
  infile=str(sys.argv[1])
else:
  infile="opt.out"  # set default name

print 'Reading :',infile
f = open(infile,'r')
ofile = open(outfile, 'w')
nat=""

# find nat
do_read=True
while do_read:
 l=f.readline()
 if "Center              X                  Y                   Z               Mass" in l:
  s = f.readline() # dummy line
  nat=0
  while do_read:
   s = f.readline() 
   if s.strip() == '':
     do_read=False
   else:
     nat+=1

print "nat: ",nat


offset=1
f.seek(0)
do_read=True
xyz=[]
# geometries
while do_read: 
 l=f.readline()
 if not l: break
 if "Center              X                  Y                   Z               Mass" in l:
   s = f.readline() # dummy line
   xyz.append(str(nat))
   xyz.append('')
   for i in range(0,nat):
    s = f.readline()
    xyz.append(s.rstrip())


# add energy/gnorm
f.seek(0)
e=0
rms=0
c=0
while do_read: 
 l=f.readline()
 if not l: break
 if "Optimization is complete" in l: break
 if "Current energy   :" in l:
   e=(l.split()[3])
 if "RMS Force" in l:
   c+=1
   l=f.readline()
   l=f.readline()
   l=f.readline()
   l=f.readline()
   rms=(l.split()[4])
   line=e+' '+rms
   print c,line,offset
   xyz[offset]=line
   offset+=nat+2


# print to file
for i in xyz:
 print >>ofile,i
