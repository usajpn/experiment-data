import sys
import os, commands

main = sys.argv[1]


for i in range(1, 11):
	host_name = str(i*10) + 'hosts'
	files = os.listdir(main + '/' + host_name)
	for f in files:
		conn = main + '/' + host_name + '/' + f
		commands.getoutput('python splitter.py ' + conn)

