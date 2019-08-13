import os
import time
import datetime

sec = time.time()
date = datetime.datetime.fromtimestamp(sec).strftime('%Y-%m-%d %H:%M:%S')

host = "google.com"
response = os.system("ping -w 3 " + host)

def logger(msg):
	with open("log.txt", 'a') as log:
            log.write(date + " >>>  " + msg + '\n')

if response == 0:
	print("wifi is up")
	logger("Wifi is up")
else:
	print("wifi is down")
	os.system("wifimanager")
	logger("Wifi is down")
