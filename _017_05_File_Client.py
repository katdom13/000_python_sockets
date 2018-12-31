import socket
import re

'''
Client Communication

socket()
connect()
send()
recv()
close()
'''
def session_connect(sock):
	filename = raw_input("Enter filename to request: ")
	sock.send(filename.encode())
	data_recv = sock.recv(1024).decode()

	print(data_recv)
	pattern = re.compile(r'\d+')
	szTotalSize = pattern.search(str(data_recv))
	if not szTotalSize:
		return

	client_resp = raw_input("Do you want to download it? (y/n): ")

	if(client_resp == "y"):
		sock.send(client_resp.lower().encode())
		with open('new_' +filename, 'ab') as f:
			data_recv = sock.recv(1024).decode()
			if not data_recv:
				return
			byteSize = len(data_recv)
			f.write(data_recv)
			print(str(byteSize / float(szTotalSize.group(0)) * 100) +'% Downloaded')
		print('Download complete!')
	
def Main():
	host = '192.168.1.5'
	port = 1234

	mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mySock.connect((host, port))

	session_connect(mySock)

	mySock.close()

if __name__ == '__main__':
	Main()