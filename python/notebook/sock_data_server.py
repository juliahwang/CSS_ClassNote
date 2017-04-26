import socket
from time import ctime

host = 'localhost'
port = 12345
bufsiz = 1024
addr = (host, port)

if __name__ == "__main__":
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(addr)
	server_socket.listen(5)
	server_socket.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	while True:
		print("Server is listening...")
		client_sock, addr = server_socket.accept()
		print("Client connected")

		while True:
			data = client_sock.recv(bufsiz)
			if not data or data.decode('utf-8') == 'END':
				break

			print("received from client")
			print("sending the server time to client: ", ctime())

			try:
				client_sock.send(bytes(ctime(), 'utf-8'))
			except KeyBoardInterrupt:
				print("Exited by user")

		client_sock.close()
	server_socket.close()
	
