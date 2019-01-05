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

host = "0.0.0.0"
port = 0
server = ('192.168.8.100', 1234)
myLock = threading.Lock()

mySock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mySock.bind((host, port))
mySock.setblocking(0)

SHUTDOWN = False

def recv_session(sock, lock):
	while not SHUTDOWN:
		try:
			lock.acquire()
			while True:
				data, addr = sock.recvfrom(1024)
				print(data.decode())
		except:
			time.sleep(0.1)
		finally:
			lock.release()


# recv data
thread1 = threading.Thread(target=recv_session, args=(mySock, myLock))
thread1.start()

# set username
username = raw_input("Enter username: ")

#send data
client_message = raw_input("-> ")
while client_message != 'q':
	if client_message != '':
		client_message = username +': ' +client_message
		mySock.sendto(client_message.encode(), server)
		myLock.acquire()
		client_message = raw_input("-> ")
		myLock.release()
		time.sleep(0.1)

SHUTDOWN = True

thread1.join()

mySock.close()
