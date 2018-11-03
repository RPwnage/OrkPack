import os, sys
Modules = []

for root, dirs, files in os.walk("./Menus/Modules"):
    for filename in files:
        Modules.append(filename[:-3])

def runModule(ModuleCC):
    ModulePath = "./Menus/Modules/" + ModuleCC + ".py"
    os.system("python " + ModulePath)

def MainMenu():
    os.system("clear")
    print "Welcome to Checker menu!"
    for index, value in enumerate(Modules):
        print "[" + str(index) + "]" , value
    choice = input("==> ")
    if choice <= len(Modules):
        runModule(Modules[choice])
    else:
        MainMenu()

MainMenu()
