import commands,sys

fname = sys.argv[1]

commands.getoutput("gnuplot -e \"fin='" + fname + ".dat'; maxX='32'; fout='" + fname + ".eps'\" dist.gp")
