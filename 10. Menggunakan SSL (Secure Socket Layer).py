import socket
import ssl

context = ssl.create_default_context()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
wrapped_socket = context.wrap_socket(sock, server_hostname='www.example.com')

wrapped_socket.connect(('www.example.com', 443))
wrapped_socket.sendall(b'GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n')
response = wrapped_socket.recv(4096)
print("Response from secured server:", response.decode())
wrapped_socket.close()
# Fungsi: Menggunakan SSL untuk mengamankan komunikasi dengan server.
# Kondisi: Ketika Anda perlu berkomunikasi dengan server menggunakan HTTPS atau protokol aman lainnya.
