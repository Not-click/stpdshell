import os
import sys
import time

#All the commands
def add(a: float,b: float):
  return(a+b)

def sub(a: float,b: float):
  return(a-b)

def mul(a: float,b: float):
  return(a*b)

def div(a: float,b: float):
  return(a/b)

def int_div(a: float,b: float):
  return(a//b)

def exp(a: float,b: float):
  return(a**b)

def clear():
  if os.name == 'nt':
    os.system("cls")
  else:
    os.system("clear")

def stop(number):
  time.sleep(number)

def RngInt(min,max):
  return(random.randint(min,max))

def rng(min,max):
  return(random.randrange(min,max))
#ls clone LOL
def lf(list_hidden=False):
    for file in os.listdir():
        if list_hidden == True:
            if file[0] == '.':
                print(f"{colors['blue']}{file}{colors['reset']}")
            else:
                print(file)
        else:
            if file[0] == '.':
                print("",end="")

            else:
                print(file)
def cf(path="~"):
    changed_folder=os.path.expanduser(path)
    os.chdir(changed_folder)

#End of command list

