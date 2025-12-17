import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))
client_socket.sendall(b'Hello, Server')
response = client_socket.recv(1024)
print("Response from server:", response.decode())
client_socket.close()
# Fungsi: Membuat klien TCP sederhana untuk mengirim dan menerima data.
# Kondisi: Ketika Anda ingin terhubung ke server menggunakan TCP.
