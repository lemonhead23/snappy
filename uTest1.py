#!/usr/bin/env python3

#import random
import unittest
import requests
import json
#import math
from random import randint

import binascii

from snAppyModules.snQueryComposers import QueryComposer_777
from snAppyTests.snTestConfig import *

import time
import sys
#import argparse



class SNET_BaseTest(unittest.TestCase):

    """


    """#
    url = SNET_url # environ['SNET_url']
    qComp_777 = QueryComposer_777(environ)
    numPongers = 1
    numHavenoders = 1
    # can count pongers and havenoders just as in snappey
    # and other basic state
    headers = {'content-type': 'application/json'}

    null = None

    NXTASSETS = NXTASSETS
    COINS = COINS

    def setUp(self):
        """ This can be overridden by any testing class if needed. """

        print("this test using generic setUp function")



    def example_query(self):
        test_RQ_ = {'requestType': 'settings'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        ##headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        for setting in rpl777:
            print(setting, " - ", rpl777[setting])


##################################
##################################
##################################
##################################
##################################
##################################
##################################



    #########################
    #########################
    #########################
    #########################
    #
    #     glue
    #########################
    #########################
    #########################
    #########################
    #########################


class ___glue():
    pass



class SNET_gotjson(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass


    def runTest(self):
        self.test_gotjson()


    def test_gotjson(self):
        """ test_gotjson

            call sequence:

            1. gotjson

            ---------

            asserts

            1.  reply has key 'result'


        """

        rpl777 = self.gotjson()
        self.assertTrue('result' in rpl777.keys())


    def gotjson(self):
        null = None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_gotjson = {'requestType': 'gotjson'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_gotjson)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################



class SNET_gotpacket(SNET_BaseTest):
    """
            query json is:  {'ip_port': '', 'msg': '', 'requestType': 'gotpacket', 'dur': ''}

        ~~~~~~~~~~~~
        ~~~~~~~~~~~~ SuperNET rpl777y: {'error': 'duplicate msg'}
        F
    """

    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_gotpacket()


    def test_gotpacket(self):
        """ test_gotjson

            call sequence:

            1. test_gotpacket

            ---------

            asserts

            1.  reply has key 'result'


        """

        rpl777 = self.gotpacket()
        self.assertTrue('result' in rpl777.keys())


    def gotpacket(self):
        print(2*"\n++++++++++++","test_gotpacket")
        test_RQ_gotpacket = {'requestType': 'gotpacket'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_gotpacket)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_gotnewpeer(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_gotnewpeer()


    def test_gotnewpeer(self):
        """ test_gotnewpeer

            call sequence:

            1. gotnewpeer

            ---------

            asserts

            1.  reply has key 'result'


        """

        rpl777 = self.gotnewpeer()
        self.assertTrue('result' in rpl777.keys())


    def gotnewpeer(self):
        null = None
        print(2*"\n++++++++++++","test_gotnewpeer")
        test_RQ_gotnewpeer = {'requestType': 'gotnewpeer'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_gotnewpeer)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################





class SNET_BTCDpoll(SNET_BaseTest):

    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_BTCDpoll()


    def test_BTCDpoll(self):
        """ test_BTCDpoll

            call sequence:

            1. BTCDpoll

            ---------

            asserts

            1.  reply has key 'result'


        """
        rpl777 = self.BTCDpoll()
        self.assertTrue('result' in rpl777.keys())


    def BTCDpoll(self):
        null = None
        print(2*"\n++++++++++++","test_BTCDpoll")
        test_RQ_BTCDpoll = {'requestType': 'BTCDpoll'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_BTCDpoll)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_GUIpoll(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_GUIpoll()


    def test_GUIpoll(self):
        """ test_gotjson

            call sequence:

            1. gotjson

            ---------

            asserts

            1.  reply has key 'result'


        """

        rpl777 = self.GUIpoll()
        self.assertTrue('result' in rpl777.keys())
        self.assertTrue( rpl777['result'] == 'nothing pending')



    def GUIpoll(self):
        null = None
        print(2*"\n++++++++++++","test_GUIpoll")
        test_RQ_GUIpoll = {'requestType': 'GUIpoll'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_GUIpoll)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################



class SNET_settings(SNET_BaseTest):

    settingsReply ="""
                query json is:  {'value': '', 'requestType': 'settings', 'field': '', 'reinit': ''}
           ./BitcoinDarkd  SuperNET '{"requestType":"settings"}'
        {
          "debug":2,
          "whitelist":[
            "209.126.70.156",
            "209.126.70.159",
            "209.126.70.170",
            "104.40.137.20",
            "104.41.129.107",
            "162.248.163.43",
            "23.97.66.164",
            "100.79.14.220",
            "137.116.193.215",
            "80.82.64.135",
            "185.21.192.9",
            "94.102.63.149",
            "37.187.200.156",
            "199.193.252.103",
            "89.212.19.49",
            "128.199.183.249",
            "190.10.10.145"
          ],
          "MMatrix":1,
          "GUIPOLL":0,
          "MAINNET":1,
          "MIN_NXTCONFIRMS":13,
          "UPNP":0,
          "MULTIPORT":1,
          "LIBTEST":1,
         "MGWROOT":"/var/www",
          "active":[
            "BTCD"
          ],
          "coins":[
            {
              "name":"BTCD",
              "maxevolveiters":10,
              "useaddmultisig":1,
              "nohexout":1,
              "conf":"/home/azure/.BitcoinDark/BitcoinDark.conf",
              "backupdir":"/home/azure/backups",
              "asset":"11060861818140490423",
              "minconfirms":3,
              "estblocktime":60,
              "rpc":"127.0.0.1:14632",
              "ciphers":[
                {
                  "skipjack":"RNmF5YmUY81wWu1njRiYvJRoKMf1Ms9kN3"
                },
                {
                  "aes":"RXcpYBAWbbNgNBSnr8kB9sufSfZDwttXwC"
                },
                {
                  "blowfish":"RJgoTjReeE2ZKbymx4PyiyXmgsbTkW9sds"
                }
              ],
              "clonesmear":1,
              "privacyServer":"127.0.0.1",
              "pubaddrBOXFISH":"RHwBRZzbETNR3nyQjuVWgaLdaBNBu3gwbw",
              "srvpubaddrBOXFISH":"RWfwbc25mPTcSN4WgDXZeMnf3SFT1rN8tM",
              "pubaddr":"RWW6FPcopt5va8TtGkPsPTK9GEr8r8QS9Q",
              "srvpubaddr":"RTib4uLAc9DfP2x6tGsQ9SZzFfXmcgGqZm",
              "grind1":"RMwvWWWRVgp7QBJuAwCpvmP6Q27kAYhnAc",
              "rarah4":"RVYtALDy7WspnvxFrdDDoVafAdTNuqipyH",
              "Lfactor":3
            }
          ]
        }

        """


    def setUp(self):
        print("SNET_settings setUp here- NOP")
        pass


    def runTest(self):
        self.test_settings()

    def test_settings(self):
        """ test_settings

            call sequence:

            1. settings

            ---------

            asserts

            1.  reply has key 'coins'


        """

        rpl777 = self.settings()


        print(rpl777)
        for setting in rpl777:
            print(setting, " - ",rpl777[setting])
        print("\n")

        self.assertTrue('coins' in rpl777.keys())


    def settings(self):
        null = None
        print(2*"\n++++++++++++","test_settings")
        test_RQ_settings = {'requestType': 'settings'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_settings)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


    #########################
    #########################
    #########################
    #########################
    #
    #     ramchains
    #########################
    #########################
    #########################
    #########################
    #########################


class ___Ramchains():
    pass


class SNET_ramstatus(SNET_BaseTest):
    """
     {'pendingdeposits': '0', 'gatewayid': '-1', 'RTNXT': {'ECblock': '7630770946270487105', 'height': '363517', 'lag': '12', 'ECheight': '363516'}, 'sentNXT': '15000000000', 'circulation': '1024989150000', 'result': 'MGWstatus', 'balance': '18446744014491661761', 'unspent': '1025204260145', 'coin': 'BTCD', 'internal': '0', 'pendingredeems': '59433000000', 'supply': '0', 'BTCD': {'height': '382851', 'lag': '3', 'permblocks': '382848'}, 'ramchain': 'BTCD : RT.382851 nonz.382848 V.382848 B.382848 B64.382848 B4096.380928 | 118.5MB 19.1MB R6.22 | minutes: V0.5 B0.5 | outputs.934661 188917683.05667377 spends.911829 187711860.41899481 -> balance: 22832 1205822.63767893 ave 52.81283452'}
    """

    def setUp(self):
        print(" test setUp func here")
        pass


    def runTest(self):
        self.test_ramstatus()



    def test_ramstatus(self):
        #query_json = {'coin': 'BTCD', 'destip': '', 'requestType': 'ramstatus'}

        print(2*"\n++++++++++++","test_ramstatus")
        test_RQ_ = {'requestType': 'ramstatus'}
        test_RQ_['coin'] = 'BTCD' #

        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        # {'ramchain': 'BTCD : RT.379953 nonz.379950 V.379950 B.379950 B64.379904 B4096.376832 | 116.8MB 18.8MB R6.20 | minutes: V2.8 B2.8 | outputs.929313 187512689.34161791 spends.906780 186307056.66912407 -> balance: 22533 1205632.67249383 ave 53.50520004', 'unspent': '1025344560145', 'result': 'MGWstatus', 'internal': '0', 'coin': 'BTCD', 'balance': '18446744014493961761', 'pendingdeposits': '0', 'RTNXT': {'height': '362110', 'lag': '12', 'ECheight': '362104', 'ECblock': '6414431364385709558'}, 'gatewayid': '-1', 'supply': '0', 'BTCD': {'height': '379953', 'lag': '3', 'permblocks': '379950'}, 'circulation': '1025127150000', 'pendingredeems': '59433000000', 'sentNXT': '15000000000'}

        self.assertTrue('result' in rpl777.keys() )

    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null = None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################



class SNET_ramaddrlist(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_ramaddrlist()


    def test_ramaddrlist(self):
        #query_json = {'coin': '', 'requestType': 'ramaddrlist'}
#  {'mine': 1, 'total': 1, 'result': 'addrlist', 'multisig': 1}


        print(2*"\n++++++++++++","test_ramaddrlist")
        test_RQ_ = {'requestType': 'ramaddrlist'}
        test_RQ_['coin'] = 'BTCD'
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        if 'error' in rpl777.keys():
            self.assertTrue(False)
            print(2*"\n~~~~~~~~~~~~","error in SuperNET rpl777y:\n\n", rpl777)
        else:
            self.assertTrue('result' in rpl777.keys() )

    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################



class SNET_ramstring(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass




    def runTest(self):
        self.test_ramstring()

    def test_ramstring(self):
        #query_json = {'destip': '', 'rawind': '', 'requestType': 'ramstring', 'type': ''}


        print(2*"\n++++++++++++","test_ramstring")
        test_RQ_ = {'requestType': 'ramstring'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        if 'error' in rpl777.keys():
            self.assertTrue(False)
            print(2*"\n~~~~~~~~~~~~","error in SuperNET rpl777y:\n\n", rpl777)
        else:
            self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_ramrawind(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_ramrawind()


    def test_ramrawind(self):
        #query_json = {'destip': '', 'coin': '', 'requestType': 'ramblock', 'blocknum': ''}


        print(2*"\n++++++++++++","test_ramrawind")
        test_RQ_ = {'requestType': 'ramrawind'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        if 'error' in rpl777.keys():
            self.assertTrue(False)
            print(2*"\n~~~~~~~~~~~~","error in SuperNET rpl777y:\n\n", rpl777)
        else:
            self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################

class SNET_ramblock(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass


    def runTest(self):
        self.test_ramblock()



    def test_ramblock(self):

        print(2*"\n++++++++++++","test_ramblock")
        test_RQ_ = {'requestType': 'ramblock'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        if 'error' in rpl777.keys():
            self.assertTrue(False)
            print(2*"\n~~~~~~~~~~~~","error in SuperNET rpl777y:\n\n", rpl777)
        else:
            self.assertTrue('result' in rpl777.keys() )

    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################



class SNET_ramscript(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_ramscript()


    def test_ramscript(self):
        #query_json = {'vout': '', 'destip': '', 'txid': '', 'requestType': 'ramscript', 'txind': '', 'v': '', 'blocknum': ''}


        print(2*"\n++++++++++++","test_ramscript")
        test_RQ_ = {'requestType': 'ramscript'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        if 'error' in rpl777.keys():
            self.assertTrue(False)
            print(2*"\n~~~~~~~~~~~~","error in SuperNET rpl777y:\n\n", rpl777)
        else:
            self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_ramtxlist(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_ramtxlist()


    def test_ramtxlist(self):
        #query_json = {'address': '', 'destip': '', 'requestType': 'ramtxlist', 'unspent': '', 'coin': ''}


        print(2*"\n++++++++++++","test_ramtxlist")
        test_RQ_ = {'requestType': 'ramtxlist'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )

    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################



class SNET_ramrichlist(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_ramrichlist()


    def test_ramrichlist(self):
        #query_json = {'recalc': '', 'coin': '', 'destip': '', 'requestType': 'ramrichlist', 'numwhales': ''}


        print(2*"\n++++++++++++","test_ramrichlist")
        test_RQ_ = {'requestType': 'ramrichlist'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_ramcompress(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_ramcompress()


    def test_ramcompress(self):
        #query_json = {'data': '', 'destip': '', 'requestType': 'ramcompress', 'coin': ''}


        print(2*"\n++++++++++++","test_x1")
        test_RQ_ = {'requestType': 'ramcompress'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_ramexpand(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_ramexpand()


    def test_ramexpand(self):
        #query_json = {'requestType': 'ramexpand', 'destip': '', 'data': '', 'coin': ''}


        print(2*"\n++++++++++++","test_ramexpand")
        test_RQ_ = {'requestType': 'ramexpand'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_rambalances(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_rambalances()


    def test_rambalances(self):
        #query_json = {'requestType': 'rambalances', 'destip': '', 'rates': '', 'coin': '', 'coins': ''}


        print(2*"\n++++++++++++","test_rambalances")
        test_RQ_ = {'requestType': 'rambalances'}

        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_rampyramid(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_rampyramid()


    def test_rampyramid(self):
        #query_json = {'destip': '', 'requestType': 'rampyramid', 'type': '', 'blocknum': '', 'coin': '', 'port': ''}


        print(2*"\n++++++++++++","test_rampyramid")
        test_RQ_ = {'requestType': 'rampyramid'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################





class SNET_ramresponse(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_ramresponse()


    def test_ramresponse(self):
        #query_json = {'data': '', 'requestType': 'ramresponse', 'coin': '', 'origcmd': ''}


        null = None #  b'{"result":null}' for when null is sent back, which py doenst know

        print(2*"\n++++++++++++","test_ramresponse")
        test_RQ_ = {'requestType': 'ramresponse'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################

    #########################
    #########################
    #########################
    #########################
    #
    #     MGW
    #########################
    #########################
    #########################
    #########################
    #########################



class ___MGW():
    pass


class SNET_genmultisig(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_genmultisig()


    def test_genmultisig(self):
        #query_json = {'destip': '', 'requestType': 'genmultisig', 'coin': '', 'refcontact': '', 'N': '', 'contacts': ''}


        print(2*"\n++++++++++++","test_genmultisig")
        test_RQ_ = {'requestType': 'genmultisig'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_getmsigpubkey(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass




    def runTest(self):
        self.test_getmsigpubkey()

    def test_getmsigpubkey(self):
        #query_json = {'requestType': 'getmsigpubkey', 'myaddr': '', 'refNXTaddr': '', 'coin': '', 'mypubkey': ''}


        print(2*"\n++++++++++++","test_getmsigpubkey")
        test_RQ_ = {'requestType': 'getmsigpubkey'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_MGWaddr(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_MGWaddr()


    def test_MGWaddr(self):
        #query_json = {'requestType': 'MGWaddr'}

        null = None #  b'{"result":null}' for when null is sent back, which py doenst know

        print(2*"\n++++++++++++","test_MGWaddr")
        test_RQ_ = {'requestType': 'MGWaddr'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_MGWresponse(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_MGWresponse()


    def test_MGWresponse(self):
        #query_json = {'requestType': 'MGWresponse'}

        null = None #  b'{"result":null}' for when null is sent back, which py doenst know

        print(2*"\n++++++++++++","test_MGWresponse")
        test_RQ_ = {'requestType': 'MGWresponse'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_setmsigpubkey(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_setmsigpubkey()


    def test_setmsigpubkey(self):

            #query_json = {'refNXTaddr': '', 'addr': '', 'pubkey': '', 'requestType': 'setmsigpubkey', 'coin': ''}

        null = None #  b'{"result":null}' for when null is sent back, which py doenst know

        print(2*"\n++++++++++++","test_setmsigpubkey")
        test_RQ_ = {'requestType': 'setmsigpubkey'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_cosign(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_cosign()


    def test_cosign(self):
        #query_json = {'text': '', 'requestType': 'cosign', 'seed': '', 'otheracct': ''}


        print(2*"\n++++++++++++","test_cosign")
        test_RQ_ = {'requestType': 'cosign'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################





class SNET_cosigned(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_cosigned()


    def test_cosigned(self):
        #query_json = {'privacct': '', 'result': '', 'seed': '', 'pubacct': '', 'requestType': 'cosigned'}


        print(2*"\n++++++++++++","test_cosigned")
        test_RQ_ = {'requestType': 'cosigned'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())



    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


    #########################
    #########################
    #########################
    #########################
    #
    #     ipComms
    #########################
    #########################
    #########################
    #########################
    #########################


class ___ipComms:
    pass


class SNET_ping(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_ping()


    def test_ping(self):
        #query_json = {'destip': 'localhost', 'ipaddr': '', 'pubkey': '', 'requestType': 'ping', 'port': ''}


        destip = '178.62.185.131' # stonefish
        print(2*"\n++++++++++++","test_ping")
        test_RQ_ = {'requestType': 'ping'}
        test_RQ_['destip'] = destip #'localhost'
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_pong(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_pong()


    def test_pong(self):
        null=None
                #query_json = {'port': '', 'pubkey': '', 'yourip': '', 'requestType': 'pong', 'yourport': '', 'ipaddr': '209.126.70.156'}

        print(2*"\n++++++++++++","test_pong")
        test_RQ_ = {'requestType': 'pong'}
        test_RQ_['ipaddr'] = '209.126.70.156'

        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################



class SNET_sendfrag(SNET_BaseTest):
    """sendfrag
Sendfrag allows to send files. This function is low level and not practical for manual use. See startxfer for more infos.
    """#

    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_sendfrag()


    def test_sendfrag(self):
        #query_json = {'fragi': '', 'pubkey': '', 'blocksize': '', 'numfrags': '', 'totalcrc': '', 'name': '', 'totallen': '', 'data': '', 'handler': '', 'ipaddr': '', 'requestType': 'sendfrag', 'datacrc': ''}


        print(2*"\n++++++++++++","test_sendfrag")
        test_RQ_ = {'requestType': 'sendfrag'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        if 'error' in rpl777.keys():
            self.assertTrue(False)

        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_gotfrag(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_gotfrag()


    def test_gotfrag(self):
# query json is:  {'fragi': '', 'totalcrc': '', 'name': '', 'blocksize': '', 'datacrc': '', 'handler': '', 'numfrags': '', 'totallen': '', 'ipaddr': '', 'count': '', 'requestType': 'sendfrag', 'pubkey': ''}

        print(2*"\n++++++++++++","test_gotfrag")
        test_RQ_ = {'requestType': 'gotfrag'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################



class SNET_startxfer(SNET_BaseTest):

    """startxfer

Startxfer allows to send files. Startxfer splits up a file (or memory buffer) into fixed size blocks. Then it starts parallel transfers using sendfrag. The receiving side receives the sendfrag and dynamically creates a incoming file data structure and sends back a gotfrag. The original sender gets the gotfrag and then sends back the first block that has not been sent yet or that has not been gotfragged yet
static char *startxfer[] = { (char *)startxfer_func, "startxfer", "V", "fname", "dest", "data", "timeout", "handler", 0 };
"timeout" is in second.
"dest" is the IP address of the receiving side.
"fname" is the name of a hex file. The default location is the "archive" folder. The DATADIR option in SuperNET.conf file allows to choose the location of datas (nb: only relative path is allowed)
"data" is hex datas to be send. *** further description needed ***
"handler" *** description needed ***
"data" and "fname" are mutualy exclusive.
example
./BitcoinDarkd SuperNET '{"requestType":"startxfer","fname":"send_msg.txt","dest":"79.245.10.166"}'
result
{"result":"pending SuperNET API call","txid":"1316152311343726577"}

"""#

    def setUp(self):
        print(" test setUp func here")
        pass


    def runTest(self):
        self.test_startxfer()



    def test_startxfer(self):

        print(2*"\n++++++++++++","test_startxfer")
        test_RQ_ = {'requestType': 'startxfer'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )

        #query_json = {'requestType': 'startxfer', 'fname': '', 'timeout': '', 'handler': '', 'dest': '', 'data': ''}

        # {'result': 'pending SuperNET API call', 'txid': '2466605655551381573'}


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_getfile(SNET_BaseTest):


    def setUp(self):
        print(" test getfile func here")
        pass



    def runTest(self):
        self.test_getfile()


    def test_getfile(self):



#  static char *getfile[] = { (char *)getfile_func, "getfile", "V", "name", "handler", 0 };
#
        print(2*"\n++++++++++++","test_getfile")
        test_RQ_ = {'requestType': 'getfile'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


    #########################
    #########################
    #########################
    #########################
    #
    #     Kademlia
    #########################
    #########################
    #########################
    #########################
    #########################

class ___Kademlia():
    pass

class SNET_store(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass


    def msg(self):


        MSGfrags = [
                        'Eight, sir; seven, sir;',
                        'Six, sir; five, sir;',
                        'Four, sir; three, sir;',
                        'Two, sir; one!',
                        'Tenser, said the Tensor.',
                        'Tenser, said the Tensor.',
                        'Tension, apprehension,',
                        'And dissension have begun.',
                        ]
        msg = ''
        for frag in range(randint(4,7)):
            msg += MSGfrags[randint(0,7)]
        return msg



    def runTest(self):
        self.test_store()


    def test_store(self):
        # {"requestType":"store",
        print(2*"\n++++++++++++","test_store")

        n1 = self.msg()
        n2 = n1.encode("utf-8")
        n2 = binascii.hexlify(n2)
        n3 = n2.decode("utf-8")
        test_RQ_store = {'requestType': 'store'}
        test_RQ_store['name']='testStoreName' + str(int(time.time())) #n1

        test_RQ_store['data']=n3


        payload= self.qComp_777.make_777POST_Request(test_RQ_store)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################



class SNET_findvalue(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_findvalue()


    def test_findvalue(self):
        #query_json = {'data': '', 'key': '', 'name': '', 'requestType': 'findvalue', 'pubkey': ''}

        #reqData1['key'] = self.storedVals[key]
        print(2*"\n++++++++++++","test_findvalue")
        test_RQ_findvalue = {'requestType': 'findvalue'}
        test_RQ_findvalue['key'] = '2685049983433793128'
        #test_RQ_findvalue[''] = ''
        payload= self.qComp_777.make_777POST_Request(test_RQ_findvalue)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        foundVal=rpl777['data']
        #foundVal = foundVal.decode("utf-8")
        foundVal = binascii.a2b_hex(foundVal)

        print(foundVal)


        self.assertTrue('data' in rpl777.keys() )



    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################



class SNET_findnode(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_findnode()


    def test_findnode(self):

        print(2*"\n++++++++++++","test_findnode")
        test_RQ_ = {'requestType': 'findnode'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_havenode(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_havenode()


    def test_havenode(self):

        print(2*"\n++++++++++++","test_havenode")
        test_RQ_ = {'requestType': 'havenode'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

# {'error': 'invalid havenode_func arguments'}
# F

        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################

class SNET_findaddress(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_findaddress()


    def test_findaddress(self):
        #query_json = {'refaddr': '', 'requestType': 'findaddress', 'numthreads': '', 'dist': '', 'duration': '', 'list': ''}

        null = None #  b'{"result":null}' for when null is sent back, which py doenst know


        test_RQ_getpeers = {'requestType': 'getpeers'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_getpeers)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        self.assertTrue('peers' in rpl777.keys())

        peers = rpl777['peers']
        for peer in peers[2:]:
            print(peer,"\n")
            psrv = peer['pserver']
            srvNXT = peer['srvNXT']
            print(psrv,"\n")
            print(srvNXT,"\n")
           #log.msg(1*"\n FINDNODE peer:", srvNXT)



        print(2*"\n++++++++++++","test_findaddress")
        testRQ_findaddress = {'requestType': 'findaddress'}

        testRQ_findaddress['refaddr'] = srvNXT #'14083245880221951726' #srvNXT
        testRQ_findaddress['dist'] = 32
        testRQ_findaddress['duration'] = 11
        testRQ_findaddress['numthreads'] = 2

        payload= self.qComp_777.make_777POST_Request(testRQ_findaddress)


        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )

    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_havenodeB(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_havenodeB()


    def test_havenodeB(self):
        #query_json = {'pubkey': '', 'name': '', 'data': '', 'key': '', 'requestType': 'havenodeB'}


        print(2*"\n++++++++++++","test_havenodeB")
        test_RQ_ = {'requestType': 'havenodeB'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777


###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_puzzles(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_puzzles()


    def test_puzzles(self):

#
# static char *puzzles[] = { (char *)challenge_func, "puzzles", "V", "reftime", "duration", "threshold", 0 };


        print(2*"\n++++++++++++","test_puzzles")
        test_RQ_ = {'requestType': 'puzzles'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################



class SNET_nonces(SNET_BaseTest):



# static char *nonces[] = { (char *)response_func, "nonces", "V", "reftime", "threshold", "nonces", 0 };
#
    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_nonces()


    def test_nonces(self):
        #query_json = {'pubkey': '', 'name': '', 'data': '', 'key': '', 'requestType': 'havenodeB'}


        print(2*"\n++++++++++++","test_nonces")
        test_RQ_ = {'requestType': 'nonces'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################

    #########################
    #########################
    #########################
    #########################
    #
    #     MofNs
    #########################
    #########################
    #########################
    #########################
    #########################



class ___MofNs():
    pass

class SNET_savefile(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_savefile()


    def test_savefile(self):
        #query_json = {'M': '', 'N': '', 'requestType': 'savefile', 'filename': '', 'backup': '', 'L': '', 'password': '', 'pin': ''}


        print(2*"\n++++++++++++","test_savefile")
        test_RQ_ = {'requestType': 'savefile'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################





class SNET_restorefile(SNET_BaseTest):
    """ this may require MASSIVE calulation, don't do this in ALL for now  """

    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_restorefile()


    def test_restorefile(self):
        #query_json = {'password': '', 'backup': '', 'sharenrs': '', 'restorefile': 'stop', 'destfile': '', 'filename': '', 'pin': '', 'L': '', 'N': '', 'txids': '', 'M': ''}

        null = None #  b'{"result":null}' for when null is sent back, which py doenst know

        print(2*"\n++++++++++++","test_restorefile")
        test_RQ_ = {'requestType': 'restorefile'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_publish(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_publish()


    def test_publish(self):
        #query_json = {'L': '', 'backup': '', 'files': '', 'N': '', 'pin': '', 'requestType': 'publish', 'M': ''}

        print(2*"\n++++++++++++","test_publish")
        test_RQ_ = {'requestType': 'publish'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


    #########################
    #########################
    #########################
    #########################
    #
    #     Telepathy
    #########################
    #########################
    #########################
    #########################
    #########################



class ___Telepathy():
    pass



class SNET_getpeers(SNET_BaseTest):


    """
    r.apparent_encoding = ascii
    r.headers
    CaseInsensitiveDict({'content-length': '1032', 'access-control-allow-headers': 'Authorization, Content-Type', 'server': 'SuperNET', 'content-type': 'text/html', 'access-control-allow-origin': '*', 'access-control-allow-credentials': 'true', 'access-control-allow-methods': 'GET, POST, OPTIONS'})

    '{\n\t"peers":\t[{\n\t\t\t"pserver":\t{\n\t\t\t\t"port":\t7777\n\t\t\t},\n\t\t\t"privateNXT":\t"12964664952395058808",\n\t\t\t"RS":\t"NXT-FMMS-4QHR-VEJ9-DYXU9",\n\t\t\t"pubkey":\t"702f4bc8d955a4f5053b245ee9a40199ff8fca2bd304c13f77bb3c863e792171"\n\t\t}, {\n\t\t\t"pserver":\t{\n\t\t\t\t"port":\t55238,\n\t\t\t\t"recv":\t1,\n\t\t\t\t"lastrecv":\t81.13409642\n\t\t\t},\n\t\t\t"srvNXT":\t"10501328530345129240",\n\t\t\t"srvipaddr":\t"178.62.185.131",\n\t\t\t"srvport":\t"55238",\n\t\t\t"recv":\t1,\n\t\t\t"RS":\t"NXT-CXAS-P5SG-EUVZ-BQ3H5",\n\t\t\t"pubkey":\t"020ad74d2c6ce659a64ac0e7fc5415559ca56a3a233be0af73cded476fd0747d"\n\t\t}, {\n\t\t\t"pserver":\t{\n\t\t\t\t"port":\t7777,\n\t\t\t\t"sent":\t93,\n\t\t\t\t"lastsent":\t0.28231793,\n\t\t\t\t"recv":\t276,\n\t\t\t\t"lastrecv":\t0.27922627,\n\t\t\t\t"pings":\t19,\n\t\t\t\t"pongs":\t92,\n\t\t\t\t"pingtime":\t25518.50000000,\n\t\t\t\t"avetime":\t316085.26991836\n\t\t\t},\n\t\t\t"srvNXT":\t"1978065578067355462",\n\t\t\t"srvipaddr":\t"89.212.19.49",\n\t\t\t"sent":\t93,\n\t\t\t"recv":\t276,\n\t\t\t"RS":\t"NXT-5TU8-78XL-W2CW-32WWQ",\n\t\t\t"pubkey":\t"c269a8b4567c0b3062e6c4be859d845c4b808a405dd03d0d1ac7b4d9cb725b40"\n\t\t}],\n\t"num":\t2,\n\t"Numpservers":\t3,\n\t"Numnxtaccts":\t0\n}'
    r.status_code 200

    r.raw
    <urllib3.response.HTTPResponse at 0x7f4ac7c652e8>
    rep=eval(r.text)

    {'Numnxtaccts': 0,
    'Numpservers': 3,
    'num': 2,
    'peers': [{'RS': 'NXT-FMMS-4QHR-VEJ9-DYXU9',
      'privateNXT': '12964664952395058808',
      'pserver': {'port': 7777},
      'pubkey': '702f4bc8d955a4f5053b245ee9a40199ff8fca2bd304c13f77bb3c863e792171'},
    {'RS': 'NXT-CXAS-P5SG-EUVZ-BQ3H5',
      'pserver': {'lastrecv': 81.13409642, 'port': 55238, 'recv': 1},
      'pubkey': '020ad74d2c6ce659a64ac0e7fc5415559ca56a3a233be0af73cded476fd0747d',
      'recv': 1,
      'srvNXT': '10501328530345129240',
      'srvipaddr': '178.62.185.131',
      'srvport': '55238'},
    {'RS': 'NXT-5TU8-78XL-W2CW-32WWQ',
      'pserver': {'avetime': 316085.26991836,
       'lastrecv': 0.27922627,
       'lastsent': 0.28231793,
       'pings': 19,
       'pingtime': 25518.5,
       'pongs': 92,
       'port': 7777,
       'recv': 276,
       'sent': 93},
      'pubkey': 'c269a8b4567c0b3062e6c4be859d845c4b808a405dd03d0d1ac7b4d9cb725b40',
      'recv': 276,
      'sent': 93,
      'srvNXT': '1978065578067355462',
      'srvipaddr': '89.212.19.49'}]}

      """#

    def setUp(self):
        print("SNET_getpeers setUp here- NOP")
        pass


    def runTest(self):
        self.test_getpeers()


    def test_getpeers(self):
        """
        self.assertTrue('peers' in rpl777.keys())

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def getpeers(self):
        print(2*"\n++++++++++++","test_getpeers")
        test_RQ_getpeers = {'requestType': 'getpeers'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_getpeers)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777




    def test_APICALL(self):
        """
        self.assertTrue('peers' in rpl777.keys())

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777


class SNET_addcontact(SNET_BaseTest):
    """addcontact
Contacts are basically a way of mapping long acct numbers to easy to remember handles for use in other API calls. Since they are not stored on HDD you need to put a "contacts":[{"jl777":""}....] field in SuperNET.conf or have the GUI do it on startup. Calling addcontact again will just update the acct. These accts have to be funded with at least 1 NXT I will add a display handle API with a special handle called "me" that shows your private acct and public key.
Maintaining a contacts list prevents spoofing. Use addcontact to add contacts.
static char *addcontact[] = { (char *)addcontact_func, "addcontact", "V", "handle", "acct", 0 };
example
./BitcoinDarkd SuperNET '{"requestType":"addcontact","handle":"jl777","acct":"NXT-P3K3-M9XB-5MDG-DVNT8"}'
result
{"result":"(jl777) acct.(NXT-P3K3-M9XB-5MDG-DVNT8) (12927190866050319905) has pubkey.(45ec94823354d56c549b475c5e3ffd49c9c2cf4a366deed809bfba38dd756318)"}
Note that the parameter is handle for addcontact, but contact for removecontact and dispcontact. This is because a handle is a NXT address, whilst a contact is a label for a handle.
"""#

    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_addcontact()


    def test_addcontact(self):
        #query_json = {'handle': '', 'acct': '', 'requestType': 'addcontact'}
#{"result":"(myHan1) acct.(1978065578067355462) (1978065578067355462) has pubkey.(c269a8b4567c0b3062e6c4be859d845c4b808a405dd03d0d1ac7b4d9cb725b40)"}
#./BitcoinDarkd  SuperNET '{"requestType":"addcontact","handle":"myHan1","acct":"8128620123513482991"}'

        ##### getpeers
        test_RQ_getpeers = {'requestType': 'getpeers'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_getpeers)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        self.assertTrue('peers' in rpl777.keys())

        peers = rpl777['peers']
        for peer in peers[2:]:
            print(peer)
            psrv = peer['pserver']
            srvNXT = peer['srvNXT']
            print(psrv)
            print(srvNXT)
           #log.msg(1*"\n FINDNODE peer:", srvNXT)



        print(2*"\n++++++++++++","test_addcontact")
        testRQ_addcontact = {'requestType': 'addcontact'}
        testRQ_addcontact['acct'] = srvNXT
        testRQ_addcontact['handle'] = "myTestHandle"  #+ str(time.time())


        payload= self.qComp_777.make_777POST_Request(testRQ_addcontact)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)



        self.assertTrue('result' in rpl777.keys() )
        self.assertTrue('pubkey' in testReq.text )




        print(2*"\n++++++++++++","test_dispcontact")
        testRQ_dispcontact = {'requestType': 'dispcontact'}
        #test_dispcontact['acct'] =
        testRQ_dispcontact['contact'] =  'myTestHandle' # "myTestHandle"  #+ str(time.time())


        payload= self.qComp_777.make_777POST_Request(testRQ_dispcontact)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('handle' in rpl777.keys() )


        print(2*"\n++++++++++++","test_RQ_removecontact")
        test_RQ_removecontact = {'requestType': 'removecontact'}
        #test_dispcontact['acct'] =
        test_RQ_removecontact['contact'] =  'myTestHandle' # "myTestHandle"  #+ str(time.time())


        payload= self.qComp_777.make_777POST_Request(test_RQ_removecontact)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )
        self.assertTrue('deleted' in testReq.text )



    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_removecontact(SNET_BaseTest):
    """removecontact
Maintaining a contacts list prevents spoofing. Use removecontact to remove contacts.
static char *removecontact[] = { (char *)removecontact_func, "removecontact", "V", "contact", 0 };
note; you cannot change a contact directly; you have to remove it and add it again with a different handle.
example
./BitcoinDarkd SuperNET '{"requestType":"removecontact","contact":"jl777"}'
result
{"result":"handle.(jl777) deleted"}
"""

    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_removecontact()


    def test_removecontact(self):

        ##### getpeers
        test_RQ_getpeers = {'requestType': 'getpeers'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_getpeers)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        self.assertTrue('peers' in rpl777.keys())

        peers = rpl777['peers']
        for peer in peers[2:]:
            print(peer)
            psrv = peer['pserver']
            srvNXT = peer['srvNXT']
            print(psrv)
            print(srvNXT)
           #log.msg(1*"\n FINDNODE peer:", srvNXT)



        print(2*"\n++++++++++++","test_addcontact")
        testRQ_addcontact = {'requestType': 'addcontact'}
        testRQ_addcontact['acct'] = srvNXT
        testRQ_addcontact['handle'] = "myTestHandle"  #+ str(time.time())


        payload= self.qComp_777.make_777POST_Request(testRQ_addcontact)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )
        self.assertTrue('pubkey' in testReq.text )





        print(2*"\n++++++++++++","test_dispcontact")
        testRQ_dispcontact = {'requestType': 'dispcontact'}
        #test_dispcontact['acct'] =
        testRQ_dispcontact['contact'] =  'myTestHandle' # "myTestHandle"  #+ str(time.time())


        payload= self.qComp_777.make_777POST_Request(testRQ_dispcontact)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('handle' in rpl777.keys() )


        print(2*"\n++++++++++++","test_RQ_removecontact")
        test_RQ_removecontact = {'requestType': 'removecontact'}
        #test_dispcontact['acct'] =
        test_RQ_removecontact['contact'] =  'myTestHandle' # "myTestHandle"  #+ str(time.time())


        payload= self.qComp_777.make_777POST_Request(test_RQ_removecontact)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )
        self.assertTrue('deleted' in testReq.text )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_dispcontact(SNET_BaseTest):
    """dispcontact
with dispcontact you can display your added contacts.
static char *dispcontact[] = { (char *)dispcontact_func, "dispcontact", "V", "contact", 0 };
example
./BitcoinDarkd SuperNET '{"requestType":"dispcontact","contact":"myhandle"}'
result
{"handle":"myhandle","acct":"NXT-KK6R-W88P-LA6E-6YR2G","NXT":"5116932371338806423", "pubkey":"a98677f8d351abd58446157dea7208fa2150dec3006ba33a06657af6eaede265"}
'myhandle' is assigned by default to your private NXT address. 'mypublic' is assigned to your public address.
example
Using * will display all current contacts:
./BitcoinDarkd SuperNET '{"requestType":"dispcontact","contact":"*"}'
result
[ {"handle":"myhandle","acct":"NXT-KK6R-W88P-LA6E-6YR2G","NXT":"5116932371338806423","pubkey":"a98677f8d351abd58446157dea7208fa2150dec3006ba33a06657af6eaede265"},
{"handle":"mypublic","acct":"NXT-NFXU-5SNN-69Q2-7NSGF","NXT":"6249611027680999354","pubkey":"8966bee9e9aef15250c2161133a6a086eeb4739e4077f2c0c4cae3b6fe7bb008"}] """#


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_dispcontact()


    def test_dispcontact(self):

        ##### getpeers
        test_RQ_getpeers = {'requestType': 'getpeers'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_getpeers)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        self.assertTrue('peers' in rpl777.keys())

        peers = rpl777['peers']
        for peer in peers[2:]:
            print(peer)
            psrv = peer['pserver']
            srvNXT = peer['srvNXT']
            print(psrv)
            print(srvNXT)
           #log.msg(1*"\n FINDNODE peer:", srvNXT)



        print(2*"\n++++++++++++","test_addcontact")
        testRQ_addcontact = {'requestType': 'addcontact'}
        testRQ_addcontact['acct'] = srvNXT
        testRQ_addcontact['handle'] = "myTestHandle"  #+ str(time.time())


        payload= self.qComp_777.make_777POST_Request(testRQ_addcontact)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )
        if 'unchanged' in testReq.text:
            self.assertTrue(True)
        else:
            self.assertTrue('pubkey' in testReq.text )


        print(2*"\n++++++++++++","test_dispcontact")
        testRQ_dispcontact = {'requestType': 'dispcontact'}
        #test_dispcontact['acct'] =
        testRQ_dispcontact['contact'] =  'myTestHandle' # "myTestHandle"  #+ str(time.time())


        payload= self.qComp_777.make_777POST_Request(testRQ_dispcontact)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('handle' in rpl777.keys() )


        print(2*"\n++++++++++++","test_RQ_removecontact")
        test_RQ_removecontact = {'requestType': 'removecontact'}
        #test_dispcontact['acct'] =
        test_RQ_removecontact['contact'] =  'myTestHandle' # "myTestHandle"  #+ str(time.time())


        payload= self.qComp_777.make_777POST_Request(test_RQ_removecontact)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )
        self.assertTrue('deleted' in testReq.text )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_telepathy(SNET_BaseTest):
    """telepathy
telepathy conducts telepathic communications (communication without requiring IP addresses to be known).
static char *telepathy[] = { (char *)telepathy_func, "telepathy", "V", "contact", "id", "type", "attach", 0 };
contact has to be in your addcontact list. Both sides must have each other as contacts for telepathy to work (but not regular messages).
id is sequenceid (-1 to set automatically)
type is the type of transfer: teleport (funds), text (message)... currently type is not required.
attach is any string (message content)
example
./BitcoinDarkd SuperNET '{"requestType":"telepathy","contact":"<privateaddr>","id":"-1","attach":"Are you thinking what I'm thinking?"}'
"""#

    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_telepathy()


    def test_telepathy(self):
        #query_json = {'attach': '', 'contact': '', 'id': '', 'requestType': 'telepathy', 'type': ''}

        print(2*"\n++++++++++++","test_telepathy")
        test_RQ_ = {'requestType': 'telepathy'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_getdb(SNET_BaseTest):
    """getdb
getdb is 'basically a low level way to do a findvalue'. getdb allows you to check the DHT store of any node remotely by verifying the contents of public.db. You can submit a DHT request and poll all nodes via getdb to make a map of which nodes received what data. This is important for debugging DHT routing.
static char *getdb[] = { (char *)getdb_func, "getdb", "V", "contact", "id", "key", "dir", "destip", 0 };
destip is the IP address of the designated node.
key is the DHT key for the store value, returned by initial store.

example getdb
./BitcoinDarkd SuperNET '{"requestType":"getdb","key":"1031470952125437106"}'
result

GETDB.({"requestType":"dbret","NXT":"6249611027680999354","key":"1031470952125437106","data":"c0ffee"}) nxtip.(167.114.2.94) {"requestType":"findnode","NXT":"11910135804814382998","time":1417778040,"key":"6249611027680999354"} search n.16 sorted mydist.0 remoteflag.0 remoteaccess.1 send_kademlia_cmd.havenode srvpubaddr or cp.0x246ab60 dest.7108754351996134253 len.826 -> 1396 send back.([["6249611027680999354", "80.41.56.181", "7777", "0"], ["8894667849638377372", "209.126.70.156", "7777", "1417655983"], ["5624143003089008155", "192.99.212.250", "7777", "1417621062"], ["2131686659786462901", "178.62.185.131", "7777", "1417701576"], ["7067340061344084047", "94.102.50.70", "7777", "1417621060"], ["2278910666471639688", "167.114.2.204", "7777", "1417621061"], ["16193842359787719847", "110.159.238.254", "54433", "1417660922"]]) to 7108754351996134253 FIND.({"result":"kademlia_findnode from.(7108754351996134253) previp.(167.114.2.171) key.(6249611027680999354) datalen.0 txid.5658681211156582719"})

"""#

    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_getdb()


    def test_getdb(self):
        #query_json = {'destip': '', 'requestType': 'getdb', 'dir': '', 'id': '', 'contact': '', 'key': ''}


        print(2*"\n++++++++++++","test_getdb")
        test_RQ_ = {'requestType': 'getdb'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_sendmessage(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def msg(self):


        MSGfrags = [
                        'Eight, sir; seven, sir;',
                        'Six, sir; five, sir;',
                        'Four, sir; three, sir;',
                        'Two, sir; one!',
                        'Tenser, said the Tensor.',
                        'Tenser, said the Tensor.',
                        'Tension, apprehension,',
                        'And dissension have begun.',
                        ]
        msg = ''
        for frag in range(randint(4,7)):
            msg += MSGfrags[randint(0,7)]
        return msg


    def runTest(self):
        self.test_sendmessage()


    def test_sendmessage(self):
        query_json = {'dest': '', 'requestType': 'sendmessage', 'msg': '', 'L': ''}

        msg = self.msg()

        null = None #  b'{"result":null}' for when null is sent back, which py doenst know

        test_RQ_getpeers = {'requestType': 'getpeers'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_getpeers)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        self.assertTrue('peers' in rpl777.keys())

        peers = rpl777['peers']
        for peer in peers[2:]:
            print(peer)
            psrv = peer['pserver']
            srvNXT = peer['srvNXT']
            print(psrv)
            print(srvNXT)
           #log.msg(1*"\n FINDNODE peer:", srvNXT)



        print(2*"\n++++++++++++","test_sendmessage")
        test_RQ_sendmessage = {'requestType': 'sendmessage'}
        test_RQ_sendmessage['dest'] = srvNXT
        test_RQ_sendmessage ['msg'] = msg


        payload= self.qComp_777.make_777POST_Request(test_RQ_sendmessage)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)



        self.assertTrue('status' in rpl777.keys() )
        self.assertTrue('sends encrypted sendmessage to' in rpl777['status'] )



    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################



class SNET_sendbinary(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def msg(self):


        MSGfrags = [
                        'Eight, sir; seven, sir;',
                        'Six, sir; five, sir;',
                        'Four, sir; three, sir;',
                        'Two, sir; one!',
                        'Tenser, said the Tensor.',
                        'Tenser, said the Tensor.',
                        'Tension, apprehension,',
                        'And dissension have begun.',
                        ]
        msg = ''
        for frag in range(randint(4,7)):
            msg += MSGfrags[randint(0,7)]
        return msg



    def runTest(self):
        self.test_sendbinary()


    def test_sendbinary(self):

        query_json = {'data': '', 'L': '', 'requestType': 'sendbinary', 'dest': ''}


        msg = self.msg()

        null = None #  b'{"result":null}' for when null is sent back, which py doenst know


        ##### getpeers
        test_RQ_getpeers = {'requestType': 'getpeers'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_getpeers)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        self.assertTrue('peers' in rpl777.keys())

        peers = rpl777['peers']
        for peer in peers[2:]:
            print(peer)
            psrv = peer['pserver']
            srvNXT = peer['srvNXT']
            print(psrv)
            print(srvNXT)
           #log.msg(1*"\n FINDNODE peer:", srvNXT)



        n1 = self.msg()
        n2 = n1.encode("utf-8")
        n2 = binascii.hexlify(n2)
        binSpam = n2.decode("utf-8")

        print(2*"\n++++++++++++","   ")
        test_RQ_sendbinary = {'requestType': 'sendbinary'}
        test_RQ_sendbinary['dest'] = srvNXT
        test_RQ_sendbinary ['data'] = binSpam


        payload= self.qComp_777.make_777POST_Request(test_RQ_sendbinary)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)



        self.assertTrue('status' in rpl777.keys() )
        self.assertTrue('sends encrypted sendmessage to' in rpl777['status'] )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


    #########################
    #########################
    #########################
    #########################
    #
    #      Teleport
    #########################
    #########################
    #########################
    #########################
    #########################



class ___Teleport():
    pass

class SNET_maketelepods(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_maketelepods()


    def test_maketelepods(self):

        #query_json = {'amount': '', 'requestType': 'maketelepods', 'coin': ''}


# {'result': 'pending SuperNET API call', 'txid': '8448558224120207202'}

        print(2*"\n++++++++++++","test_maketelepods")
        test_RQ_ = {'requestType': 'maketelepods'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################

class SNET_telepodacct(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_telepodacct()


    def test_telepodacct(self):

        #query_json = {'amount': '', 'comment': '', 'coin': '', 'contact': '', 'cmd': '', 'requestType': 'telepodacct', 'withdraw': ''}

# {'result': 'pending SuperNET API call', 'txid': '13468243516026239723'}

        print(2*"\n++++++++++++","test_telepodacct")
        test_RQ_ = {'requestType': 'telepodacct'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )

    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


class SNET_teleport(SNET_BaseTest):

    def setUp(self):
        print(" test setUp func here")
        pass

    def runTest(self):
        self.test_teleport()

    def test_teleport(self):
        #query_json = {'coin': '', 'minage': '', 'requestType': 'teleport', 'amount': '', 'contact': '', 'withdraw': ''}
		# {'result': 'pending SuperNET API call', 'txid': '12100319098835243886'}

        print(2*"\n++++++++++++","test_teleport")
        test_RQ_ = {'requestType': 'teleport'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )



    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################


    #########################
    #########################
    #########################
    #########################
    #
    #     Privatebet
    #########################
    #########################
    #########################
    #########################
    #########################





class ___Privatebet():
    pass

class SNET_lotto(SNET_BaseTest, ):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_lotto()


    def test_lotto(self):

        #query_json = {'rel': '', 'stop': '', 'requestType': 'pricedb', 'exchange': '', 'base': ''}

# {'error': 'bad pricedb paramater'}


        null = None

        print(2*"\n++++++++++++","test_lotto")
        test_RQ_ = {'requestType': 'lotto'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################



    #########################
    #########################
    #########################
    #########################
    #
    #     Tradebot
    #########################
    #########################
    #########################
    #########################
    #########################




class ___Tradebot():
    pass



class SNET_allsignals(SNET_BaseTest,  ):
    """
   test_allsignals
query json is:  {'requestType': 'allsignals'}

~~~~~~~~~~~~
~~~~~~~~~~~~ SuperNET rpl777y:

 {'signals': [{'scale': 'price', 'signal': 'firstbid'}, {'scale': 'price', 'signal': 'firstask'}, {'scale': 'price', 'signal': 'lowbid'}, {'scale': 'price', 'signal': 'highask'}, {'scale': 'price', 'signal': 'highbid'}, {'scale': 'price', 'signal': 'lowask'}, {'scale': 'price', 'signal': 'lowbid'}, {'scale': 'price', 'signal': 'lastask'}, {'scale': 'price', 'signal': 'arbbid'}, {'scale': 'price', 'signal': 'arbask'}, {'scale': 'price', 'signal': 'virtbid'}, {'scale': 'price', 'signal': 'virtask'}, {'scale': 'price', 'signal': 'avebid'}, {'scale': 'price', 'signal': 'aveask'}, {'scale': 'price', 'signal': 'median'}, {'scale': 'price', 'signal': 'aveprice'}, {'scale': 'price', 'n': 4, 'signal': 'ohlc'}, {'scale': 'positive', 'signal': 'volume'}]}
.
----------------------------------------------------------------------
Ran 1 test in 0.124s

OK

    """#
    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_allsignals()


    def test_allsignals(self):

        rpl777 = self.allsignals( )

        self.assertTrue('signals' in rpl777.keys() )
        self.assertIsInstance(rpl777['signals'], list  )

    def allsignals(self):
        null = None
        print(2*"\n++++++++++++","test_allsignals")
        test_RQ_allsignals = {'requestType': 'allsignals'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_allsignals)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        return rpl777



    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################




class SNET_getsignal(SNET_BaseTest,  ):
    """
        test_getsignal
    query json is:  {'resolution': '', 'exchange': '', 'width': '', 'signal': '', 'requestType': 'getsignal', 'baseid': '', 'start': '', 'relid': '', 'rel': '', 'base': ''}

    ~~~~~~~~~~~~
    ~~~~~~~~~~~~
    ~~~~~~~~~~~~
    ~~~~~~~~~~~~
    ~~~~~~~~~~~~ SuperNET rpl777y:

     {'error': 'too wide'}
    F

    """#
    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_getsignal()


    def test_getsignal(self):

        #query_json = {'requestType': 'getquotes', 'base': '', 'rel': '', 'oldest': '', 'exchange': ''}

        null = None
        print(2*"\n++++++++++++","test_getsignal")
        test_RQ_ = {'requestType': 'getsignal'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )

#
#
# class SNET_getsignal_obs(SNET_BaseTest, ):
#
#     def setUp(self):
#         print(" test getsignal setUp func here")
#         pass
#
#     def runTest(self):
#         self.test_getsignal()
#
#     def test_getsignal(self):
#
#         print("##", self.apicall({'requestType': 'getsignal'}))
#         rpl777 = self.apicall({'requestType': 'getsignal'})
#
#         self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################



class SNET_tradebot(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_tradebot()


    def test_tradebot(self):
        #query_json = {'code': '', 'requestType': 'tradebot'}

        null = None
# {'result': 'invalid tradebot request'}



        print(2*"\n++++++++++++","test_tradebot")
        test_RQ_ = {'requestType': 'tradebot'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################




    #########################
    #########################
    #########################
    #########################
    #
    #     plugins
    #########################
    #########################
    #########################
    #########################
    #########################

class ___plugins():
    pass





class SNET_checkmessages(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def msg(self):


        MSGfrags = [
                        'Eight, sir; seven, sir;',
                        'Six, sir; five, sir;',
                        'Four, sir; three, sir;',
                        'Two, sir; one!',
                        'Tenser, said the Tensor.',
                        'Tenser, said the Tensor.',
                        'Tension, apprehension,',
                        'And dissension have begun.',
                        ]
        msg = ''
        for frag in range(randint(4,7)):
            msg += MSGfrags[randint(0,7)]
        return msg




    def runTest(self):
        self.test_checkmsg()


    def test_checkmsg(self):


        #SENDMESSAGE
        query_json = {'dest': '', 'requestType': 'sendmessage', 'msg': '', 'L': ''}

        msg = self.msg()

        null = None #  b'{"result":null}' for when null is sent back, which py doenst know

        test_RQ_ = {'requestType': 'getpeers'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        self.assertTrue('peers' in rpl777.keys())

        peers = rpl777['peers']
        for peer in peers[2:]:
            print(peer)
            psrv = peer['pserver']
            srvNXT = peer['srvNXT']
            print(psrv)
            print(srvNXT)
           #log.msg(1*"\n FINDNODE peer:", srvNXT)



        print(2*"\n++++++++++++","test_sendmessage")
        test_RQ_sendmessage = {'requestType': 'sendmessage'}
        test_RQ_sendmessage['dest'] = srvNXT
        test_RQ_sendmessage ['msg'] = msg


        payload= self.qComp_777.make_777POST_Request(test_RQ_sendmessage)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        query_json = {'sender': '', 'requestType': 'checkmessages'}

        null = None #  b'{"result":null}' for when null is sent back, which py doenst know

        for peer in peers[2:]:
                    print(peer)
                    psrv = peer['pserver']
                    srvNXT = peer['srvNXT']
                    print(psrv)
                    print(srvNXT)
                   #log.msg(1*"\n FINDNODE peer:", srvNXT)


        print(2*"\n++++++++++++","test_checkmessages")
        testRQ_checkmessages = {'requestType': 'checkmessages'}
        testRQ_checkmessages['sender'] = srvNXT #= peer['srvNXT']

        payload= self.qComp_777.make_777POST_Request(testRQ_checkmessages)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################



class SNET_syscall(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass

    def runTest(self):
        self.test_syscall()


    def test_syscall(self):
        #query_json = {'name': '', 'requestType': 'syscall', 'cmd': ''}

        null = None #  b'{"result":null}' for when null is sent back, which py doenst know

        print(2*"\n++++++++++++","test_syscall")
        test_RQ_ = {'requestType': 'syscall'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}

        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )


    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################



class SNET_passthru(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_passthru()


    def test_passthru(self):
        #query_json = {'method': '', 'requestType': 'passthru', 'coin': '', 'params': ''}
        null = None
        print(2*"\n++++++++++++","test_passthru")
        test_RQ_ = {'requestType': 'passthru'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        if 'error' in rpl777.keys():
            self.assertTrue(False)
            print(2*"\n~~~~~~~~~~~~","error in SuperNET rpl777y:\n\n", rpl777)
        else:
            self.assertTrue('result' in rpl777.keys() )



    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################



class SNET_remote(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_remote()


    def test_remote(self):
        #query_json = {'method': '', 'coin': '', 'tag': '', 'result': '', 'requestType': 'remote'}
        null = None
        print(2*"\n++++++++++++","test_remote")
        test_RQ_ = {'requestType': 'remote'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        if 'error' in rpl777.keys():
            self.assertTrue(False)
            print(2*"\n~~~~~~~~~~~~","error in SuperNET rpl777y:\n\n", rpl777)
        else:
            self.assertTrue('result' in rpl777.keys() )




    def test_APICALL(self):
        """

        """ #
        rpl777 = self.getpeers()
        self.assertTrue('peers' in rpl777.keys())


    def APICALL(self):
        null=None
        print(2*"\n++++++++++++","test_APICALL")
        test_RQ_APICALL = {'requestType': 'APICALL'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_APICALL)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777
###############################################
###############################################
###############################################
###############################################
###############################################



    #########################
    #########################
    #########################
    #########################
    #
    #     InstantDEX
    #########################
    #########################
    #########################
    #########################
    #########################



class ___InstantDex():
    """
orderbooks are created dynamically when placebid or placeask is called. this is then sent to the network as bid or ask API calls with the price/volume pair changed to base and rel satoshi amounts for the assets.

allorderbooks returns an array of, yes you guess it!, all the orderbooks

orderbook returns, yes!, an orderbook with base -> rel. So the base NXT, rel BTC orderbook is NXT/BTC
but you can ask for it with base BTC and rel NXT and it will return it with the prices as BTC/NXT

a bunch of gory details regarding asset decimal places and other mundane things, but in my tests it is propagating pretty fast to other nodes. still need to get more timing results to know if I need to optimize it more.

now that the orderbooks are back online, next up is ordermatching. This is pretty tricky as I need to make it do an atomic swap of any two assets, with NXT itself treated as a special case asset. Good thing this was done last summer, but still need to get it ported into the new codebase and get it debugged.

I remember it was quite touchy, so I will plan for just achieving this automated orderfilling triggered with a makeoffer API. it actually needs at least two more internal ones to match the state transitions.

At that point, the low level InstantDEX API would basically be done for asset<->asset and other than supporting the GUI port to use this, I dont foresee too much more at this level. However, this is only the lowest level. After this step I need to add another layer for the tradebots. But I like to just do one step at a time as often when I do that next step I can see a bit better what is best to do next


char *assetmap[][2] =
{
    { "5527630", "NXT" },
    { "17554243582654188572", "BTC" },
    { "4551058913252105307", "BTC" },
    { "12659653638116877017", "BTC" },
    { "11060861818140490423", "BTCD" },
    { "6918149200730574743", "BTCD" },
    { "13120372057981370228", "BITS" },
    { "2303962892272487643", "DOGE" },
    { "16344939950195952527", "DOGE" },
    { "6775076774325697454", "OPAL" },
    { "7734432159113182240", "VPN" },
    { "9037144112883608562", "VRC" },
    { "1369181773544917037", "BBR" },
    { "17353118525598940144", "DRK" },
    { "2881764795164526882", "LTC" },
    { "7117580438310874759", "BC" },
    { "275548135983837356", "VIA" },
};


"""#
    pass




##############################################
##############################################
#
#	InstantDEX Tests
#
#
##############################################
##############################################

class SNET_orderbook(SNET_BaseTest, ):
    """
             ./uTest1.py SNET_orderbook
         test setUp func here
        query json is:  {'duration': '', 'relid': '5527630', 'baseamount': '', 'automatch': '', 'gui': '', 'timestamp': '', 'price': '0.014', 'volume': '1.00', 'minperc': '', 'baseid': '17554243582654188572', 'requestType': 'placeask', 'relamount': ''}

        ++++++++++++
        ++++++++++++ orderbook
        query json is:  {'allfields': '', 'rel': '', 'base': '', 'maxdepth': '', 'baseid': '17554243582654188572', 'requestType': 'orderbook', 'relid': '5527630', 'oldest': '', 'gui': ''}

        ~~~~~~~~~~~~
        ~~~~~~~~~~~~ SuperNET rpl777y:

         {'obookid': '17554243582651323474', 'NXT': '10501328530345129240', 'timestamp': 1429679438, 'asks': [{'price': '0.00014000', 'volume': '1.00001000'}, {'price': '0.01400000', 'volume': '1.00000000'}, {'price': '0.01400000', 'volume': '1.00000000'}], 'bids': [{'price': '0.01400000', 'volume': '1.00000000'}], 'baseid': '17554243582654188572', 'maxdepth': 0, 'relid': '5527630', 'pair': 'BTC/NXT'}
        .
        ----------------------------------------------------------------------
        Ran 1 test in 0.384s

        OK

    """


    def setUp(self):
        print(" test setUp func here")
        pass

    def runTest(self):
        #self.test_orderbook_empty()
        self.test_orderbook()


    def test_orderbook_empty(self):
        """ test_orderbook_empty

            call sequence:

            1. orderbook

            ---------

            asserts

            1.  reply has key 'error'
            2.  error message is 'empty orderbook'


        """
        baseid = '11060861818140490423'
        relid = '17554243582654188572'
        rpl777 = self.orderbook(baseid, relid) # param passing can be done a bit better here

        self.assertTrue(rpl777['error']=='empty orderbook')
        self.assertTrue('error' in rpl777.keys() )


    def test_orderbook(self):
        """ test_orderbook

            call sequence:

            1. place order
            2. orderbook

            ---------

            asserts

            1.  reply has correct orderbook with key 'NXT'


        """
        price = '0.014'
        volume = '1.00'
        baseid = '17554243582654188572'
        relid = '5527630'

        testRQ_placeask = {'requestType': 'placeask'}
        payload= self.qComp_777.make_777POST_Request(testRQ_placeask)
        payload['volume'] = volume
        payload['price'] =  price
        payload['baseid'] = baseid
        payload['relid'] =  relid
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        #rpl777 = eval(testReq.text)

        rpl777 = self.orderbook(baseid, relid) # param passing can be done a bit better here
        self.assertTrue('NXT' in rpl777.keys() )



    def orderbook(self, baseid, relid):
        null = None
        print(2*"\n++++++++++++","orderbook")
        test_RQ_orderbook = {'requestType': 'orderbook'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_orderbook)
        payload['baseid'] = baseid
        payload['relid'] =  relid
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)
        return rpl777

    #{"requestType":"placeask","baseid":"11060861818140490423","relid":"17554243582654188572","volume":"80","price":"0.0065"}'
    #{"result":"success","txid":"15021359626299573695"}

    #
    #     # http://docs.pylonsproject.org/en/latest/community/testing.html
    # Tips for Avoiding Bad Unit Tests
    #
    # Some folks have drunk the “don’t repeat yourself” KoolAid: we agree that not repeating code is a virtue in most cases, but unit test code is an exception: cleverness in a test both obscures the intent of the test and makes a subsequent failure massively harder to diagnose.
    # Others want to avoid writing both tests and documentation: they try to write test cases (almost invariably as “doctests”) which do the work of real tests, while at the same time trying to make “readable” docs.
    # Most of the issues involved with the first motive are satisfactorily addressed later in this document: refusing to share code between test modules makes most temptations to cleverness go away. Where the temptation remains, the cure is to look at an individual test and ask the following questions:
    #
    # Is the intent of the test clearly explained by the name of the testcase?
    #
    # Does the test follow the “canonical” form for a unit test? I.e., does it:
    # set up the preconditions for the method/function being tested.
    # call the method/function exactly one time, passing in the values established in the first step.
    # make assertions about the return value, and/or any side effects.
    # do absolutely nothing else.


class SNET_placeask(SNET_BaseTest,  ):
    """

       ./uTest1.py SNET_placeask
     test setUp func here
    query json is:  {'timestamp': '', 'relamount': '', 'requestType': 'placeask', 'volume': '1.00', 'baseid': '17554243582654188572', 'minperc': '', 'price': '0.014', 'duration': '', 'relid': '5527630', 'gui': '', 'baseamount': '', 'automatch': ''}
    test_placeask:  {'timestamp': 1429429594, 'baseamount': '100000000', 'relamount': '1400000', 'requestType': 'ask', 'base': 'BTC', 'NXT': '10501328530345129240', 'minperc': 75, 'baseid': '17554243582654188572', 'price': 0.014, 'quoteid': '6191161196027104713', 'duration': 3600, 'exchange': 'InstantDEX', 'age': 0, 'relid': '5527630', 'rel': 'NXT', 'askoffer': 1, 'volume': 1, 'offerNXT': '10501328530345129240'}
    query json is:  {'timestamp': '', 'relamount': '', 'requestType': 'placeask', 'volume': '1.00001', 'baseid': '17554243582654188572', 'minperc': '', 'price': '0.00014', 'duration': '', 'relid': '5527630', 'gui': '', 'baseamount': '', 'automatch': ''}
    test_placeask_a:  {'timestamp': 1429429594, 'baseamount': '100001000', 'relamount': '14000', 'requestType': 'ask', 'base': 'BTC', 'NXT': '10501328530345129240', 'minperc': 75, 'baseid': '17554243582654188572', 'price': 0.00014, 'quoteid': '18108422846743312101', 'duration': 3600, 'exchange': 'InstantDEX', 'age': 0, 'relid': '5527630', 'rel': 'NXT', 'askoffer': 1, 'volume': 1.00001, 'offerNXT': '10501328530345129240'}
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.977s

    OK


        """#
    def setUp(self):
        print(" test setUp func here")
        pass

    def runTest(self):
        self.test_placeask()
        #self.test_placeask_a()



    def test_placeask(self):
        """ test_placeask

            call sequence:

            1. placeask with fixed params


            ---------

            asserts

            1.  reply has key 'quoteid'


        """
        price = '0.014'
        volume = '1.00'
        baseid = '17554243582654188572'
        relid = '5527630'
        rpl777 = self.placeask(volume,price,baseid,relid)
        print("test_placeask: ", rpl777)
        self.assertTrue('quoteid' in rpl777.keys() )

    def test_placeask_a(self): #??
        price = '0.00014'
        volume = '1.00001'
        baseid = '17554243582654188572'
        relid = '5527630'
        rpl777 = self.placeask(volume,price,baseid,relid)
        print("test_placeask_a: ", rpl777)
        self.assertTrue('quoteid' in rpl777.keys() )

    def placeask(self, volume, price, baseid, relid):
        """ args for these calls can be extended w/ defaults   """#
        testRQ_placeask = {'requestType': 'placeask'}
        payload= self.qComp_777.make_777POST_Request(testRQ_placeask)
        payload['volume'] = volume
        payload['price'] =  price
        payload['baseid'] = baseid
        payload['relid'] =  relid
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        return rpl777

        #{"requestType":"placeask","baseid":"11060861818140490423","relid":"17554243582654188572","volume":"80","price":"0.0065"}'
        #{"result":"success","txid":"15021359626299573695"}




class SNET_placebid(SNET_BaseTest, ):
    """ ++++++++++++
        ++++++++++++ test_placebid
        query json is:  {'timestamp': '', 'requestType': 'placebid', 'duration': '', 'baseid': '17554243582654188572', 'price': '0.014', 'gui': '', 'minperc': '', 'volume': '1.00', 'baseamount': '', 'relid': '5527630', 'automatch': '', 'relamount': ''}

        ~~~~~~~~~~~~
        ~~~~~~~~~~~~ SuperNET rpl777y:

         {'askoffer': 0, 'base': 'BTC', 'NXT': '10501328530345129240', 'timestamp': 1429356528, 'requestType': 'bid', 'duration': 3600, 'minperc': 75, 'baseid': '17554243582654188572', 'price': 0.014, 'age': 0, 'volume': 1, 'exchange': 'InstantDEX', 'baseamount': '100000000', 'relamount': '1400000', 'rel': 'NXT', 'quoteid': '4435496911217030133', 'offerNXT': '10501328530345129240', 'relid': '5527630'}
        .
        ----------------------------------------------------------------------
        Ran 1 test in 0.391s

        OK

    """

    def setUp(self):
        print("test placebid")

    def runTest(self):
        self.test_placebid()
        #self.params()

    def params(self):
        price = '0.00014'
        volume = '1.00001'

        baseid = '17554243582654188572'
        relid = '5527630'
        self.test_placebid_a(volume,price,baseid,relid)

        price = '0.00014'
        volume = '1.00001'

        baseid = '17554243582654188572'
        relid = '5527630'
        self.test_placebid_a(volume,price,baseid,relid)

    def test_placebid(self):
        """ test_placebid

            call sequence:

            1. placebid  with fixed params


            ---------

            asserts

            1.  reply has key 'quoteid'


        """
        null = None
        price = '0.014'
        volume = '1.00'

        baseid = '17554243582654188572'
        relid = '5527630'
        rpl777 = self.placebid(volume,price,baseid,relid)
        #print(apiResponse);
        self.assertTrue('quoteid' in rpl777.keys() )

    def test_placebid_a(self,volume,price,baseid,relid):

        rpl777 = self.placebid(volume,price,baseid,relid)
        self.assertTrue('quoteid' in rpl777.keys() )



    def placebid(self,volume,price,baseid,relid):
        null = None
        #query_json = {'price': '', 'volume': '', 'requestType': 'placebid', 'baseid': '', 'relid': ''}

        print(2*"\n++++++++++++","test_placebid")
        testRQ_placebid = {'requestType': 'placebid'}


        payload= self.qComp_777.make_777POST_Request(testRQ_placebid)

        payload['volume'] = volume
        payload['price'] =  price
        payload['baseid'] = baseid
        payload['relid'] =  relid

        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        return rpl777









class SNET_allorderbooks(SNET_BaseTest, ):
    """
   ++++++++++++
++++++++++++ test_allorderbooks
query json is:  {'requestType': 'allorderbooks'}

~~~~~~~~~~~~
~~~~~~~~~~~~ SuperNET rpl777y:

 {'orderbooks': [{'rel': 'NXT', 'exchange': 'InstantDEX', 'relid': '5527630', 'type': 'bids', 'baseid': '17554243582654188572', ....

 .
----------------------------------------------------------------------
Ran 1 test in 0.214s

OK


    """#
    def setUp(self):
        print(" test setUp func here")
        pass

    def runTest(self):
        self.test_allorderbooks()

    def test_allorderbooks(self):
        """ test_placebid

            call sequence:

            1.


            ---------

            asserts

            1.  reply has


        """
        rpl777 = self.allorderbooks()
        self.assertTrue('orderbooks' in rpl777.keys() )


    def allorderbooks(self):
        null = None

        print(2*"\n++++++++++++","test_allorderbooks")
        test_RQ_allorderbooks = {'requestType': 'allorderbooks'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_allorderbooks)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        return rpl777






class SNET_openorders(SNET_BaseTest, ):
    """
       ++++++++++++
    ++++++++++++ test_openorders
    query json is:  {'requestType': 'openorders'}

    ~~~~~~~~~~~~
    ~~~~~~~~~~~~ SuperNET rpl777y:

     {'openorders': [{'NXT': '10501328530345129240', 'offerNXT': '10501328530345129240', 'rel': 'NXT', 'price': 0.014, 'askoffer': 0, 'exchange': 'InstantDEX', 'base': 'BTC', 'iQ': '139904608199392', 'relamount': '1400000', 'relid': '5527630', 'baseamount': '100000000', 'age': 713, 'duration': 3600, 'baseid': '17554243582654188572', 'quoteid': '4435496911217030133', 'volume': 1, 'timestamp': 1429356528, 'requestType': 'makeoffer3', 'minperc': 75}, {'NXT': '10501328530345129240', 'offerNXT': '10501328530345129240', 'rel': 'NXT', 'price': 100, 'askoffer': 1, 'exchange': 'InstantDEX', 'base': '1000BURST', 'iQ': '139904602575664', 'relamount': '220000000000', 'relid': '5527630', 'baseamount': '2200000000', 'age': 2195, 'duration': 3600, 'baseid': '251006016744564741', 'quoteid': '17155999699314532503', 'volume': 22, 'timestamp': 1429355046, 'requestType': 'makeoffer3', 'minperc': 75}, {'NXT': '10501328530345129240', 'offerNXT': '10501328530345129240', 'rel': 'NXT', 'price': 100, 'askoffer': 1, 'exchange': 'InstantDEX', 'base': '1000BURST', 'iQ': '139904602575752', 'relamount': '220000000000', 'relid': '5527630', 'baseamount': '2200000000', 'age': 2226, 'duration': 3600, 'baseid': '251006016744564741', 'quoteid': '14797648200742204788', 'volume': 22, 'timestamp': 1429355015, 'requestType': 'makeoffer3', 'minperc': 75}, {'NXT': '10501328530345129240', 'offerNXT': '10501328530345129240', 'rel': 'NXT', 'price': 100, 'askoffer': 1, 'exchange': 'InstantDEX', 'base': '1000BURST', 'iQ': '139904602575840', 'relamount': '220000000000', 'relid': '5527630', 'baseamount': '2200000000', 'age': 2236, 'duration': 3600, 'baseid': '251006016744564741', 'quoteid': '17475451133874014289', 'volume': 22, 'timestamp': 1429355005, 'requestType': 'makeoffer3', 'minperc': 75}, {'NXT': '10501328530345129240', 'offerNXT': '10501328530345129240', 'rel': 'NXT', 'price': 100, 'askoffer': 1, 'exchange': 'InstantDEX', 'base': '1000BURST', 'iQ': '139904602576192', 'relamount': '220000000000', 'relid': '5527630', 'baseamount': '2200000000', 'age': 2790, 'duration': 3600, 'baseid': '251006016744564741', 'quoteid': '8308605579349557750', 'volume': 22, 'timestamp': 1429354451, 'requestType': 'makeoffer3', 'minperc': 75}]}
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.150s

    OK


        """#


    def setUp(self):
        print(" test setUp func here")
        pass

    def runTest(self):
        self.test_openorders()

    def test_openorders(self):
        """ test_openorders

            call sequence:

            1.


            ---------

            asserts

            1.  reply has


        """

        openorders = self.openorders()


        self.assertTrue('openorders' in openorders.keys() )

        openordersLi=openorders['openorders']
        for order in openordersLi:
            print("\n",order)



    def openorders(self):
        null = None
        print(2*"\n++++++++++++","test_openorders")
        test_RQ_openorders = {'requestType': 'openorders'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_openorders)
        print("query json is: ", payload)
        #headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        #print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        return rpl777



class SNET_respondtx(SNET_BaseTest, ):
    """

        respondtx and processutx are internal trade negotiation API's and can be ignored, there will be other internal API calls too, like "bid" and "ask"

    """#

    def setUp(self):
        print(" test setUp func here")
        pass

    def runTest(self):
        self.test_respondtx()

    def test_respondtx(self):
        """ test_respondtx

            call sequence:

            1.


            ---------

            asserts

            1.  reply has


        """
        rpl777 = self.respondtx()
        self.assertTrue('result' in rpl777.keys() )

    def respondtx(self):
        null = None
        print(2*"\n++++++++++++","test_respondtx")
        test_RQ_respondtx = {'requestType': 'respondtx'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_respondtx)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)
        return rpl777




class SNET_bid(SNET_BaseTest,):
    """++++++++++++
        ++++++++++++ test_bid
        query json is:  {'type': '', 'baseid': '11060861818140490423', 'baseamount': '', 'relid': '17554243582654188572', 'timestamp': '', 'minperc': '', 'price': '1', 'volume': '1', 'requestType': 'bid', 'duration': '', 'gui': '', 'relamount': '', 'automatch': ''}

        ~~~~~~~~~~~~
        ~~~~~~~~~~~~ SuperNET rpl777y:

         {'baseid': '11060861818140490423', 'duration': 3600, 'exchange': 'InstantDEX', 'relid': '17554243582654188572', 'rel': 'BTC', 'timestamp': 1429359243, 'minperc': 75, 'quoteid': '5273789868954063273', 'age': 0, 'price': 1, 'baseamount': '100000000', 'volume': 1, 'requestType': 'bid', 'NXT': '10501328530345129240', 'askoffer': 0, 'base': 'BTCD', 'relamount': '100000000', 'offerNXT': '10501328530345129240'}
        .
        ----------------------------------------------------------------------
        Ran 1 test in 0.328s

        OK

        """#

    def setUp(self):
        print(" test setUp func here")
        pass

    def runTest(self):
        self.test_bid()

	# {'txid': '14590711946411376684', 'result': 'success'}
	# static char *bid[] = { (char *)bid_func, "bid", "V", "baseid", "relid", "volume", "price", "timestamp", "baseamount", "relamount", "type", 0 };
    def test_bid(self):
        """ test_bid

            call sequence:

            1.


            ---------

            asserts

            1.  reply has


        """
        baseid = '11060861818140490423'
        relid = '17554243582654188572'
        rpl777 = self.bid(baseid, relid)
        if 'error' in rpl777:
            print(2*"\n~~~~~~~~~~~~","error in SuperNET rpl777y:\n", rpl777)
            self.assertTrue(False)
        else:
            self.assertTrue('exchange' in rpl777.keys() )


    def bid(self, baseid, relid):
        null = None

        test_RQ_bid = {'requestType': 'bid'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_bid)
        payload['volume'] = '1'
        payload['price'] =  '1'
        payload['baseid'] = baseid
        payload['relid'] =  relid

        print(2*"\n++++++++++++","test_bid")
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)
        return rpl777

        #ask and bid are internal calls
        #only use them if you are debugging internal calls
        # static char *ask[] = { (char *)ask_func, "ask", "V", "baseid", "relid", "volume", "price", "timestamp", "baseamount", "relamount", "type", 0 };
        #{'txid': '11713518629359241926', 'result': 'success'}



class SNET_ask(SNET_BaseTest,):
    """

    ++++++++++++
    ++++++++++++ test_ask
    query json is:  {'minperc': '', 'timestamp': '', 'relamount': '', 'type': '', 'baseamount': '', 'requestType': 'ask', 'duration': '', 'baseid': '11060861818140490423', 'volume': '1', 'relid': '17554243582654188572', 'automatch': '', 'gui': '', 'price': '1'}

    ~~~~~~~~~~~~
    ~~~~~~~~~~~~ SuperNET rpl777y:

     {'minperc': 75, 'relid': '17554243582654188572', 'exchange': 'InstantDEX', 'relamount': '100000000', 'offerNXT': '10501328530345129240', 'rel': 'BTC', 'askoffer': 1, 'timestamp': 1429359379, 'requestType': 'ask', 'baseamount': '100000000', 'quoteid': '2136393601792993271', 'duration': 3600, 'NXT': '10501328530345129240', 'volume': 1, 'base': 'BTCD', 'age': 0, 'price': 1, 'baseid': '11060861818140490423'}
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.271s

    OK


        """#

    def setUp(self):
        print(" test setUp func here")
        pass

    def runTest(self):
        self.test_ask()

	# {'txid': '14590711946411376684', 'result': 'success'}
	# static char *ask[] = { (char *)ask_func, "ask", "V", "baseid", "relid", "volume", "price", "timestamp", "baseamount", "relamount", "type", 0 };
    def test_ask(self):
        """ test_ask

            call sequence:

            1.


            ---------

            asserts

            1.  reply has


        """
        baseid = '11060861818140490423'
        relid = '17554243582654188572'
        rpl777 = self.ask(baseid, relid)
        if 'error' in rpl777:
            print(2*"\n~~~~~~~~~~~~","error in SuperNET rpl777y:\n", rpl777)
            self.assertTrue(False)
        else:
            self.assertTrue('exchange' in rpl777.keys() )



    def ask(self, baseid, relid):
        null = None

        test_RQ_ask = {'requestType': 'ask'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_ask)

        payload['volume'] = '1'
        payload['price'] =  '1'
        payload['baseid'] = baseid
        payload['relid'] =  relid

        print(2*"\n++++++++++++","test_ask")

        print("query json is: ", payload)

        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        return rpl777


class SNET_cancelquote(SNET_BaseTest, ):
    """
        ++++++++++++
    ++++++++++++ test_cancelquote
    query json is:  {'quoteid': '123', 'requestType': 'cancelquote'}

    ~~~~~~~~~~~~
    ~~~~~~~~~~~~ SuperNET rpl777y: {'result': 'you can only cancel your InstantDEX orders'}
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.140s

    OK


        """#

    def setUp(self):
        print(" test cancelquote setUp func here")
        pass

    def runTest(self):
        self.test_cancelquote()

    def test_cancelquote(self):
        """ test_cancelquote

            call sequence:

            1.


            ---------

            asserts

            1.  reply has


        """
        qId = '123'
        rpl777 = self.cancelquote(qId)
        self.assertTrue('result' in rpl777.keys() )

    def cancelquote(self,qId):
        print(2*"\n++++++++++++","test_cancelquote")
        test_RQ_cancelquote = {'requestType': 'cancelquote'}
        test_RQ_cancelquote['quoteid'] = qId
        payload= self.qComp_777.make_777POST_Request(test_RQ_cancelquote)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        return rpl777



class SNET_lottostats(SNET_BaseTest, ):
    """
         ./uTest1.py SNET_lottostats
     test lottostats setUp func here

    ++++++++++++
    ++++++++++++ lottostats call
    query json is:  {'timestamp': '', 'requestType': 'lottostats'}

    ~~~~~~~~~~~~
    ~~~~~~~~~~~~ SuperNET rpl777y:

     {'NXT': '10501328530345129240', 'odds': '0.00', 'result': 'lottostats', 'totaltickets': '200', 'numtickets': '0', 'topMM': '13632947951045332845'}
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.263s

    OK

    """#
    def setUp(self):
        print(" test lottostats setUp func here")
        pass

    def runTest(self):
        self.test_lottostats()

    def test_lottostats(self):
        """ test_lottostats

            call sequence:

            1.


            ---------

            asserts

            1.  reply has


        """
        rpl777 = self.lottostats()
        self.assertTrue('result' in rpl777.keys() )
        self.assertTrue('numtickets' in rpl777.keys() )
        self.assertTrue(rpl777['result']  == 'lottostats')

    def lottostats(self):
        null = None
        print(2*"\n++++++++++++","lottostats call")
        test_RQ_lottostats = {'requestType': 'lottostats'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_lottostats)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)
        return rpl777



class SNET_tradehistory(SNET_BaseTest, ):
    """
       azure@boxfish:~/workbench/nxtDev/snappy$ ./uTest1.py SNET_tradehistory
     test tradehistory setUp func here

    ++++++++++++
    ++++++++++++ tradehistory call
    query json is:  {'requestType': 'tradehistory', 'timestamp': ''}

    ~~~~~~~~~~~~
    ~~~~~~~~~~~~ SuperNET rpl777y:

     {}
    F
    ======================================================================
    FAIL: runTest (__main__.SNET_tradehistory)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "./uTest1.py", line 3741, in runTest
        self.test_tradehistory()
      File "./uTest1.py", line 3746, in test_tradehistory
        self.assertTrue('result' in rpl777.keys() )
    AssertionError: False is not true

    ----------------------------------------------------------------------
    Ran 1 test in 0.181s

    FAILED (failures=1)

    """#
    def setUp(self):
        print(" test tradehistory setUp func here")
        pass

    def runTest(self):
        self.test_tradehistory()


    def test_tradehistory(self):
        """ test_tradehistory

            call sequence:

            1.


            ---------

            asserts

            1.  reply has


        """
        rpl777 = self.tradehistory()
        self.assertTrue('result' in rpl777.keys() )

    def tradehistory(self):
        null = None
        print(2*"\n++++++++++++","tradehistory call")
        test_RQ_tradehistory = {'requestType': 'tradehistory'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_tradehistory)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)
        return rpl777




class SNET_jumptrades(SNET_BaseTest, ):
    """
        ./uTest1.py SNET_jumptrades
     test jumptrades setUp func here

    ++++++++++++
    ++++++++++++ jumptrades call
    query json is:  {'requestType': 'jumptrades'}

    ~~~~~~~~~~~~
    ~~~~~~~~~~~~ SuperNET rpl777y:

     {}
    F


    """#
    def setUp(self):
        print(" test jumptrades setUp func here")
        pass

    def runTest(self):
        self.test_jumptrades()

    def test_jumptrades(self):
        """ test_jumptrades

            call sequence:

            1.


            ---------

            asserts

            1.  reply has


        """
        rpl777 = self.jumptrades( )
        self.assertTrue('result' in rpl777.keys() )

    def jumptrades(self):
        null = None
        print(2*"\n++++++++++++","jumptrades call")
        test_RQ_jumptrades = {'requestType': 'jumptrades'}
        payload = self.qComp_777.make_777POST_Request(test_RQ_jumptrades)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)
        return rpl777



class SNET_makeoffer(SNET_BaseTest, ):

    def setUp(self):
        print("test makeoffer")
        pass

    def runTest(self):
        self.test_makeoffer_a()

    def test_makeoffer_a(self):
        null = None
        baseid = '11060861818140490423'
        relid = '5527630'

        #Max NXT Amount
        maxAmount=50

        orderbookResponse = self.orderbook(baseid,relid)
        print('\nCheck orderbook\n')
        print(orderbookResponse['bids'][0],'\n')

        #get first bid
        query_json = orderbookResponse['bids'][0]

        query_json['perc']=100
        query_json['askoffer']=1

        totalAmount = orderbookResponse['bids'][0]['volume']*orderbookResponse['bids'][0]['price']

        print(totalAmount, orderbookResponse['bids'][0]['rel'])

        if(totalAmount<maxAmount):
            print('ok total Amount of Order is in Range. Proceeding.\n')
            self.apicall(query_json)

#-----------------> go to makeoffer3 from makeoffer here!
#

#-----------------> go to makeoffer3 from makeoffer here!
#

#-----------------> go to makeoffer3 from makeoffer here!
#

#-----------------> go to makeoffer3 from makeoffer here!
#


class SNET_makeoffer3(SNET_BaseTest):
    """
       static char *makeoffer3[] = { (char *)makeoffer3_func, "makeoffer3", "V", "baseid", "relid", "quoteid", "perc", "deprecated", "baseiQ", "reliQ", "askoffer", "price", "volume", "exchange", "baseamount", "relamount", "offerNXT", "minperc", "jumpasset", 0 };


    """#
    baseid=0
    if(sys.argv[2:]):
        baseid = sys.argv[2:]
    
    SNET_orderbook = SNET_orderbook

    def setUp(self):
        print(" test setUp func here")
        pass

    def runTest(self):
        self.test_makeoffer3()


    def test_makeoffer3(self):
        null = None
        if(self.baseid==0):
            baseid = self.baseid = '11060861818140490423'
        relid = '5527630'

        #Max NXT Amount
        maxAmount=15

        orderbookResponse = self.SNET_orderbook.orderbook(self, baseid,relid)
        print('\nCheck orderbook\n')
        print(orderbookResponse['asks'][0],'\n')

        #get first ask
        query_json = orderbookResponse['asks'][0]

        query_json['perc']=100
        query_json['askoffer']=1
        
        totalAmount = ((orderbookResponse['asks'][0]['volume']*orderbookResponse['asks'][0]['price'])/100)*query_json['perc']
        
        while(totalAmount>maxAmount):
            query_json['perc']-=1
            totalAmount = ((orderbookResponse['asks'][0]['volume']*orderbookResponse['asks'][0]['price'])/100)*query_json['perc']
        
        print('Trade will be a total of: ',totalAmount, orderbookResponse['asks'][0]['rel'])
        print('Perc is set to: ',query_json['perc'])

        if(totalAmount<maxAmount):
            print('ok total Amount of Order is in Range. Proceeding.\n')
            self.makeoffer3(query_json)
        else:
            print('Total Amount out of Range. Aborting.\n')

    def makeoffer3(self, query):
        null = None #  b'{"result":null}' for when null is sent back, which py doenst know
        print(2*"\n++++++++++++","test_makeoffer3")
        query['requestType'] = 'makeoffer3'
        payload= self.qComp_777.make_777POST_Request(query)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)
        return rpl777



class SNET_trollbox(SNET_BaseTest):
    """
    #static char *trollbox[] = { (char *)trollbox_func, "trollbox", "V", "post", "whaleindex", 0 };
     ./uTest1.py SNET_trollbox
     test setUp func here

    ++++++++++++
    ++++++++++++ test_trollbox
    query json is:  None

    ~~~~~~~~~~~~
    ~~~~~~~~~~~~ SuperNET rpl777y:

     {'error': 'command disabled'}
    {'error': 'command disabled'}
    F

    """#

    def setUp(self):
        print(" test setUp func here")
        pass

    def runTest(self):
        self.test_trollbox()

    def test_trollbox(self):
        """ test_trollbox

            call sequence:

            1.


            ---------

            asserts

            1.  reply has


        """
        rpl777 = self.trollbox()
        print(rpl777)
        self.assertTrue('result' in rpl777.keys() )

    def trollbox(self):
        null = None #  b'{"result":null}' for when null is sent back, which py doenst know
        print(2*"\n++++++++++++","test_trollbox")
        test_RQ_trollbox = {'requestType': 'trollbox'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_trollbox)
        print("query json is: ", payload)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(2*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)
        return rpl777


    #########################
    #########################
    #########################
    #########################
    #
    #     composites
    #########################
    #########################
    #########################
    #########################
    #########################



class ___composites():
    pass

class SNET_placeask_full(SNET_BaseTest, ):

    SNET_placeask = SNET_placeask
    SNET_orderbook = SNET_orderbook
    SNET_openorders = SNET_openorders
    SNET_cancelquote = SNET_cancelquote

    def setUp(self):
        print("test placeask")

    def runTest(self):
        self.test_placeask()



    def test_placeask(self):
        null = None

# query json is:  {'duration': '', 'relid': '5527630', 'relamount': '', 'minperc': '', 'volume': '1.00', 'requestType': 'placeask', 'price': '0.014', 'automatch': '', 'baseid': '17554243582654188572', 'baseamount': '', 'timestamp': '', 'gui': ''}
# test_placeask:  {'rel': 'NXT', 'duration': 3600, 'offerNXT': '10501328530345129240', 'relamount': '1400000', 'exchange': 'InstantDEX', 'age': 0, 'askoffer': 1, 'base': 'BTC', 'volume': 1, 'NXT': '10501328530345129240', 'requestType': 'ask', 'quoteid': '3340965897362686873', 'baseamount': '100000000', 'baseid': '17554243582654188572', 'relid': '5527630', 'minperc': 75, 'timestamp': 1429679816, 'price': 0.014}
# .
        price = '0.014'
        volume = '1.00'
        baseid = '17554243582654188572'
        relid = '5527630'
        placeask = self.SNET_placeask.placeask(self, volume,price,baseid,relid)

        self.assertTrue('quoteid' in placeask.keys())
        self.quoteID=placeask['quoteid']
        self.exchange = placeask['exchange']

        time.sleep(0.2)
        orderbook = self.SNET_orderbook.orderbook(self, baseid,relid)

        self.assertTrue('obookid' in orderbook.keys())

        self.asks = orderbook['asks']

        oBook={'maxdepth': 0,
               'obookid': '17554243582651323474',
               'NXT': '10501328530345129240',
               'baseid': '17554243582654188572',
               'asks':
                   [{'price': '0.00014000', 'volume': '1.00001000'}, {'price': '0.00014000', 'volume': '1.00001000'}, {'price': '0.01400000', 'volume': '1.00000000'}, {'price': '0.01400000', 'volume': '1.00000000'}, {'price': '0.01400000', 'volume': '1.00000000'}, {'price': '0.01400000', 'volume': '1.00000000'}, {'price': '0.01400000', 'volume': '1.00000000'}, {'price': '0.01400000', 'volume': '1.00000000'}],
               'bids': [{'price': '0.01400000', 'volume': '1.00000000'}],
               'timestamp': 1429681910,
               'relid': '5527630',
               'pair': 'BTC/NXT'}

        time.sleep(0.2)
        openorders1 = self.SNET_openorders.openorders(self)

        found = False
        for openorder in openorders1['openorders']:

            if openorder['quoteid'] == self.quoteID:
                print(openorder)
                found = True
        self.assertTrue(found)

        time.sleep(0.2)
        cancelquote = self.SNET_cancelquote.cancelquote(self, self.quoteID )

        print('\nCheck cancelquote works\n')
        self.assertTrue(cancelquote['result']=='quote cancelled')



class SNET_placebid_full(SNET_BaseTest, ):

    SNET_placebid = SNET_placebid
    SNET_orderbook = SNET_orderbook
    SNET_openorders = SNET_openorders
    SNET_cancelquote = SNET_cancelquote

    def setUp(self):
        print("test placebid")

    def runTest(self):
        self.test_placebid()



    def test_placebid(self):
        null = None

        price = '0.014'
        volume = '0.010'
        baseid = '17554243582654188572'
        relid = '5527630'
        placebid = self.SNET_placebid.placebid(self, volume,price,baseid,relid)

        self.assertTrue('quoteid' in placebid.keys())
        self.quoteID=placebid['quoteid']
        self.exchange = placebid['exchange']

        time.sleep(0.2)
        orderbook = self.SNET_orderbook.orderbook(self, baseid,relid)

        self.assertTrue('obookid' in orderbook.keys())

        self.bids = orderbook['bids']

        time.sleep(0.2)
        openorders1 = self.SNET_openorders.openorders(self)

        found = False
        for openorder in openorders1['openorders']:

            if openorder['quoteid'] == self.quoteID:
                print(openorder)
                found = True
        self.assertTrue(found)

        time.sleep(0.2)
        cancelquote = self.SNET_cancelquote.cancelquote(self, self.quoteID )

        print('\nCheck cancelquote works\n')
        self.assertTrue(cancelquote['result']=='quote cancelled')







class SNET_baseSetup(SNET_BaseTest):
    """ this tests
     settings
     getpeers
     ping
     pong
     GUIpoll
     findnode
     havenode

     """#
    maxPolls = 15
    pollsDone = 0

    has_pong = False
    has_havenode = False
    SNET_baseSetupOK = False

    pongers =  {} # LOCAL AUXILIARY REGISTER
    havenoders =  {} #  LOCAL AUXILIARY REGISTER
    peersDiLoc = {}


    def setUp(self):

        print(2*"\n++++++++++++","SNET_baseSetup")
        req_settings = {'requestType': 'settings'}
        payload= self.qComp_777.make_777POST_Request(req_settings)

        # print(payload)
        # #headers = {'content-type': 'application/json'}
        # print(self.url)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)

        self.whitelist = rpl777['whitelist']

        self.assertTrue('whitelist' in rpl777.keys())


        establishNetwork = True
        while establishNetwork:

            req_getpeers = {'requestType': 'getpeers'}
            payload = self.qComp_777.make_777POST_Request(req_getpeers)
            #headers = {'content-type': 'application/json'}
            testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

            print(payload)
            rpl777 = eval(testReq.text)

            print("rpl777 req_getpeers", rpl777)
            self.localpeers=rpl777['peers']
            # print("localpeers:,", self.localpeers)
            # print( self.localpeers[2:])

            time.sleep(0.1)


            for ip in self.whitelist:
                req_ping = {'requestType': 'ping'}

                payload= self.qComp_777.make_777POST_Request(req_ping)

                payload['destip'] = ip
                #print(payload)
                time.sleep(0.2)
                testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
                rpl777 = eval(testReq.text)
                print("ping whitelist rpl777: ",rpl777)


                time.sleep(0.1)

                #
                # test_RQ_ = {'requestType': 'GUIpoll'}
                # payload= self.qComp_777.make_777POST_Request(test_RQ_)
                # testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
                #
                # rpl777 = eval(testReq.text)
                # print(rpl777)
                # if 'kademlia_pong' in rpl777['result']:
                #     print("kademlia_pong -------> ", rpl777['result'])
                #     self.has_pong=True

                #
                #  This is a testig suite. So keep this comment here.
                #
                # print(testReq.text)
                # print(testReq.content)
                #
                # {"result":"{\"result\":\"kademlia_pong\",\"tag\":\"\",\"isMM\":\"0\",\"NXT\":\"1978065578067355462\",\"ipaddr\":\"89.212.19.49\",\"port\":0,\"lag\":\"430430.250\",\"numpings\":5,\"numpongs\":66,\"ave\":\"516774.061\"}","from":"89.212.19.49","port":0,"args":"[{\"requestType\":\"pong\",\"NXT\":\"1978065578067355462\",\"time\":1424245045,\"MMatrix\":0,\"yourip\":\"178.62.185.131\",\"yourport\":33978,\"ipaddr\":\"89.212.19.49\",\"pubkey\":\"c269a8b4567c0b3062e6c4be859d845c4b808a405dd03d0d1ac7b4d9cb725b40\",\"ver\":\"0.599\"},{\"token\":\"aqqagqe2sph302rsgieobfm482580iqs386jrk2teb5tjd67a9bfcg2rsiss5o82ik5t372e28kcalo6t6l9rcm6e5ol2qad2sn479go2kqgho6kkvq3ne0496t396vvcobl2fpg4ngmtmb3pac0grs7knhn8qe4\"}]"}
                #
                # b'{"result":"{\\"result\\":\\"kademlia_pong\\",\\"tag\\":\\"\\",\\"isMM\\":\\"0\\",\\"NXT\\":\\"1978065578067355462\\",\\"ipaddr\\":\\"89.212.19.49\\",\\"port\\":0,\\"lag\\":\\"430430.250\\",\\"numpings\\":5,\\"numpongs\\":66,\\"ave\\":\\"516774.061\\"}","from":"89.212.19.49","port":0,"args":"[{\\"requestType\\":\\"pong\\",\\"NXT\\":\\"1978065578067355462\\",\\"time\\":1424245045,\\"MMatrix\\":0,\\"yourip\\":\\"178.62.185.131\\",\\"yourport\\":33978,\\"ipaddr\\":\\"89.212.19.49\\",\\"pubkey\\":\\"c269a8b4567c0b3062e6c4be859d845c4b808a405dd03d0d1ac7b4d9cb725b40\\",\\"ver\\":\\"0.599\\"},{\\"token\\":\\"aqqagqe2sph302rsgieobfm482580iqs386jrk2teb5tjd67a9bfcg2rsiss5o82ik5t372e28kcalo6t6l9rcm6e5ol2qad2sn479go2kqgho6kkvq3ne0496t396vvcobl2fpg4ngmtmb3pac0grs7knhn8qe4\\"}]"}'
                #
                #
                #



            time.sleep(0.1)

            print(5*"\n++localpeers+",self.localpeers[2:] )

            print("number of peers is:", len(self.localpeers[2:]))
            if len(self.localpeers[2:]) ==0:
                print("EMPTY!")

            for peer in self.localpeers[2:]:
                req_findnode = {'requestType': 'findnode'}

                payload= self.qComp_777.make_777POST_Request(req_findnode)
                #print(peer)
                payload['key'] = peer['srvNXT']
                print("doing findnode for peer: ",payload)
                time.sleep(0.2)
                testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
                rpl777 = eval(testReq.text)
                print("req_findnode rpl777: ",rpl777)


            time.sleep(0.1)

            test_RQ_ = {'requestType': 'GUIpoll'}
            payload= self.qComp_777.make_777POST_Request(test_RQ_)

            testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

            rpl777 = eval(testReq.text)
            print("GUIpoll",rpl777)


            #
            #  This is a testig suite. So keep this comment here.
            #
            # print(testReq.text)
            # print(testReq.content)
            #
            # {"result":"{\"result\":\"kademlia_pong\",\"tag\":\"\",\"isMM\":\"0\",\"NXT\":\"1978065578067355462\",\"ipaddr\":\"89.212.19.49\",\"port\":0,\"lag\":\"430430.250\",\"numpings\":5,\"numpongs\":66,\"ave\":\"516774.061\"}","from":"89.212.19.49","port":0,"args":"[{\"requestType\":\"pong\",\"NXT\":\"1978065578067355462\",\"time\":1424245045,\"MMatrix\":0,\"yourip\":\"178.62.185.131\",\"yourport\":33978,\"ipaddr\":\"89.212.19.49\",\"pubkey\":\"c269a8b4567c0b3062e6c4be859d845c4b808a405dd03d0d1ac7b4d9cb725b40\",\"ver\":\"0.599\"},{\"token\":\"aqqagqe2sph302rsgieobfm482580iqs386jrk2teb5tjd67a9bfcg2rsiss5o82ik5t372e28kcalo6t6l9rcm6e5ol2qad2sn479go2kqgho6kkvq3ne0496t396vvcobl2fpg4ngmtmb3pac0grs7knhn8qe4\"}]"}
            #
            # b'{"result":"{\\"result\\":\\"kademlia_pong\\",\\"tag\\":\\"\\",\\"isMM\\":\\"0\\",\\"NXT\\":\\"1978065578067355462\\",\\"ipaddr\\":\\"89.212.19.49\\",\\"port\\":0,\\"lag\\":\\"430430.250\\",\\"numpings\\":5,\\"numpongs\\":66,\\"ave\\":\\"516774.061\\"}","from":"89.212.19.49","port":0,"args":"[{\\"requestType\\":\\"pong\\",\\"NXT\\":\\"1978065578067355462\\",\\"time\\":1424245045,\\"MMatrix\\":0,\\"yourip\\":\\"178.62.185.131\\",\\"yourport\\":33978,\\"ipaddr\\":\\"89.212.19.49\\",\\"pubkey\\":\\"c269a8b4567c0b3062e6c4be859d845c4b808a405dd03d0d1ac7b4d9cb725b40\\",\\"ver\\":\\"0.599\\"},{\\"token\\":\\"aqqagqe2sph302rsgieobfm482580iqs386jrk2teb5tjd67a9bfcg2rsiss5o82ik5t372e28kcalo6t6l9rcm6e5ol2qad2sn479go2kqgho6kkvq3ne0496t396vvcobl2fpg4ngmtmb3pac0grs7knhn8qe4\\"}]"}'
            #
            #
            #

            #print(rpl777['result'])

            #
            # if 'nothing pending' in rpl777['result']:
            #     print(1*"GUIpoll : ",rpl777  )
            #
            if 'kademlia_pong' in rpl777['result']:
                print("kademlia_pong -------> ", rpl777['result'])

                #
                # print("kademlia_pong -------> ", rpl777)
                # print("kademlia_pong -------> ", rpl777['result'])
                #
                #
                # kademlia_pong ------->  {'result': '{"result":"kademlia_pong","tag":"","isMM":"0","NXT":"1978065578067355462","ipaddr":"89.212.19.49","port":0,"lag":"430430.250","numpings":5,"numpongs":66,"ave":"516774.061"}', 'args': '[{"requestType":"pong","NXT":"1978065578067355462","time":1424245045,"MMatrix":0,"yourip":"178.62.185.131","yourport":33978,"ipaddr":"89.212.19.49","pubkey":"c269a8b4567c0b3062e6c4be859d845c4b808a405dd03d0d1ac7b4d9cb725b40","ver":"0.599"},{"token":"aqqagqe2sph302rsgieobfm482580iqs386jrk2teb5tjd67a9bfcg2rsiss5o82ik5t372e28kcalo6t6l9rcm6e5ol2qad2sn479go2kqgho6kkvq3ne0496t396vvcobl2fpg4ngmtmb3pac0grs7knhn8qe4"}]', 'port': 0, 'from': '89.212.19.49'}
                # kademlia_pong ------->  {"result":"kademlia_pong","tag":"","isMM":"0","NXT":"1978065578067355462","ipaddr":"89.212.19.49","port":0,"lag":"430430.250","numpings":5,"numpongs":66,"ave":"516774.061"}
                #


                self.has_pong=True
            elif 'kademlia_havenode' in rpl777['result']:
                self.has_havenode=True
                print("kademlia_havenode -------> ", rpl777)
            else:
                #log.msg(1*"GUIpoll ---> misc.  ", rpl777, type(rpl777))
                print(1*"GUIpoll ---> misc.  ", rpl777)

            print("base setup- has ponger(s): ", self.has_pong)
            print("base setup- has havenoder(s): ",self.has_havenode,"\n")

            if self.has_pong and self.has_havenode:
                establishNetwork = False
                self.SNET_baseSetupOK = True


            if self.pollsDone > self.maxPolls:
                establishNetwork = False # give up
                self.SNET_baseSetupOK = False

            self.pollsDone += 1


    def runTest(self):
        self.test_SNET_baseSetup()



    def test_SNET_baseSetup(self):

        print(5*"\ntest_SNET_baseSetup")
        time.sleep(3)

        self.assertTrue(self.SNET_baseSetupOK)


    # GUIpoll reply: kademlia_pong ------->
    # {'result': '{"result":"kademlia_pong","tag":"","isMM":"0","NXT":"1978065578067355462","ipaddr":"127.0.0.1","port":0,"lag":"143.250","numpings":5,"numpongs":24,"ave":"366301.170"}', 'from': '89.212.19.49', 'args': '[{"requestType":"pong","NXT":"1978065578067355462","time":1424204548,"MMatrix":0,"yourip":"178.62.185.131","yourport":35671,"ipaddr":"127.0.0.1","pubkey":"c269a8b4567c0b3062e6c4be859d845c4b808a405dd03d0d1ac7b4d9cb725b40","ver":"0.599"},{"token":"aqqagqe2sph302rsgieobfm482580iqs386jrk2teb5tjd67a6scag2ricaddi82i9cgd2qokv9147cqp2aqbtoogldjbaofuoga3cb3r2m06qjmfu5gpl8s63m6hn2gfahl3l4o7t0eds96d78t4eiclm5psims"}]', 'port': 0}
    # {'args': '[{"requestType":"pong","NXT":"1978065578067355462","time":1424241662,"MMatrix":0,"yourip":"178.62.185.131","yourport":33978,"ipaddr":"89.212.19.49","pubkey":"c269a8b4567c0b3062e6c4be859d845c4b808a405dd03d0d1ac7b4d9cb725b40","ver":"0.599"},{"token":"aqqagqe2sph302rsgieobfm482580iqs386jrk2teb5tjd67a94rsg2r93ggu7o2va245utlbcftdrfqkm74cjnc4nomh0tsrbe3iupfn2mg2r2ii6k40iki6b70ppfo3naq2vcmndtab86m036r22g3ka2f2a4f"}]', 'from': '89.212.19.49', 'result': '{"result":"kademlia_pong","tag":"","isMM":"0","NXT":"1978065578067355462","ipaddr":"89.212.19.49","port":0,"lag":"84380.922","numpings":0,"numpongs":2,"ave":"70919.423"}', 'port': 0}
    # {'result': 'nothing pending'}



        
##############################################
##############################################
##############################################
##############################################
##############################################

# no Suites for single calls! Suites only to run multiple tests and get 'ran 5 of 5 tests 0 fails'

def suite_idexSuite():

    suite = unittest.TestSuite()
    suite.addTest(SNET_placebid())
    suite.addTest(SNET_placeask())
    suite.addTest(SNET_orderbook())
    suite.addTest(SNET_allorderbooks())
    suite.addTest(SNET_openorders())
    suite.addTest(SNET_respondtx())
    suite.addTest(SNET_bid())
    suite.addTest(SNET_ask())
    suite.addTest(SNET_lottostats())
    suite.addTest(SNET_cancelquote())
    suite.addTest(SNET_placebid_full())
    suite.addTest(SNET_placeask_full())
    #suite.addTest(SNET_jumptrades()) FUTURE!
    #suite.addTest(SNET_tradehistory()) FUTURE!
    # TRADEBOT
    #suite.addTest(SNET_allsignals())
    #suite.addTest(SNET_getsignal())

    return suite


def suite_baseSetup():
    suite = unittest.TestSuite()
    suite.addTest(SNET_baseSetup('setUp'))
    suite.addTest(SNET_baseSetup('test_SNET_baseSetup'))
    return suite

def suite_SG():
    suite = unittest.TestSuite()
    suite.addTest(SNET_getpeers('test_getpeers'))
    suite.addTest(SNET_settings('test_settings'))
    return suite




class TestCollector(object):
    """
    The Testcollector class provides three methods of grouping test cases.

    1: getTestClassDict
        returns a dictionary with named test classes as values

    2: getTestSuitesDict
        returns a dict of test suites with suites as values

    3: getTestList
        returns lists of test classes by name of list
    """#
    def getTestClassDict(self, ):
        """
        test status as in comments below::

        *  verified
        ~  returns null
        +  returns None
        !  crashes server
        ?  needs params

        null = None #  b'{"result":null}' for when null is sent back, which py doenst know

        """

        testClasses = {}
        #
        testClasses['SNET_baseSetup'] = SNET_baseSetup # *
        # glue
        testClasses['SNET_gotjson'] = SNET_gotjson     # ~
        testClasses['SNET_gotpacket'] = SNET_gotpacket # ?
        testClasses['SNET_gotnewpeer'] = SNET_gotnewpeer # * +
        testClasses['SNET_BTCDpoll'] = SNET_BTCDpoll # *
        testClasses['SNET_GUIpoll'] = SNET_GUIpoll    # *
        testClasses['SNET_settings'] = SNET_settings  # *
        #remo ramch
        testClasses['SNET_rampyramid'] = SNET_rampyramid # ?
        testClasses['SNET_ramresponse'] = SNET_ramresponse # ~
        testClasses['SNET_ramstatus'] = SNET_ramstatus # *
        testClasses['SNET_ramstring'] = SNET_ramstring # ?
        testClasses['SNET_ramrawind'] = SNET_ramrawind # ?
        testClasses['SNET_ramblock'] = SNET_ramblock # ?
        testClasses['SNET_ramscript'] = SNET_ramscript # ?
        # local Ramch
        testClasses['SNET_ramtxlist'] = SNET_ramtxlist # ?
        testClasses['SNET_ramrichlist'] = SNET_ramrichlist # ?
        testClasses['SNET_ramaddrlist'] = SNET_ramaddrlist # *
        testClasses['SNET_ramcompress'] = SNET_ramcompress # ?
        testClasses['SNET_ramexpand'] = SNET_ramexpand # ?
        testClasses['SNET_rambalances'] = SNET_rambalances # ?
        # mgw
        testClasses['SNET_genmultisig'] = SNET_genmultisig # ?
        testClasses['SNET_getmsigpubkey'] = SNET_getmsigpubkey # ?
        testClasses['SNET_MGWaddr'] = SNET_MGWaddr # * ~
        testClasses['SNET_MGWresponse'] = SNET_MGWresponse # * ~
        testClasses['SNET_setmsigpubkey'] = SNET_setmsigpubkey # ?
        testClasses['SNET_cosign'] = SNET_cosign # ?
        testClasses['SNET_cosigned'] = SNET_cosigned # ?
        #ipcomm
        testClasses['SNET_ping'] = SNET_ping # *
        testClasses['SNET_pong'] = SNET_pong # *
        testClasses['SNET_sendfrag'] = SNET_sendfrag # ?
        testClasses['SNET_gotfrag'] = SNET_gotfrag # ?
        testClasses['SNET_startxfer'] = SNET_startxfer # *
        testClasses['SNET_getfile'] = SNET_getfile # *
        # Kademlia DHT 8
        testClasses['SNET_store'] = SNET_store
        testClasses['SNET_findvalue'] = SNET_findvalue # ?
        testClasses['SNET_findnode'] = SNET_findnode # *
        testClasses['SNET_havenode'] = SNET_havenode # ?
        testClasses['SNET_findaddress'] = SNET_findaddress # ? ~
        testClasses['SNET_havenodeB'] = SNET_havenodeB # ?
        testClasses['SNET_puzzles'] = SNET_puzzles # *
        testClasses['SNET_nonces'] = SNET_nonces # *
        # mofns
        testClasses['SNET_savefile'] = SNET_savefile # ?
        #""" this may require MASSIVE calulation, don't do this in ALL for now  """
        # ToDo check with jl777
        #testClasses['SNET_restorefile'] = SNET_restorefile # ?
        testClasses['SNET_publish'] = SNET_publish # ?
        # pbet
        testClasses['SNET_lotto'] = SNET_lotto  # ?
        # telepa
        testClasses['SNET_getpeers'] = SNET_getpeers # *
        testClasses['SNET_addcontact'] = SNET_addcontact # ?
        testClasses['SNET_removecontact'] = SNET_removecontact # ?
        testClasses['SNET_dispcontact'] = SNET_dispcontact # ?
        testClasses['SNET_telepathy'] = SNET_telepathy # ?
        testClasses['SNET_getdb'] = SNET_getdb # ?
        testClasses['SNET_sendmessage'] = SNET_sendmessage # ?
        testClasses['SNET_sendbinary'] = SNET_sendbinary # ?
        # telepo
        testClasses['SNET_maketelepods'] = SNET_maketelepods # ?
        testClasses['SNET_telepodacct'] = SNET_telepodacct # ?
        testClasses['SNET_teleport'] = SNET_teleport # ?
        # idex
        testClasses['SNET_trollbox'] = SNET_trollbox # *
        testClasses['SNET_allorderbooks'] = SNET_allorderbooks # *
        testClasses['SNET_openorders'] = SNET_openorders       # *
        testClasses['SNET_orderbook'] = SNET_orderbook # *
        testClasses['SNET_placebid'] = SNET_placebid # *
        testClasses['SNET_placeask'] = SNET_placeask # *
        testClasses['SNET_makeoffer3'] = SNET_makeoffer3 # *?
        testClasses['SNET_respondtx'] = SNET_respondtx  # * ?
        testClasses['SNET_bid'] = SNET_bid # *
        testClasses['SNET_ask'] = SNET_ask # *
        testClasses['SNET_tradehistory'] = SNET_tradehistory # *
        testClasses['SNET_cancelquote'] = SNET_cancelquote # *
        testClasses['SNET_jumptrades'] = SNET_jumptrades # *
        testClasses['SNET_placeask_full'] = SNET_placeask_full
        testClasses['SNET_placebid_full'] = SNET_placebid_full
        # plugins
        testClasses['SNET_passthru'] = SNET_passthru # ?
        testClasses['SNET_remote'] = SNET_remote # ?
        testClasses['SNET_syscall'] = SNET_syscall  # ? ~
        testClasses['SNET_checkmsg'] = SNET_checkmessages # ?
        # tbot
        testClasses['SNET_tradebot'] = SNET_tradebot   # ?
        testClasses['SNET_allsignals'] = SNET_allsignals # *
        testClasses['SNET_lottostats'] = SNET_lottostats # *
        testClasses['SNET_getsignal'] = SNET_getsignal # *
        return testClasses


    def  getTestSuitesDict(self, ):

        testSuites = {}

        testSuites['idex'] = suite_idexSuite
        #testSuites['base1'] = suite_baseSetup
        testSuites['base'] = suite_baseSetup
        testSuites['sg'] = suite_SG
        return testSuites

    def getTestList(self, testListName):

        if testListName == 'all':

            testList = [
                        SNET_baseSetup ,\
                        # glue
                        SNET_gotjson     ,\
                        SNET_gotpacket ,\
                        SNET_gotnewpeer ,\
                        SNET_BTCDpoll ,\
                        SNET_GUIpoll    ,\
                        SNET_settings  ,\
                        #remo ramch
                        SNET_rampyramid ,\
                        SNET_ramresponse ,\
                        SNET_ramstatus ,\
                        SNET_ramstring ,\
                        SNET_ramrawind ,\
                        SNET_ramblock ,\
                        SNET_ramscript ,\
                        # local Ramch
                        SNET_ramtxlist ,\
                        SNET_ramrichlist ,\
                        SNET_ramaddrlist ,\
                        SNET_ramcompress ,\
                        SNET_ramexpand ,\
                        SNET_rambalances ,\
                        # mgw
                        SNET_genmultisig ,\
                        SNET_getmsigpubkey ,\
                        SNET_MGWaddr ,\
                        SNET_MGWresponse ,\
                        SNET_setmsigpubkey ,\
                        SNET_cosign ,\
                        SNET_cosigned ,\
                        #ipcomm
                        SNET_ping ,\
                        SNET_pong ,\
                        SNET_sendfrag ,\
                        SNET_gotfrag ,\
                        SNET_startxfer ,\
                        SNET_getfile ,\
                        # Kademlia DHT 8
                        SNET_store,\
                        SNET_findvalue ,\
                        SNET_findnode ,\
                        SNET_havenode ,\
                        SNET_findaddress ,\
                        SNET_havenodeB ,\
                        SNET_puzzles ,\
                        SNET_nonces ,\
                        # mofns
                        SNET_savefile ,\
                        SNET_restorefile ,\
                        SNET_publish ,\
                        # telepa
                        SNET_getpeers ,\
                        SNET_addcontact ,\
                        SNET_removecontact ,\
                        SNET_dispcontact ,\
                        SNET_telepathy ,\
                        SNET_getdb ,\
                        SNET_sendmessage ,\
                        SNET_sendbinary ,\
                        # telepo
                        SNET_maketelepods ,\
                        SNET_telepodacct ,\
                        SNET_teleport ,\
                        #privatebt
                        SNET_lotto  ,\
                        # tradebots
                        SNET_allsignals ,\
                        SNET_getsignal ,\
                        SNET_tradebot   ,\
                        # idex
                        SNET_allorderbooks ,\
                        SNET_openorders       ,\
                        SNET_orderbook ,\
                        SNET_placebid ,\
                        SNET_placeask ,\
                        SNET_makeoffer3 ,\
                        SNET_respondtx  ,\
                        SNET_bid ,\
                        SNET_ask ,\
                        SNET_lottostats ,\
                        SNET_tradehistory ,\
                        SNET_cancelquote ,\
                        SNET_jumptrades ,\
                        # plugins
                        SNET_passthru ,\
                        SNET_remote ,\
                        SNET_syscall  ,\
                        SNET_checkmessages ,\
                        ]

        elif testListName == 'contacts':

            testList = [
                       SNET_addcontact,\
                        SNET_dispcontact,\
                        SNET_removecontact
                        ]

        elif testListName == 'tradebotOK':
            testList =  [
                        SNET_allsignals,\
                                ]

        elif testListName == 'idexOK':
            testList =          [
                        SNET_orderbook,\
                        SNET_placeask,\
                        SNET_placebid,\
                        SNET_allorderbooks,\
                        SNET_openorders,\
                        SNET_ask,\
                        SNET_bid,\
                        SNET_lottostats,\
                        ]

        elif testListName == 'idexFuture':
            testList =     [
                        SNET_tradehistory,\
                        SNET_trollbox,\
                        SNET_jumptrades,\
                        ]

        elif testListName == 'idexInternals':
            testList =     [
                         SNET_respondtx,\
                        ]

        elif testListName == 'idexAll':
            testList = [
                        SNET_allorderbooks ,\
                        SNET_openorders,\
                        SNET_orderbook,\
                        SNET_placebid,\
                        SNET_placeask,\
                        SNET_bid,\
                        SNET_ask,\
                        SNET_respondtx,\
                        SNET_lottostats ,\
                        SNET_cancelquote,\
                        SNET_makeoffer3 ,\
                        ]

        elif testListName == 'err':
            testList =     [
                        SNET_gotpacket,\
                        ]

        elif testListName == 'smoketests':
            testList =     [
                        SNET_gotjson,\
                        SNET_gotnewpeer,\
                        SNET_BTCDpoll,\
                        ]

        elif testListName == 'okALL':
            testList =     [
                        SNET_GUIpoll  ,\
                        SNET_settings ,\
                        ]


        else:

            testList = []

        return testList





def main():
    """

    The test cases can be grouped in three ways:

    1 by list name
    2 by class name
    3 by suite name

    arguments represent names of lists or classes or suites to be run


    ./uTest1.py sg base settings testList1


    The Testcollector class provides three methods of grouping test cases.

    1: getTestClassDict
        returns a dictionary with named test classes as values

    2: getTestSuitesDict
        returns a dict of test suites with suites as values

    3: getTestList
        returns lists of test classes by name of list




    can also be invoked via pythons unittest syntax:
    python3 -m unittest -vvv uTest1.py

    python3 -m unittest -vvv uTest1.SNET_baseSetup

    """#

    # this is the collector class that contains test cases in various groupings
    # either as names lists or as named suites or as classes
    testCollector = TestCollector()

    # this is the dict that is returned by getTestClassDict
    testClasses = testCollector.getTestClassDict() # enter className as arg
    testSuites = testCollector.getTestSuitesDict() # enter suitename as arg

    suiteList = ['sg', 'base'] # this is a list of suites that can be run with 'sList'

    args = sys.argv[1:]

    for  testCase in args:

        if testCase == 'makeoffer3'
            runner = unittest.TextTestRunner()
            runner.run(SNET_makeoffer3())
        
        elif testCase in testClasses: # dict of classes
            runner = unittest.TextTestRunner()
            runner.run(testClasses[testCase]())
            

        elif testCase in testSuites: # dict of suites
             suite  = testSuites[testCase]()
             runner = unittest.TextTestRunner()
             runner.run(suite)

        elif testCase == 'sList': # list of suites
            for singleSuite in suiteList:
                 suite  = testSuites[singleSuite]() # this returns a callable!
                 runner = unittest.TextTestRunner()
                 runner.run(suite)

        else: # enter listName as arg
            verifTestList = testCollector.getTestList(testCase) # this interprets each cmd line arg as a name for a test list
            for test in verifTestList:

                runner = unittest.TextTestRunner()
                runner.run(test())


    try:
        if args[0] == 'all': # should run all tests in the main class that follow the python unittest naming convention 'def test_TESTNAME()'
            unittest.main()
    except:
        print(main.__doc__)




if __name__ == '__main__':
    main()





    """



STONEFISH_IP = '178.62.185.131'   #


 ./BitcoinDarkd dumpprivkey RWW6FPcopt5va8TtGkPsPTK9GEr8r8QS9Q
NXT-FMMS-4QHR-VEJ9-DYXU9
702f4bc8d955a4f5053b245ee9a40199ff8fca2bd304c13f77bb3c863e792171


 ./BitcoinDarkd dumpprivkey RTib4uLAc9DfP2x6tGsQ9SZzFfXmcgGqZm
NXT-CXAS-P5SG-EUVZ-BQ3H5
020ad74d2c6ce659a64ac0e7fc5415559ca56a3a233be0af73cded476fd0747d






api.h: list of all calls. date: 0413515:

char *SuperNET_json_commands(struct NXThandler_info *mp,char *previpaddr,cJSON *origargjson,char *sender,int32_t valid,char *origargstr)
{
    // local glue
    static char *gotjson[] = { (char *)gotjson_func, "BTCDjson", "V", "json", 0 };
    static char *gotpacket[] = { (char *)gotpacket_func, "gotpacket", "V", "msg", "dur", "ip_port", 0 };
    static char *gotnewpeer[] = { (char *)gotnewpeer_func, "gotnewpeer", "V", "ip_port", 0 };
    static char *BTCDpoll[] = { (char *)BTCDpoll_func, "BTCDpoll", "V", 0 };
    static char *GUIpoll[] = { (char *)GUIpoll_func, "GUIpoll", "V", 0 };
    static char *stop[] = { (char *)stop_func, "stop", "V", 0 };
    static char *settings[] = { (char *)settings_func, "settings", "V", "field", "value", "reinit", 0 };

    // remotable ramchains
    static char *rampyramid[] = { (char *)rampyramid_func, "rampyramid", "V", "destip", "port", "coin", "blocknum", "type", 0 };
    static char *ramstatus[] = { (char *)ramstatus_func, "ramstatus", "V", "destip", "port", "coin", 0 };
    static char *ramstring[] = { (char *)ramstring_func, "ramstring", "V", "destip", "port", "coin", "type", "rawind", 0 };
    static char *ramrawind[] = { (char *)ramrawind_func, "ramrawind", "V", "destip", "port", "coin", "type", "string", 0 };
    static char *ramscript[] = { (char *)ramscript_func, "ramscript", "V", "destip", "port", "coin", "txid", "vout", "blocknum", "txind", "v", 0 };
    static char *ramblock[] = { (char *)ramblock_func, "ramblock", "V", "destip", "port", "coin", "blocknum", 0 };
    static char *ramresponse[] = { (char *)ramresponse_func, "ramresponse", "V", "coin", "origcmd", "data", 0 };
    // local ramchains
    static char *ramtxlist[] = { (char *)ramtxlist_func, "ramtxlist", "V", "coin", "address", "unspent", 0 };
    static char *ramrichlist[] = { (char *)ramrichlist_func, "ramrichlist", "V", "coin", "numwhales", "recalc", 0 };
    static char *ramaddrlist[] = { (char *)ramaddrlist_func, "ramaddrlist", "V", "coin", 0 };
    static char *rambalances[] = { (char *)rambalances_func, "rambalances", "V", "coin", "coins", "rates", 0 };
    static char *ramcompress[] = { (char *)ramcompress_func, "ramcompress", "V", "coin", "data", 0 };
    static char *ramexpand[] = { (char *)ramexpand_func, "ramexpand", "V", "coin", "data", 0 };

    // MGW
    static char *genmultisig[] = { (char *)genmultisig_func, "genmultisig", "", "userpubkey", "coin", "refcontact", "M", "N", "contacts", "destip", "destport", "email", "buyNXT", 0 };
    static char *getmsigpubkey[] = { (char *)getmsigpubkey_func, "getmsigpubkey", "V", "coin", "refNXTaddr", "myaddr", "mypubkey", 0 };
    static char *MGWaddr[] = { (char *)MGWaddr_func, "MGWaddr", "V", 0 };
    static char *MGWresponse[] = { (char *)MGWresponse_func, "MGWresponse", "V", 0 };
    static char *setmsigpubkey[] = { (char *)setmsigpubkey_func, "setmsigpubkey", "V", "coin", "refNXTaddr", "addr", "userpubkey", 0 };
    //static char *MGW[] = { (char *)MGW_func, "MGW", "", "NXT0", "NXT1", "NXT2", "ip0", "ip1", "ip2", "coin", "asset", "rescan", "actionflag", "specialNXT", "exclude0", "exclude1", "exclude2", "destip", "destport", "userpubkey", "email", "destNXT", 0 };
    static char *cosign[] = { (char *)cosign_func, "cosign", "V", "otheracct", "seed", "text", 0 };
    static char *cosigned[] = { (char *)cosigned_func, "cosigned", "V", "seed", "result", "privacct", "pubacct", 0 };

    // IP comms
    static char *ping[] = { (char *)ping_func, "ping", "V", "pubkey", "ipaddr", "port", "destip", "MMatrix", 0 };
    static char *pong[] = { (char *)pong_func, "pong", "V", "pubkey", "ipaddr", "port", "yourip", "yourport", "tag", "MMatrix", 0 };
    static char *sendfrag[] = { (char *)sendfrag_func, "sendfrag", "V", "pubkey", "name", "fragi", "numfrags", "ipaddr", "totalcrc", "datacrc", "data", "totallen", "blocksize", "handler", "syncmem", 0 };
    static char *gotfrag[] = { (char *)gotfrag_func, "gotfrag", "V", "pubkey", "name", "fragi", "numfrags", "ipaddr", "totalcrc", "datacrc", "totallen", "blocksize", "count", "handler", "syncmem", "snapshotcrc", 0 };
    static char *startxfer[] = { (char *)startxfer_func, "startxfer", "V", "fname", "dest", "data", "timeout", "handler", "syncmem", 0 };
    static char *getfile[] = { (char *)getfile_func, "getfile", "V", "name", "handler", 0 };

    // Kademlia DHT
    static char *puzzles[] = { (char *)challenge_func, "puzzles", "V", "reftime", "duration", "threshold", 0 };
    static char *nonces[] = { (char *)response_func, "nonces", "V", "reftime", "threshold", "nonces", 0 };
    static char *store[] = { (char *)store_func, "store", "V", "pubkey", "key", "name", "data", 0 };
    static char *findvalue[] = { (char *)findvalue_func, "findvalue", "V", "pubkey", "key", "name", "data", 0 };
    static char *findnode[] = { (char *)findnode_func, "findnode", "V", "pubkey", "key", "name", "data", 0 };
    static char *havenode[] = { (char *)havenode_func, "havenode", "V", "pubkey", "key", "name", "data", 0 };
    static char *havenodeB[] = { (char *)havenodeB_func, "havenodeB", "V", "pubkey", "key", "name", "data", 0 };
    static char *findaddress[] = { (char *)findaddress_func, "findaddress", "V", "refaddr", "list", "dist", "duration", "numthreads", 0 };

    // MofNfs
    static char *savefile[] = { (char *)savefile_func, "savefile", "V", "fname", "L", "M", "N", "backup", "password", "pin", 0 };
    static char *restorefile[] = { (char *)restorefile_func, "restorefile", "V", RESTORE_ARGS, 0 };
    static char *publish[] = { (char *)publish_func, "publish", "V", "files", "L", "M", "N", "backup", "password", "pin", 0  };

    // Telepathy
    static char *getpeers[] = { (char *)getpeers_func, "getpeers", "V",  "scan", 0 };
    static char *addcontact[] = { (char *)addcontact_func, "addcontact", "V",  "handle", "acct", 0 };
    static char *removecontact[] = { (char *)removecontact_func, "removecontact", "V",  "contact", 0 };
    static char *dispcontact[] = { (char *)dispcontact_func, "dispcontact", "V",  "contact", 0 };
    static char *telepathy[] = { (char *)telepathy_func, "telepathy", "V",  "contact", "id", "type", "attach", 0 };
    static char *getdb[] = { (char *)getdb_func, "getdb", "V",  "contact", "id", "key", "dir", "destip", 0 };
    static char *sendmsg[] = { (char *)sendmsg_func, "sendmessage", "V", "dest", "msg", "L", 0 };
    static char *sendbinary[] = { (char *)sendbinary_func, "sendbinary", "V", "dest", "data", "L", 0 };

    // Teleport
    static char *maketelepods[] = { (char *)maketelepods_func, "maketelepods", "V", "amount", "coin", 0 };
    static char *telepodacct[] = { (char *)telepodacct_func, "telepodacct", "V", "amount", "contact", "coin", "comment", "cmd", "withdraw", 0 };
    static char *teleport[] = { (char *)teleport_func, "teleport", "V", "amount", "contact", "coin", "minage", "withdraw", 0 };

    // InstantDEX
    static char *trollbox[] = { (char *)trollbox_func, "trollbox", "V", "post", "whaleindex", 0 };
    static char *allorderbooks[] = { (char *)allorderbooks_func, "allorderbooks", "V", 0 };
    static char *orderbook[] = { (char *)orderbook_func, "orderbook", "V", "baseid", "relid", "allfields", "oldest", "maxdepth", "base", "rel", "gui", "showall", 0 };
    static char *lottostats[] = { (char *)lottostats_func, "lottostats", "V", "timestamp", 0 };
    static char *cancelquote[] = { (char *)cancelquote_func, "cancelquote", "V", "quoteid", 0 };
    static char *openorders[] = { (char *)openorders_func, "openorders", "V", 0 };
    static char *placebid[] = { (char *)placebid_func, "placebid", "V", "baseid", "relid", "volume", "price", "timestamp", "baseamount", "relamount", "gui", "automatch", "minperc", "duration", "exchange", 0 };
    static char *placeask[] = { (char *)placeask_func, "placeask", "V", "baseid", "relid", "volume", "price", "timestamp", "baseamount", "relamount", ",gui", "automatch", "minperc", "duration", "exchange", 0 };
    static char *bid[] = { (char *)bid_func, "bid", "V", "baseid", "relid", "volume", "price", "timestamp", "baseamount", "relamount", "gui", "automatch", "minperc", "duration", "exchange", 0 };
    static char *ask[] = { (char *)ask_func, "ask", "V", "baseid", "relid", "volume", "price", "timestamp", "baseamount", "relamount", "gui", "automatch", "minperc", "duration", "exchange", 0 };
    static char *makeoffer3[] = { (char *)makeoffer3_func, "makeoffer3", "V", "baseid", "relid", "quoteid", "perc", "deprecated", "baseiQ", "reliQ", "askoffer", "price", "volume", "exchange", "baseamount", "relamount", "offerNXT", "minperc", "jumpasset", 0 };
    static char *respondtx[] = { (char *)respondtx_func, "respondtx", "V", "cmd", "assetid", "quantityQNT", "priceNQT", "triggerhash", "quoteid", "sig", "data", "minperc", "offerNXT", "otherassetid", "otherqty", 0 };
    static char *jumptrades[] = { (char *)jumptrades_func, "jumptrades", "V", 0 };
    static char *tradehistory[] = { (char *)tradehistory_func, "tradehistory", "V", "timestamp", 0 };
  //static char *processjumptrade[] = { (char *)processjumptrade_func, "processjumptrade", "V", "assetA", "amountA", "other", "assetB", "amountB", "feeA", "feeAtxid", "triggerhash", "jumper", "jumpasset", "jumpamount", "balancing", "balancetxid", "gui", "quoteid", 0 };
    //static char *processutx[] = { (char *)processutx_func, "processutx", "V", "utx", "sig", "full", "feeAtxid", "quoteid", 0 };
    //static char *makeoffer[] = { (char *)makeoffer_func, "makeoffer", "V", "baseid", "relid", "baseamount", "relamount", "other", "type", "quoteid", 0 };
    //static char *makeoffer2[] = { (char *)makeoffer2_func, "makeoffer2", "V", "baseid", "baseamount", "jumpaddr", "jumpasset", "jumpamount", "other", "relid", "relamount", "gui", "quoteid", 0 };

    // Tradebot
    static char *allsignals[] = { (char *)allsignals_func, "allsignals", "V", 0 };
    static char *getsignal[] = { (char *)getsignal_func, "getsignal", "V", "signal", "start", "width", "resolution", "baseid", "relid", "base", "rel", "exchange", 0 };
    //static char *pricedb[] = { (char *)pricedb_func, "pricedb", "V", "exchange", "base", "rel", "stop", 0 };
    //static char *getquotes[] = { (char *)getquotes_func, "getquotes", "V", "exchange", "base", "rel", "oldest", 0 };
    static char *tradebot[] = { (char *)tradebot_func, "tradebot", "V", "code", 0 };

    // Privatbet
    static char *lotto[] = { (char *)lotto_func, "lotto", "V", "refacct", "asset", "lottoseed", "prizefund", 0 };

    // plugins
    static char *passthru[] = { (char *)passthru_func, "passthru", "V", "coin", "method", "params", "tag", "daemonid", 0 };
    static char *remote[] = { (char *)remote_func, "remote", "V",  "coin", "method", "result", "tag", 0 };
    //static char *python[] = { (char *)python_func, "python", "V",  "name", "launch", "websocket", 0 };
    static char *syscall[] = { (char *)syscall_func, "syscall", "V", "name", "launch", "websocket", "jsonargs", 0 };
    static char *checkmsg[] = { (char *)checkmsg_func, "checkmessages", "V", "daemonid", 0 };

    static char **commands[] = { stop, GUIpoll, BTCDpoll, settings, gotjson, gotpacket, gotnewpeer, getdb, cosign, cosigned, telepathy, addcontact, dispcontact, removecontact, findaddress, puzzles, nonces, ping, pong, store, findnode, havenode, havenodeB, findvalue, publish, syscall, getpeers, maketelepods, tradebot, respondtx, checkmsg, openorders, allorderbooks, placebid, bid, placeask, ask, sendmsg, sendbinary, orderbook, teleport, telepodacct, savefile, restorefile, passthru, remote, genmultisig, getmsigpubkey, setmsigpubkey, MGWaddr, MGWresponse, sendfrag, gotfrag, startxfer, lotto, ramstring, ramrawind, ramblock, ramcompress, ramexpand, ramscript, ramtxlist, ramrichlist, rambalances, ramstatus, ramaddrlist, rampyramid, ramresponse, getfile, allsignals, getsignal, jumptrades, cancelquote, lottostats, tradehistory, makeoffer3, trollbox };


    """ #

#

#
# Common Assertions
#
# Method
#
# assertTrue(x, msg=None)
#
# assertFalse(x, msg=None)
#
# assertIsNone(x, msg=None)
#
# assertIsNotNone(x, msg=None)
#
# assertEqual(a, b, msg=None)
#
# assertNotEqual(a, b, msg=None)
#
# assertIs(a, b, msg=None)
#
# assertIsNot(a, b, msg=None)
#
# assertIn(a, b, msg=None)
#
# assertNotIn(a, b, msg=None)
#
# assertIsInstance(a, b, msg=None)
#
# assertNotIsInstance(a, b, msg=None)
#
#
# Other Assertions
#
# Method
#
# assertAlmostEqual(a, b, places=7, msg=None, delta=None)
#
# assertNotAlmostEqual(a, b, places=7, msg=None, delta=None)
#
# assertGreater(a, b, msg=None)
#
# assertGreaterEqual(a, b, msg=None)
#
# assertLess(a, b, msg=None)
#
# assertLessEqual(a, b, msg=None)
#
# assertRegex(text, regexp, msg=None)
#
# assertNotRegex(text, regexp, msg=None)
#
# assertCountEqual(a, b, msg=None)
#
# assertMultiLineEqual(a, b, msg=None)
#
# assertSequenceEqual(a, b, msg=None)
#
# assertListEqual(a, b, msg=None)
#
# assertTupleEqual(a, b, msg=None)
#
# assertSetEqual(a, b, msg=None)
#
# assertDictEqual(a, b, msg=None)
#

#
#
# class SNET_processutx(SNET_BaseTest, ):
#
#     def setUp(self):
#         print(" test setUp func here")
#         pass
#
#     def runTest(self):
#         self.test_processutx()
#
#     def test_processutx(self):
#
#         rpl777 = self.processutx()
#
#         self.assertTrue('result' in rpl777.keys())
#

        #
#
# class SNET_processjumptrade(SNET_BaseTest, ):
#
#     def setUp(self):
#         print(" test processjumptrade setUp func here")
#         pass
#
#     def runTest(self):
#         self.test_processjumptrade()
#
#     def test_processjumptrade(self):
#         rpl777 = self.apicall({'requestType': 'processjumptrade'})
#
#         self.assertTrue('result' in rpl777.keys())




