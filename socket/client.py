import socket
host = '127.0.0.1'
port = 3000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    welcome = s.recv().decode()
    print(welcome)
    while True:
        message = input('input message')
        if message == False:
            break
        s.sendall((message + '\n').encode())
        response = s.recv(1024).decode
        print(f'response from {host}: {response}')
        print('Disconnect')