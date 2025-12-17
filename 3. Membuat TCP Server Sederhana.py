import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(1)

print("Server berjalan di http://localhost:8080")
connection, address = server_socket.accept()
print("Connected by", address)
data = connection.recv(1024)
connection.sendall(b'Hello, Client')
connection.close()
# Fungsi: Membuat server TCP sederhana yang menerima koneksi dan mengirim respons.
# Kondisi: Ketika Anda ingin membuat server yang melayani permintaan dari klien TCP.
