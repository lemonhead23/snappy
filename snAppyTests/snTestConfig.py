#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" this is a configuration repo. this is th eplace where as much as possible of the configuration data is supposed
to be placed in order to NOT hardcode it into the code.
 """#


LISTEN_PORT_SNT = 7800 #


environ = {}
# Note: this dict has currently four levels of nesting.
# The top level contains immediate configuraiton informatin for launching the app,
#
# It also contains UC_schedules that contain info for timer driven looping calls.
# These Have three nesting levels to accommodate flexibility in UC design.
#
# This dict can also contain informatin on XML data sources.
# It can be extended t use an sqlite db later.

##################################################################
#
# SuperNET configuration

STONEFISH_IP = '178.62.185.131'
BOXFISH_IP   = 'localhost'

SNET_port = '7778'
SNET_url = 'http://' + STONEFISH_IP + ":" + SNET_port
#SNET_url = 'http://' + BOXFISH_IP + ":" + SNET_port


SERVER_ADDR_jl777 = BOXFISH_IP
#SERVER_ADDR_jl777 =  STONEFISH_IP


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
