#!/usr/bin/python

import sys
import httplib

def fetch():
	"""
	Fetch a cliowl API server to make future operations
	"""
	
	conn = httplib.HTTPConnection("localhost")
	conn.request("GET", "/cliowl/fetch")
	r1 = conn.getresponse()
	data1 = r1.read()

	print r1.status, r1.reason 
	print data1

def usage():
	"""
	Displays program usage
	"""
	
	print 'Usage: cliowl COMMAND [COMMAND_ARGUMENTS...]'

def unknown_command(command):
	"""
	Displays an error message for an unknown command
	"""
	
	print "Unknown command '%s'" % command

def bad_params():
	"""
	Displays an error message for inadequate arguments
	"""
	
	print 'Bad arguments'



# Program

if len(sys.argv) > 1:
	if sys.argv[1] == 'fetch':
		if len(sys.argv) > 2:
			bad_params()
		else:
			fetch()
	else:
		unknown_command(sys.argv[1])
else:
	usage()
