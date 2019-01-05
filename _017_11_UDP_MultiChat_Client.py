import socket
import threading
import time

'''
Client Communication

socket()
connect() # scratched, for TCP only
bind() # for UDP only
send()
recv()
close()
'''

def recv_session(sock, lock):
	while True:
		lock.acquire()
		server_message, addr = sock.recvfrom(1024)
		if server_message.decode() == 'q':
			break
		print(server_message.decode())
		lock.release()

host = "0.0.0.0"
port = 0
server = ('192.168.8.100', 1234)
myLock = threading.Lock()

mySock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mySock.bind((host, port))

# set username
username = raw_input("Enter username: ")

# recv data
thread1 = threading.Thread(target=recv_session, args=(mySock, myLock))
thread1.start()

#send data
client_message = raw_input("-> ")
while client_message != 'q':
	client_message = username +': ' +client_message
	mySock.sendto(client_message.encode(), server)
	client_message = raw_input("-> ")

mySock.close()
