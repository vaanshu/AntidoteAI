from termcolor import colored
import os
import time
import pyfiglet

def animate_text(text):
    for i in range(30):  
        print("\033c" + " " * i + colored(text, 'green'))
        time.sleep(0.1)


        

def after():
    choice = input("Do you want to search again? (y/n)")
    if choice.lower() not in ['y', 'n']:
        print("Bad input\nExiting...")
        time.sleep(3)
        exit()
    else:
        if choice.lower() == 'y':
            start()
        elif choice.lower() == 'n':
            print(pyfiglet.figlet_format('BYE , visit   again'))
            exit()

def run_PE():
    file = input("Enter the path and name of the file : ")
    os.system("python3 PE/extractPE.py {}".format(file))
    
def run_URL():
    url = input("Enter the URL: ")
    command = "python3 URL/extractURL.py {}".format(url)
    os.system(command)
    
def run_RamBooster():
    os.system("python3 RAM/processes.py")
    os.system("python3 RAM/action.py")
    
def run_JunkFileRemover():
    os.system("python3 CLEAN/main_menu.py")
    
def run_BGexeLiveScanner():
    os.system("python LIVEexe/x.py")
    
def run_systemHealthchecker():
    os.system("python HEALTH/healthcheck.py")
    


def exit_program():
    print(pyfiglet.figlet_format('BYE , visit   again'))
    os.system('exit')

def start():
    animate_text("Antivirus Loading . . . . . . . .")
    print(pyfiglet.figlet_format('ANTIDOTE AI'))
    print(" 1. PE scanner")
    print(" 2. URL scanner")
    print(" 3. RAM Booster")
    print(" 4. Junk File Finder")
    print(" 5. Running processes")
    print(" 6. System health checker")
    print(" 8. Exit\n")

    select = int(input("Enter your choice : "))

    if select in [1, 2, 3, 4, 5, 6, 7, 8]:
        if select == 1:
            run_PE()
            after()
        elif select == 2:
            run_URL()
            after()
        elif select == 3:
            run_RamBooster()
            after()
        elif select == 4:
            run_JunkFileRemover()
            after()
        elif select == 5:
            run_BGexeLiveScanner()
            after()
        elif select == 6:
            run_systemHealthchecker()
            after()
        elif select == 7:
            run_firewallNetworkDefender()
            after()
        else:
            exit_program()
    else:
        print("Bad input\nExiting...")
        time.sleep(3)
        exit()

start()
