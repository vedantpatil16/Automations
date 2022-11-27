import subprocess
import os
import time
from sys import *
import datetime
import schedule

def ProcessLaunch(exepath):
    exists = os.path.exists(exepath)

    if exists:
        subprocess.Popen(exepath)

    else:
        print("No such executable file present")


def main():
    print("----------------Marvellous Infosystems Automations-----------------")

    print("Automation script started with name : ", argv[0])

    if (len(argv) != 2):
        print("Error : Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("Help : This script is used to launch an executable process")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Provide .... number of arguments as")
        print("First Argument as : Absolute Path of the executable you want to launch")
        exit()

    try:
        schedule.every().day.at("00:00").do(ProcessLaunch, argv[1])

    except ValueError:
        print("Error : Invalid Datatype of input")

    except Exception as E:
        print("Error : Invalid input ", E)

    while(1):
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    main()