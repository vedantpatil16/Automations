import re
import os
from sys import *
import time

def ReadFile(Fname,log_dir, blocksize=1024):

    if (os.path.isabs(Fname)):
        pass
    else:
        Fname = os.path.abspath(Fname)

    if os.path.exists(log_dir):
        pass
    else:
        try:
            os.mkdir(argv[2])
        except:
            pass

    regex = re.compile("Enter * (card number|cvv|bank details)", flags=re.I)
    regex2 = re.compile("sex|fuck", flags=re.I)
    regex3 = re.compile("(http:|https:|www\.) * porn|videos|naughty|xxx|hot", flags=re.I)
    log_dir = os.path.join(log_dir, "MaliciousLog%s.log" % (time.time()))

    if(os.path.exists(Fname)):
        fd = open(Fname, "r")
        Data = fd.read(blocksize)
        if(re.search(regex, Data)):
            separator = "-" * 80
            f = open(log_dir, 'a')
            f.write(separator + "\n")
            f.write("%s may contain financially suspicious activities"%Fname + "\n")
            f.write(separator + "\n")


        else:
            pass

        matches = re.findall(regex2, Data)
        if(len(matches) > 3):
            f = open(log_dir, 'a')
            f.write(separator + "\n")
            f.write("%s may contain some unethical malicious words" % Fname + "\n")
            f.write(separator + "\n")

        else:
            pass

        if(re.search(regex3, Data)):
            f = open(log_dir, 'a')
            f.write(separator + "\n")
            f.write("%s may contain some links for malicious websites" % Fname + "\n")
            f.write(separator + "\n")

        else:
            pass

    else:
        print("This file doesn't exist")



def main():

    print("----------------Marvellous Infosystems Automations-----------------")

    print("Automation script started with name : ", argv[0])

    if (len(argv) != 3):
        print("Error : Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("Help : This script is used to launch an executable process")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Provide 2 number of arguments as")
        print("First Argument as : File you want to read")
        print("Second Argument : Absolute path of directory")
        exit()

    try:
        ReadFile(argv[1], argv[2])

    except ValueError:
        print("Error : Invalid Datatype of input")

    except Exception as E:
        print("Error : Invalid input ", E)

if __name__ == "__main__":
    main()