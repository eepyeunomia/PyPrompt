#!/usr/bin/python3 
#
# PyPrompt - An alternative cross-platform terminal shell made in Python!
# PyPrompt made by
#    _             _      _      _            ___    __ ___  
#   (_)           | |    (_)    | |          / _ \  / // _ \ 
#    _  ___   __ _| |_ __ _  ___| |__   __ _| (_) |/ /| (_) |
#   | |/ _ \ / _` | | '__| |/ __| '_ \ / _` |> _ <| '_ \__, |
#   | | (_) | (_| | | |  | | (__| | | | (_| | (_) | (_) |/ / 
#   | |\___/ \__,_|_|_|  |_|\___|_| |_|\__,_|\___/ \___//_/  
#  _/ |                                                      
# |__/  
#
# Based on Termithon by idkDwij
# Testing a new engine! Yay! Finally no more dependence on Termithon (i hope lol)
# Some commands were not made by me, check CREDITS for info about devs
# btw do not trust anyone named theopensour or thesouropen or theclosedbitter
# 
# Billions of imports ahead!
#
#          .?77777777777777$.            
#          777..777777777777$+           
#         .77    7777777777$$$           
#         .777 .7777777777$$$$           
#         .7777777777777$$$$$$           
#         ..........:77$$$$$$$           
#  .77777777777777777$$$$$$$$$.=======.  
# 777777777777777777$$$$$$$$$$.========  
# 7777777777777777$$$$$$$$$$$$$.=========
# 77777777777777$$$$$$$$$$$$$$$.=========
# 777777777777$$$$$$$$$$$$$$$$ :========+.
# 77777777777$$$$$$$$$$$$$$+..=========++~
# 777777777$$..~=====================+++++
# 77777777$~.~~~~=~=================+++++.
# 777777$$$.~~~===================+++++++.
# 77777$$$$.~~==================++++++++:
# 7$$$$$$$.==================++++++++++. 
# .,$$$$$$.================++++++++++~.  
#         .=========~.........           
#         .=============++++++           
#         .===========+++..+++           
#         .==========+++.  .++           
#          ,=======++++++,,++,           
#          ..=====+++++++++=.            
#                ..~+=...  
#
from __future__ import division
from __future__ import print_function
import platform

global uname
uname = platform.uname()

import os
import string
import random
from random import choice
from random import randint
import socket
import fnmatch
import time
import uuid
import py_compile
import getpass
import speedtest
import geocoder
import wget
import pyvim
# 69 lines nice lol
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import sys
import openai
import pathlib
import warnings

if uname.system == "Windows":
    from ctypes import *
else:
  pass
from blessed import *
from blessed import Terminal

try:
    pass
except Warning:
    pass

try:
    pass
except Exception:
    pass

term = Terminal()

warnings.simplefilter("ignore")
warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore", category=FutureWarning)

# Fixes 'distutils' error in PyInstaller
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
    warnings.filterwarnings("ignore")
    warnings.filterwarnings("ignore", category=FutureWarning)

# Checks if Python version is more than 3.9 (Will only take effect on uncompiled build)
if sys.version_info < (3, 9):
    sys.stderr.write('You need Python 3.9 or later\n')
    sys.exit(1)

# Aw man no more neofetch screen :(
hostname = socket.gethostname()
curr_user = getpass.getuser()
global echo_on


# Ten Billion Imports Later...

global pypromptascii
pypromptascii = '''
    _____       _____                           _   
   |  __ \     |  __ \                         | |  
   | |__) |   _| |__) | __ ___  _ __ ___  _ __ | |_ 
   |  ___/ | | |  ___/ '__/ _ \| '_ ` _ \| '_ \| __|
   | |   | |_| | |   | | | (_) | | | | | | |_) | |_ 
   |_|    \__, |_|   |_|  \___/|_| |_| |_| .__/ \__|
           __/ |                         | |        
          |___/                          |_|        '''
centerASCII = pypromptascii.center(50)
print(term.green + centerASCII + term.normal)
def warnings():
    warningASCII = '''
._________________________________________________________________________________.
|                                                                                 |
|     db   d8b   db  .d8b.  d8888b. d8b   db d888888b d8b   db  d888b       db    |
|     88   I8I   88 d8' `8b 88  `8D 888o  88   `88'   888o  88 88' Y8b      88    |
|     88   I8I   88 88ooo88 88oobY' 88V8o 88    88    88V8o 88 88           YP    |
|     Y8   I8I   88 88~~~88 88`8b   88 V8o88    88    88 V8o88 88  ooo            |
|     `8b d8'8b d8' 88   88 88 `88. 88  V888   .88.   88  V888 88. ~8~      db    |
|      `8b8' `8d8'  YP   YP 88   YD VP   V8P Y888888P VP   V8P  Y888P       YP    |'''
    print(term.bold_red(warningASCII))
    print(term.bold_red("|                                                                                 |"))
    print(term.bold_red("|                                                                                 |"))
    print(term.bold_red("|                      THIS IS A BETA BUILD OF PYPROMPT                           |"))
    print(term.bold_red("|            NOTE THAT MOST COMMANDS MIGHT NOT WORK OR BE UNSTABLE                |"))
    print(term.bold_red("|             IT IS RECOMMENDED TO INSTALL PYTHON FOR BETA BUILDS                 |"))
    print(term.bold_red("|                                                                                 |"))
    print(term.bold_red("|_________________________________________________________________________________|"))
# if not beta build disable 'warnings()'
warnings()
print(" ")
hostnamecomputer = socket.gethostname()
global current_dir
current_dir = os.getcwd()

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

commands = '''
DIR                     (Integrated dir/ls command. To use vanilla dir on Windows, Enter CMD Mode and type dir.)
IP                      (Gives you your IP)
HOSTNAME                (Gives you your Computer's ID)
MAC                     (Retrieves the Physical MAC Address of The Device)
PING                    (lets you ping a website)
CALC                    (A simple CLI calculator)
PASSGEN                 (A very efficient password generator)
SYSINFO                 (Gets relevant system info)
TEST                    (Tests PyPrompt Sample Command)
MAILGEN                 (Generates dummy E-Mail Addresses)
VER                     (Reports PyPrompt Version)
CLEAR                   (Clears screen)
INTRO                   (Displays initial text)
SQRT                    (Enter a number and it will calculate the square root)
DATE                    (Displays date)
CD                      (Navigate through folders) (NOTE: Applicable on PyPrompt Mode ONLY!. If you use CMD/BASH directories will change)
IPLOCATION              (Find the physical location of your IP address)
SPEEDTEST               (Speedtest.net but built into PyPrompt!)
FILESEARCH              (Searches files via their file name)
FILEDOWNLOADER          (Download any file via their url)
IDK                     (i'm not sure what this is. it just exists.)
LOCATOR                 (Locate basically any location in the planet)
DEVHELP                 (Detailed info about PyPrompt useful for troubleshooting)
COMPILER                (Compile any standard Python file to a *.pyc format)
PYVIM                   (Vim clone 'MADE BY jonathanslenders On GitHub') WILL REQUIRE PYTHON!!
PYINSTALLER             (Another Python compiler) REQUIRES PYTHON AND PYINSTALLER TO BE INSTALLED!
EZFORMAT                (Simplified disk formatter) ONLY WORKS ON WINDOWS
EZTASKKILL              (Eliminate some process without using the task mamager) ONLY WORKS ON WINDOWS
WEATHER                 (Gets the weather from any city) Made by imkaka. Github: https://github.com/imkaka
MAGIC8BALL              (A virtual Magic-8-Ball made in Python)
CREDITS                 (Credits for all commands & dev list)
BSOD                    (Cause a BSOD) Windows Only
WIFIPASS                (Get the password from your WiFi) Windows Only
LOCALHOSTER             (Create a localhost webserver via the terminal)
CHATGPT                 (ChatGPT in a Terminal) Requires OpenAI
WORDLE                  (Wordle in a CLI App)

'''

linuxcommands='''
DIR                     (Integrated dir/ls command. To use vanilla dir on Windows, Enter CMD Mode and type dir.)
IP                      (Gives you your IP)
HOSTNAME                (Gives you your Computer's ID)
MAC                     (Retrieves the Physical MAC Address of The Device)
PING                    (lets you ping a website)
CALC                    (A simple CLI calculator)
PASSGEN                 (A very efficient password generator)
SYSINFO                 (Gets relevant system info)
TEST                    (Tests PyPrompt Sample Command)
MAILGEN                 (Generates dummy E-Mail Addresses)
VER                     (Reports PyPrompt Version)
CLEAR                   (Clears screen)
INTRO                   (Displays initial text)
SQRT                    (Enter a number and it will calculate the square root)
DATE                    (Displays date)
CD                      (Navigate through folders) (NOTE: Applicable on PyPrompt Mode ONLY!. If you use CMD/BASH directories will change)
IPLOCATION              (Find the physical location of your IP address)
SPEEDTEST               (Speedtest.net but built into PyPrompt!)
FILESEARCH              (Searches files via their file name)
FILEDOWNLOADER          (Download any file via their url)
IDK                     (i'm not sure what this is. it just exists.)
LOCATOR                 (Locate basically any location in the planet)
DEVHELP                 (Detailed info about PyPrompt useful for troubleshooting)
COMPILER                (Compile any standard Python file to a *.pyc format)
PYVIM                   (Vim clone 'MADE BY jonathanslenders On GitHub') WILL REQUIRE PYTHON!!
PYINSTALLER             (Another Python compiler) REQUIRES PYTHON AND PYINSTALLER TO BE INSTALLED!
WEATHER                 (Gets the weather from any city) Made by imkaka. Github: https://github.com/imkaka
MAGIC8BALL              (A virtual Magic-8-Ball made in Python)
CREDITS                 (Credits for all commands & dev list)
LOCALHOSTER             (Create a localhost webserver via the terminal) (REAQUIRES A FILE NAMED test.html to runs)
CHATGPT                 (ChatGPT in a Terminal)
BTCMAN                  (Bitcoin Manager)
WORDLE                  (Wordle in a CLI App)

'''

def whatiscommand(current_dir):
    args = cmd.split()
    if cmd == 'help':
        global uname
        uname = platform.uname()
        if uname.system == "Windows":
            print(commands)
        else:
            print(linuxcommands)
        main(current_dir)
    elif cmd == 'dir':
        print(os.listdir(current_dir))
        main(current_dir)
    elif cmd == 'exit':
        sys.exit(1)
    elif cmd == 'ip':
        print("Your IP Address is " + getip())
        main(current_dir)
    elif cmd == 'hostname':
        uname = platform.uname()
        print(hostnamecomputer)
        main(current_dir)
    elif cmd == "mac":
        getmac()
        main(current_dir)
    elif "calc" in cmd:
        calc()
        main(current_dir)
    elif cmd == "passgen":
        passGen()
    elif cmd == "sysinfo":
        getSystemInfo()
        main(current_dir)
    elif cmd == "ver":
        ver()
        main(current_dir)
    elif cmd == "test":
        testFunc()
        main(current_dir)
    elif cmd == "mailgen":
        mailGen()
        main(current_dir)
    elif cmd == "clear":
        clear()
    elif "loadbartest" in cmd:
        progressbar()
        main(current_dir)
    elif "intro" in cmd:
        intro()
        main(current_dir)
    elif "sqrt" in cmd:
        sqrt()
        main(current_dir)
    elif "date" in cmd:
        date()
        main(current_dir)
    elif "ignore" in cmd:
        easterEgg()
        main(current_dir)
    elif cmd == "speedtest":
        speedtestapp()
        main(current_dir)
    elif cmd == "iplocation":
        iplocation()
        main(current_dir)
    elif cmd == "idk":
        print("The command is 'ignore'")
        main(current_dir)
    elif "cd" in cmd:
        args.remove('cd')
        args = ' '.join(args)
        if cmd == "cd":
            main(current_dir)
        old_dir = current_dir
        if os.path.isdir(args) == True:
            current_dir = args
            main(args)
        elif os.path.isdir(old_dir + '\\' + args):
            new_dir = old_dir + '\\' + args
            current_dir = new_dir
            main(new_dir)
        else:
            print('The system cannot find the path specified. \n')
            main(current_dir)
    elif cmd == "filesearch":
        fileSearch()
        main(current_dir)
    elif cmd == "filedownloader":
        fileDownloader()
        main(current_dir)
    elif "locator" in cmd:
        locator()
        main(current_dir)
    elif cmd == "devhelp":
        devHelp()
        main(current_dir)
    elif cmd == "compiler":
        pyCompiler()
        main(current_dir)
    elif cmd == "wifipass":
        heckWifi()
        main(current_dir)
    elif cmd == "ezformat":
        ezformatter()
        main(current_dir)
    elif cmd == "eztaskkill":
        eztaskkill()
        main(current_dir)
    elif cmd == "credits":
        credits()
        main(current_dir)
    elif cmd == "weather":
        GetCurrentWeather()
        main(current_dir)
    elif cmd == "magic8ball":
        magic8Ball()
    elif cmd == "bsod":
        var1 = platform.uname()
        if var1.system == "Windows":
            bsod()
        else:
            print("BSOD is only supported on Windows")
            main(current_dir)
    elif cmd == "shutdown":
        shutdown()
        main(current_dir)
    elif cmd == "welcome":
        welcome()
        main(current_dir)
    elif cmd == "localhoster":
        localhoster()
        main(current_dir)
    elif cmd == "chatgpt":
        chatGPT()
        main(current_dir)
    elif cmd == "wordle":
        wordle()
        main(current_dir)
    elif str(cmd) in cmd:
        print("This MUST be a shell command in the OS else your command won't work!")
        os.system(cmd)
        main(current_dir)
    else:
        error()

def main(current_dir):
    global main
    global old_dir
    old_dir = current_dir
    global cmd
    cmd = input(current_dir + '>')
    whatiscommand(current_dir)

global osver
osver = platform.platform()

global architecture
architecture = platform.architecture()

def getSystemInfo():
    print("=" * 40, "System Information", "=" * 40)
    print(f"System Base: {uname.system}")
    print(f"Operating System Version: {osver}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")
    print(f"Processor Architecture: {architecture}")
    print("System Info Retrieved!")


# Calculator by BigBoyTaco
def calc():
    if "+" in cmd:
        numbers = cmd.split()
        first_number = float(numbers[1])
        second_number = float(numbers[3])
        print(first_number + second_number)
        # LMAO 420 lines
    elif "-" in cmd:
        numbers = cmd.split()
        first_number = float(numbers[1])
        second_number = float(numbers[3])
        print(first_number - second_number)
    elif "/" in cmd:
        numbers = cmd.split()
        first_number = float(numbers[1])
        second_number = float(numbers[3])
        print(first_number / second_number)
    elif "*" in cmd:
        numbers = cmd.split()
        first_number = int(numbers[1])
        second_number = int(numbers[3])
        print(first_number * second_number)
    elif cmd == "calc help":
        print("Proper use of calculator: calc 1 + 2")
        print("Only two numbers are allowed")
        print('''Calculator supports:
        1. Addition
        2. Subtraction
        3. Division
        4. Multiplication''')
    else:
        print('Error... use "calc help" for more help')


def passGen():
    characters = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(characters) for x in range(randint(8, 16)))
    print("Is your Generated Password: ", password)
    repeatGen = input("Generate another one? ")
    if repeatGen == "yes":
        # 420 lines lol
        passGen()
    else:
        main(current_dir)


def getmac():
    print("The MAC address of this Device is : ", end="")
    print(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                    for ele in range(0, 8 * 6, 8)][::-1]))


def getip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = "Either your connection is VERY limited or you don't have internet so your ip is just the default: 127.0.0.1"
    finally:
        st.close()
    return IP


def clear():
    os.system('cls||clear')
    main(current_dir)

def error():

    if (cmd == ""):
        main(current_dir)
    else:
        
        print("'" + str(cmd) + "'" + ''' is not recognized as an internal or external command''')
        print("For more help go to: https://github.com/joalricha869/PyPrompt or https://github.com/IdkDwij/Termithon")
        main(current_dir)


def testFunc():
    print("Testing Geocoder: " + geocoder.__version__)
    print("Testing Speedtest: " + speedtest.__version__)
    print("Testing Wget: " + wget.__version__)
    print("Testing Getpass: " + getpass.__doc__)


def mailGen():
    extensions = ['com']
    domains = ['gmail', 'yahoo', 'comcast', 'verizon', 'charter', 'hotmail', 'outlook', 'frontier', 'icloud', 'yandex']
    characters = string.ascii_letters + string.digits
    winext = extensions[random.randint(0, len(extensions) - 1)]
    windom = domains[random.randint(0, len(domains) - 1)]
    acclen = random.randint(1, 20)
    winacc = ''.join(choice(characters) for _ in range(acclen))
    finale = winacc + "@" + windom + "." + winext
    progressbar()
    print("Your Generated E-Mail Address is: ", finale)
    again = input("Generate another address? ")
    if again == "yes":
        progressbar()
        mailGen()
    else:
        main(current_dir)


def progressbar():
    def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
        percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '▒' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
        if iteration == total:
            print()

    items = list(range(0, 50))
    l = len(items)

    loadbar(0, l, prefix='Generating...', suffix='Done!', length=l)
    for i, item in enumerate(items):
        time.sleep(0.1)
        loadbar(i + 1, l, prefix='Generating...', suffix='Done!', length=l)


def intro():
    print(term.green + centerASCII + term.normal)
    print(" ")
    warnings()
    print(" ")


def sqrt():
    num = float(input('Enter a number: '))
    num_sqrt = num ** 0.5
    print('The square root of %0.3f is %0.3f' % (num, num_sqrt))


def date():
    from datetime import date
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    print("Today's date is:", d2)
    main(current_dir)


def easterEgg():
    print("PyPrompt Made by joalricha869")
    print("Termithon Kernel by idkDwij")
    print("calc Fix by BigBoyTaco")


def speedtestapp():
    speed = speedtest.Speedtest()
    option = int(input('''
    What do you want to know:
    1) Download speed
    2) Upload speed
    3) Both Download and Upload
    4) Ping
    Your choice: '''))

    if option < 1 or option > 4:
        time.sleep(2)
        print('Option Non-Existent')
    else:
        time.sleep(1)
        print()
        print('Testing your Internet Download Speeds')
        print()
        down_speed = round(speed.download() / 1000000, 3)
        up_speed = round(speed.upload() / 1000000, 3)
        print('One more sec please...')
        time.sleep(1.5)
        print()
        if option == 1:
            print('Your Download speed is: ', down_speed, 'Mbps')
        elif option == 2:
            print('Your Upload speed is: ', up_speed, 'Mbps')
        elif option == 3:
            print('Your Download speed is: ', down_speed, 'Mbps', end=" ")
            print(',and your Upload speed is: ', up_speed, 'Mbps')

        elif option == 4:
            s = []
            speed.get_servers(s)
            print(speed.results.ping, 'ms')
        else:
            print("Test Failed: Couldn't connect to Speedtest")


def iplocation():
    g = geocoder.ipinfo('me')
    print(g.latlng)


def fileSearch():
    rootPath = '/'
    print("Note that the file extension format must be '*.extension' without the apostrophe obv")
    print("Depending on the speed of your HDD/SSD this may take a while (depending on the extension asw)")
    pattern = input("Specify File Name: ")
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            print(os.path.join(root, filename))


def fileDownloader():
    wget.download = input("Enter URL for file download: ")
    main(current_dir)


def locator():
    t = input("Enter the location: ")
    g = geocoder.arcgis(t)
    print(g.latlng)


def devHelp():
    print("----------PyPrompt System Details----------\n")
    print("PYPROMPT VERSION: " + y)
    print("TERMITHON KERNEL VERSION: 0.1.4 (MODIFIED)")
    print("CODENAME: ARCH")
    print(f"OPERATING SYSTEM: {uname.system}")
    print(f"OS VERSION: {osver}")


def pyCompiler():
    fileinput = input("Enter name of file you want to compile into .pyc format: ")
    py_compile.compile(fileinput)


def testModules():
    print(pyvim.__version__)


def ezformatter():
    print("Easy Formatter\n")
    print("This tool simplifies the format command in Windows")
    print("Please be aware that you need to run PyPrompt as an administrator")
    print("Drive letter formatting (G:)")
    volume = input("Please specify drive letter: ")
    print("Supported File Systems are NTFS, FAT, FAT32, exFAT, UDF, ReFS")
    filesystem = input("Please type the file system you want to format your drive with: ")
    volumename = input("Type the volume name of your drive: ")
    quickformatconfirm = input("Quick format your drive?: ")
    if quickformatconfirm == "yes":
        formattype = "/Q"
    else:
        formattype = ""
    os.system("format " + volume + "/FS:" + filesystem + "/V:" + volumename + formattype)


def eztaskkill():
    print("Kill an Annoying Process")
    print(" ")
    print("Have some process that you need to eliminate but you either can't use the Task Manager")
    processName = input("What is the name of the process you want to kill? IE: msedge.exe: ")
    os.system("taskkill /f /im " + processName)
    print("Done!")
    taskAgain = input("Kill another process: ")
    if taskAgain == "yes":
        eztaskkill()
    else:
        main(current_dir)

def GetCurrentWeather():
    def get_temperature(json_data):
        temp_in_farenheit = json_data['main']['temp']
        return temp_in_farenheit

    def get_weather_type(json_data):
        weather_type = json_data['weather'][0]['description']
        return weather_type

    def get_wind_speed(json_data):
        wind_speed = json_data['wind']['speed']
        return wind_speed



    def get_weather_data(json_data, city):
        description_of_weather = json_data['weather'][0]['description']
        weather_type = get_weather_type(json_data)
        temperature = get_temperature(json_data)
        wind_speed = get_wind_speed(json_data)
        weather_details = ''
        return weather_details + ("The weather in {} is currently {} with a temperature of {} degrees farenheit and wind speeds reaching {} km/ph".format(city, weather_type, temperature, wind_speed))


    def weather():
        print("Gather the Weather!")
        print(" ")
        print("NOTE: The inputs are CASE-SENSITIVE!!!")
        print("Any wrong misspell and PyPrompt will crash")
        city = input("Please Input City Name: ")
        countrycode = input("Please Input Country Code (ie. us, mx): ")
        api_address = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + ',' + countrycode + '&appid=a10fd8a212e47edf8d946f26fb4cdef8&q='
        units_format = "&units=imperial"
        final_url = api_address + city + units_format
        json_data = requests.get(final_url).json()
        weather_details = get_weather_data(json_data, city)
        # print formatted data
        print(weather_details)



    weather()

def magic8Ball():
    title = '''

        __  __                        __                 ____         ___             __  __ 
    F  \/  ]     ___ _     ___ _   LJ    ____        F __ J       F _ ",   ___ _   LJ  LJ 
    J |\__/| L   F __` L   F __` L       F ___J.     J `--' L     J `-'(|  F __` L  FJ  FJ 
    | |`--'| |  | |--| |  | |--| |  FJ  | |---LJ     / ,--. \     | ,--.\ | |--| | J  LJ  L
    F L    J J  F L__J J  F L__J J J  L F L___--.    F L__J J     F L__J \F L__J J J  LJ  L
    J__L    J__LJ\____,__L )-____  LJ__LJ\______/F   J\______/L   J_______J\____,__LJ__LJ__L
    |__L    J__| J____,__FJ\______/F|__| J______F     J______F    |_______FJ____,__F|__||__|
                            J______F                                                         
    '''
    ball = '''
            ____
        ,dP9CGG88@b,
    ,IP  _   Y888@@b,
    dIi  (_)   G8888@b
    dCII  (_)   G8888@@b
    GCCIi     ,GG8888@@@
    GGCCCCCCCGGG88888@@@
    GGGGCCCGGGG88888@@@@...
    Y8GGGGGG8888888@@@@P.....
    Y88888888888@@@@@P......
    `Y8888888@@@@@@@P'......
        `@@@@@@@@@P'.......
            """"........
    '''


    def magicBall():
        responses = ["It is certain.", 
        "It is decidedly so.", 
        "Without a doubt.", 
        "Yes definitely.", 
        "You may rely on it.", 
        " As I see it, yes.", 
        "Most likely.", 
        "Outlook good.", 
        "Yes.", 
        "Signs point to yes.", 
        "Reply hazy, try again.", 
        "Ask again later.", 
        "Better not tell you now.", 
        "Cannot predict now.", 
        "Concentrate and ask again.", 
        "Don't count on it.", 
        "My reply is no.", 
        "My sources say no.", 
        "Outlook not so good.", 
        "Very doubtful."]
        
        question = input("What do you want to ask the Magic 8 Ball? ")
        if question == str(question):
            print(random.choice(responses))
            again = input("Run Again? ")
            if again == "yes":
                magicBall()
            else:
                main(current_dir)
        else:
            print(random.choice(responses))
            again2 = input("Run Again? ")
            if again2 == "yes":
                magicBall()
            else:
                main(current_dir)

    def M8B():
        print(title)
        print(ball)
        magicBall()


    M8B()

joalricha = '''
    _             _      _      _            ___    __ ___  
   (_)           | |    (_)    | |          / _ \  / // _ \ 
    _  ___   __ _| |_ __ _  ___| |__   __ _| (_) |/ /| (_) |
   | |/ _ \ / _` | | '__| |/ __| '_ \ / _` |> _ <| '_ \__, |
   | | (_) | (_| | | |  | | (__| | | | (_| | (_) | (_) |/ / 
   | |\___/ \__,_|_|_|  |_|\___|_| |_|\__,_|\___/ \___//_/  
  _/ |                                                      
 |__/                                                       

'''
taco = '''

  ____  _       ____           _______              
 |  _ \(_)     |  _ \         |__   __|             
 | |_) |_  __ _| |_) | ___  _   _| | __ _  ___ ___  
 |  _ <| |/ _` |  _ < / _ \| | | | |/ _` |/ __/ _ \ 
 | |_) | | (_| | |_) | (_) | |_| | | (_| | (_| (_) |
 |____/|_|\__, |____/ \___/ \__, |_|\__,_|\___\___/ 
           __/ |             __/ |                  
          |___/             |___/                   

'''
dwij = '''

  _     _ _    _____           _ _ 
 (_)   | | |  |  __ \         (_|_)
  _  __| | | _| |  | |_      ___ _ 
 | |/ _` | |/ / |  | \ \ /\ / / | |
 | | (_| |   <| |__| |\ V  V /| | |
 |_|\__,_|_|\_\_____/  \_/\_/ |_| |
                               _/ |
                              |__/ 

'''

def credits():
    pyCredits = '''
PYPROMPT v1.6 CREDITS:

Developer / Maker: joalricha869 | https://github.com/joalricha869
Termithon Kernel: idkDwij | https://github.com/idkDwij | https://github.com/idkDwij/Termithon
CLI Calculator FIX: BigBoyTaco | https://github.com/BigBoyTaco

Command Credits:

WEATHER                 Made by imkaka      | https://github.com/imkaka

Most Commands by hastagAB | https://github.com/hastagAB/Awesome-Python-Scripts

LICENSE: GPL 3.0 | https://www.gnu.org/licenses/gpl-3.0.en.html
    '''
    print(pyCredits)
    print(" ")
    print('Made by:' + joalricha + 'it says joalricha https://github.com/joalricha869')
    print(" ")
    print('Thanks to ' + taco + 'for help  https://github.com/BigBoyTaco')
    print(" ")
    print('Based on Termithon by' + dwij + 'https://github.com/IdkDwij/Termithon')
    print(" ")
    print("The source is at my GitHub page! 'https://github.com/joalricha869/PyPrompt'")
    print("Type in 'help' for the command list.")
    print("SOME COMMANDS ARE MADE BY OTHER PEOPLE!")
    print("READ CREDITS ABOVE FOR MORE INFO")


def bsod():
    nullptr = POINTER(c_int)()
    
    windll.ntdll.RtlAdjustPrivilege(
        c_uint(19), 
        c_uint(1), 
        c_uint(0), 
        byref(c_int())
    )
    
    windll.ntdll.NtRaiseHardError(
        c_ulong(0xC000007B), 
        c_ulong(0), 
        nullptr, 
        nullptr, 
        c_uint(6), 
        byref(c_uint())
    )

def shutdown():
    print("Shutdown / Reboot your PC")
    print("(S)hutdown")
    print("(R)eboot")
    why = input("Select an Option: ")
    if why == "S":
        osDetector = platform.uname()
        if osDetector.system == "Windows":
            os.system("shutdown /s /t 0")
        else:
            os.system("sudo shutdown now -h")
            # Temporary Code
    elif why == "R":
          osDetector = platform.uname()
          if osDetector.system == "Windows":
              os.system("shutdown /r /t 1")
          else:
              os.system("sudo reboot")
    elif why == "s":
            osDetector = platform.uname()
            if osDetector.system == "Windows":
                os.system("shutdown /s /t 0")
            else:
                os.system("sudo shutdown now -h")
    elif why == "r":
          osDetector = platform.uname()
          if osDetector.system == "Windows":
              os.system("shutdown /r /t 1")
          else:
              os.system("sudo reboot")
    else:
        print("ERROR CODE: NONEXISTENT_OPTION")
        print("Booting back to PyPrompt Console")
        main(current_dir)

def welcome():
    print("Just confused on what to do?")
    input("Press Enter to Continue...")
    print("Well then, let me show you around!")
    input("To Begin, Press Enter...")
    os.system('cls||clear')
    print("Introduction")
    print(" ")
    print("To use PyPrompt, just type in a command.")
    print("The list of commands is available in the 'help' command")
    input("Press Enter to Continue...")
    os.system('cls||clear')
    print("That's it.")
    print("For real, what do you expect out of a CLI app.")
    print("Oh well i have better things to do XD")
    print("Im outta here!")
    input("Press Enter to Use PyPrompt...")
    os.system('cls||clear')
    print('Exiting "Tutorial" in 3')
    time.sleep(1)
    os.system('cls||clear')
    print('Exiting "Tutorial" in 2')
    time.sleep(1)
    os.system('cls||clear')
    print('Exiting "Tutorial" in 1')
    time.sleep(1)
    os.system('cls||clear')
    main(current_dir)

def heckWifi():
    print("View Wifi Password (Windows Only)")
    print(" ")
    print("NOTE: This only works on networks you have connected to or are currently connected to.")
    print("DISCLAIMER: Please do NOT use this tool to get another network's password.")
    SSID = input("Enter the SSID of the network: ")
    os.system('netsh wlan show profile name=' + SSID + ' key=clear | find "Key Content"')
    time.sleep(5)
    main(current_dir)

def localhoster():
    class Serv(BaseHTTPRequestHandler):

        def do_GET(self):
            if self.path == '/':
                self.path = '/test.html'
            try:
                file_to_open = open(self.path[1:]).read()
                self.send_response(200)
            except:
                file_to_open = "File not found"
                self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))

    httpd = HTTPServer(('localhost',8080),Serv)
    httpd.serve_forever()

global chatgptascii
chatgptascii = '''
   _____ _           _    _____ _____ _______ 
  / ____| |         | |  / ____|  __ \__   __|
 | |    | |__   __ _| |_| |  __| |__) | | |   
 | |    | '_ \ / _` | __| | |_ |  ___/  | |   
 | |____| | | | (_| | |_| |__| | |      | |   
  \_____|_| |_|\__,_|\__|\_____|_|      |_|   
                                              
'''


def chatGPT():
    apiKey = input("Type in your OpenAI API Key")
    openai.api_key = apiKey
    openaiKey = openai.api_key
    if uname.system == "Linux":
        os.system("export OPENAI_API_KEY='" + openaiKey + "'")
    else:
        pass

        print(chatgptascii)
        print("Hello, i'm ChatGPT.")
        print("Currently supports GPT-3.5 Turbo & GPT4")
        print("Options: 'gpt3' | 'gpt4'")
        global model
        model = input("Which model will you use? ")
        # - 1000 LINES
        if model == "gpt3":
            model = "gpt-3.5-turbo"
        elif model == "gpt4":
            model = "gpt-4"

    def request():
        chat = input("Ask me anything: ")
        global completion

        completion = openai.ChatCompletion.create(model=model, messages=[{"role": "user", "content": chat}])
        print(completion.choices[0].message.content)
        global gptcontinue
        gptcontinue = input("Need anything else? ")
        continueFunc()
    def continueFunc():
        if gptcontinue == "yes":
            request()
        else:
            main(current_dir)

    request()

def wordle():
    WORDLIST = pathlib.Path("wordlist.txt")
    if os.path.isfile(WORDLIST):
        pass
    else:
        print("You require the wordlist to continue")
        print("Returning to Terminal")
        main(current_dir)
    words = [
        word.upper()
        for word in WORDLIST.read_text(encoding="utf-8").strip().split("\n")
]
    while True:
        secret_word = random.choice(words)
        attempts = 6
        guessed_letters = []

        print(term.bold("Welcome to Wordle!"))

        while attempts > 0:
            print(f"{term.bold}Attempts remaining: {attempts}")
            guess = input("Enter a 5-letter word: ").upper()

            if len(guess) != 5:
                print(term.yellow("Please enter a 5-letter word."))
                continue

            if guess in guessed_letters:
                print(term.yellow("You have already guessed this word."))
                continue

            guessed_letters.append(guess)
            correct_positions = sum([g == s for g, s in zip(guess, secret_word)])
            correct_letters = sum([g in secret_word for g in guess])

            colored_guess = ""
            for g, s in zip(guess, secret_word):
                if g == s:
                    colored_guess += term.green(g)
                elif g in secret_word:
                    colored_guess += term.yellow(g)
                else:
                    colored_guess += g

            print(f"{colored_guess}\n")
            attempts -= 1

            if correct_positions == 5:
                print(term.green(f"Congratulations! You guessed the word: {secret_word}"))
                break

        if attempts == 0:
            print(term.red(f"Game Over! The secret word was: {secret_word}"))

        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again != "Y":
            break



btcfix = '''
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" `
-Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
'''



# Changes from 1.7.beta1
# ____________________________________________________________________
# - QUICKFIX: Removed all mentions of BTCMAN

y = "1.7.1.beta1.quickfix1"

def ver():
    print("PyPrompt Version: " + y)
    print("(C) 2023 joalricha869, All Rights Reserved.")

main(current_dir)
