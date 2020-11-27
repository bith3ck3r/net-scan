import requests
import socket
from socket import *
import time
from datetime import datetime
import sys
print("." * 100, "\n")
print("Bitnet\nWritten by BitH3ck3r\n")
print("#" * 100, "\n")
print("Type 'help' for availlable comands\n")
print("Type q or Q to quit the program\n")
def scan_host(ip, scan):
	print("##### Detected ", scan, " scaning on: ", ip, "\n")
	if scan == "port":
		print("X" * 50, "\n")
		t1 = datetime.now()
		print("Started ", scan, "scan on ", t1, "\n")
		print("X" * 50)
		print("PORT                               STATUS\n")
		for port in range(1, 1025):
			sock = socket(AF_INET, SOCK_STREAM)
			magic = sock.connect_ex((ip, port))
			if magic == 0:
				print("Port {}                OPEN".format(port))
			sock.close()
def pro_url(url, scan):
	if "www" in url:
		print ("www detected\n")
		print("Invalid host name please try again!\n")
		print("Do not inlcude 'www' or any protocol ('http' https'\n")
		pro_url(input("=> "))
	elif "http://" in url:
		print ("http detected\n")
		print("Invalid host name please try again!\n")
		print("Do not inlcude 'www' or any protocol ('http' https'\n")
		pro_url(input("=> "), scan)
	elif "https://" in url:
		print ("www detected\n")
		print("Invalid host name please try again!\n")
		print("Do not inlcude 'www' or any protocol ('http' https'\n")
		pro_url(input("=> "), scan)
	else:
		print("host name seems to be fine\n")
		ipaddr = gethostbyname(url)
		print("Starting the selected scan on: ", ipaddr,"\n")
		scan_host(ipaddr, scan)
def chc_proc(chc):
	if "1" in chc:
		print("#" * 50, "\n")
		print("#### Port scanning Bitnet ####\n")
		print("Enter host url\n")
		print("Do not inlude 'www' or any protocol ('http' https')\n")
		pro_url(input("=> "), "port")
	else:
		print("Invalid comand!\n")
		chc_proc(input("=> "))
def pro_exit(exit):
	if "y" in exit:
		print("Exit successful...")
	elif "Y" in exit:
		print("Exit successful...")
	elif "n" in exit:
		print("Exit successfully cancelled!\n")
		cmd_proc(input("=> "))
	elif "N" in exit:
		print("Exit successfully cancelled!\n")
		cmd_proc(input("=> "))
def cmd_proc(cmd):
	if "help" in cmd:
		print("#" * 50, "\n")
		print("COMAND                                                USE\n")
		print("help                                                  Open comands list\n")
		print("./start                                               Open program menu\n")
		print("./update                                              Update the script from Gihub\n")
		print("./run                                                 Run the selected module\n")
		cmd_proc(input("=> "))
	elif "./start" in cmd:
		print("#" * 50, "\n")
		print("##### Bitnet Menu ####")
		print("Reply with:\n")
		print("1 for port scanning\n")
		print("2 for live host scanning\n")
		print("3 for combined port & host scanning\n")
		print("4 for server status scanning\n")
		chc_proc(input("=> "))
	elif "q" in cmd:
		print("#" * 50, "\n")
		print("Reply with 'y', 'Y' for yes and 'n' 'N' for no\n")
		print("Are sure you want to quit?")
		pro_exit(input("=> "))
	elif "Q" in cmd:
		print("#" * 50, "\n")
		print("Reply with 'y', 'Y' for yes and 'n' 'N' for no\n")
		print("Are sure you want to quit?")
		pro_exit(input("=> "))
	else:
		print("#" * 50, "\n")
		print("Invalid comand!\n")
		print("Type 'help' for availlable comands lists\n")
		cmd_proc(input("=> "))
cmd_proc(input("=> "))
