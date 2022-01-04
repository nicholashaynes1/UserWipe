import os
from getpass import getuser
from datetime import date

today = date.today()

user = getuser() 
path = "C:\\Users\\%s\\date.txt" % user

with open(path, 'w') as f:
	f.write(str(today))