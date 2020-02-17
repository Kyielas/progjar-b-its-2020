import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31001)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    # Send data
    name="test.jpg"
    file = open(name,'rb')
    content =file.read()
    print ('sending data...')
    sock.sendall(content)
finally:
    print("closing")
    sock.close()