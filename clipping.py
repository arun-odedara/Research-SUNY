from __future__ import division
import csv

from optparse import OptionParser
from gnuradio.eng_option import eng_option

parser = OptionParser(option_class=eng_option, usage="%prog [options] input txers_file output")
parser.add_option("-f", "--fft-size", type="int", default=1024,
                          help="FFT size [default=1024]")
parser.add_option("-s", "--samp-rate", type="int", default=2e6,
                          help="sample rate [default=2e6]")
parser.add_option("-w", "--awake-time", type="int", default=4,
                          help="Awake Time of sensor [default=4]")
parser.add_option("-l", "--sleep-time", type="int", default=4,
                          help="Sleep Time of sensor [default=4]")

(options, args) = parser.parse_args()

input_file = args[0]
output_file = args[1]

fft_size = options.fft_size
samp_rate = options.samp_rate
t_awake = options.awake_time
t_sleep = options.sleep_time

def clip():							 #CLIPPING OF THE DATA WHERE TRANSMITTER IS SLEEPING AND KEEPING THE DATA WHILE TRANSMISSION IS GOING ON
	total_time = 30
	samp_rate_real = samp_rate
	t_line = fft_size/samp_rate_real  #TIME REQUIRED FOR ONE LINE
	def delete():
		return round(t_sleep/t_line) #PART WHERE TRANSMITTER  IS SLEEPING
	def keep():
		return round(t_awake/t_line) #PART WHERE TRANSMISSION IS GOING AND AWAKE
	with open(input_file, "rb") as old, open(output_file, "ab") as new:
		lines = [[float(i) for i in line.strip().split(',')] for line in old]
		one_round = delete() + keep()
		start_row = one_round -1
		next = one_round + keep()
		#print "length of lines: ", len(lines), "\nkeep is :" ,keep(), "\nDelete is : ", delete()	
		writer = csv.writer(new)
		row = 0		
		for row in lines:
			if lines.index(row) < keep():
				writer.writerow(row)
				#print lines.index(row)
			if lines.index(row) > start_row and lines.index(row) < next:	
				writer.writerow(row)
				#print lines.index(row)
			if lines.index(row) == next:
				start_row += one_round
				next += one_round
clip()
