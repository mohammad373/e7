# e7

import os
import time
import requests
import socket
import sys
from colorama import Fore

def __target1__():
    os.system("clear")
    time.sleep(0.5)
    print(Fore.RED +"""
        ///////////////////////
        //////////////////////
        /////////////////////
        ////////////////////
        ///////////////////
        //////////////////
        /////////////////
        ////////////////
        ///////////////
        //////////////
        /////////////
        ////////////
        ///////////
        //////////
        /////////
        ////////
        ///////
        //////
        /////
        ////
        ///
        //
        /""")
    target = input(Fore.BLUE + "\n[!]" + Fore.RED + " ~ " + Fore.YELLOW + "Pleass Enter Your Address Target" + Fore.GREEN + " ==>  ")
    if target == "" or None:
        try:
            time.sleep(0.5)
            print(Fore.RED + "\nError : Your Target Is None Or Not Found ;(")
            time.sleep(1)
            sys.exit()
        except:
            pass
    if not "http" in target or not "https" in target :
        target = "http://" + target
    # ip = socket.gethostbyname(target)
    r = requests.get(target)
    while True:
         coun = 1   
         if r.status_code == 404 or r.status_code == 500:
             print(Fore.YELLOW + "[ " + Fore.RED + coun+ Fore.YELLOW + " ]" + Fore.BLUE + " ~ " + Fore.RED + target )
             coun += 1
         if r.status_code == 200:
             print(Fore.BLUE + "[ " + Fore.RED + coun+ Fore.BLUE + " ]" + Fore.BLUE + " ~ " + Fore.GREEN + target)
             coun += 1
         if coun == 10:
            time.sleep(0.1)
            sys.exit()

__target1__()
