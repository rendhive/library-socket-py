import socket
import threading

def handle_client(connection):
    while True:
        data = connection.recv(1024)
        if not data:
            break
        connection.sendall(data)
    connection.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8091))
server_socket.listen(5)

while True:
    connection, address = server_socket.accept()
    print("Connection accepted from:", address)
    threading.Thread(target=handle_client, args=(connection,)).start()
# Fungsi: Membuat thread terpisah untuk setiap klien yang terhubung.
# Kondisi: Ketika Anda perlu melayani banyak klien secara bersamaan.
