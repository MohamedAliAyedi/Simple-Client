#!/usr/bin/python3
import socket
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("TEST Client")
lhost = socket.gethostname()
lport = 1177
clientsocket.connect((lhost,lport))
message = clientsocket.recv(1024)
clientsocket.close()
print(message.decode('ascii'))
