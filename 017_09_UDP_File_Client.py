
import socket
import re
import os

'''
Client Communication

socket()
connect() # scratched, for TCP only
bind() # for UDP only
send()
recv()
close()
'''

DEFSIZE = 1024

def client_connect(sock, server):
	filename = raw_input("Enter filename to request: ")

	sock.sendto(filename.encode(), server)

	server_reply, addr = sock.recvfrom(DEFSIZE)

	fileSize_pattern = re.compile(r'\d+')
	fileSize_match = fileSize_pattern.search(server_reply)
	fileSize = fileSize_match.group(0)

	if not fileSize:
		return

	fileSize = float(fileSize)

	client_resp = raw_input("Do you want to download it? (y/n): ")

	if client_resp == 'y':
		sock.sendto(client_resp.encode(), server)
		if os.path.exists('new_' +filename):
			os.remove('new_' +filename)
		with open('new_' +filename, 'ab') as f:
			while True:
				data, addr = sock.recvfrom(DEFSIZE)
				if data == 'QUIT':
					break
				f.write(data)
				bytesRead = len(data)
				print(str(bytesRead / float(fileSize) * 100) +'% downloaded...')
			
			print('Download complete!')

	else:
		return

def Main():

	host = '0.0.0.0'
	port = 1236
	server = ('192.168.1.5', 1234)
	
	mySock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	mySock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	mySock.bind((host, port))

	client_connect(mySock, server)

	mySock.close()

if __name__ == '__main__':
	Main()