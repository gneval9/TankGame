import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))

mensaje = "Hola desde el cliente"
client.sendall(mensaje.encode())

client.close()
