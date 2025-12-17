import socket

# Membuat socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 8082))

print("UDP Server berjalan di http://localhost:8082")
data, address = server_socket.recvfrom(1024)
print("Received data:", data.decode())
server_socket.close()
# Fungsi: Membuat server UDP sederhana untuk menerima pesan dari klien.
# Kondisi: Ketika Anda ingin membuat layanan yang akan menerima data tanpa konektivitas.
