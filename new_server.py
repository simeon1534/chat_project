import socket
import threading

HEADER = 64
PORT = 5050
SERVER = "192.168.1.6"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients_server = []


def send_to_client(curr_conn, msg):
    msg_legth = len(msg)
    send_length = str(msg_legth).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    curr_conn.send(send_length)
    curr_conn.send(msg)


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
            encrypted_msg = conn.recv(msg_length) # msg_length
            msg = encrypted_msg.decode(FORMAT)
            if msg.split(': ')[1] == DISCONNECT_MESSAGE: # simeon: zdr
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
