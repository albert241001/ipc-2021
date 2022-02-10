# /usr/bin/python3
#-*- coding: utf-8-*-
# -------------------------------------
import sys, os, signal
a=60
def unmes(signum,frame):
  print("un minut mes!")
  actual=signal.alarm(0)
  signal.alarm(actual+60)

def unmenys(signum,frame):
  print("Un minut menys")
  actual=signal.alarm(0)
  if actual-60<0: 
    print("ignored %d" % (actual))
    signal.alarm(actual)
  else:
    signal.alarm(actual-60)

def reiniciar(signum,frame):
   actual=signal.alarm(0)
   signal.alarm(actual=60)  

def mostrar(signum,frame):
  print("queden %d segons",signal.alarm(0))

signal.signal(signal.SIGUSR2,unmenys) # 12
signal.signal(signal.SIGUSR1,unmes)   # 10
signal.signal(signal.SIGTERM,mostrar)
signal.signal(signal.SIGHUP,reiniciar)
signal.signal(signal.SIGINT,signal.SIG_IGN)
signal.alarm(a)
while True:
  pass
signal.alarm(0)
sys.exit(0)
