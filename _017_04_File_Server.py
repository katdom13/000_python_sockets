import socket
import os
import threading

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
def session_thread(sock):

	DEFSIZE = 1024
	totalSize = 0
	filename = ''
	server_message = ''
	client_response = ''

	filename = sock.recv(DEFSIZE).decode()
	if os.path.isfile(filename):
		totalSize = os.path.getsize(filename)
		server_message = 'File exists with size ' +str(totalSize)
		sock.send(server_message.encode())
		client_response = sock.recv(1024).decode()
		if client_response == "y":
			print(client_response)
			with open(filename, 'rb') as f:
				readBytes = f.read(1024)
				if not readBytes:
					return
				sock.send(readBytes)
		else:
			return
	else:
		server_message = "File does not exist!"
		sock.send(server_message.encode())

def Main():
	host = '192.168.1.5'
	port = 1234

	mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mySock.bind((host, port))
	mySock.listen(5)

	print('Server started')

	# be able to accept multiple connections
	while True:
		c, addr = mySock.accept()
		print('Connection from <' +str(addr) +'>')
		thread1 = threading.Thread(target=session_thread, args=(c,))
		thread1.start()

	c.close()
	mySock.close()

if __name__ == '__main__':
	Main()
