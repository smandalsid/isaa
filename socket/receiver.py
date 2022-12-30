import socket
rec=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SENDER="127.0.1.1"
FORMAT="utf-8"
PORT=2003

print("***  SIDDHARTH MANDAL ***")
print("*** 20BDS0157 ***")

print("[CONNECTING] Connecting with the sender...")
# connect with the sender
rec.connect((SENDER, PORT))
print("Connected...")


q=11
alpha = 2
xb=int(input("Enter receiver private key: "))
while(xb>=q):
    print("xb not less than "+str(q))
    print("Enter xb again: ")
    xb=int(input("Enter receiver private key: "))
yb=str((alpha**xb)%q)
print("Private key: "+yb)

print("Sending public key to sender")
rec.send(yb.encode(FORMAT))
print("Receiving public key of sender(from middle man)")
ya=(rec.recv(2048)).decode(FORMAT)
print("Public key of sender: "+ya)
ya=int(ya)
print("Generating secret key...")
sk=(ya**xb)%q
print("Secret key generated: "+str(sk))

rec.close()