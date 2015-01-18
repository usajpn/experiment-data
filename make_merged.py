#!/usr/bin/python

import os, sys

def merge(dn):
	files = os.listdir(dn)	
	merged = ''
	for f in files:
		fn = dn + '/' + f
		merged = merged + splitter(fn)
	return merged

# 123,456\n => 124\n
def splitter(fn):
	f = open(fn)
	a = ''
	for line in f:
		a = line.split(',')[0]
	f.close()
	return a + '\n'

inp = sys.argv[1]
out_main = inp + '_merged'
if not os.path.exists(out_main):
	os.makedirs(out_main)

for i in range(1, 11):
	dn = inp + '/' + str(i*10) + 'hosts'
	merged = merge(dn)
	f = open(out_main + '/' + str(i*10) + 'hosts', 'w')
	f.write(merged)
	f.close()
