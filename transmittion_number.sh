gnuplot <<EOF
set terminal postscript eps enhanced color
set output "/dev/null"
set style line 1 linewidth 2
set datafile separator ","
set title "Transmittion Numbers (msec)"
set xlabel "Device Numbers"
set ylabel "Transmittion Numbers (msec)"
plot "transmittion_number.txt" using 1:2 title "Olsr network" w lp
replot "transmittion_number.txt" using 1:3 title "Openflow network" w lp
replot "transmittion_number.txt" using 1:4 title "SDMANET with a network segment" w lp
set output "transmittion_numbers.eps"
replot "transmittion_number.txt" using 1:5 title "SDMANET with two network segments" w lp

EOF
