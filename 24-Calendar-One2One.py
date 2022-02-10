# /usr/bin/python3
#-*- coding: utf-8-*-
# -------------------------------------
import sys,socket,os,argparse
from subprocess import Popen, PIPE
parser = argparse.ArgumentParser(description="""CAL server""")
parser.add_argument("-a","--any",type=int, default=2021)
parser.add_argument("-p","--port",type=int, default=50001)
args=parser.parse_args()

pid=os.fork() 
if pid !=0:   
    print("Programa Pare(MORT)", os.getpid(), pid)   
    sys.exit(0)

print("Programa fill", os.getpid(), pid)
HOST = ''
PORT = args.port
ANY = args.any

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

while True:
    conn, addr = s.accept()
    print("Connected by", addr)
    command ="cal %d" % (ANY)
    pipeData = Popen(command,shell=True,stdout=PIPE)
    for line in pipeData.stdout:   
        conn.send(line)
    conn.close()
sys.exit(0)
