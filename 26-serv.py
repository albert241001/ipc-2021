# /usr/bin/python3
#-*- coding: utf-8-*-
import sys,socket, os
from subprocess import Popen, PIPE
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", type=int, dest="port", metavar="port",
       help=" port del server", default=50001)
parser.add_argument("-d", "--debug", action="store_true", help="trace de les accions")
args=parser.parse_args()
HOST = ''
PORT = args.port
MYEOF = bytes(chr(4), 'utf-8')
DEBUG = args.debug
# ---------------------------------------------------------
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST,PORT))
s.listen(1)
while True:
    conn, addr = s.accept()
    print("Connected by", addr)
    while True:
        command = conn.recv(1024)
        if DEBUG: print('Recive', repr(command))
        if not command: break                
        pipeData = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
        for line in pipeData.stdout:
            conn.sendall(line)
            if DEBUG: sys.stderr.write(str(line,'utf-8'))
        for line in pipeData.stderr:
            conn.sendall(line)
            if DEBUG: sys.stderr.write(str(line,'utf-8'))        
        conn.sendall(MYEOF)        
    conn.close()
s.close()
sys.exit(0)




