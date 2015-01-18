set font "Helvetica,16"
set xl "Platform"
set yl "Execution Time (ms)"
set font "Helvetica,16"
set terminal postscript eps enhanced color
set output fout
set style fill solid 0.5 noborder
set boxwidth 0.6 relative
set yrange [0:10000]
plot fin using 0:2:xtic(1) title 'SIFT Execution Time' with boxes
