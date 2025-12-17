import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(('localhost', 0))  # Port dinamis
    print("Server berjalan di port:", server_socket.getsockname()[1])
    server_socket.listen()
    
    connection, address = server_socket.accept()
    with connection:
        print("Connection accepted from:", address)
        connection.sendall(b'Hello, Client')
# Fungsi: Mengatur server untuk menggunakan port dinamis.
# Kondisi: Ketika Anda ingin membiarkan OS memilih port bebas untuk Anda.
