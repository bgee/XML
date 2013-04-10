import git
import urllib2
import filecmp
import os
u = urllib2.urlopen('http://www.ncaa.com/newsrss/')

localFile = open('ncaa_New.xml', 'w')
#oldFile = open('ncaa.xml', 'r')
#print localFile==oldFile
#print filecmp.cmp(localFile, oldFile)
#if localFile != u.read():

localFile.write(u.read())
localFile.close()
if filecmp.cmp('ncaa.xml', 'ncaa_New.xml'):
    print "diff file, rename..."
    os.raname('ncaa_New.xml', 'ncaa.xml')
    print "finish"
#os.rename(localFile, 'ncaa.xml')
'''else:
    print "same file"
'''
