import socket, time

print("SHREYAANS NAHATA: 19BCE2686\n")
sock = socket.socket()
host = socket.gethostname()
ip_addr = socket.gethostbyname(host)

print("Establishing a connection to the server...")
port = 8080
sock.connect((host, port))
print("Established a connection to the server!")
server_data = sock.recv(1024)
server_data = server_data.decode()
print("\nReceived data from server: " + server_data)
print("\nConnection from the server terminated!")