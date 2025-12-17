import socket

# Membuat socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.sendto(b'Hello, Server', ('localhost', 8083))

data, address = udp_socket.recvfrom(1024)
print("Response from server:", data.decode())
udp_socket.close()
# Fungsi: Mengirim pesan menggunakan UDP dan menunggu untuk menerima balasan.
# Kondisi: Ketika Anda perlu mengirim data dan mendengar jawaban dengan UDP.
