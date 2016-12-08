
#Load a LAMMPS data file, a trajectory,
#set some representations to our liking,
#adjust the display size and rotate/zoom,
#loop over frames and render

# Script requires TopoTools and pbctools
package require topotools
package require pbctools


# Load the data file and trajectory


# ------------------- get all frames -------------------
# -- load original molecule
set molid [mol new graphene.xyz]

# --- generate "script.tcl"
#./vmd.script.sh #
# --- source it
source script.tcl

# Set the representation, delete the initial representation
# created by vmd
mol delrep 0 top
mol representation CPK 2.0 0.30 10.0 10.0
mol color Name
mol selection {all}
mol material AOEdgy
mol addrep top

# Set the scene: adjust display height
# and rotate axes a bit, set the background
# to white
display height 15
rotate x by -45; rotate y by 45; rotate z by 45
color Display Background white

# Draw the periodic box centered at the origin
pbc box_draw -center origin

# Get the number of frames
set nframes [molinfo $molid get numframes]

# Loop over frames, calling render.
# Format the output filename as snap-03.00001.tga
# Skip the first "junk" frame from lammpsdata
for {set i 1} {$i < $nframes} {incr i} {
  render TachyonInternal\
  [format "snap-03.%05d.tga" $i]
}

## Call external script to encode movie
# exec ./03-encode-vmd.sh
ffmpeg -i snap-03.%05d.tga 03.movie.mp4
