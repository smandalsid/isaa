import socket
rec=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SENDER="127.0.1.1"
FORMAT="utf-8"
PORT=2003

print("**  SIDDHARTH MANDAL **")
print("** 20BDS0157 **")

print("[CONNECTING] Connecting with the receiver...")
# connect with the sender
rec.connect((SENDER, PORT))
print("Connected...")


q=11
alpha = 2
xa=int(input("Enter sender private key: "))
while(xa>=q):
    print("xa not less than "+str(q))
    print("Enter xa again: ")
    xa=int(input("Enter private key: "))
ya=str((alpha**xa)%q)

print("Sender Private key: "+ya)

print("Sending public key to receiver")
rec.send(ya.encode(FORMAT))
print("Receiving public key of receiver(from middle man)")
yb=(rec.recv(2048)).decode(FORMAT)
print("Public key of Receiver: "+yb)
yb=int(yb)
print("Generating secret key...")
sk=(yb**xa)%q
print("Secret key generated: "+str(sk))

rec.close()