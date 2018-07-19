#open socket using connection , function 
#Create file containing issues
#check against known issues

import socket
import os
import sys


def getBanner(ip,port):
	s = socket.socket()
	try:
		s.connect((ip,port))
		banner = s.recv(2048)
		return banner
	except Exception, e:
		return e


def testBanner(banner,filename):
	
	f = open(filename,'r')
	for line in f.readlines():
		if line in banner:
			print "Server is vulnerable"



def  main():

	if not len(sys.argv) == 2:
		print "Invalid Number of Parameters"
	else:
		filename = sys.argv[1]
		portList = [22,80]
		#print filename

		if not os.path.isfile(filename):
			print "File non existant"
			exit(0)

			if not os.access(filename,os.R_OK):
				print "File Unreadable, Check permission"
				exit(0)
		else:
	
			for x in range (10,16):
				testIP = '10.0.2.' + str(x)
				
				for port in portList:
					print "Testing IP --- " + str(testIP)+ " ------ " + str(port)
	
					banner = getBanner(testIP,port)
					print banner
					if banner:
						testBanner(banner,filename)

if __name__ == "__main__":
	main()



