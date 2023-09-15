import socket
import threading
from cryptography.fernet import Fernet

HEADER = 64
PORT = 5050
SERVER = "192.168.1.6"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen()
while True:
    conn, addr = server.accept()
    connected = True
    print('Connected')
    while connected:
        msg = conn.recv(1024)
        if msg:
            msg = msg.decode(FORMAT)
            print(msg)
            conn.send(b'Thanks for using our app!')
