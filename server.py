import socket

# Định nghĩa host và port mà server sẽ chạy và lắng nghe
host = '192.168.1.67'
port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen(1) 
print(f"Server listening on {port}...")

c, addr = s.accept()
print("Connect from ", str(addr))


def sendDataFromClient(buffer):
    buffer = str(buffer)
    # c.send(b"Welcome!")
    c.send(buffer.encode())
    # buffer = c.recv(1024)
    # print(str(buffer))

def falseCase():
    c.send(b"Sorry!")
    # buffer = c.recv(1024)
    # print(str(buffer))
