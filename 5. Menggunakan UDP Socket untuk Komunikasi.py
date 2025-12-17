import socket

# Membuat socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Mengirim pesan
udp_socket.sendto(b'Hello, UDP Server', ('localhost', 8082))
print("Message sent via UDP.")
udp_socket.close()
# Fungsi: Mengirim pesan ke server menggunakan UDP socket.
# Kondisi: Ketika Anda ingin mengirim data tanpa kadaluarsa (non-connection oriented).
