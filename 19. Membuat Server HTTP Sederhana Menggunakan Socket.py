import socket

http_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
http_server.bind(('localhost', 8092))
http_server.listen(1)

while True:
    connection, address = http_server.accept()
    request = connection.recv(1024)
    print("Received request:", request.decode())
    
    response = 'HTTP/1.1 200 OK\n\nHello, HTTP!'
    connection.sendall(response.encode())
    connection.close()
# Fungsi: Menyajikan server HTTP sederhana untuk menangani permintaan.
# Kondisi: Ketika Anda ingin mengimplementasikan HTTP langsung menggunakan socket tanpa framework tambahan.
