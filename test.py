import socket as s

clients = []

def new_client():
    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    sock.connect(('localhost', 8080))
    clients.append(sock)

def send_data():
    for c in clients:
        c.send(bytearray("test".encode("ascii")));

while 1:
    ins = input("what to do: ")
    if ins == 'n':
        for i in range(10):
            new_client()
    elif ins == "s":
        send_data()
