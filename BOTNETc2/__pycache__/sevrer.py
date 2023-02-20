import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(('127.0.0.1', 8082))
serv.listen(5)

while True:
    conn, addr = serv.accept()
    from_client=''
    while True:
        from_client=''
        data = conn.recv(4096)
        if not data : break
        from_client+=data
        print(from_client)

        input1=str(b'HI')
        conn.send(input1)