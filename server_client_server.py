import socket, random

sock = socket.socket()
host = socket.gethostname()
ipaddr = socket.gethostbyname(host)

print("SHREYAANS NAHATA: 19BCE2686\n")
thoughts = ["Hello World!", "Hey, this is the server!", "Server has entered the chat"]

port = 8080
sock.bind((host, port))
sock.listen(1)

print("Waiting for client-side connection...")
conn, addr = sock.accept()
print("Connection received from: " + str(addr))

rand = random.randint(0,2)
response = thoughts[rand]
print("\nSending message to client: " + response)
conn.send(response.encode())
sock.close()
print("\nConnection from the client terminated!")