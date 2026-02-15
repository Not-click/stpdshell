import os
import json
from functions import *

os.system('')

# The "Theme" Box
colors = {
    "green": "\033[92m",
    "blue":  "\033[94m",
    "red":   "\033[91m",
    "reset": "\033[0m"
}


path = os.path.expanduser('login.json')

try:
    with open(path, 'r') as file:
        data = json.load(file)
        username = data["username"]

except FileNotFoundError:
    print(f"{colors['red']}Folder not found{colors['reset']}")
    username = input("Enter your username: ")
    choice=input("Do you want to make a example config y/n defult=n: ")

    if choice == "y":
        with open ("login.json","w") as file:
            file.write(
                f"""
{{
  "username": "{username}",
  "config": {{
    "ShowCurrentDir": true
  }}
}}

                """
            )

    print("File created")
    exit()

#login json file

print("""
\033[92m Welcome to stpdshell \033[0m
""")
print(" ")

while True:
    try:
        if data['config']['ShowCurrentDir'] == True:
            cmd = input(f"{colors['blue']}{os.getcwd()} @{username}{colors['reset']}➜ ")
        else:
            cmd = input(f"{colors['blue']}@{username}{colors['reset']}➜ ") 
    except Exception:
        print("Please make a login.json file")

        choice=input("Do you want to make a example config y/n defult=n: ")

        if choice == "y":
            with open ("login.json","w") as file:
                file.write(
                    """
{
  "username": "Not_Click",
  "config": {
    "ShowCurrentDir": true
  }
}

                """
                )
        cmd=input("")
    try:
        exec(cmd)
    except Exception as e:
        print(e)


#The actual execution loop

