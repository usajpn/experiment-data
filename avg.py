import sys
import os, commands
import os.path

main = sys.argv[1]

fout = main + '_avg/'

if not os.path.exists(fout):
	os.makedirs(fout)

for i in range(1, 11):
	host_name = str(i*10) + 'hosts'
	files = os.listdir(main + '/' + host_name)
	
	summ = 0
	counter = 0
	for f in files:
		conn = main + '/' + host_name + '/' + f
		fo = open(conn, 'r')
		for line in fo:
			if line:
				summ = summ + int(line)
				counter = counter + 1
		fo.close()
	
	o = open(fout + host_name, 'w')
	o.write(str(summ / float(counter)) + '\n')
	o.close()

for j in range(1, 11):
	fout = main + '_avg/'
	o = open(fout + str(j*10) + 'hosts')
	for line in o:
		print line.strip()

			

