# /usr/bin/python
#-*- coding: utf-8-*-
import sys,socket,os,signal,argparse,time
from subprocess import Popen, PIPE
HOST = ''
PORT = 50001
pid=os.fork()
if pid !=0:
  print("Engegat el server CAL:", pid)
  sys.exit(0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
while True:
  conn, addr = s.accept()
  fileName="/tmp/%s-%s-%s.log" % (addr[0],addr[1],time.strftime("%Y%m%d-%H%M%s"))
  fileLog=open(fileName,"w")
  while True:
    data = conn.recv(1024)
    if not data: break
    fileLog.write(str(data))
  conn.close()
  fileLog.close()
s.close()

