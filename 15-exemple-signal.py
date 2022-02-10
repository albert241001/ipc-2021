# /usr/bin/python3
#-*- coding: utf-8-*-
# -------------------------------------
import sys, os, signal
def myhandler(signum,frame):
  print("Signal handler called with signal:", signum)
  print("hasta luego lucas!")
  sys.exit(1)
def mydeath(signum,frame):
  print("Signal handler called with signal:", signum)
  print("no em dona la gana de morir!")
signal.signal(signal.SIGALRM,myhandler) # 14
signal.signal(signal.SIGUSR2,myhandler) # 12
signal.signal(signal.SIGUSR1,mydeath)   # 10
signal.signal(signal.SIGTERM,signal.SIG_IGN)
signal.signal(signal.SIGINT,signal.SIG_IGN)
signal.alarm(60)
print(os.getpid())
while True:
  pass
signal.alarm(0)
sys.exit(0)
