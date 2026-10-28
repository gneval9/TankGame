import socket

HOST = "0.0.0.0"
PORT = 5000

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST,PORT))
    server.listen()

    print("Esperando conexión...")

    conn, addr = server.accept()
    print("Conectado:", addr)
    
    return connm, server


def recv_data(conn):
    while True:
        data = conn.recv(1024)

        if not data:
            break

        return data.decode("utf-8")


   
def send_data(conn):
    while True:
        data2send = str("Hola")
        conn.sendall((data2send + "\n").encode("utf-8"))



def close_server():
    conn.close()
    server.close()
