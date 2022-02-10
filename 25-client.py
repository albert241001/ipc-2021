# /usr/bin/python
#-*- coding: utf-8-*-
# -------------------------------------
import sys,socket,os,argparse
from subprocess import Popen, PIPE
parser = argparse.ArgumentParser(description="""Client servidor""")
parser.add_argument("-s","--server",type=str,default='')
parser.add_argument("-p","--port",type=int,default=50001)
args=parser.parse_args()

HOST = args.server
PORT = args.port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
command="ps ax"
pipeData = Popen(command,shell=True,stdout=PIPE)
for line in pipeData.stdout:     
  s.send(line)
s.close()
sys.exit(0)
