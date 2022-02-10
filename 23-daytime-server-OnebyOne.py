# /usr/bin/python3
#-*- coding: utf-8-*-
# -------------------------------------
import sys,socket
from subprocess import Popen, PIPE
HOST = ''
PORT = 50001    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

while True:
    conn, addr = s.accept()
    print("Connected by", addr)
    command ="date"
    pipeData = Popen(command,stdout=PIPE)
    for line in pipeData.stdout:   
        conn.send(line)
    conn.close()
sys.exit(0)

