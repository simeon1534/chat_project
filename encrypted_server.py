import socket
import threading
from cryptography.fernet import Fernet


def get_ip_address():
    # Create a socket object using the AF_INET address family (IPv4) and SOCK_DGRAM socket type.
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Doesn't really send data, just connects to the specified address and port.
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]  # Retrieve the local IP address.
    except socket.error:
        ip_address = "Unable to get IP address"
    finally:
        s.close()  # Close the socket.

    return ip_address





HEADER = 64
PORT = 5050
SERVER = str(get_ip_address())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)

clients_server = []
key = b'8tqWJ5x5fH9Dqq5ecj8lHyIaLdNbuTHkPv-wN_zDRN8='
cipher_suite = Fernet(key)


def send_to_client(curr_conn, msg):
    encrypted_msg = cipher_suite.encrypt(msg)
    msg_legth = len(encrypted_msg)
    send_length = str(msg_legth).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    curr_conn.send(send_length)
    curr_conn.send(encrypted_msg)


def broadcast(conn, addr, msg):
    for client in clients_server:
        curr_conn = client[0]
        curr_addr = client[1]
        if curr_conn == conn and curr_addr == addr:
            continue
        message = f"{msg}".encode(FORMAT)
        send_to_client(curr_conn,message)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER)
        if msg_length:
            msg_length = int(msg_length)
            encrypted_msg = conn.recv(msg_length)
            msg = cipher_suite.decrypt(encrypted_msg).decode(FORMAT)
            if msg.split(': ')[1] == DISCONNECT_MESSAGE:
                connected = False
                broadcast(conn, addr, f"{msg.split(': ')[0]} disconnected!")


            else:
                broadcast(conn, addr, msg)
            print(f"{addr} {msg}")
    message = f"Disconnected successfully !".encode(FORMAT)
    send_to_client(conn, message)
    clients_server.remove((conn, addr))
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        clients_server.append((conn, addr))
        thread.start()
        print(f"ACTIVE CONNECTIONS {threading.active_count() - 1}")


print("SERVER STARTED....")
start()
