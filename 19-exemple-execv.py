# /usr/bin/python
#-*- coding: utf-8-*-
# -------------------------------------
import sys,os
print("Hola, començament del programa principal")
print("PID pare: ", os.getpid())

pid=os.fork()
if pid !=0:
  print("Programa Pare", os.getpid(), pid)
  sys.exit(0)

print("Programa fill", os.getpid(), pid)
#os.execv("/usr/bin/ls",["/usr/bin/ls","-ls","/"])
#os.execl("/usr/bin/ls","/usr/bin/ls","-ls","/")
#os.execlp("ls","ls","-ls","/")
#os.execvp("uname",["uname","-a"])
#os.execv("/usr/bin/bash",["/usr/bin/bash","/var/tmp/m06/ipc-2019/show.sh"])
os.execle("/usr/bin/bash","/usr/bin/bash","show.sh",{"nom":"joan","edat":"25"})
print("Hasta lugo lucas!")
sys.exit(0)


