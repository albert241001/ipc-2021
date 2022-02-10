# /usr/bin/python
#-*- coding: utf-8-*-
# -------------------------------------
import sys,socket,argparse

parser = argparse.ArgumentParser(description="""Client servidor""")
parser.add_argument("-s","--server",type=str,default='')
parser.add_argument("-p","--port",type=int,default=50001)
args=parser.parse_args()

HOST = args.server
PORT = args.port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
  data = s.recv(1024)
  if not data: break
  print('Data:', repr(data))
s.close()
sys.exit(0)
