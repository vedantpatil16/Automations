import psutil

def ProcessDisplay():

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'username', 'name'])

            if pinfo['name'] == "Notepad.exe":
                print("Found")
                break

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def main():
    print("Marvellous Infosystems : Python Automation & Machine Learning")

    print("Process Monitor")

    ProcessDisplay()

if __name__ == "__main__":
    main()