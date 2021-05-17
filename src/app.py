import os
import subprocess


def fetchfile():
    getpath = input("Enter Path to check files:  ")
    print(f'Entered path:  {getpath}')
    try:
        dir_list = os.listdir(getpath)
        print(f'Below are the list of files and directories from {getpath}')
        for file in dir_list:
            print(file)
    except Exception as e:
        print(e)


def runcommand():
    # 1. method
    scout = os.popen("df -h")
    print(f"Long list of files in present directory: \n{scout.read()}")
    # 2. Method
    scout1 = subprocess.Popen("ls -l", shell=True)
    print(scout1.communicate())
    # 3. Method
    putcmd = input("Enter OS Command:")
    scout2 = subprocess.Popen(putcmd, shell=True)
    print(f'{scout2.communicate()}')


runcommand()
fetchfile()
