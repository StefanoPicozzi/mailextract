mailextract
===========

This tool will extract archived mail for mailing lists as at: http://post-office.corp.redhat.com/mailman/listinfo  so that they can be consolidated into a single local Thunderbird folder.  This enables the user to leverage the Thunderbird mail client, e.g. to do advanced searches through historic threads.
 
For examples, let's say a new hire subscribes to the se-jboss mailing list.  Searching historic content prior to subscription activation using the provided intranet facility is problematic as the archives are split into individual bundles based on list-name, year and month.
 
The steps involved are as per below:
 
Check that you have access to each of these archives by inspecting the archive list of interest
 
Create a local folder in Thunderbird for each list of interest, e.g. se-jboss-archive, sme-soa-p-archive
 
Inspect the folder properties and note the location of this local folder on your local file system, e.g. call this $DIR
 
Launch a terminal window and check that python is installed, e.g. $ python -V and install it otherwise, e.g. $ sudo yum install python
 
Download the attached python script and ensure it is executable, e.g. $ chmod 755 mailextract.py
 
Run it from the command line passing a parameter list of mailing lists, e.g. $ ./mailextract.py se-jboss sme-soa-p
 
On completion copy across the extracted archive e.g. $ cp /tmp/data/se-jboss-archive $DIR; $ cp /tmp/data/sme-soa-p-archive $DIR
 
Back in Thunderbird, open the properties for the local folder, e.g. se-jboss-archive and sme-soa-p-archive and press Repair Folder and the archived message should now appear
 
Done.
 
Please note that this the tool has been built and tested for Mac OS X 10.7.x and Fedora 17.
