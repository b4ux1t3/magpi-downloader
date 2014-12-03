import os
import urllib2
import cookielib
from datetime import datetime

# Checking if log.txt exists, creating it if not
if os.path.isfile("log.txt"):
    logFile = open("log.txt", "a")
else:
    logFile = open("log.txt", "w")

# Main loop check    
run = True

# Issue number
check = 0

# Today's date
now = datetime.now()

date = "%s/%s/%s" % (now.month, now.day, now.year)
time = "%s:%s.%s" % (now.hour, now.minute, now.second)

# Where do we find the copies
src = "http://people.ds.cam.ac.uk/mcj33/themagpi/The-MagPi-issue-"
suf = "-en.pdf"

# Documentation is key
logFile.write(date + " " + time + ": Attempting to download MagPi Issues from " + src[:-16] + "\n")

# How many files we are downloading today.
downloaded = 0

while run:
    check += 1
    
    # Checking time every loop
    now = datetime.now()
    date = "%s/%s/%s" % (now.month, now.day, now.year)
    time = "%s:%s.%s" % (now.hour, now.minute, now.second)
    
    # Check if this issue exists
    if not os.path.isfile("magpi" + str(check) + ".pdf"):
            
        # Logging attempt
        logEntry = date + " " + time + ": Trying to download MagPi issue " + str(check) + "\n"
        logFile.write(logEntry)
        
        # Try to download the issue
        try:
            request = urllib2.Request(src + str(check) + suf)
            handle = urllib2.urlopen(request)
        except urllib2.HTTPError, e:
            logEntry = date + " " + time + ": 404, MagPi Issue " + str(check) + " does not exist (yet).\n"
            run = False
            logFile.write(logEntry)
            request = 0
        
        if request != 0:
            # Make a new issue if there was a request, then write handle to the file
            # I will fix this later
            #newIssue = open("magpi" + str(check) + ".pdf", "wb")
            #newIssue.write(handle)
            #neweIssue.close()
            
            # Download the PDF and write to the log
            os.system("wget -O magpi" + str(check) + ".pdf " + src + str(check) + suf)
            downloaded += 1
            logFile.write(date + " " + time + ": Downloaded The MagPi Issue " + str(check) + "\n")
            
    else:
        print "The MagPi Issue " + str(check) + " already exists"
        
now = datetime.now()
date = "%s/%s/%s" % (now.month, now.day, now.year)
time = "%s:%s.%s" % (now.hour, now.minute, now.second)

if downloaded == 0:
    logFile.write(date + " " + time + ": No new files today.\n")
else:
    logFile.write(date + " " + time + ": Downloaded " + str(downloaded) + " files today.\n")

logFile.close()
