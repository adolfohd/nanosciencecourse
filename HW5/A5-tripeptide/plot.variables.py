
# import sys, traceback


#def main():

#	try:
# 		do

# 1 arg

logfile = "out.2ii"
l = log(logfile)

#   1    2   3        4       5     6    7     8         9      10     11      12   13
# Step Temp PotEng KinEng TotEng Press Volume E_bond E_angle E_dihed E_impro E_pair E_coul 
# vn1= "Step" vn2, vn3, vn4, vn5, vn6, vn7, vn8, vn9, vn10, vn11, vn12, vn13
#v1, v2, v3, v4, v5, v6,v7,v8,v9,v10,v11, v12, v13= l.get(vn1, vn2, vn3, vn4, vn5, vn6, vn7, vn8, vn9, vn10, vn11, vn12, vn13)
v1, v2, v3, v4, v5, v6,v7,v8,v9,v10,v11, v12, v13= l.get("Step", "Temp", "PotEng", "KinEng", "TotEng", "Press",
 "Volume", "E_bond", "E_angle", "E_dihed", "E_impro", "E_pair", "E_coul") 
g = gnu()
g.export("tempData", v1, v2, v3, v4, v5, v6,v7, v8, v9, v10, v11, v12, v13)

#	except KeyboardInterrupt:
#		print "Chao"
#	except Exception:
#		traceback.print_exc(file=sys.stdout)
# 	sys.exit(0)
#
#if __name__ == "__main__"
#	main()
