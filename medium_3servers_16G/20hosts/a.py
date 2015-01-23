import os

files = os.listdir('./')

for f in files:
	o = open(f, 'r')
	print o.readline().strip()
	o.close()
