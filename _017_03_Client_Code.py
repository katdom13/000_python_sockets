import socket

'''
Client Communication

socket()
connect()
send()
recv()
close()
'''

host = '192.168.1.5'
port = 1234

mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySock.connect((host, port))

client_message = raw_input('-> ')

while client_message != 'q':
	mySock.send(client_message.encode())
	data_recv = mySock.recv(1024).decode()
	print('SERVER: ' +str(data_recv))
	client_message = raw_input('-> ')

mySock.close()