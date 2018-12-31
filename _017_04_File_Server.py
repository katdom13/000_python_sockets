
import socket
import os
import threading

# 1) The server will wait for clients to connect then request a file
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

# ============== VARIABLES ================

host = '192.168.1.5'
port = 1234
totalSize = 0
filename = ''
server_message = ''
client_response = ''

mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.bind((host, port))
mySock.listen(5)
c, addr = mySock.accept()

while True:
	filename = c.recv(1024).decode()
	if filename == "q" or not filename:
		break
	if os.path.isfile(filename):
		totalSize = os.path.getsize(filename)
		server_message = 'File exists with size ' +str(totalSize)
		c.send(server_message.encode())
		client_response = c.recv(1024).decode()
		if client_response == "y":
			print(client_response)
			with open(filename, 'rb') as f:
				readBytes = f.read(1024)
				if not readBytes:
					break
				c.send(readBytes)
		else:
			break
	else:
		server_message = "File does not exist!"
		c.send(server_message)

c.close()
mySock.close()

'''
mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySock.bind((host, port))
mySock.listen(5)

print('Server started')

client, client_addr = mySock.accept()

while True:
	filename = client.recv(1024).decode()
	if not filename or filename == 'q':
		break

	# 2) If the file exists then we start sending it to the client otherwise we tell them the file does not exist

	if os.path.isfile(filename):
		# print('File exists')
		filesize = os.path.getsize(filename)
		defSize = 1024
		server_message = 'File exists with size: ' +str(filesize)
		client.send(server_message.encode())

		client_response = client.recv(1024).decode()
		
		#if(str(client_response).lower() == "y"):
		#	print(str(client_response))
		
		if(str(client_response).lower() == 'y'):
			print(str(client_response))
			with open(filename, 'rb') as f:
				while True:
					readBytes = f.read(defSize)
					if not readBytes:
						break
					client.send(readBytes)

	else:
		server_message = 'File does not exist'
		client.send(server_message)

client.close()
mySock.close()
		
'''

