from socket import socket, AF_INET, SOCK_DGRAM
recv_socket = socket(AF_INET, SOCK_DGRAM)
recv_socket.bind(('127.0.0.1', 8888))
recv_data,addr=recv_socket.recvfrom(1024)
print('接收到的数据:',recv_data.decode('utf-8'))


data=input('请输入回复的数据')
recv_socket.sendto(data.encode('utf-8'),addr)

recv_socket.close()