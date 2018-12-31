import socket

'''
Server communication

socket()
bind()
listen()
accept()
recv()
send()
close()
'''

host = '192.168.1.5'
port = 1234

mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.bind((host, port))
mySock.listen(1)

print('Server started')

client, client_addr = mySock.accept()

print(f'Connection from ' + str(client_addr))

# eternal listening for connections
while True:
	data_recv = client.recv(1024).decode()
	if not data_recv or data_recv == 'q':
		break

	print('CLIENT: ' +str(data_recv))
	server_msg = input("SERVER: ")
	client.send(server_msg.encode())

client.close()
mySock.close()





