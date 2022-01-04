import os
from getpass import getuser
from datetime import date, timedelta

today = date.today() - timedelta(days=7)

user = getuser() 
path = "C:\\Users\\%s\\date.txt" % user

with open(path, 'w') as f:
	f.write(str(today))