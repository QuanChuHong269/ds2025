import socket

def server_program():
    server_socket = socket.socket()
    server_socket.bind(('localhost', 5000))
    server_socket.listen(1)
    conn, address = server_socket.accept()

    print("Connection from: " + str(address))
    
    with open('received_file', 'wb') as f:
        print("Receiving file...")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)
    print("File received.")
    conn.close()

if __name__ == '__main__':
    server_program()