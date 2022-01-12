# /usr/bin/python
#-*- coding: utf-8-*-
import argparse
parser=argparse.ArgumentParser(description=\
  "programa exemple de processar arguments",prog="2-argument.py",epilog="hasta luegu lucas!")
parser.add_argument("-e","--edat", type=int, dest="useredat", help="edat a processar", metavar="edat")
parser.add_argument("-n","--nom", type=str, help="nom de usuari")
parser.add_argument("fit", type=str, help="fitxer")
args=parser.parse_args()
print(parser)
print(args)
print(args.useredat, args.nom)
exit(0)

