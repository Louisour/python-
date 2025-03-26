from socket import socket, AF_INET, SOCK_DGRAM
recv_socket = socket(AF_INET, SOCK_DGRAM)
recv_socket.bind(('127.0.0.1', 8888))

while True:
    recv_data,addr = recv_socket.recvfrom(1024)
    print('客户说:',recv_data.decode('utf-8'))
    if recv_data.decode('utf-8')=='bye':
        break
    data = input('客服回:')
    recv_socket.sendto(data, addr)
recv_socket.close()