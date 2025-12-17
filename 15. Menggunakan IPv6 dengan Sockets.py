import socket

server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
server_socket.bind(('::1', 8089))  # Menggunakan alamat IPv6
server_socket.listen()

print("Server berjalan di http://[::1]:8089")
connection, address = server_socket.accept()
print("Connection accepted from:", address)
connection.close()
# Fungsi: Menggunakan socket untuk komunikasi IPv6.
# Kondisi: Ketika Anda bekerja dengan jaringan yang menggunakan alamat IPv6.
