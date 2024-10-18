import socket 

def start_udp_server(host='localhostrick', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_socket.bind((host, port))

    print(f"UDP сервер запущено і слухає на {host}:{port}")
    
    while True:
        # Отримуємо повідомлення від клієнта
        message, client_address = server_socket.recvfrom(1024)
        device_id = message.decode('utf-8')
        print(f"Новий пристрій з ID: {device_id} підключився з {client_address}")

if __name__ == "__main__":
    start_udp_server()