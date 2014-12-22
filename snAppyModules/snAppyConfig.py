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
BOXFISH_IP   = '85.xx'   #

#SERVER_ADDR_jl777 = 'localhost'
SERVER_ADDR_jl777 =  STONEFISH_IP
#SERVER_ADDR_jl777 = BOXFISH_IP #STONEFISH_IP

SERVER_PORT_SUPERNETHTTP = 7778 # http  14632 twisted wants int

SCHEME = 'http://'
FULL_URL = SCHEME + SERVER_ADDR_jl777 + ":" + str(SERVER_PORT_SUPERNETHTTP)
POSTHEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}


##################################################################
#
# BitcoinDarkd configuration

SERVER_PORT_BTCD_RPC = 14632    # going thorugh BTCT RPC
BitcoinDarkRPCCreds = {'user' : 'azure', 'rpcPw' : 'Ir9qDmicntTxH8C'}
environ['BitcoinDarkRPCCreds'] = BitcoinDarkRPCCreds




###################################################################
#
#
#
# The top environ {dict} contains all configuration information.
# 
#  environ['whatIsNeeded'] = 'whatIsNeeded'
#
#


CACHE_DIR = '/localCache/' # use dedicated install subdir later

environ['CACHE_DIR'] = CACHE_DIR
environ['CACHE_FILENAMES'] = {
                                'soccer_schedule' : 'soccer_schedule.xml',\
                                'other_schedule' : 'other_schedule.xml',\
                                'more' : 'more.csv'
                                }

###################################################################


# The Use Cases need control schedulers that contain the calling frequency
# and the requestTypes to be called.
#
# For each frequency, multiple calls can be registered.
#
# Each UC scheduler has three levels of dict:
#
# UC_scheduler_xy
#   
#     schedFrequency
#
#          schedRequestTypes
#
#
# These triplets are cointained in the top environ dict


###################################################################
###################################################################
###################################################################
# UC schedulers
#
#
#

UC_sched_1={}


# Three schedules here

TIMER2_Freq = 0.850 # how often the the base timer is called for loopedCall

#----------------------------------------
sched_GUIpoll ={}
sched_GUIpoll['schedName'] = 'GUIpoll'
sched_GUIpoll['callFreq'] = 900               # ms!!

schedReqTypes={}
schedReqTypes['GUIpoll'] = {'requestType':'GUIpoll'}
sched_GUIpoll['schedReqTypes']  = schedReqTypes
sched_GUIpoll['target'] = 'this Uses requests!'

#----------------------------------------
sched1={}
sched1['schedName'] = 'settingsForPing'
sched1['callFreq'] = 13500               # ms!!

schedReqTypes={}
schedReqTypes['uc_settings'] = {'requestType':'settings'}
schedReqTypes['ping'] = {'requestType':'ping'}

sched1['schedReqTypes']  = schedReqTypes
#  legacy: sched1['target'] = 'GET /nxt?requestType=settings HTTP/1.1\r\nUser-Agent: curl/7.35.0\r\nHost: 127.0.0.1:7800\r\nAccept: */*\r\ncontent-type: text/plain;\r\n\r\n'
sched1['target'] = 'this Uses requests!'

#----------------------------------------
sched_findnodePeers ={}
sched_findnodePeers['schedName'] = 'findnodePeers'
sched_findnodePeers['callFreq'] = 15500               # ms!!

schedReqTypes={}
schedReqTypes['findnodePeers'] = {'requestType':'findnode'}
sched_findnodePeers['schedReqTypes']  = schedReqTypes
sched_findnodePeers['target'] = 'this Uses requests!'


### ++++++


# plug the schedules into the environment
UC_sched_1[sched_GUIpoll['schedName']] = sched_GUIpoll
UC_sched_1[sched_findnodePeers['schedName']] = sched_findnodePeers
UC_sched_1[sched1['schedName']] = sched1


environ['UCTEST_1_ping_whitelist_777'] = UC_sched_1







##################################################################


UC_sched_3={}


#SERVER_ADDR_TEST_1 = SERVER_ADDR_jl777 #"localhost"
#SERVER_PORT_TEST_1 = 7776
#FULL_URL_TEST1 = SCHEME + SERVER_ADDR_TEST_1 + ":" + str(SERVER_PORT_TEST_1)

TIMER3_Freq = 0.850 # how ofthe the base timer is called for loopedCall

#----------------------------------------
sched_GUIpoll ={}
sched_GUIpoll['schedName'] = 'GUIpoll'
sched_GUIpoll['callFreq'] = 900               # ms!!

schedReqTypes={}
schedReqTypes['GUIpoll'] = {'requestType':'GUIpoll'}
sched_GUIpoll['schedReqTypes']  = schedReqTypes
sched_GUIpoll['target'] = 'this Uses requests!'


#----------------------------------------
sched_findvalue ={}
sched_findvalue['schedName'] = 'sched_findvalue'
sched_findvalue['callFreq'] = 4500               # ms!!

schedReqTypes={}
schedReqTypes['sched_findvalue'] = {'requestType':'findvalue'}
sched_findvalue['schedReqTypes']  = schedReqTypes
sched_findvalue['target'] = 'this Uses requests!'
### ++++++
#----------------------------------------
sched_store ={}
sched_store['schedName'] = 'sched_store'
sched_store['callFreq'] = 6500               # ms!!

schedReqTypes={}
schedReqTypes['sched_store'] = {'requestType':'store'}
sched_store['schedReqTypes']  = schedReqTypes
sched_store['target'] = 'this Uses requests!'
### ++++++


# plug the schedules into the environment

UC_sched_3[sched_GUIpoll['schedName']] = sched_GUIpoll
UC_sched_3[sched_findvalue['schedName']] = sched_findvalue
UC_sched_3[sched_store['schedName']] = sched_store



environ['UCTEST_3_store_findvalue'] = UC_sched_3






###################################################################
# sportdsdataLLC scheduler
#

schedSportsData={}
SERVER_ADDR_xmlFeed1 = "api.sportsdatallc.org"
SERVER_PORT_xmlFeed1 = 80

TIMER1_SportsdataLLC_SECS = 5000.0



schedReqTypes={}

schedReqTypes['xml1'] = {'requestType':'get1'}
schedReqTypes['xml2'] = {'requestType':'get2'}


sched1={}
sched1['schedName'] = 'matchesSchedule'
sched1['callFreq'] = 6000
sched1['reqType'] = 'xml'
sched1['target'] = 'http://api.sportsdatallc.org/soccer-t2/eu/schema/matches-schedule.xml?api_key=fv37s4rd2arqqxav774wb2kc'

sched1['schedReqTypes']  = schedReqTypes
schedSportsData[sched1['schedName']] = sched1


sched2={}
sched2['schedName'] = 'sched_matchSumm1'
sched2['callFreq'] = 11000
sched2['reqType'] = 'xml'
sched2['target'] = 'http://api.sportsdatallc.org/soccer-t2/eu/matches/2014/08/22/summary.xml?api_key=fv37s4rd2arqqxav774wb2kc'

sched2['schedReqTypes']  = schedReqTypes
schedSportsData[sched2['schedName']] = sched2


sched3={}
sched3['schedName'] = 'sched_matchSumm2'
sched3['callFreq'] = 17000
sched3['reqType'] = 'xml'
sched3['target'] = 'http://api.sportsdatallc.org/soccer-t2/eu/matches/2014/08/21/summary.xml?api_key=fv37s4rd2arqqxav774wb2kc'

sched3['schedReqTypes']  = schedReqTypes
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

