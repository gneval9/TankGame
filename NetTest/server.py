import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))
server.listen()

print("Esperando conexión...")

conn, addr = server.accept()
print("Conectado:", addr)

data = conn.recv(1024)
print("Recibido:", data.decode())

conn.close()
server.close()
