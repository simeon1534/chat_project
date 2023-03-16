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

key = b'8tqWJ5x5fH9Dqq5ecj8lHyIaLdNbuTHkPv-wN_zDRN8='
cipher_suite = Fernet(key)

username = input("Enter username\n")


def send():
    msg = input()
    while True:
        message = f"{username}: {msg}".encode(FORMAT)
        encrypted_message = cipher_suite.encrypt(message)
        msg_legth = len(encrypted_message)
        send_length = str(msg_legth).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)  # send_length
        client.send(encrypted_message)
        msg = input()


def receive():
    while True:
        msg_length = client.recv(HEADER)
        if msg_length:
            msg_length = int(msg_length)
            encrypted_msg = client.recv(msg_length)
            msg = cipher_suite.decrypt(encrypted_msg).decode(FORMAT)
            print(msg)
            if msg == f"Disconnected successfully !":
                os._exit(0)


t1 = threading.Thread(target=receive)
t1.start()

t2 = threading.Thread(target=send)
t2.start()
