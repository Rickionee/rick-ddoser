import platform
import os
from termcolor import colored
import time

def CheckOs():
    global OS
    OS=''
    if "aarch64" in platform.machine():
        OS = "termux"
    elif "Linux" in platform.platform() or "linux" in platform.platform():
        OS = "linux"
    elif "Windows" in platform.platform() or "windows" in platform.platform():
        OS = "windows"
    elif "darwin" in platform.platform() or "Darwin" in platform.platform():
        OS = "macos"
    else:
        print("os not identified, please make sure your platform is supported and tested.")
        quit()

CheckOs()

def GetRelDir():
    global rdir
    cdir = os.getcwd()
    cdir = cdir.replace('\\', '/')
    dk = cdir.split('/')
    rdir = cdir.replace(f'/{dk[len(dk)- 1]}', '')

if OS == "termux":
    GetRelDir()
    os.system(f"cd {rdir} && rm -rf rick-ddoser")
    os.system(f"cd {rdir} && git clone https://github.com/Rickionee/rick-ddoser && clear")
    print(colored("done...", 'green'))
    time.sleep(0.7)
    os.system(f"cd {rdir}/rick-ddoser")
