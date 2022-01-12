# /usr/bin/python
#-*- coding: utf-8-*-
#
# head [file]
#  10 lines, file o stdin
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys
MAXLIN=10
fileIn=sys.stdin
if len(sys.argv)==2:
  fileIn=open(sys.argv[1],"r")
counter=0
#si hi ha 2 arguments llegeix
for line in fileIn:
  counter+=1
  print (line, end="")
  if counter==MAXLIN: break
#lee lineas hasta llegar al max
fileIn.close()
exit(0)

