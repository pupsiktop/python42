import socket
def handle_client(conn, address):
    print(f'connect client {address}')
    conn.sendall('hello!'.encode())
    while True:
        date = conn.recv(1024).decode(encoding = 'utf-8')
        if date == False:
            print('Disconnect')
            break
        print(f'Massage from{address}:{date}')
        response = input('input response to client')
        conn.sendall((response + '\n').encode())

host = '127.0.0.1'
port = 3000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port)) #связывание с адресом
    print(f'server {host} runer')
    s.listen()
    while True:
        conn, address = s.accept()
        handle_client(conn, address)
        print('waiting for the next client')