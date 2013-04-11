from git import *
import urllib2
import filecmp
import os, time
from progressbar import *
fname = 'ncaa'
postfix = '.xml'
dir = os.path.dirname(os.path.abspath(__file__))
repo = Repo(dir)
index = repo.index

if repo.is_dirty():
    print "directory is dirty"
    repo.git.add('.')
    commit = index.commit("another commit")
    print repo.untracked_files
try:
    while True:
        u = urllib2.urlopen('http://www.ncaa.com/newsrss/')
    
        localFile = open(fname+'_New'+postfix, 'w')
        
        localFile.write(u.read())
        
        localFile.close()
        
        if not filecmp.cmp('ncaa.xml', 'ncaa_New.xml'):
            print "diff file, rename..."
            os.rename('ncaa_New.xml', 'ncaa.xml')
            print "finish"
            

        else:
            print "wait for 5 seconds"
            pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval = 500).start()
            for i in range(500):
                time.sleep(0.01)
                pbar.update(i+1)
            pbar.finish()
except KeyboardInterrupt:
    print "finish uploading"
