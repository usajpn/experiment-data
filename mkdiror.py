#!/usr/bin/python

import glob
import commands, os

exp_num = "exp1"

hostlist = []

f = open('106hosts', 'r')

for host in f:
	hostlist.append(host)

f.close()

for hostNum in range(1, 11):
	for i in range(0, hostNum*10):
		host = hostlist[i]
		dir_name = exp_num + "/" + str(hostNum*10) + "hosts"

		if not os.path.exists(dir_name):
			os.makedirs(dir_name)
		
		ip = host.strip().split('@')[1]
		open(dir_name + '/' + ip, 'a').close()
