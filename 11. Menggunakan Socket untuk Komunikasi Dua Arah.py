import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8086))
server_socket.listen(1)

connection, address = server_socket.accept()
print("Connection accepted from:", address)

while True:
    data = connection.recv(1024)
    if not data:
        break
    print("Received:", data.decode())
    connection.sendall(data)  # Mengirim kembali
connection.close()
# Fungsi: Memungkinkan komunikasi dua arah dengan klien.
# Kondisi: Ketika Anda perlu membuat layanan yang dapat menerima dan mengirim data kembali.
