import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()

PORT = 12345

s.bind((HOST_NAME,PORT))


s.listen(4)


while True:

    client, address=s.accept()
    jls_extract_var = "utf-8"
    client.send(bytes("hey there!",jls_extract_var))

    client.send(bytes("hey there!","utf-8"))
    print(address)