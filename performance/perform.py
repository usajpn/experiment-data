import commands
import sys

fin = sys.argv[1]
fout = sys.argv[2]

commands.getoutput("gnuplot -e \"fin='" + fin + "'; fout='" + fout + ".eps'\" perform.gp")
