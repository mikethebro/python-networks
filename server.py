# server.py
import socket
import time

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

TCP_IP = '192.168.0.118'
TCP_PORT = 3000
BUFFER_SIZE = 2048

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while True:
    # establish a connection
    conn, addr = s.accept()
    print 'Connection address:', addr
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        print "received data:", data
    conn.close()

"""
# get local machine name
host = socket.gethostname()

port = 3000

# bind to the port
serversocket.bind((host, port))

print 'starting up on' + host + ' port ' + str(port)
# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()
    
    print("Got a connection from %s" % str(addr))
    print(serversocket.data)
    #currentTime = time.ctime(time.time()) + "\r\n"
    #clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()
"""
