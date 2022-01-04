import os
from getpass import getuser
from datetime import datetime, timedelta


today = datetime.today()

user = getuser() 
path = "C:\\Users\\%s\\date.txt" % user
dataFormat = "%Y-%m-%d"

with open(path, 'r') as f:
	loggedDate = f.read()
	loggedDate = datetime.strptime(loggedDate,dataFormat)

if (today-loggedDate).days >= 7: print("It has been more than 7 days")
else: print("Less than 7 days")