import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8090))
server_socket.listen(1)

connection, address = server_socket.accept()
data_buffer = b''

while True:
    data = connection.recv(1024)
    if not data:
        break
    data_buffer += data

print("Received data:", data_buffer.decode())
connection.close()
# Fungsi: Mengelola penerimaan data yang lebih besar melalui buffer.
# Kondisi: Ketika Anda perlu menangani pengiriman data yang mungkin lebih besar dari kapasitas satu panggilan recv().
