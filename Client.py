#!/usr/bin/python3
import socket
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Client TCP By Ayedi")
host = socket.gethostname()
port = 6000
clientsocket.connect((host,port))
message = clientsocket.recv(1024)
clientsocket.close()
print(message.decode('ascii'))
