#!/usr/bin/python
import subprocess

def run():
    print "Copying static files"
    # shutils pls no :(
    subprocess.Popen("cp -r ./templates/img ../")
    subprocess.Popen("cp -r ./templates/css ../")
    
if __name__ == "__main__":
    run()