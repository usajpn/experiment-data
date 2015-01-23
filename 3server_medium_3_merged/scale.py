import commands

for i in range(1, 11):
	host_num = str(i*10)
	commands.getoutput("gnuplot -e \"fin='" + host_num + "hosts'; maxX='" + host_num + "'; fout='medium_" + host_num + ".eps'\" scale.gp")
