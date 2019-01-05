
import socket

'''
Server communication

socket()
bind()
listen() // scratched, for TCP only
accept() // scratched, for TCP only
recv() recvfrom()
send() sendto()
close()
'''

host = '192.168.8.100'
port = 1234
DEFSIZE = 1024
client_list = []

mySock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mySock.bind((host, port))

print('Server started')

while True:
	client_data, addr = mySock.recvfrom(DEFSIZE)
	client_data = client_data.decode()
	if client_data == 'q':
		break
	print(str(client_data))
	if addr not in client_list:
		client_list.append(addr)
	for c in client_list:
		mySock.sendto(client_data.encode(), c)

mySock.close()