import socket
import threading

def handle_request(conn):
    while True:
        request = conn.recv(1024)
        if not request:
            break
        print("Request:", request.decode())
        conn.sendall(b'HTTP/1.1 200 OK\r\n\r\nHello')
    conn.close()

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8093))
    server_socket.listen()
    print("Server berjalan di http://localhost:8093")
    while True:
        conn, addr = server_socket.accept()
        print("Koneksi diterima dari:", addr)
        threading.Thread(target=handle_request, args=(conn,)).start()

run_server()
# Fungsi: Menjalankan server yang dapat menangani beberapa koneksi secara bersamaan.
# Kondisi: Ketika Anda ingin melayani banyak klien tanpa memblokir.
