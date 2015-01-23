set font "Helvetica,16"
set xl "Client ID"
set yl "Execution Time"
set font "Helvetica,16"
set terminal postscript eps enhanced color
set output fout
plot [0:maxX] [0:] fin using 1 title 'SIFT Application Execution Time' w p pt 13
