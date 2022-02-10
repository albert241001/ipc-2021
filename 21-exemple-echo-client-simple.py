# /usr/bin/python3
#-*- coding: utf-8-*-
# -------------------------------------
import sys,socket
HOST = ''
PORT = 50001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((HOST, PORT))
s.send(b'Hello, world')
data = s.recv(1024)
s.close()
print('Received', repr(data))
sys.exit(0)

