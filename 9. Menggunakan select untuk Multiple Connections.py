import socket
import select

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8085))
server_socket.listen(5)

sockets_list = [server_socket]
print("Server berjalan di http://localhost:8085")

while True:
    read_sockets, _, _ = select.select(sockets_list, [], [])
    
    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            connection, address = server_socket.accept()
            sockets_list.append(connection)
            print(f"New connection from {address}")
        else:
            data = notified_socket.recv(1024)
            if not data:
                print(f"Connection {notified_socket.getpeername()} closed")
                sockets_list.remove(notified_socket)
            else:
                notified_socket.send(data)
# Fungsi: Mengelola banyak koneksi secara bersamaan menggunakan select.
# Kondisi: Ketika Anda ingin menangani banyak klien pada server tanpa blocking.
