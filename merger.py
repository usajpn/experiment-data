import sys

main = sys.argv[1]
foutname = main + '_p'

fin = open(main, 'r')
fout = open(foutname, 'w')

counter = 1

out = ''
for line in fin:
	a = line.strip().split(',')[0]
	out = str(counter) + ' ' + a + '\n')
	counter = counter + 1

fout.write(out)	

fin.close()
fout.close()

