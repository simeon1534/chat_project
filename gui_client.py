from tkinter import *
from tkinter import filedialog
import threading
import socket
import os
from cryptography.fernet import Fernet

print("Enter IP address of server: ")
HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = input()
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

key = b'8tqWJ5x5fH9Dqq5ecj8lHyIaLdNbuTHkPv-wN_zDRN8='
cipher_suite = Fernet(key)

username = input("Enter username\n")

# GUI
root = Tk()
root.title("ChatClient")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


# Send function
def send():
    msg = e.get()
    if msg.strip() == "":  # check for empty string
        return
    e.delete(0, END)  # delete last input
    send_tk = "You: " + msg
    txt.insert(END, "\n" + send_tk)
    message = f"{username}: {msg}".encode(FORMAT)
    encrypted_message = cipher_suite.encrypt(message)
    msg_length = len(encrypted_message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(encrypted_message)


# Recv function
def receive():
    while True:
        msg_length = client.recv(HEADER)
        if msg_length:
            msg_length = int(msg_length)
            encrypted_msg = client.recv(msg_length)
            msg = cipher_suite.decrypt(encrypted_msg).decode(FORMAT)
            print(msg)
            txt.insert(END, "\n" + f"{msg}")
            if msg == f"Disconnected successfully !":
                os._exit(0)


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text=f"Welcome {username}", font=FONT_BOLD, pady=10, width=20,
               height=1).grid(
    row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)

e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
              command=send).grid(row=2, column=1)


def browse_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'rb') as file:
        file_data = file.read()
        filename = os.path.basename(file_path)
        message = f"{username} sent file {filename}"
        client.sendall(message.encode(FORMAT))
        client.sendall(file_data)
        txt.insert(END, f"\n{message}")

        encrypted_message = cipher_suite.encrypt(bytes(message))
        msg_length = len(encrypted_message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(encrypted_message)


browse_btn = Button(root, text="Browse", font=FONT_BOLD, bg=BG_GRAY) #command=browse_file
browse_btn.grid(row=2, column=2)

t1 = threading.Thread(target=receive)
t1.start()

t2 = threading.Thread(target=send)
t2.start()

root.mainloop()
