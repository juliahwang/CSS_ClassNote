import socket
import sys

'''TCP socket making'''
if __name__ == '__main__':
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error as e:
		print("Failed")
		print("Reason: %s" % str(e))
		sys.exit(); ''' sys module uses semi-colon.'''
	
	print("socket created")

	host = input("Enter host: ")
	port = input("Enter port: ")


''' try connecting with socket '''
	try:
		sock.connect((host, int(port)))
		print("socket connected")
		sock.shutdown(2)  '''2: shutdown both server and client'''
	except sock.error as err:
		print("Failed")
		print("Reason: ", str(err))
		sys.exit();		
