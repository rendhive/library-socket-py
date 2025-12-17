import socket

hostname = 'localhost'
ip_address = socket.gethostbyname(hostname)
print(f"IP Address of {hostname} is {ip_address}")
# Fungsi: Mengambil alamat IP untuk nama host menggunakan socket.
# Kondisi: Ketika Anda perlu memetakan nama alamat ke IP dalam aplikasi Anda.
