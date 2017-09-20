# server.py
import socket
import time
import atexit

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

TCP_IP = '192.168.0.118'
TCP_PORT = 3000
BUFFER_SIZE = 2048

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

# establish a connection
print 'looking for connection...'
conn, addr = s.accept()
print 'Connection address:', addr

while True:
    print "type a command (listen or send):"
    cmd = raw_input()
    
    if (cmd == "listen"):
        print "listening..."
        t_end = time.time() + 15
        while time.time() < t_end:
            data = conn.recv(BUFFER_SIZE)
            if not data: break
            print "received data:", data
        #conn.close()
    elif (cmd == "send"):
        print "data to send: ",
        data = raw_input()
        conn.sendall(data)
    elif (cmd == "exit"):
        conn.close()

def closing():
    conn.close()

atexit.register(closing)

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
