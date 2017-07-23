

import datetime
import StringIO
import sys
import time
import ConfigParser
import subprocess
import platform
import shutil


strCurrentTime = sys.argv[1]
sFailedCase = sys.argv[2]
strFailedCase = sFailedCase.split(",")
reportHTMLfile = "log/report_midletTest_"+strCurrentTime+"/Report_"+strCurrentTime+".html"
createHTMLFile = open(reportHTMLfile,"w+")
comConfig = ConfigParser.ConfigParser()
comConfig.read("conf/config.ini")
ProjectName = comConfig.get("COM_CONFIG","ProjectName")
caseConfig = ConfigParser.ConfigParser()
caseConfig.read("conf/midletCaseList_{0}.ini".format(ProjectName))
#FailedCase = ConfigParser.ConfigParser()
#FailedCase.read("log/report_midletTest_"+strCurrentTime+"/midletFailedCase.txt")
#f1 = open("log/report_midletTest_"+strCurrentTime+"/midletFailedCase.txt","r")
#strFailedCase = FailedCase.sections()
#strFailedCase = f1.readlines()
userCaseList = caseConfig.sections()
np=0
nf=0
ne=0
passes = ''
fail = ''
error = ''
blackColor = 'lightgreen'
#Start to create HTML page
from pyh import *
page = PyH('Test_Report')
page<<div(style="text-align:center")<<h1('Test_Report')<<h4('StartTime: '+strCurrentTime)
mytab = page << table(border="2",cellpadding="5",cellspacing="2",width="1600",style="align:left")
tr1 = mytab << tr(bgcolor="lightgrey")
tr1 << th('name') + th('Pass') + th('Fail') + th('Error') + th('ATLog') + th('TraceLog')
for thisCase in userCaseList:
    tr1 = mytab << tr()
    for failCase in strFailedCase:
        if failCase == thisCase:
            passes = ''
            fail = 'true'
            error = ''
            nf=nf+1
            blackColor = 'red'
            break
            
        else:
             passes = 'true'
             fail = ''
             error = ''
             blackColor = 'lightgreen'
             
    np=np+1        
    aTLog = "ATLog/"+thisCase+".txt"
    traceLog = "MIDletTrace/"+thisCase+".txt"
    tr1.attributes['bgcolor']=blackColor
    tr1 << td(thisCase)+td(passes)+td(fail)+td(error)+td(a('OpenATLog', href=aTLog))+td(a('OpenTraceLog', href=traceLog))
np = np-nf   
tr2 = mytab << tr(bgcolor="lightgrey")
tr2 <<td('Total')+td(np)+td(nf)+td(ne)+td(' ')+td(' ')
page.printOut(reportHTMLfile)
