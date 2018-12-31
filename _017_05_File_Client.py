
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

host = '192.168.1.5'
port = 1234

mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect((host, port))

# 1) The client will ask user for filename to request

filename = raw_input("Enter filename to request: ")

while filename != 'q':
	mySock.send(filename.encode())
	data_recv = mySock.recv(1024).decode()

	print(data_recv)

	# regex part
	pattern = re.compile(r'\d+')
	szTotalSize = pattern.search(str(data_recv))
	if not szTotalSize:
		break

	# 2) Will then inform the user if the file exists or not and then tells them the size of the file
	# and if they wish to download it

	client_resp = raw_input("Do you want to download it? (y/n): ")

	if(client_resp == "y"):
		mySock.send(client_resp.lower())
		with open('new_' +filename, 'ab') as f:
			data_recv = mySock.recv(1024).decode()
			if not data_recv:
				break
			byteSize = len(data_recv)
			f.write(data_recv)
			print(str(byteSize / float(szTotalSize.group(0)) * 100) +'% Downloaded')
		print('Download complete!')
	
mySock.close()

	# 3) Downloads the file into the local directory and adds a 'new_' prefix to the title


