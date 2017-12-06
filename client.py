import socket

host_ip = '192.168.0.170'
server_port = 9999

data = "1"

# Initialize a TCP client socket using SOCK_STREAM
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	#Establish connection to TCP server and exchange data
	tcp_client.connect((host_ip, server_port))
	tcp_client.sendall(data.encode())

	# Read data from the TCP server
	received = tcp_client.recv(1024)
finally:
	tcp_client.close()

print("Bytes sent:		{}".format(data))
print("Bytes received: 	{}".format(received.decode()))


