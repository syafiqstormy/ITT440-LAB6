import sys
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
print(Response.decode())
while True:
    Input = input(
        'Choose mathematical function, [L]ogarithmic, [S]quare Root, or [E]xponential. Enter only the first capital letter or [Q] to quit: ')

    if Input == 'L' or Input == 'S' or Input == 'E':
        value = input("Enter a value: ")
        Input = Input + ":" + value
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024)
        print(Response.decode("utf-8"))

    elif Input == 'Q':
        print("Quiting app.")
        ClientSocket.send(str.encode(Input))
        sys.exit()
    else:
        print("Invalid input! Enter only L, S, or E.")
        print("Please try again.")
        Input = "0"
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024)
        print('***********')

ClientSocket.close()

