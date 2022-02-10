#!/usr/bin/python
#-*- coding: utf-8-*-
import socket, sys, select, os, argparse 
from subprocess import Popen, PIPE

HOST = '10.200.243.212'                 
PORT = 50002            
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print(os.getpid())
conns=[s]
while True:
    actius,x,y = select.select(conns,[],[])
    for actual in actius:
        if actual == s:
            conn, addr = s.accept()
            print('Connected by', addr)
            conns.append(conn)
        else:
            while True:
                cmd = actual.recv(1024)
                if not cmd: 
                    break
                pipeData = Popen(cmd,shell=True, stdout=PIPE, stderr=PIPE)
                for line in pipeData.stdout:
                    actual.send(line)
                for line in pipeData.stderr:
                    actual.send(line)
                conn.send(b'\x04')
s.close
sys.exit(0)
