#!/usr/bin/env python
import sys
if __name__ == "__main__":

	if len(sys.argv) > 3:
		print("saisissez que deux argument")
	elif len(sys.argv) == 3:
		x = int(sys.argv[1])
		y = int(sys.argv[2])
		print(("x * y = "),(x*y))
	
	elif len(sys.argv)==2:
		print("peu d'argument")
		x = int(sys.argv[1])
		y = int(input("inserez le 2eme valeur: "))
		print((x), "*",(y) ,"= ",(x*y))
	else:
		print("ajouter des valeur")
		x  = int(input("ajoutez 1er valeur: "))
		y  = int(input("ajoutez la 2eme valeur: "))
		print((x),"*",(y),"=",(x*y))
