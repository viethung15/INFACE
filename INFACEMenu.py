import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd INFACE && bash src/Logo.sh")

print("  \033[1;34m[1] >> \033[1;36;40mInfect")
print("  \033[1;34m[2] >> \033[1;36;40mUpdate")
print("  \033[1;34m[3] >> \033[1;36;40mAbout")
print("  \033[1;34m[4] >> \033[1;36;40mExit")

op=int(raw_input("Infect: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd INFACE && python2 src/INFACEMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && rm -rf AutoUpdateMyTools && git clone https://github.com/mishakorzik/AutoUpdateMyTools && bash AutoUpdateMyTools/Files/InfectUpdateUtility.sh")
elif(op==3):
 time.sleep(0.2)
 os.system("cd && cd INFACE && bash src/About.sh")
elif(op==4):
 time.sleep(0.2)
 print("\033[1;31;40mVui lòng chờ...")
 os.system("cd")
else:
 print("\033[1;31;40mInvalid input. Reloading Tool") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd INFACE")
 os.system("python2 INFACEMenu.py")
