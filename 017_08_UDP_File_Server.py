
import socket
import os
import threading
import queue

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

def server_thread(sock, result_queue):

	filename, addr = sock.recvfrom(DEFSIZE)
	filename = filename.decode()

	print('Connection from <' +str(addr) +'>')

	if filename == 'q':
		result_queue.put(-1)
		return

	# if file exists
	if os.path.isfile(filename):
		fileSize = os.path.getsize(filename)
		server_message = 'File exists with size ' +str(fileSize)
		sock.sendto(server_message.encode(), addr)

		client_resp, addr = sock.recvfrom(DEFSIZE)
		client_resp = client_resp.decode()

		if client_resp.lower() == 'y':
			print(client_resp)
			with open(filename, 'rb') as f:
				while True:
					readBytes = f.read(DEFSIZE)
					if not readBytes:
						sock.sendto('QUIT'.encode(), addr)
						break
					sock.sendto(readBytes, addr)

			print('Finished sending ' +filename +' to <' +str(addr) +'>')
		else:
			result_queue.put(-1)
			return
	# if file does not exist
	else:
		server_message = 'File does not exist or is not a file'
		sock.sendto(server_message.encode(), addr)

def Main():

	DEFSIZE = 1024
	server_message = None
	fileSize = 0.0
	client_resp = None

	mySock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	mySock.bind((host, port))

	print('Server started')

	while True:
		result = queue.Queue(1)
		thread1 = threading.Thread(target=server_thread, args=(mySock, result))
		thread1.start()
		if result.get() == -1:
			result.task_done()
			break

	mySock.close()

if __name__ == '__main__':
	Main()

