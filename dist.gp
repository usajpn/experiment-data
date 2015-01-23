set font "Helvetica,16"
set xl "Number of Clients"
set yl "Average Execution Time (ms)"
set font "Helvetica,16"
set terminal postscript eps enhanced color
set output fout
set xrange [0:maxX]
set yrange [0:8000] 
plot fin index 0:0 using 1:2:3 with yerrorbars title '1 server' w p pt 13, \
fin index 1:1 using 1:2:3 with yerrorbars title '3 servers' w p pt 13
