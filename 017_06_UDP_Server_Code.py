
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

host = '192.168.1.5'
port = 1234
DEFSIZE = 1024

mySock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mySock.bind((host, port))

print('Server started...')

while True:
	data_recv, addr = mySock.recvfrom(DEFSIZE)
	data_recv = data_recv.decode()

	if not data_recv or data_recv == 'q':
		break

	print('Connection from <' +str(addr) +'>')
	print('\tMessage: ' +str(data_recv))
	server_message = input("-> ")
	mySock.sendto(server_message.encode(), addr)

mySock.close()