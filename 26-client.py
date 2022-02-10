# /usr/bin/python3
#-*- coding: utf-8-*-
import sys,socket
from subprocess import Popen, PIPE
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", type=int, dest="port", metavar="port",
       help="port del server", required=True)
parser.add_argument("-s", "--server", type=str, required=True, metavar="server",
       help="ip/host del servidor")
args=parser.parse_args()
HOST = args.server
PORT = args.port
MYEOF = bytes(chr(4), 'utf-8')
# -------------------------------------------------------------
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((HOST, PORT))
while True:
    command = input("~$ ")
    if not command: break    
    s.sendall(bytes(command, 'utf-8'))    
    while True:
        data = s.recv(1024)
        if data[-1:] == MYEOF: 
            print(str(data[:-1]))
            break
        print(str(data))
s.close()
sys.exit(0)
