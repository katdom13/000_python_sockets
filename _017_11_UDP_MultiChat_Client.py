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

def send_session(sock, server, lock):
	client_username = raw_input("Username: ")
	client_message = raw_input("-> ")
	while client_message != "q":
		client_message = client_username +": " +client_message
		sock.sendto(client_message.encode(), server)
		lock.acquire()
		client_message = raw_input("-> ")
		lock.release()
		client_message = client_message.decode()
		time.sleep(0.1)

	sock.sendto(client_message.encode(), server)

def recv_session(sock, lock):
	while True:
		lock.acquire()
		data, addr = sock.recvfrom(1024)
		data = data.decode()
		if data == 'q':
			break
		print(data.decode())
		lock.release()
		time.sleep(0.2)
	
host = "0.0.0.0"
port = 0
server = ('192.168.8.100', 1234)
myLock = threading.Lock()

mySock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mySock.bind((host, port))

#send thread
send_t = threading.Thread(target=send_session, args=(mySock, server, myLock))
#recv thread
recv_t = threading.Thread(target=recv_session, args=(mySock, myLock))

send_t.start()
recv_t.start()

send_t.join()
recv_t.join()

mySock.close()