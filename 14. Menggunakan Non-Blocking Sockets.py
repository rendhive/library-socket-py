import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setblocking(False)  # Set socket ke non-blocking
server_socket.bind(('localhost', 8088))
server_socket.listen(5)

try:
    while True:
        try:
            connection, address = server_socket.accept()
            print("Connection accepted from:", address)
        except BlockingIOError:
            continue
finally:
    server_socket.close()
# Fungsi: Menangani socket non-blocking untuk menghindari penundaan dalam kode.
# Kondisi: Ketika Anda ingin membuat server yang responsif.
