import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8081))
server_socket.listen(1)

print("Server berjalan di http://localhost:8081")
connection, address = server_socket.accept()
data = connection.recv(1024)
print("Received data:", data.decode())
connection.close()
# Fungsi: Menerima data dari klien dan menampilkannya.
# Kondisi: Ketika Anda ingin mengelola komunikasi input dari klien ke server.
