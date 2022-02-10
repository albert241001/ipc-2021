# /usr/bin/python
#-*- coding: utf-8-*-
import sys,os
print("Hola, començament del programa principal")
print("PID pare: ", os.getpid())

pid=os.fork()
if pid !=0:
  print("Programa Pare", os.getpid(), pid)
  sys.exit(0)

print("Programa fill", os.getpid(), pid)
os.execv("/usr/bin/python",["/usr/bin/python","16-signal.py","60"])
print("Hasta lugo lucas!")
sys.exit(0)

