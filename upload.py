import git
import urllib2
import filecmp
import os, time
while True:
    u = urllib2.urlopen('http://www.ncaa.com/newsrss/')
    
    localFile = open('ncaa_New.xml', 'w')
    
    localFile.write(u.read())

    localFile.close()
    
    if not filecmp.cmp('ncaa.xml', 'ncaa_New.xml'):
        print "diff file, rename..."
        os.rename('ncaa_New.xml', 'ncaa.xml')
        print "finish"

    else:
        print "they are same"
        time.sleep(5)
