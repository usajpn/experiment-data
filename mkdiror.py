#!/usr/bin/python

import glob, sys
import commands, os
import shutil

exp_name = sys.argv[1]

hostlist = []

f = open('106hosts', 'r')

for host in f:
	hostlist.append(host)

f.close()

for hostNum in range(1, 7):
	for i in range(0, hostNum*5):
		host = hostlist[i]
		dir_name = exp_name + "/" + str(hostNum*5) + "hosts"

		if os.path.exists(dir_name):
			shutil.rmtree(dir_name)
		os.makedirs(dir_name)
		
		ip = host.strip().split('@')[1]
		open(dir_name + '/' + ip, 'a').close()
