import socket

def client_program():
    client_socket = socket.socket()
    client_socket.connect(('localhost', 5000))

    with open('file_to_send', 'rb') as f:
        print("Sending file...")
        data = f.read(1024)
        while data:
            client_socket.send(data)
            data = f.read(1024)
            
    print("File sent.")
    client_socket.close()

if __name__ == '__main__':
    client_program()