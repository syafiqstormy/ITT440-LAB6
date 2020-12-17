
import socket

ClientSocket = socket.socket()
host = '192.168.0.66'
port = 8888

print("Waiting for connection")
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response.decode('UTF-8'))

while True:
    Input = input('Say Something:')
    mesej = Input.encode('UTF-8')
    ClientSocket.send(mesej)
    Response = ClientSocket.recv(1024)
    print(Response.decode("UTF-8"))

ClientSocket.close()

