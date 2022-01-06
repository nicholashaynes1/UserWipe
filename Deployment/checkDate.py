import os
from datetime import datetime, timedelta
import subprocess


today = datetime.today()

path = "C:\\Users\\date.txt"
dataFormat = "%Y-%m-%d"

with open(path, 'r') as f:
	loggedDate = f.read()
	loggedDate = datetime.strptime(loggedDate,dataFormat)

if (today-loggedDate).days >= 7: 
	print(subprocess.run("C:\\wipeUsers.exe", stdout=subprocess.PIPE).stdout.decode('utf-8')) 

else: print("Less than 7 days")