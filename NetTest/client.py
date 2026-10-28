import socket

HOST = "192.168.1.100"
PORT = 5000

def connect_to_server():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((HOST, PORT))
    
    return conn


def recv_data(conn):
    while True:
        data = conn.recv(1024)

        if not data:
            break

        return data.decode("utf-8")


def send_data(conn):
    while True:
        data2send = str("Hola")
        conn.sendall((data2send + "\n").enconde("utf-8"))
    


def close_server():
    conn.close()
    server.close()
client.close()
