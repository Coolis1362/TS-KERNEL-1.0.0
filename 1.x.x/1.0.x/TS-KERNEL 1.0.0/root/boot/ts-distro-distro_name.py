import time
import os

def put_distro_name_here(): # Replace put_distro_name_here with the name of your distro
    MAIN_USER_NAME = "ADMIN_USER"
    DISTRO_NAME_PREFIX = "TS-DISTRO"
    DISTRO_NAME = "distro_name" # Replace distro_name with the name of your distro
    print(f"Welcome To {DISTRO_NAME_PREFIX} {DISTRO_NAME}!")
    time.sleep(2)
    print("This is Based on TS-KERNEL 1.0.0")
    time.sleep(2)
    print("Loading...")
    time.sleep(2)
    for step in range(100):
        print("#", end="", flush=True)
        time.sleep(0.05)
    
    os.system("cls" if os.name == "nt" else "clear")
    time.sleep(2)
    print("****************************************************************")
    print(f"*        WELCOME TO {DISTRO_NAME_PREFIX} {DISTRO_NAME}                      *") # The Spaces Depends On How Long The Distro Name
    print("*                        NO COPYRIGHT                          *")
    print("*             YOU CAN MAKE A DISTRO BASED ON IT!               *")
    print("*                  TYPE 'help' FOR COMMANDS                    *")
    print("****************************************************************")

    while True:
        tsdistrocommand = input(f"CONSOLE FOR {DISTRO_NAME_PREFIX} {DISTRO_NAME}>>>> ")
        if tsdistrocommand == "help":
            print("Commands:")
            print("help - Show this help message")
            print("exit - Exit the console")
            print("clear - Clear the console")
            print("whoami - Show the current user")
            print("add your commands here") # Replace It With Your Comamnds and On

        elif tsdistrocommand == "exit":
            print("Exiting...")
            time.sleep(1)
            os.system("taskkill /F /IM cmd.exe")
            os._exit(0)

        elif tsdistrocommand == "clear":
            os.system("cls" if os.name == "nt" else "clear")

        elif tsdistrocommand == "whoami":
            print(f"Current user: {MAIN_USER_NAME}")




if __name__ == "__main__": # DON'T REMOVE THIS LINE
    put_distro_name_here() # REPLACE THIS LINE WITH THE NAME OF THE MAIN FUNCTION



# use auto-py-to-exe to Turn this Code To An .exe And replace The current .exe With Yours If auto-py-to-exe is not installed use pip install auto-py-to-exe to install it
# And Add C:\Users\<YourUsername>\AppData\Local\Programs\Python\<PythonVersion>\Lib\site-packages to Yuor PATH (Search How To Add It to PATHS)
# And Type in auto-py-to-exe In Your Terminal To Run It and Choose This File Yuo Had Edited and Choose The Output Folder As C:\Path\To\TS-KERNEL 1.0.0\root\boot\ And Choose The Icon You Want To Use And Click On Convert .py To .exe And Wait For It To Finish (Replace C:\Path\To\TS-KERNEL 1.0.0 With The Actal Path To Your TS-KERNEL 1.0.0 Folder) (AND DON'T FORGET TO TEST IT!)
# When You're Done Upload This To GitHub As Your Title Being Like TS-DISTRO Put Distro Here (REPLACE Put Distro Here WITH ACTAL NAME OF YOUR DISTRO) And Add A Description Like TS-DISTRO Put Distro Here Is A Distro Based On TS-KERNEL 1.0.0 And Add Tags Like TS-KERNEL, TS-DISTRO, Put Distro Here (REPLACE Put Distro Here WITH ACTAL NAME OF YOUR DISTRO) And Click On Publish And Wait For It To Finish (If You Don't Want To Upload It To GitHub Just Delete The .exe File And The .py File Will Be Left) And You're Done! Enjoy Your New Distro! (REPLACE Put Distro Here WITH ACTAL NAME OF YOUR DISTRO) (And Don't Forget To Replace The Name Of Your Distro In The Code!) (AND DON'T REMOVE THEESE LINES)