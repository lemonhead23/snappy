#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" this is a configuration repo. this is th eplace where as much as possible of the configuration data is supposed
to be placed in order to NOT hardcode it into the code.
 """#


LISTEN_PORT_SNT = 7800 #

environ = {}


##################################################################
#
# SuperNET configuration

STONEFISH_IP = '178.62.185.131'   #
BOXFISH_IP   = '85.178.202.108'   #

SERVER_ADDR_jl777 = 'localhost'
#SERVER_ADDR_jl777 =  STONEFISH_IP
#SERVER_ADDR_jl777 = BOXFISH_IP #STONEFISH_IP

SERVER_PORT_SUPERNETHTTP = 7778 # http  14632 twisted wants int


SCHEME = 'http://'
FULL_URL = SCHEME + SERVER_ADDR_jl777 + ":" + str(SERVER_PORT_SUPERNETHTTP)
POSTHEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}

environ['a'] =''

##################################################################
#
# BitcoinDarkd configuration

SERVER_PORT_BTCD_RPC = 14632    # going thorugh BTCT RPC
BitcoinDarkRPCCreds = {'user' : 'azure', 'rpcPw' : 'Ir9qDmicntTxH8C'}
environ['BitcoinDarkRPCCreds'] = BitcoinDarkRPCCreds




###################################################################
# local config information

CACHE_DIR = '/localCache/' # use dedicated install subdir later

environ['CACHE_DIR'] = CACHE_DIR
environ['CACHE_FILENAMES'] = {
                                'soccer_schedule' : 'soccer_schedule.xml',\
                                'other_schedule' : 'other_schedule.xml',\
                                'more' : 'more.csv'
                                }

###################################################################


# this contains config information for all UseCases as simple dicts



###################################################################
###################################################################
###################################################################
# TESTS scheduler
#

sched_Test_1={}

SERVER_ADDR_TEST_1 = SERVER_ADDR_jl777 #"localhost"
SERVER_PORT_TEST_1 = 7776
FULL_URL_TEST1 = SCHEME + SERVER_ADDR_TEST_1 + ":" + str(SERVER_PORT_TEST_1)

TIMER2_Freq = 4

sched1={}
sched1['schedName'] = 'settingsForPing'
sched1['callFreq'] = 1500               # ms!!
#
#
#

SNreqTypes={}

SNreqTypes['uc1Start_settings'] = {'requestType':'settings'}
SNreqTypes['ping'] = {'requestType':'ping'}
SNreqTypes['GUIpoll'] = {'requestType':'GUIpoll'}

sched1['SNreqTypes']  = SNreqTypes
sched1['target'] = 'GET /nxt?requestType=settings HTTP/1.1\r\nUser-Agent: curl/7.35.0\r\nHost: 127.0.0.1:7800\r\nAccept: */*\r\ncontent-type: text/plain;\r\n\r\n'

sched_Test_1[sched1['schedName']] = sched1

environ['UCTEST_1_ping_whitelist_777'] = sched_Test_1


## HAVE THE REQUESTS ASSEMBLED BY REQUETSTS, BUT SEND IT VIA WRITE RANSPIRT!!

##################################################################



###################################################################
# sportdsdataLLC scheduler
#

schedSportsData={}
SERVER_ADDR_xmlFeed1 = "api.sportsdatallc.org"
SERVER_PORT_xmlFeed1 = 80

TIMER1_SportsdataLLC_SECS = 5000.0



SNreqTypes={}

SNreqTypes['xml1'] = {'requestType':'get1'}
SNreqTypes['xml2'] = {'requestType':'get2'}


sched1={}
sched1['schedName'] = 'matchesSchedule'
sched1['callFreq'] = 6000
sched1['reqType'] = 'xml'
sched1['target'] = 'http://api.sportsdatallc.org/soccer-t2/eu/schema/matches-schedule.xml?api_key=fv37s4rd2arqqxav774wb2kc'

sched1['SNreqTypes']  = SNreqTypes
schedSportsData[sched1['schedName']] = sched1


sched2={}
sched2['schedName'] = 'sched_matchSumm1'
sched2['callFreq'] = 11000
sched2['reqType'] = 'xml'
sched2['target'] = 'http://api.sportsdatallc.org/soccer-t2/eu/matches/2014/08/22/summary.xml?api_key=fv37s4rd2arqqxav774wb2kc'

sched2['SNreqTypes']  = SNreqTypes
schedSportsData[sched2['schedName']] = sched2


sched3={}
sched3['schedName'] = 'sched_matchSumm2'
sched3['callFreq'] = 17000
sched3['reqType'] = 'xml'
sched3['target'] = 'http://api.sportsdatallc.org/soccer-t2/eu/matches/2014/08/21/summary.xml?api_key=fv37s4rd2arqqxav774wb2kc'

sched3['SNreqTypes']  = SNreqTypes
schedSportsData[sched3['schedName']] = sched3





environ['envSportsData'] = schedSportsData




# 8)
# In [16]: r.content
# Out[16]: b'<h1>Developer Over Rate</h1>'
# In [17]: r=requests.get(url)
# In [18]: r.headers
# Out[18]: CaseInsensitiveDict({'date': 'Sun, 30 Nov 2014 12:04:47 GMT', 'connection': 'keep-alive', 'server': 'Mashery Proxy', 'content-type': 'text/xml', 'content-length': '28', 'x-mashery-responder': 'prod-j-worker-us-east-1e-75.mashery.com', 'x-mashery-error-code': 'ERR_403_DEVELOPER_OVER_RATE'})
# In [19]: r.history
# In [20]: r.url
# Out[20]: 'http://api.sportsdatallc.org/soccer-t2/eu/matches/2014/08/21/summary.xml?api_key=fv37s4rd2arqqxav774wb2kc'

