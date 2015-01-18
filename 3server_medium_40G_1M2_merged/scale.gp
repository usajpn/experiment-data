set font "Helvetica,16"
set xl "Client ID"
set yl "Execution Time"
set font "Helvetica,16"
set terminal postscript eps enhanced color
set output fout
plot [0:maxX] [0:5000] fin using 1 title 'SIFT 480 x 640 Image' w p pt 13
