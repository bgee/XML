from git import *
import urllib2
import filecmp
import os, time
from progressbar import *


def sleep_bar(second):
    millsecond = 100*second
    print "wait for %d seconds" % second
    pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=millsecond).start()
    for i in range(millsecond):
        time.sleep(0.01)
        pbar.update(i+1)
    pbar.finish()


def main():
    
    
    
    try:
        while True:
            u = urllib2.urlopen('http://www.ncaa.com/newsrss/')
            
            localFile = open(fname+postfix, 'w')
            
            localFile.write(u.read())
            
            localFile.close()
            
            '''if not filecmp.cmp('ncaa.xml', 'ncaa_New.xml'):
                print "diff file, rename..."
                os.rename('ncaa_New.xml', 'ncaa.xml')
                print "finish'''
            if repo.is_dirty():
                print "updating new file to git repo"
       
                index.add([diff.a_blob.name for diff in index.diff(None)])
                commit = index.commit("another commit")
                origin = repo.remotes.origin
                origin.push()
                
                sleep_bar(10)
                    
            else:
                sleep_bar(5)
            
                    
    except KeyboardInterrupt:
        print "finish uploading"


if __name__ == "__main__":
    fname = 'ncaa'
    postfix = '.xml'
    dir = os.path.dirname(os.path.abspath(__file__))
    repo = Repo(dir)
    index = repo.index
    main()
