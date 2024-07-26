import socket
import threading

def handle_client(client_socket, address):
    print(f"Got connection from {address}")
    con = True
    while con:
        try:
            msg = client_socket.recv(1024).decode("utf-8")
            print(f"Received message from {address}: {msg}")
            if msg == "quit":
                con = False
        except:
            break
    client_socket.close()
    print(f"Connection closed from {address}")

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set server IP and port
host = '192.168.100.21'  # Change this to your server's IP address
port = 1255

# Bind the socket to the address and port
s.bind((host, port))

# Put the socket into listening mode
s.listen(5)
print("Server is listening on port", port)

while True:
    # Accept a connection from a client
    client_socket, address = s.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()
