import os, sys
Modules = ["Checkers", "Tools"]

for root, dirs, files in os.walk("./Modules"):
    for filename in files:
        Modules.append(filename[:-3])

def runModule(ModuleCC):
    ModulePath = "./Menus/" + ModuleCC + ".py"
    os.system("python " + ModulePath)


def MainMenu():
    os.system("clear")
    print "Welcome to CheckTheDeck!"
    print "This tool is supplied by @OrkSec."
    print "What Menu would you like to enter?"
    for index, value in enumerate(Modules):
        print "[" + str(index) + "]" , value
    choice = input("==> ")
    if choice <= len(Modules):
        runModule(Modules[choice])
    else:
        MainMenu()

MainMenu()
