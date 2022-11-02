import os
import sys
import time
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./20)
slowprint("Tool Spam Sms By Nguyễn Cao Sang")
time.sleep(1.0)
slowprint("[+] Install Resources . . .")
os.system("pip install pystyle")
os.system("pip install colorama")
os.system("pip install requests")
slowprint("[+]Install Successful")

