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

# Made in python
# collaborated with https://github.com/BigBoyTaco/ for this little update
# Made in Python, with PyCharm and OnlineGDB
# Compiled on desktop in Visual Studio 2019
# Thanks for green1490#2863 for helping me with arguments
# Edited by joalricha869 to expand code

print("="*40, "Termithron 2.0", "="*40)
idkdwij = '''
    I   D       K   K   D       W         W     I       J
    I   D   D   K K     D  D    W    W    W     I   J   J
    I   D       K   K   D       W  W   W  W     I     J J
'''
joalricha = '''
    J    OOO    AAA   L    RRRR   I   CCC  H  H   AAA
    J   O   O  A   A  L    R   R  I  C     HHHH  A   A
    J   O   O  AAAAA  L    RRRR   I  C     H  H  AAAAA
  JJJ    OOO   A   A  LLL  R   R  I   CCC  H  H  A   A
'''
print('The Python based terminal by:' + idkdwij + 'it says idkdwij tho https://github.com/IdkDwij')
print(" ")
print('Expanded by:' + joalricha + 'it says joalricha https://github.com/joalricha869')
print('edited by https://github.com/BigBoyTaco')
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

commands = '''dir (Shows files in current directory)
1. exit (Exits Termithron)
2. ip (Gives you your IP)
3. hostname (Gives you your Computer's ID)
4. mac (Retrieves the Physical MAC Address of The Device)
5. ping (lets you ping a website)
6. calc (A simple calculator)
7. passgen (A very efficient password generator)
8. sysinfo (Gets relevant system info)
9. test (Tests Termithron Sample Command)
10. mp3search (Searches your File System for mp3 files)
11. mp4search (Searches your File System for mp4 files)
12. pysearch (Searches your File System for py files)
13. docxsearch (Searches your File System for docx files)
14. mailgen (Generates dummy E-Mail Addresses)
15. ver (Reports Termithron Version)
'''

#cd command (work in progress)
def cdCmd():
    print("sorry, the cd command doesnt update so no ")
    main()
    # Someone help on this code pls.
    '''
    path = input('Directory: ')
    if os.path.isdir(path) == True:
        current_dir = args
        global new_current_dir
        new_current_dir = args
        global newcurrdir
        newcurrdir = True
        main()
    else:
        print('wrong directory')
        main()
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
    #cd command
    elif cmd == "cd":
        global args
        args = cmd
        cdCmd()
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
    #ping
    elif "ping" in cmd:
        os.system(cmd)
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
    print("Termithron BETA 3.0 Codename: PyTermi3")
    print("(C) 2022 joalricha869, idkDwij All Rights Reserved.")
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
