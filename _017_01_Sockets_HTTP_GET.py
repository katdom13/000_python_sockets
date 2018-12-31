
import socket

HOST = 'www.cs.cmu.edu' # strictly no http prefix
PORT = 80

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect((HOST, PORT))

# client send GET request
szCommand = 'GET ' +'https://www.cs.cmu.edu/~spok/grimmtmp/122.txt' +' HTTP/1.0\n\n'
mysocket.send(szCommand.encode())

#recv data
while True:
	szDataRead = mysocket.recv(1024)
	if(len(szDataRead) <= 0):
		break
	print(szDataRead.decode())
	
mysocket.close()
