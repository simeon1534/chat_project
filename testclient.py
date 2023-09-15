import threading
import socket
import os
from cryptography.fernet import Fernet

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.6"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
while True:
    msg = input().encode(FORMAT)
    msg = bytes(msg)
    client.send(msg)
    response = client.recv(1024).decode(FORMAT)
    print(response)
