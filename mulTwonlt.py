#!/usr/bin/env python
import sys
if __name__ == "__main__":

	if len(sys.argv) > 3:
		print("saisissez que deux argument")
	elif len(sys.argv) == 3:
		x = int(sys.argv[1])
		y = int(sys.argv[2])
		print(("x * y = ")(x*y))
	else:
		print("peu d'argument")

