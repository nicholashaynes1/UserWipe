import os
from datetime import date, timedelta

today = date.today() - timedelta(days=7)

path = "C:\\Users\\date.txt"

with open(path, 'w') as f:
	f.write(str(today))