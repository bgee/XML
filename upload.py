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

def update_repo():
    
    flag = repo.is_dirty()
    print flag
    if flag:
        print "updating new file to git repo"
        index.add([diff.a_blob.name for diff in index.diff(None)])
        commit = index.commit("another commit")
        origin.push()
    return flag

def main():
    
    
    
    try:
        while True:
            '''u = urllib2.urlopen('http://www.ncaa.com/newsrss/')
            localFile = open(fname+postfix, 'w')
            localFile.write(u.read())
            localFile.close()
                      
            if update_repo():
                sleep_bar(10)'''
            u = urllib2.urlopen('http://www.ncaa.com/newsrss/')
            
            localFile = open(fname+'_New'+postfix, 'w')
            
            localFile.write(u.read())
            
            localFile.close()
            
            if not filecmp.cmp('ncaa.xml', 'ncaa_New.xml'):
                print "diff file, rename..."
                update_repo()
                os.rename('ncaa_New.xml', 'ncaa.xml')
                
                print "finish"
                    
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
    origin = repo.remotes.origin
    # check current for any uncommited/unpushed file
    update_repo()
    main()
