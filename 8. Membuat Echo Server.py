import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8084))
server_socket.listen(1)

print("Echo Server berjalan di http://localhost:8084")
connection, address = server_socket.accept()

while True:
    data = connection.recv(1024)
    if not data:
        break
    connection.sendall(data)  # Mengirim kembali data yang diterima
connection.close()
# Fungsi: Membuat server yang mengulangi kembali semua data yang diterima (echo).
# Kondisi: Ketika Anda ingin membuat layanan untuk menguji koneksi.
