#imports
from __future__ import division
import os
import socket
import getpass
from uuid import getnode as get_mac
import string
import random
from random import choice
import time
from random import randint
import socket
import platform
import subprocess
import re
import uuid
import fnmatch
import csv
import math
import signal
import sys
import itertools

print("="*40, "PyPrompt", "="*40)

joalricha = '''
    J    OOO    AAA   L    RRRR   I   CCC  H  H   AAA
    J   O   O  A   A  L    R   R  I  C     HHHH  A   A
    J   O   O  AAAAA  L    RRRR   I  C     H  H  AAAAA
  JJJ    OOO   A   A  LLL  R   R  I   CCC  H  H  A   A
'''

print('Expanded by:' + joalricha + 'it says joalricha https://github.com/joalricha869')
print('Thanks to https://github.com/BigBoyTaco for help')
print(" ")
print('The source is here')
print("Type in 'help' for the command list.")
print("")

#setup
#gets hostname
hostname = socket.gethostname()
#gets mac address
mac = get_mac()
#gets current directory
current_dir = os.getcwd()

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

commands = '''1. dir (Shows files in current directory)
2. exit (Exits the terminal)
3. ip (Gives you your IP)
4. hostname (Gives you your Computer's ID)
5. mac (Retrieves the Physical MAC Address of The Device)
6. ping (lets you ping a website)
7. calc (A simple calculator)
8. passgen (A very efficient password generator)
9. sysinfo (Gets relevant system info)
10. test (Tests Termithron Sample Command)
11. mp3search (Searches your File System for mp3 files)
12. mp4search (Searches your File System for mp4 files)
14. pysearch (Searches your File System for py files)
15. docxsearch (Searches your File System for docx files)
16. mailgen (Generates dummy E-Mail Addresses)
17. ver (Reports Software Version)
'''

#what command was requested
def whatiscommand():
    #help command
    if cmd == 'help':
        print(commands)
        main()
    #ls command
    elif cmd == 'dir':
        print(os.listdir(current_dir))
        main()
    #exit command
    elif cmd == 'exit':
        exit()
    #ip command
    elif cmd == 'ip':
        print("Your IP Address is " + getip())
        main()
    #hostname command
    elif cmd == 'hostname':
        uname = platform.uname()
        print(hostname)
        main()
    #get mac adress
    elif cmd == "mac":
        getmac()
        main()
    #calculator
    elif cmd == "calc":
        calc()
    #password genorator
    elif cmd == "passgen":
        passGen()
    #system information
    elif cmd == "sysinfo":
        getSystemInfo()
        main()
    #version
    elif cmd == "ver":
        ver()
        main()
    #test
    elif cmd == "test":
        testFunc()
        main()
    #mp3 file searh
    elif cmd == "mp3search":
        mp3search()
        main()
    #mp4 file search
    elif cmd == "mp4search":
        mp3search()
        main()
    #python file search
    elif cmd == "pysearch":
        pysearch()
        main()
    #word doc search
    elif cmd == "docxsearch":
        docxsearch()
        main()
    #email genorator
    elif cmd == "mailgen":
        mailGen()
        main()
    #else
    else:
        error()

#define functions
def main():
    global cmd
    cmd = input(current_dir + '>')
    whatiscommand()
#version function
def ver():
    print("PyPrompt BETA 1 Codename: PyTermi")
    print("(C) 2022 joalricha869, All Rights Reserved.")
#system information function
def getSystemInfo():
    print("="*40, "System Information", "="*40)
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")
    print("System Info Retrieved!")
#calculator function
def calc():
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        while True:
            choice = input("Enter choice(1/2/3/4): ")
            if choice in ('1', '2', '3', '4'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == '1':
                    print(num1, "+", num2, "=", add(num1, num2))
                elif choice == '2':
                    print(num1, "-", num2, "=", subtract(num1, num2))
                elif choice == '3':
                    print(num1, "*", num2, "=", multiply(num1, num2))
                elif choice == '4':
                    print(num1, "/", num2, "=", divide(num1, num2))
                next_calculation = input("Let's do next calculation? (yes/no): ")
                if next_calculation == "no":
                  main()
            else:
                print("Invalid Input")
                main()
#password genorator function
def passGen():
        characters = string.ascii_letters + string.punctuation  + string.digits
        password =  "".join(choice(characters) for x in range(randint(8, 16)))
        print("Is your Generated Password: ",password)
        repeatGen = input("Generate another one? ")
        if repeatGen == "yes":
            passGen()
        else:
            main()
#mac address function
def getmac():
    import re, uuid
    print ("The MAC address of this Device is : ", end="")
    print (':'.join(re.findall('..', '%012x' % uuid.getnode())))
#get ip function
def getip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:       
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP

#error function
def error():
    if(cmd == ""):
        main()
    else:
        print("'" + str(cmd) + "'" + ''' is not recognized as an internal or external command''')
        print("for more help go https://github.com/joalricha869/Termithon-3.0 or https://github.com/IdkDwij/Termithon")
        main()
#test function
def testFunc():
    print("If this command works, then your Termithron is fine... maybe")
#mp3 search function
def mp3search():
    rootPath = '/'
    pattern = '*.mp3'
    
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            print( os.path.join(root, filename))
#mp4 search function
def mp4search():
    rootPath = '/'
    pattern = '*.mp4'
    
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            print( os.path.join(root, filename))
#py search function
def pysearch():
    rootPath = '/'
    pattern = '*.py'
    
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            print( os.path.join(root, filename))
#word doc search
def docxsearch():
    rootPath = '/'
    pattern = '*.docx'
    
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            print( os.path.join(root, filename))
#email genorator
def mailGen():
    extensions = ['com']
    domains = ['gmail','yahoo','comcast','verizon','charter','hotmail','outlook','frontier','icloud','yandex']
    characters = string.ascii_letters + string.digits
    winext = extensions[random.randint(0,len(extensions)-1)]
    windom = domains[random.randint(0,len(domains)-1)]
    acclen = random.randint(1,20)
    winacc = ''.join(choice(characters) for _ in range(acclen))
    finale = winacc + "@" + windom + "." + winext
    print("Your Generated E-Mail Address is: ",finale)
    again = input("Generate another address? ")
    if again == "yes":
        mailGen()
    else:
        main()

main()
