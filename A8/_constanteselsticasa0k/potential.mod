# NOTE: This script can be modified for different pair styles 
# See in.elastic for more info.

# Choose potential
pair_style      eam/fs 
pair_coeff      * * Al_mm.eam.fs Al
#pair_coeff     * * Al_zhou.eam.alloy Al

# Setup neighbor style
neighbor        2.0 bin 
neigh_modify    delay 10 check yes one 30000 page 300000 

# Setup neighbor style
#neighbor 1.0 nsq
#neigh_modify once no every 1 delay 0 check yes

# Setup minimization style
min_style	     cg
min_modify	     dmax ${dmax} line quadratic

# Setup output
thermo		1
thermo_style custom step temp pe press pxx pyy pzz pxy pxz pyz lx ly lz vol
thermo_modify norm no
