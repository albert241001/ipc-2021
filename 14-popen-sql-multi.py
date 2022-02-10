# /usr/bin/python
#-*- coding: utf-8-*-
# -------------------------------------------
import sys
from subprocess import Popen, PIPE
import argparse
#clieList=[]
parser = argparse.ArgumentParser(description='Consulta SQL interactiva')
parser.add_argument("-d","--database", help="base de dades a usar",\
     default="training")
parser.add_argument('-c',"--client", help='client',type=str,\
     action="append",dest="clieList",required="True")
args = parser.parse_args()
# -------------------------------------------
cmd = "psql -qtA -F',' -h 172.17.0.2 -U postgres "+ args.database
pipeData = Popen(cmd, shell = True, bufsize=0, universal_newlines=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
for num_clie in args.clieList:
  sqlStatment="select * from clientes where num_clie=%s;" % (num_clie)
  pipeData.stdin.write(sqlStatment+"\n")
  print(pipeData.stdout.readline(), end="")

pipeData.stdin.write("\q\n")
sys.exit(0)


