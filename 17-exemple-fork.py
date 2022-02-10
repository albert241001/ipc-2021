# /usr/bin/python
#-*- coding: utf-8-*-
import sys,os
print("Hola, començament del programa principal")
print("PID pare: ", os.getpid())

pid=os.fork()
if pid !=0:
#  os.wait()
  print("Programa Pare", os.getpid(), pid)
else:
  print("Programa fill", os.getpid(), pid)
  while True:
      pass
print("Hasta lugo lucas!")
sys.exit(0)

