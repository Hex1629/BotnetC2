import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8082))

client.send("I am CLIENT\n")
from_server = client.recv(4096)
input1=str('HI')
client.send(input1)
data = client.recv(65536)
client.close()
client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client2.connect(('127.0.0.1', 8082))
client2.send(data)
client2.close()