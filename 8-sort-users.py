# /usr/bin/python
#-*- coding: utf-8-*-
import sys, argparse
parser = argparse.ArgumentParser(description=\
        """Llistar els usuaris de file o stdin (format /etc/passwd""",\
        epilog="thats all folks")
parser.add_argument("-s","--sort",type=str,\
        help="sort criteria: login | gid", metavar="criteria",\
        choices=["login","gid"],dest="criteria",default="login")
parser.add_argument("-u","--userFile",type=str,\
        help="user file (/etc/passwd style)", metavar="userFile",required=True)
parser.add_argument("-g","--groupFile",type=str,\
        help="user file (/etc/passwd style)", metavar="groupFile",required=True)
args=parser.parse_args()
# -------------------------------------------------------
class UnixUser():
  """Classe UnixUser: prototipus de /etc/passwd
  login:passwd:uid:gid:gecos:home:shell"""
  def __init__(self,userLine):
    "Constructor objectes UnixUser"
    userField=userLine.split(":")
    self.login=userField[0]
    self.passwd=userField[1]
    self.uid=int(userField[2])
    self.gid=int(userField[3])
    self.gecos=userField[4]
    self.home=userField[5]
    self.shell=userField[6][:-1]
  def show(self):
    "Mostra les dades de l'usuari"
    print("login: {self.login} uid: {self.uid} gid: {self.gid} gecos: {self.gecos} home: {self.home} shell: {self.shell}")
  def __str__(self):
    "functió to_string"
    return "%s %s %d %d %s %s %s" %(self.login, self.passwd, self.uid, self.gid, self.gecos, self.home, self.shell)
def ord_login(user):
    return user.login
def sort_gid(user):
  '''Comparador d'usuaris segons el gid'''
  return (user.gid, user.login)
# -------------------------------------------------------
class UnixGroup():
  def __init__(self,groupLine):
    "Constructor objectes UnixUser"
    groupField=groupLine.split(":")
    self.name=userField[0]
    self.passwd=userField[1]
    self.gid=int(userField[3])
    self.members=userField[4]
  def __str__(self):
    "functió to_string"
    return "%s %d %s" %(self.name, self.passwd, self.gid, self.members)


# -------------------------------------------------------
fileIn=open(args.fitxer,"r")
userList=[]
for line in fileIn:
  oneUser=UnixUser(line)
  userList.append(oneUser)
fileIn.close()
if args.criteria=="login":
  userList.sort(key=sort_login)
else:
  userList.sort(key=sort_gid)
for user in userList:
 print(user)

# -------------------------------------------------------
groupFile=open(args.groupFile,"r") 
for line in groupFile:   
    group=UnixGroup(line)   
    groupDict[group.gid]=group 
groupFile.close()
exit(0)
