import os
import re

file_open = open(filename,'r')
try:
	regex_in = raw_input("Enter the regular expression")
	match = re.search(regex_in,filename)
	if match!=None:
		match_all = re.findall(regex_in,filename)
		print "Result:" + str(match_all)
except IOError as e:
	print ("File requested doesn't exist. Try again!")
file_open.close()
