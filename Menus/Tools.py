import os, sys
Modules = []

for root, dirs, files in os.walk("./Menus/Tools"):
    for filename in files:
        Modules.append(filename[:-3])

def runModule(ModuleCC):
    ModulePath = "./Menus/Tools/" + ModuleCC + ".py"
    os.system("clear")
    os.system("python " + ModulePath)

def MainMenu():
    os.system("clear")
    print "Welcome to Tools menu!"
    for index, value in enumerate(Modules):
        print "[" + str(index) + "]" , value.replace("_", " ")
    choice = input("==> ")
    if choice <= len(Modules):
        runModule(Modules[choice])
    else:
        MainMenu()

MainMenu()
