#Created by :Gu Jingzhi
#Date :2017.7.4
#GitHub :https://github.com/gujingzhi

import datetime
import StringIO
import sys
import time
import ConfigParser
import subprocess
import platform
import shutil

ISOTIMEFORMAT='%Y-%m-%d_%H_%M_%S'
CurrentTime = time.strftime(ISOTIMEFORMAT, time.localtime())
createHTMLFile = open(r'Report_{0}.html'.format(CurrentTime),'w+')
caseConfig = ConfigParser.ConfigParser()
caseConfig.read("CaseList.ini")
#FailedCase = ConfigParser.ConfigParser()
#FailedCase.read("log/report_midletTest_"+strCurrentTime+"/midletFailedCase.txt")
#f1 = open("log/report_midletTest_"+strCurrentTime+"/midletFailedCase.txt","r")
#strFailedCase = FailedCase.sections()
#strFailedCase = f1.readlines()
userCaseList = caseConfig.sections()

failcase = ConfigParser.ConfigParser()
failcase.read("failList.ini")
strFailedCase = failcase.sections()

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
page<<div(style="text-align:center")<<h1('Test_Report')<<h4('StartTime: '+CurrentTime)
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
page.printOut('Report_{0}.html'.format(CurrentTime))
createHTMLFile.close()
