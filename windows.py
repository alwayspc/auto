import subprocess
import os
import time

subprocess.call(['ipconfig'])
time.sleep(5)
subprocess.call("getmac")
time.sleep(5)
subprocess.call("netstat")
time.sleep(5)
print ("end")
sdsd