

#!/usr/bin/env python

import sys

print(sys.argv)
while true:
    try:
	x = int( sys.argv[1] )
	y = int( sys.argv[2] )
            print((x)," + ",(y)," = ",(x+y))
            break
     except ValueError:
        print("Erreur,entrer pas plus de deux variable!")
