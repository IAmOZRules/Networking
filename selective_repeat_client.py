import socket

def client():
    n = 4
    win_start = 0
    win_end = win_start + n - 1

    host = socket.gethostname()
    port = 12344
    sender = []

    flag = 0
    print("Establishing a connection to the server...")
    client_socket = socket.socket()
    client_socket.connect((host, port))
    print("Established a connection to the server!")

    print("\n----- Enter 'exit' to close the connection -----")
    message = input("Press ENTER to start sending frames -> ")

    while message.lower() != "exit":
        print("Sending frames...")
        if flag == 0:
            for i in range(n):
                sender.append(win_start + i)
            for i in sender:
                print("Frame -> ", i)
        
        else:
            print("Frame -> ", win_start)
        
        msg = str(win_start)
        client_socket.send(msg.encode())
        data = client_socket.recv(1024).decode()
        msg = str(data)
        ack = int(msg)

        if ack not in sender:
            win_start = ack
            win_end = win_start + n - 1
            flag = 0
            for i in range(n):
                sender.pop()
        
        else:
            win_start = int(msg)
            flag = 1

        print("\n****************************")         
        print("Received ACK Server: ", data)
       
        
        message = input("\nPress ENTER to start sending frames -> ")
    
    client_socket.close()

print("SHREYAANS NAHATA: 19BCE2686\n")
client()
print("\nConnection from the server terminated!")