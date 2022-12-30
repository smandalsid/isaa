import socket

FORMAT="utf-8"
PORT=2003

SERVER=socket.gethostbyname(socket.gethostname())
FORMAT="utf-8"
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))


# MIDDLE MAN
def handle_client(conn1, addr1, conn2, addr2):
    q=11
    alpha = 2

    # creating connections with sender and receiver
    xm=int(input("Enter middle man private key: "))
    while(xm>=q):
        print("xm not less than "+str(q))
        print("Enter xm again: ")
        xa=int(input("Enter middle man private key: "))

    ym=str((alpha**xm)%q)
    print("middle man public key: "+ym)

    ya=int(conn1.recv(2048).decode(FORMAT))
    print("Public key of sender: "+str(ya))
    yb=int(conn2.recv(2048).decode(FORMAT))
    print("Public key of receiver: "+str(yb))

    ym=str((alpha**xm)%q)

    print("\nSending middle man public key to sender")
    conn1.send(ym.encode(FORMAT))
    print("Secret key between middle man and sender: "+str((ya**xm)%q))
    print("Sending middle man key to receiver")
    conn2.send(ym.encode(FORMAT))
    print("Secret key between middle man and receiver: "+str((yb**xm)%q))


    conn1.close()
    conn2.close()


def start():
    print(SERVER+" I am middle man")
    server.listen(2)
    conn1, addr1 = server.accept()
    print("Sender connected with the middle man")
    conn2, addr2 = server.accept()
    print("Receiver connected with the middle man")
    handle_client(conn1, addr1, conn2, addr2)

start()