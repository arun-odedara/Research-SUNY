import scipy
from optparse import OptionParser
import sys, math, csv
from gnuradio.eng_option import eng_option


parser = OptionParser(option_class=eng_option, usage="%prog [options] input txers_file output")
parser.add_option("-k", "--keep", type="int", default=1,
                          help="keep one in N [default=1]")
parser.add_option("-f", "--fft-size", type="int", default=1024,
                          help="FFT size [default=1024]")
(options, args) = parser.parse_args()
if len(args) == 3:
	inputfilename = args[0]	
	txersfilename = args[1]
	outputfilename = args[2]	
elif len(args) == 2:
	inputfilename = args[0]
	outputfilename = args[1]
else:
	print "Incorrect number of arguments."	
fft_size = options.fft_size
oneinn = options.keep



f = scipy.fromfile(open(inputfilename), dtype=scipy.float32)
f = f.reshape((-1,fft_size))
extractedData = f[:,(fft_size/8-1):(-1*(fft_size/8+1))]



from numpy import random
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig = plt.figure()
plt.set_cmap('Greys')
fig.set_size_inches(4, 4)
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)

rows,columns = f.shape

im = ax.imshow(f,extent=[0,columns,0,rows], aspect = 'auto', interpolation='nearest')

im.set_clim(-120,-10)
#im.set_clim(-97,-60)

if len(args) == 3:
	# open txerfile
	f = open(txersfilename, 'rb')
	txers = csv.reader(f)
	# loop through each row, add a rectangle for each: first tuple is bottom left corner of rectangle, then width and height
	for row in txers:
		ax.add_patch( patches.Rectangle((int(row[0]), int(row[1])), int(row[2]), int(row[3]), fc='none', ec='r', lw=2) )

# save the figure
fig.savefig(outputfilename+".png",dpi=100)
