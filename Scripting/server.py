#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

serversocket.bind(('192.168.29.98',port))

serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()
    print("received connection from " % str(address))

    message = 'some message' + "\r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()
