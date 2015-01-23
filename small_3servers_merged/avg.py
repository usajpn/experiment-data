
fout = open('avg.dat', 'w')


for i in range(1, 11):
	fin = open(str(i*10) + 'hosts', 'r')
	summ = 0
	counter = 0
	for line in fin:
		num = line.strip()
		if num:
			summ += float(num)
			counter = counter + 1
	
	fout.write(str(float(summ) / counter) + '\n')


fout.close()
