
import socket

'''
Client Communication

socket()
connect() # scratched, for TCP only
bind() # for UDP only
send()
recv()
close()
'''

host = '127.0.0.1'
port = 1235
DEFSIZE = 1024

server = ('192.168.1.5', 1234)

mySock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mySock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySock.bind((host, port))

client_message = raw_input("-> ")
while client_message != 'q':
	mySock.sendto(client_message.encode(), server)
	server_message, addr = mySock.recvfrom(DEFSIZE)
	print('SERVER: ' +str(server_message))
	client_message = raw_input("-> ")

mySock.sendto('q'.encode(), server)
mySock.close()