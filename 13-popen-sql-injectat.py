# /usr/bin/python
#-*- coding: utf-8-*-

import sys,argparse
from subprocess import Popen, PIPE

parser = argparse.ArgumentParser(description=\
        """Consulta a la base de dades entrada per argument al prigrama.""")
parser.add_argument("cons",type=str,\
        help="consulta a la base de dades training")
args=parser.parse_args()

# ------------------------------------------------------------------------------

command = [f"psql -qtA -F',' -h 172.17.0.2 -U postgres training -c \"{args.cons}\""]
pipeData = Popen(command, stdout=PIPE, shell=True)


for line in pipeData.stdout:
    print(line.decode("utf-8")[:-1])

exit(0)

