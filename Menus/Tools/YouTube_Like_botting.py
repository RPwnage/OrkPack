import requests
import webbrowser
import os, sys
import time
import inspect
import json
from datetime import datetime



def log(value2print):
    print "["+datetime.now().strftime('%H:%M:%S').replace("''", "")+"] " + value2print

def loginWithBot(username, password):
    log("Logging in with",username+":"+password+"...")


def loadBots(botsfile):
    filename = (os.path.basename(botsfile)).replace(" ", "")
    print  "Trying to load Botfile called '" + filename + "'..."
    with open(botsfile.replace(" ", ""), 'r') as myfile:
         for line in myfile:
            print line
            line = line.replace('\n', '')
            email = line.split(":")[0]
            password = line.split(":")[1]

def askBotFile():
    print "Please drag and drop a email:password list, which contains only working GMAIL and YouTube accounts."
    accountsInput = raw_input("==> ")
    if accountsInput is not "":
        loadBots(accountsInput)
    else:
        exit()

askBotFile()
