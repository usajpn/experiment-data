set font "Helvetica,16"
set xl "Client ID"
set yl "Execution Time"
set font "Helvetica,16"
set terminal postscript eps enhanced color
set output fout
plot [0:maxX] [0:1500] fin using 1 title 'SIFT 240 x 360 Image' w p pt 13
