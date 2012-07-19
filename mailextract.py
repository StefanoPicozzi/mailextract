#!/usr/bin/env python
# encoding: utf-8
'''
Created on Jul 17, 2012

@author: StefanoPicozzi
'''

import os
import sys
from optparse import OptionParser  

# ----------------------------------------------------------------------------

use = "Usage: %prog mailist1 [mailist2] ..."
parser = OptionParser(usage = use)
options, args = parser.parse_args()

if len( args ) < 1:
    parser.error( 'require at least one mailing list argument' )
# ----------------------------------------------------------------------------

MAILLIST = []
for arg in args:
    MAILLIST.append(arg)
    

YEARS = [ '2006', '2007', '2008', '2009', '2010', '2011', '2012' ]

MONTHS = [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ]

#MAILLIST = [ 'sme-eap' ]

URL = "http://post-office.corp.redhat.com/archives"

def main():
    
    os.system("mkdir /tmp/data")

    for mailList in MAILLIST: 
        
        os.system("rm /tmp/data/" + mailList + "-archive") 
        outfile = "/tmp/data/" + mailList + "-archive"
        os.system("rm /tmp/" + mailList + "*")

        for year in YEARS:
            for month in MONTHS:
           
                archive = URL + "/" + mailList + "/" + year + "-" + month + ".txt.gz"
                tmpfile = "/tmp/" + mailList + "-" + year + "-" + month
                print ">>>>>>> Processing: %s" % archive

                curl_cmd = "curl " + archive + " > " + tmpfile + ".gz"
                gunzip_cmd = "gunzip " + tmpfile + ".gz"
                cat_cmd = "cat " + tmpfile + " >> " + outfile

                os.system(curl_cmd)
                os.system(gunzip_cmd)
                os.system(cat_cmd)
                
    print "Done"

if __name__ == "__main__":
    sys.exit(main())
