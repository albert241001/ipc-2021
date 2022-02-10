# /usr/bin/python
#-*- coding: utf-8-*-
# -------------------------------------
import sys, argparse
parser = argparse.ArgumentParser(description=\
        """Count-by-users.py llistat de grups per gid, gname o nusers""",
        epilog="thats all folks")
parser.add_argument("-s","--sort",type=str,\
        help="sort criteria: gid | gname | nusers", metavar="criteria",\
        choices=["gid","gname","nusers"],dest="criteria")
parser.add_argument("userFile",type=str,\
        help="user file (/etc/passwd style)", metavar="userFile")
parser.add_argument("groupFile",type=str,\
        help="user file (/etc/passwd style)", metavar="groupFile")
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
    self.gname=""
    if self.gid in groupDict:
      self.gname=groupDict[self.gid].gname
    self.gecos=userField[4]
    self.home=userField[5]
    self.shell=userField[6]
  def __str__(self):
    "functió to_string d'un objcete UnixUser"
    return "%s %s %d %d %s %s %s %s" %(self.login, self.passwd, self.uid, self.gid, self.gname, self.gecos, self.home, self.shell)
# -------------------------------------------------------
class UnixGroup():
  """Classe UnixGroup: prototipus de /etc/group
  gname_passwd:gid:listUsers"""
  def __init__(self,groupLine):
    "Constructor objectes UnixGroup"
    groupField = groupLine.split(":")
    self.gname = groupField[0]
    self.passwd = groupField[1]
    self.gid = int(groupField[2])
    self.userListStr = groupField[3]
    self.userList=[]
    if self.userListStr[:-1]:
      self.userList = self.userListStr[:-1].split(",")
  def __str__(self):
    "functió to_string d'un objecte UnixGroup"
    return "%s %d %s" % (self.gname, int(self.gid), self.userList)
# -------------------------------------------------------
groupDict={}
groupFile=open(args.groupFile,"r")
for line in groupFile:
  group=UnixGroup(line)
  groupDict[group.gid]=group
groupFile.close()
# ---------------------------------
userFile=open(args.userFile,"r")
userList=[]
for line in userFile:
  user=UnixUser(line)
  userList.append(user)
  if user.gid in groupDict:
    if user.login not in groupDict[user.gid].userList:
      groupDict[user.gid].userList.append(user.login)
userFile.close()
# ---------------------------------
index=[]
if args.criteria=="gname":
  index = [ (groupDict[k].gname,k) for k in groupDict ]
elif args.criteria=="nusers":
  index = [ (len(groupDict[k].userList),k) for k in groupDict ]
else:
  index = [ k for k in groupDict ]
index.sort()

if args.criteria=="gname" or args.criteria=="nusers":
  for g,k in index:
   print(groupDict[k])
else:
  for k in index:
   print(groupDict[k])	
exit(0)
