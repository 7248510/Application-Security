import socket
import threading
#Black hat python inspired
IP = '0.0.0.0'
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT)) #Bind your IP and port
    server.listen(5) #Can accept 5 connections/5 threads
    print(f'[*] Listening on {IP}:{PORT}') #Will print the constents
    while True: #If the conditions are True then:
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,)) #Init the threads
        client_handler.start() #start

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'You have made a request')

if __name__ == '__main__':
    main()