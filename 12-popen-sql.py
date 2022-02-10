# /usr/bin/python
#-*- coding: utf-8-*-
import sys, argparse
from subprocess import Popen, PIPE
# -------------------------------------------------------
command = " psql -qtA -F',' -h 172.17.0.2 -U edtasixm06 training -c \"select * from clientes; \""
pipeData = Popen(command,shell=True,stdout=PIPE)
for line in pipeData.stdout:
  print(line.decode("utf-8"), end="")
exit(0)

