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
    message = 'PEMOGRAMAN JARINGAN TEKNIK INFORMATIKA'
    print ('sending "%s"' % message)
    sock.sendall(message.encode())
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(32)
        amount_received += len(data)
        print ('received "%s"' % data.decode())
finally:
    print("closing")
    sock.close()