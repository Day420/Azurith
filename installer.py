import requests, os, time

if not os.path.isfile("Azurith.py"):
    version = requests.get("https://azurith.day1337.repl.co/azurith/version.txt").text
    print(f" Installing latest version of Azurith... ({float(version)})")
    azurithfile = requests.get("https://azurith.day1337.repl.co/azurith.py").text
    azurith = open("Azurith.py", "w")
    azurith.write(str(azurithfile))
    azurith.close()
    print(" Azurith installed! Launching...")
    time.sleep(2)
    os.system("python3 Azurith.py")
else:
    print(" Azurith already installed, if you want to update, do it in Azurith.py!")

 
