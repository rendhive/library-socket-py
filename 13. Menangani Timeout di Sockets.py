import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(5)  # Menetapkan timeout untuk koneksi

try:
    client_socket.connect(('localhost', 8087))
except socket.timeout:
    print("Connection timed out")
client_socket.close()
# Fungsi: Mengatur batas waktu pada operasi socket untuk menghindari blocking selamanya.
# Kondisi: Ketika Anda ingin memastikan bahwa program tidak menunggu selamanya untuk koneksi.
