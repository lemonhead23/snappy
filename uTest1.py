#!/usr/bin/env python3

#import random
import unittest
import requests
import json
from random import randint

import binascii

from snAppyModules.snQueryComposers import QueryComposer_777
from snAppyTests.snTestConfig import *

import time
import sys
import argparse



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

    def setUp(self):
        """ This can be overridden by any testing class if needed. """

        print("this test using generic setUp function")



    def example_query(self):
        test_RQ_ = {'requestType': 'settings'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        headers = {'content-type': 'application/json'}
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

    def setUp(self):

        print(5*"\n++++++++++++","SNET_baseSetup")
        req_settings = {'requestType': 'settings'}
        payload= self.qComp_777.make_777POST_Request(req_settings)

        # print(payload)
        headers = {'content-type': 'application/json'}
        # print(self.url)
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)

        self.whitelist = rpl777['whitelist']

        self.assertTrue('whitelist' in rpl777.keys())


        establishNetwork = True
        while establishNetwork:

            req_getpeers = {'requestType': 'getpeers'}
            payload = self.qComp_777.make_777POST_Request(req_getpeers)
            headers = {'content-type': 'application/json'}
            testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

            print(payload)
            rpl777 = eval(testReq.text)

            print("rpl777 req_getpeers", rpl777)
            self.localpeers=rpl777['peers']
            print( self.localpeers[2:])
            print( self.localpeers)

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

            for peer in self.localpeers[2:]:
                req_findnode = {'requestType': 'findnode'}

                payload= self.qComp_777.make_777POST_Request(req_findnode)
                #print(peer)
                payload['key'] = peer['srvNXT']
                print(payload)
                time.sleep(0.2)
                testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
                rpl777 = eval(testReq.text)
                print("req_findnode rpl777: ",rpl777)


            time.sleep(0.1)

            test_RQ_ = {'requestType': 'GUIpoll'}
            payload= self.qComp_777.make_777POST_Request(test_RQ_)

            headers = {'content-type': 'application/json'}
            testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

            rpl777 = eval(testReq.text)

            # #####################
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
            self.pollsDone += 1
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


class ___glue():
    pass

class SNET_getpeers(SNET_BaseTest):
    """
    has basic test
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
                #query_json = {'scan': '', 'requestType': 'getpeers'}


        print(5*"\n++++++++++++","test_getpeers")
        test_RQ_ = {'requestType': 'getpeers'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)

        self.assertTrue('peers' in rpl777.keys())




        details_of_expected_SuperNET_reply = """
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
          """




class SNET_gotjson(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_gotjson()


    def test_gotjson(self):
        null = None #  b'{"result":null}' for when null is sent back, which py doenst know
                #query_json = {'requestType': 'gotjson', 'json': ''}

        print(5*"\n++++++++++++","test_gotjson")
        test_RQ_ = {'requestType': 'gotjson'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777.content:", testReq.content) #  b'{"result":null}'


        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777.content:", rpl777) # rpl777)

        # azure@boxfish:~/workbench/nxtDev/TEAM/snappy$ curl   -H 'content-type: text/plain;' 'http://127/nxt?requestType=gotjson'
        # {'result': None}
        #

        self.assertTrue('result' in rpl777.keys() )



class SNET_gotpacket(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_gotpacket()


    def test_gotpacket(self):
                #query_json = {'ip_port': '', 'msg': '', 'requestType': 'gotpacket', 'dur': ''}

       #     null = None #  b'{"result":null}' for when null is sent back, which py doenst know
        print(5*"\n++++++++++++","test_gotpacket")
        test_RQ_ = {'requestType': 'gotpacket'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        if 'error' in rpl777.keys():
            self.assertTrue(False)
            print(5*"\n~~~~~~~~~~~~","error in SuperNET rpl777y:\n\n", rpl777)
        else:
            self.assertTrue('result' in rpl777.keys() )



class SNET_gotnewpeer(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_gotnewpeer()


    def test_gotnewpeer(self):
#        null = None #  b'{"result":null}' for when null is sent back, which py doenst know
        #query_json = {'requestType': 'gotnewpeer', 'ip_port': ''}

        print(5*"\n++++++++++++","test_gotnewpeer")
        test_RQ_ = {'requestType': 'gotnewpeer'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        null = None # to be determined
        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )





    #// passthru


class SNET_BTCDpoll(SNET_BaseTest):
    """{'result': 'nothing pending'}
    """

    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_BTCDpoll()


    def test_BTCDpoll(self):
#        null = None #  b'{"result":null}' for when null is sent back, which py doenst know


        #query_json = {'requestType': 'BTCDpoll'}


        print(5*"\n++++++++++++","test_BTCDpoll")
        test_RQ_ = {'requestType': 'BTCDpoll'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )


class SNET_GUIpoll(SNET_BaseTest):
    """{'result': 'nothing pending'}
    """


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_GUIpoll()


    def test_GUIpoll(self):
        #query_json = {'requestType': 'GUIpoll'}

        print(5*"\n++++++++++++","test_GUIpoll")
        test_RQ_ = {'requestType': 'GUIpoll'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )



class SNET_settings(SNET_BaseTest):


    def setUp(self):
        print("SNET_settings setUp here- NOP")
        pass


    def runTest(self):
        self.test_settings()

    def test_settings(self):
                #query_json = {'value': '', 'field': '', 'requestType': 'settings', 'reinit': ''}

        print(5*"\n++++++++++++","test_settings")
        test_RQ_ = {'requestType': 'settings'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)

        # here we can add individual params to the request dict

        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)

        print(rpl777)
        for setting in rpl777:
            print(setting, " - ",rpl777[setting])
        print("\n")

        self.assertGreater(3,2)

        settingsReply="""
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


class ___passthru():
    pass


class SNET_passthru(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_passthru()


    def test_passthru(self):
        #query_json = {'method': '', 'requestType': 'passthru', 'coin': '', 'params': ''}

        print(5*"\n++++++++++++","test_passthru")
        test_RQ_ = {'requestType': 'passthru'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        if 'error' in rpl777.keys():
            self.assertTrue(False)
            print(5*"\n~~~~~~~~~~~~","error in SuperNET rpl777y:\n\n", rpl777)
        else:
            self.assertTrue('result' in rpl777.keys() )





    #// ramchains   13


class SNET_remote(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_remote()


    def test_remote(self):
        #query_json = {'method': '', 'coin': '', 'tag': '', 'result': '', 'requestType': 'remote'}


        print(5*"\n++++++++++++","test_remote")
        test_RQ_ = {'requestType': 'remote'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        if 'error' in rpl777.keys():
            self.assertTrue(False)
            print(5*"\n~~~~~~~~~~~~","error in SuperNET rpl777y:\n\n", rpl777)
        else:
            self.assertTrue('result' in rpl777.keys() )


    #########################



    #     // ramchains 13
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

        print(5*"\n++++++++++++","test_ramstatus")
        test_RQ_ = {'requestType': 'ramstatus'}
        test_RQ_['coin'] = 'BTCD' #

        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        # {'ramchain': 'BTCD : RT.379953 nonz.379950 V.379950 B.379950 B64.379904 B4096.376832 | 116.8MB 18.8MB R6.20 | minutes: V2.8 B2.8 | outputs.929313 187512689.34161791 spends.906780 186307056.66912407 -> balance: 22533 1205632.67249383 ave 53.50520004', 'unspent': '1025344560145', 'result': 'MGWstatus', 'internal': '0', 'coin': 'BTCD', 'balance': '18446744014493961761', 'pendingdeposits': '0', 'RTNXT': {'height': '362110', 'lag': '12', 'ECheight': '362104', 'ECblock': '6414431364385709558'}, 'gatewayid': '-1', 'supply': '0', 'BTCD': {'height': '379953', 'lag': '3', 'permblocks': '379950'}, 'circulation': '1025127150000', 'pendingredeems': '59433000000', 'sentNXT': '15000000000'}

        self.assertTrue('result' in rpl777.keys() )



class SNET_ramaddrlist(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_ramaddrlist()


    def test_ramaddrlist(self):
        #query_json = {'coin': '', 'requestType': 'ramaddrlist'}
#  {'mine': 1, 'total': 1, 'result': 'addrlist', 'multisig': 1}


        print(5*"\n++++++++++++","test_ramaddrlist")
        test_RQ_ = {'requestType': 'ramaddrlist'}
        test_RQ_['coin'] = 'BTCD'
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        if 'error' in rpl777.keys():
            self.assertTrue(False)
            print(5*"\n~~~~~~~~~~~~","error in SuperNET rpl777y:\n\n", rpl777)
        else:
            self.assertTrue('result' in rpl777.keys() )



class SNET_ramstring(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass




    def runTest(self):
        self.test_ramstring()

    def test_ramstring(self):
        #query_json = {'destip': '', 'rawind': '', 'requestType': 'ramstring', 'type': ''}


        print(5*"\n++++++++++++","test_ramstring")
        test_RQ_ = {'requestType': 'ramstring'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        if 'error' in rpl777.keys():
            self.assertTrue(False)
            print(5*"\n~~~~~~~~~~~~","error in SuperNET rpl777y:\n\n", rpl777)
        else:
            self.assertTrue('result' in rpl777.keys() )



class SNET_ramrawind(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_ramrawind()


    def test_ramrawind(self):
        #query_json = {'destip': '', 'coin': '', 'requestType': 'ramblock', 'blocknum': ''}


        print(5*"\n++++++++++++","test_ramrawind")
        test_RQ_ = {'requestType': 'ramrawind'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        if 'error' in rpl777.keys():
            self.assertTrue(False)
            print(5*"\n~~~~~~~~~~~~","error in SuperNET rpl777y:\n\n", rpl777)
        else:
            self.assertTrue('result' in rpl777.keys() )


class SNET_ramblock(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass


    def runTest(self):
        self.test_ramblock()



    def test_ramblock(self):

        print(5*"\n++++++++++++","test_ramblock")
        test_RQ_ = {'requestType': 'ramblock'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        if 'error' in rpl777.keys():
            self.assertTrue(False)
            print(5*"\n~~~~~~~~~~~~","error in SuperNET rpl777y:\n\n", rpl777)
        else:
            self.assertTrue('result' in rpl777.keys() )



class SNET_ramscript(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_ramscript()


    def test_ramscript(self):
        #query_json = {'vout': '', 'destip': '', 'txid': '', 'requestType': 'ramscript', 'txind': '', 'v': '', 'blocknum': ''}


        print(5*"\n++++++++++++","test_ramscript")
        test_RQ_ = {'requestType': 'ramscript'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        if 'error' in rpl777.keys():
            self.assertTrue(False)
            print(5*"\n~~~~~~~~~~~~","error in SuperNET rpl777y:\n\n", rpl777)
        else:
            self.assertTrue('result' in rpl777.keys() )



class SNET_ramtxlist(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_ramtxlist()


    def test_ramtxlist(self):
        #query_json = {'address': '', 'destip': '', 'requestType': 'ramtxlist', 'unspent': '', 'coin': ''}


        print(5*"\n++++++++++++","test_ramtxlist")
        test_RQ_ = {'requestType': 'ramtxlist'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_ramrichlist(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_ramrichlist()


    def test_ramrichlist(self):
        #query_json = {'recalc': '', 'coin': '', 'destip': '', 'requestType': 'ramrichlist', 'numwhales': ''}


        print(5*"\n++++++++++++","test_ramrichlist")
        test_RQ_ = {'requestType': 'ramrichlist'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_ramcompress(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_ramcompress()


    def test_ramcompress(self):
        #query_json = {'data': '', 'destip': '', 'requestType': 'ramcompress', 'coin': ''}


        print(5*"\n++++++++++++","test_x1")
        test_RQ_ = {'requestType': 'ramcompress'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_ramexpand(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_ramexpand()


    def test_ramexpand(self):
        #query_json = {'requestType': 'ramexpand', 'destip': '', 'data': '', 'coin': ''}


        print(5*"\n++++++++++++","test_ramexpand")
        test_RQ_ = {'requestType': 'ramexpand'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_rambalances(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_rambalances()


    def test_rambalances(self):
        #query_json = {'requestType': 'rambalances', 'destip': '', 'rates': '', 'coin': '', 'coins': ''}


        print(5*"\n++++++++++++","test_rambalances")
        test_RQ_ = {'requestType': 'rambalances'}

        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_rampyramid(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_rampyramid()


    def test_rampyramid(self):
        #query_json = {'destip': '', 'requestType': 'rampyramid', 'type': '', 'blocknum': '', 'coin': '', 'port': ''}


        print(5*"\n++++++++++++","test_rampyramid")
        test_RQ_ = {'requestType': 'rampyramid'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )






    # // MGW


class SNET_ramresponse(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_ramresponse()


    def test_ramresponse(self):
        #query_json = {'data': '', 'requestType': 'ramresponse', 'coin': '', 'origcmd': ''}


        null = None #  b'{"result":null}' for when null is sent back, which py doenst know

        print(5*"\n++++++++++++","test_ramresponse")
        test_RQ_ = {'requestType': 'ramresponse'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )




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


        print(5*"\n++++++++++++","test_genmultisig")
        test_RQ_ = {'requestType': 'genmultisig'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )



class SNET_getmsigpubkey(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass




    def runTest(self):
        self.test_getmsigpubkey()

    def test_getmsigpubkey(self):
        #query_json = {'requestType': 'getmsigpubkey', 'myaddr': '', 'refNXTaddr': '', 'coin': '', 'mypubkey': ''}


        print(5*"\n++++++++++++","test_getmsigpubkey")
        test_RQ_ = {'requestType': 'getmsigpubkey'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_MGWaddr(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_MGWaddr()


    def test_MGWaddr(self):
        #query_json = {'requestType': 'MGWaddr'}

        null = None #  b'{"result":null}' for when null is sent back, which py doenst know

        print(5*"\n++++++++++++","test_MGWaddr")
        test_RQ_ = {'requestType': 'MGWaddr'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )



class SNET_MGWresponse(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_MGWresponse()


    def test_MGWresponse(self):
        #query_json = {'requestType': 'MGWresponse'}

        null = None #  b'{"result":null}' for when null is sent back, which py doenst know

        print(5*"\n++++++++++++","test_MGWresponse")
        test_RQ_ = {'requestType': 'MGWresponse'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_setmsigpubkey(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_setmsigpubkey()


    def test_setmsigpubkey(self):

            #query_json = {'refNXTaddr': '', 'addr': '', 'pubkey': '', 'requestType': 'setmsigpubkey', 'coin': ''}

        null = None #  b'{"result":null}' for when null is sent back, which py doenst know

        print(5*"\n++++++++++++","test_setmsigpubkey")
        test_RQ_ = {'requestType': 'setmsigpubkey'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_cosign(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_cosign()


    def test_cosign(self):
        #query_json = {'text': '', 'requestType': 'cosign', 'seed': '', 'otheracct': ''}


        print(5*"\n++++++++++++","test_cosign")
        test_RQ_ = {'requestType': 'cosign'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )






    # // IPcomms(MGW)


class SNET_cosigned(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_cosigned()


    def test_cosigned(self):
        #query_json = {'privacct': '', 'result': '', 'seed': '', 'pubacct': '', 'requestType': 'cosigned'}


        print(5*"\n++++++++++++","test_cosigned")
        test_RQ_ = {'requestType': 'cosigned'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )

#ping

    #########################




    #     // IPcomms 5

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
        print(5*"\n++++++++++++","test_ping")
        test_RQ_ = {'requestType': 'ping'}
        test_RQ_['destip'] = destip #'localhost'
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_pong(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_pong()


    def test_pong(self):
        null=None
                #query_json = {'port': '', 'pubkey': '', 'yourip': '', 'requestType': 'pong', 'yourport': '', 'ipaddr': '209.126.70.156'}

        print(5*"\n++++++++++++","test_pong")
        test_RQ_ = {'requestType': 'pong'}
        test_RQ_['ipaddr'] = '209.126.70.156'

        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )




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


        print(5*"\n++++++++++++","test_sendfrag")
        test_RQ_ = {'requestType': 'sendfrag'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        if 'error' in rpl777.keys():
            self.assertTrue(False)

        self.assertTrue('result' in rpl777.keys() )



class SNET_gotfrag(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_gotfrag()


    def test_gotfrag(self):
# query json is:  {'fragi': '', 'totalcrc': '', 'name': '', 'blocksize': '', 'datacrc': '', 'handler': '', 'numfrags': '', 'totallen': '', 'ipaddr': '', 'count': '', 'requestType': 'sendfrag', 'pubkey': ''}

        print(5*"\n++++++++++++","test_gotfrag")
        test_RQ_ = {'requestType': 'gotfrag'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



    # // Kademlia DHT


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

        print(5*"\n++++++++++++","test_startxfer")
        test_RQ_ = {'requestType': 'startxfer'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )

        #query_json = {'requestType': 'startxfer', 'fname': '', 'timeout': '', 'handler': '', 'dest': '', 'data': ''}

        # {'result': 'pending SuperNET API call', 'txid': '2466605655551381573'}



class SNET_getfile(SNET_BaseTest):


    def setUp(self):
        print(" test getfile func here")
        pass



    def runTest(self):
        self.test_getfile()


    def test_getfile(self):



#  static char *getfile[] = { (char *)getfile_func, "getfile", "V", "name", "handler", 0 };
#
        print(5*"\n++++++++++++","test_getfile")
        test_RQ_ = {'requestType': 'getfile'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



    #########################




    #     // Kademlia DHT 8

    #########################

class __Kademlia():
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
        print(5*"\n++++++++++++","test_store")

        n1 = self.msg()
        n2 = n1.encode("utf-8")
        n2 = binascii.hexlify(n2)
        n3 = n2.decode("utf-8")
        test_RQ_store = {'requestType': 'store'}
        test_RQ_store['name']='testStoreName' + str(int(time.time())) #n1

        test_RQ_store['data']=n3


        payload= self.qComp_777.make_777POST_Request(test_RQ_store)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )




class SNET_findvalue(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_findvalue()


    def test_findvalue(self):
        #query_json = {'data': '', 'key': '', 'name': '', 'requestType': 'findvalue', 'pubkey': ''}

        #reqData1['key'] = self.storedVals[key]
        print(5*"\n++++++++++++","test_findvalue")
        test_RQ_findvalue = {'requestType': 'findvalue'}
        test_RQ_findvalue['key'] = '2685049983433793128'
        #test_RQ_findvalue[''] = ''
        payload= self.qComp_777.make_777POST_Request(test_RQ_findvalue)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        foundVal=rpl777['data']
        #foundVal = foundVal.decode("utf-8")
        foundVal = binascii.a2b_hex(foundVal)

        print(foundVal)


        self.assertTrue('data' in rpl777.keys() )





class SNET_findnode(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_findnode()


    def test_findnode(self):

        print(5*"\n++++++++++++","test_findnode")
        test_RQ_ = {'requestType': 'findnode'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_havenode(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_havenode()


    def test_havenode(self):

        print(5*"\n++++++++++++","test_havenode")
        test_RQ_ = {'requestType': 'havenode'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

# {'error': 'invalid havenode_func arguments'}
# F

        self.assertTrue('result' in rpl777.keys() )


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
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        self.assertTrue('peers' in rpl777.keys())

        peers = rpl777['peers']
        for peer in peers[2:]:
            print(peer,"\n")
            psrv = peer['pserver']
            srvNXT = peer['srvNXT']
            print(psrv,"\n")
            print(srvNXT,"\n")
           #log.msg(1*"\n FINDNODE peer:", srvNXT)



        print(5*"\n++++++++++++","test_findaddress")
        testRQ_findaddress = {'requestType': 'findaddress'}

        testRQ_findaddress['refaddr'] = srvNXT #'14083245880221951726' #srvNXT
        testRQ_findaddress['dist'] = 32
        testRQ_findaddress['duration'] = 11
        testRQ_findaddress['numthreads'] = 2

        payload= self.qComp_777.make_777POST_Request(testRQ_findaddress)


        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )


class SNET_havenodeB(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_havenodeB()


    def test_havenodeB(self):
        #query_json = {'pubkey': '', 'name': '', 'data': '', 'key': '', 'requestType': 'havenodeB'}


        print(5*"\n++++++++++++","test_havenodeB")
        test_RQ_ = {'requestType': 'havenodeB'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )




###


class SNET_puzzles(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_puzzles()


    def test_puzzles(self):

#
# static char *puzzles[] = { (char *)challenge_func, "puzzles", "V", "reftime", "duration", "threshold", 0 };


        print(5*"\n++++++++++++","test_puzzles")
        test_RQ_ = {'requestType': 'puzzles'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )

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


        print(5*"\n++++++++++++","test_nonces")
        test_RQ_ = {'requestType': 'nonces'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )

    # // MofNfs

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


        print(5*"\n++++++++++++","test_savefile")
        test_RQ_ = {'requestType': 'savefile'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_restorefile(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_restorefile()


    def test_restorefile(self):
        #query_json = {'password': '', 'backup': '', 'sharenrs': '', 'restorefile': 'stop', 'destfile': '', 'filename': '', 'pin': '', 'L': '', 'N': '', 'txids': '', 'M': ''}

        null = None #  b'{"result":null}' for when null is sent back, which py doenst know

        print(5*"\n++++++++++++","test_restorefile")
        test_RQ_ = {'requestType': 'restorefile'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_publish(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_publish()


    def test_publish(self):
        #query_json = {'L': '', 'backup': '', 'files': '', 'N': '', 'pin': '', 'requestType': 'publish', 'M': ''}

        print(5*"\n++++++++++++","test_publish")
        test_RQ_ = {'requestType': 'publish'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )





    # // Telepathy

    #########################
    #     // Telepathy 9
    #########################


class ___Telepathy():
    pass



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
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        self.assertTrue('peers' in rpl777.keys())

        peers = rpl777['peers']
        for peer in peers[2:]:
            print(peer)
            psrv = peer['pserver']
            srvNXT = peer['srvNXT']
            print(psrv)
            print(srvNXT)
           #log.msg(1*"\n FINDNODE peer:", srvNXT)



        print(5*"\n++++++++++++","test_addcontact")
        testRQ_addcontact = {'requestType': 'addcontact'}
        testRQ_addcontact['acct'] = srvNXT
        testRQ_addcontact['handle'] = "myTestHandle"  #+ str(time.time())


        payload= self.qComp_777.make_777POST_Request(testRQ_addcontact)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)



        self.assertTrue('result' in rpl777.keys() )
        self.assertTrue('pubkey' in testReq.text )




        print(5*"\n++++++++++++","test_dispcontact")
        testRQ_dispcontact = {'requestType': 'dispcontact'}
        #test_dispcontact['acct'] =
        testRQ_dispcontact['contact'] =  'myTestHandle' # "myTestHandle"  #+ str(time.time())


        payload= self.qComp_777.make_777POST_Request(testRQ_dispcontact)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('handle' in rpl777.keys() )


        print(5*"\n++++++++++++","test_RQ_removecontact")
        test_RQ_removecontact = {'requestType': 'removecontact'}
        #test_dispcontact['acct'] =
        test_RQ_removecontact['contact'] =  'myTestHandle' # "myTestHandle"  #+ str(time.time())


        payload= self.qComp_777.make_777POST_Request(test_RQ_removecontact)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )
        self.assertTrue('deleted' in testReq.text )




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
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        self.assertTrue('peers' in rpl777.keys())

        peers = rpl777['peers']
        for peer in peers[2:]:
            print(peer)
            psrv = peer['pserver']
            srvNXT = peer['srvNXT']
            print(psrv)
            print(srvNXT)
           #log.msg(1*"\n FINDNODE peer:", srvNXT)



        print(5*"\n++++++++++++","test_addcontact")
        testRQ_addcontact = {'requestType': 'addcontact'}
        testRQ_addcontact['acct'] = srvNXT
        testRQ_addcontact['handle'] = "myTestHandle"  #+ str(time.time())


        payload= self.qComp_777.make_777POST_Request(testRQ_addcontact)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )
        self.assertTrue('pubkey' in testReq.text )





        print(5*"\n++++++++++++","test_dispcontact")
        testRQ_dispcontact = {'requestType': 'dispcontact'}
        #test_dispcontact['acct'] =
        testRQ_dispcontact['contact'] =  'myTestHandle' # "myTestHandle"  #+ str(time.time())


        payload= self.qComp_777.make_777POST_Request(testRQ_dispcontact)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('handle' in rpl777.keys() )


        print(5*"\n++++++++++++","test_RQ_removecontact")
        test_RQ_removecontact = {'requestType': 'removecontact'}
        #test_dispcontact['acct'] =
        test_RQ_removecontact['contact'] =  'myTestHandle' # "myTestHandle"  #+ str(time.time())


        payload= self.qComp_777.make_777POST_Request(test_RQ_removecontact)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )
        self.assertTrue('deleted' in testReq.text )



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
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        self.assertTrue('peers' in rpl777.keys())

        peers = rpl777['peers']
        for peer in peers[2:]:
            print(peer)
            psrv = peer['pserver']
            srvNXT = peer['srvNXT']
            print(psrv)
            print(srvNXT)
           #log.msg(1*"\n FINDNODE peer:", srvNXT)



        print(5*"\n++++++++++++","test_addcontact")
        testRQ_addcontact = {'requestType': 'addcontact'}
        testRQ_addcontact['acct'] = srvNXT
        testRQ_addcontact['handle'] = "myTestHandle"  #+ str(time.time())


        payload= self.qComp_777.make_777POST_Request(testRQ_addcontact)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )
        if 'unchanged' in testReq.text:
            self.assertTrue(True)
        else:
            self.assertTrue('pubkey' in testReq.text )


        print(5*"\n++++++++++++","test_dispcontact")
        testRQ_dispcontact = {'requestType': 'dispcontact'}
        #test_dispcontact['acct'] =
        testRQ_dispcontact['contact'] =  'myTestHandle' # "myTestHandle"  #+ str(time.time())


        payload= self.qComp_777.make_777POST_Request(testRQ_dispcontact)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('handle' in rpl777.keys() )


        print(5*"\n++++++++++++","test_RQ_removecontact")
        test_RQ_removecontact = {'requestType': 'removecontact'}
        #test_dispcontact['acct'] =
        test_RQ_removecontact['contact'] =  'myTestHandle' # "myTestHandle"  #+ str(time.time())


        payload= self.qComp_777.make_777POST_Request(test_RQ_removecontact)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )
        self.assertTrue('deleted' in testReq.text )



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

        print(5*"\n++++++++++++","test_telepathy")
        test_RQ_ = {'requestType': 'telepathy'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



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


        print(5*"\n++++++++++++","test_getdb")
        test_RQ_ = {'requestType': 'getdb'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



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
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        self.assertTrue('peers' in rpl777.keys())

        peers = rpl777['peers']
        for peer in peers[2:]:
            print(peer)
            psrv = peer['pserver']
            srvNXT = peer['srvNXT']
            print(psrv)
            print(srvNXT)
           #log.msg(1*"\n FINDNODE peer:", srvNXT)



        print(5*"\n++++++++++++","test_sendmessage")
        test_RQ_sendmessage = {'requestType': 'sendmessage'}
        test_RQ_sendmessage['dest'] = srvNXT
        test_RQ_sendmessage ['msg'] = msg


        payload= self.qComp_777.make_777POST_Request(test_RQ_sendmessage)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)



        self.assertTrue('status' in rpl777.keys() )
        self.assertTrue('sends encrypted sendmessage to' in rpl777['status'] )





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
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
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

        print(5*"\n++++++++++++","   ")
        test_RQ_sendbinary = {'requestType': 'sendbinary'}
        test_RQ_sendbinary['dest'] = srvNXT
        test_RQ_sendbinary ['data'] = binSpam


        payload= self.qComp_777.make_777POST_Request(test_RQ_sendbinary)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)



        self.assertTrue('status' in rpl777.keys() )
        self.assertTrue('sends encrypted sendmessage to' in rpl777['status'] )




class SNET_checkmsg(SNET_BaseTest):


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
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)
        self.assertTrue('peers' in rpl777.keys())

        peers = rpl777['peers']
        for peer in peers[2:]:
            print(peer)
            psrv = peer['pserver']
            srvNXT = peer['srvNXT']
            print(psrv)
            print(srvNXT)
           #log.msg(1*"\n FINDNODE peer:", srvNXT)



        print(5*"\n++++++++++++","test_sendmessage")
        test_RQ_sendmessage = {'requestType': 'sendmessage'}
        test_RQ_sendmessage['dest'] = srvNXT
        test_RQ_sendmessage ['msg'] = msg


        payload= self.qComp_777.make_777POST_Request(test_RQ_sendmessage)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        #
        #
        #


        query_json = {'sender': '', 'requestType': 'checkmsg'}

        null = None #  b'{"result":null}' for when null is sent back, which py doenst know

        for peer in peers[2:]:
                    print(peer)
                    psrv = peer['pserver']
                    srvNXT = peer['srvNXT']
                    print(psrv)
                    print(srvNXT)
                   #log.msg(1*"\n FINDNODE peer:", srvNXT)


        print(5*"\n++++++++++++","test_checkmsg")
        testRQ_checkmsg = {'requestType': 'checkmsg'}
        testRQ_checkmsg['sender'] = srvNXT #= peer['srvNXT']

        payload= self.qComp_777.make_777POST_Request(testRQ_checkmsg)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )








    # // Teleport



    #########################





    #     // Teleport 3
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

        print(5*"\n++++++++++++","test_maketelepods")
        test_RQ_ = {'requestType': 'maketelepods'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )


class SNET_telepodacct(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_telepodacct()


    def test_telepodacct(self):

        #query_json = {'amount': '', 'comment': '', 'coin': '', 'contact': '', 'cmd': '', 'requestType': 'telepodacct', 'withdraw': ''}

# {'result': 'pending SuperNET API call', 'txid': '13468243516026239723'}

        print(5*"\n++++++++++++","test_telepodacct")
        test_RQ_ = {'requestType': 'telepodacct'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )


class SNET_teleport(SNET_BaseTest):

    def setUp(self):
        print(" test setUp func here")
        pass

    def runTest(self):
        self.test_teleport()

    def test_teleport(self):
        #query_json = {'coin': '', 'minage': '', 'requestType': 'teleport', 'amount': '', 'contact': '', 'withdraw': ''}
		# {'result': 'pending SuperNET API call', 'txid': '12100319098835243886'}

        print(5*"\n++++++++++++","test_teleport")
        test_RQ_ = {'requestType': 'teleport'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )




    #     Tradebot 3
    #########################

class ___Tradebot():
    pass


class SNET_pricedb(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_pricedb()


    def test_pricedb(self):

        #query_json = {'rel': '', 'stop': '', 'requestType': 'pricedb', 'exchange': '', 'base': ''}

# {'error': 'bad pricedb paramater'}


        print(5*"\n++++++++++++","test_pricedb")
        test_RQ_ = {'requestType': 'pricedb'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_getquotes(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_getquotes()


    def test_getquotes(self):

        #query_json = {'requestType': 'getquotes', 'base': '', 'rel': '', 'oldest': '', 'exchange': ''}


# {'error': 'bad getquotes paramater'}


        print(5*"\n++++++++++++","test_getquotes")
        test_RQ_ = {'requestType': 'getquotes'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )



class SNET_tradebot(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_tradebot()


    def test_tradebot(self):
        #query_json = {'code': '', 'requestType': 'tradebot'}


# {'result': 'invalid tradebot request'}



        print(5*"\n++++++++++++","test_tradebot")
        test_RQ_ = {'requestType': 'tradebot'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )




    # // # privatebet

class ___Privatebet():
    pass


    # // Embedded Langs
class ___EmLang():
    pass





#########################
#    InstantDEX 8
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



class SNET_python(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass


    def runTest(self):
        self.test_python()



    def test_python(self):
        #query_json = {'requestType': 'python', 'name': ''}

# {'result': None}


        null = None #  b'{"result":null}' for when null is sent back, which py doenst know

        print(5*"\n++++++++++++","test_python")
        test_RQ_ = {'requestType': 'python'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )


class SNET_syscall(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass

    def runTest(self):
        self.test_syscall()


    def test_syscall(self):
        #query_json = {'name': '', 'requestType': 'syscall', 'cmd': ''}


        null = None #  b'{"result":null}' for when null is sent back, which py doenst know

        print(5*"\n++++++++++++","test_syscall")
        test_RQ_ = {'requestType': 'syscall'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}

        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )
        
        
        
##############################################
##############################################
#
#	All SuperNET API Call functions
#
#
##############################################
##############################################
class SNET_apicalls():

    ##############################################
	##############################################
	#
	#	todo: Other API Calls
	#
	#
	##############################################
	##############################################
	
    
    
    
    NXTASSETS = [
    {
        "name": "1000BURST", 
        "asset": "251006016744564741", 
        "description": "Each one 1000BURST asset represents 1000 (one thousand) BURST coins. To obtain these assets just send your BURST coins to the BURTS Gateaway address BURST-MCHC-LBKK-ZLZY-C3XL5 _and_ send an Arbitrary Message containing your NXT address (in alpha-numeric format) to the same address. To withdraw your 1000BURST assets you should transfer them to this issuing account (NXT-VVTV-U25N-U2FY-2V35H) _and_ in the attached message place your BURST address (in alpha-numeric format). More info can be found here: https://bitcointalk.org/index.php?topic=731923.msg8381305#msg8381305"
    }, 
    {
        "name": "1000FIM", 
        "asset": "12404894802398759379", 
        "description": "Each 1000FIM asset represents 1000 FIM coins. To obtain these assets send your FIM coins to FIM-SESR-CDCR-F86V-A2ABQ _and_ send an Arbitrary Message containing your NXT address (in Reed Solomon format) to the same address (FIM-SESR-CDCR-F86V-A2ABQ). In order to guarantee smooth withdrawals, the amount of the 1000FIM assets in circulation will always be less then the balance of FIM-SESR-CDCR-F86V-A2ABQ. To withdraw your 1000FIM assets transfer them to NXT-M667-6GVL-3JNZ-GRN96 _and_ in the attached message place your FIM address (in Reed Solomon format). More info can be found here: https://bitcointalk.org/index.php?topic=633304.msg8097620#msg8097620"
    }, 
    {
        "name": "ATOMIC", 
        "asset": "11694807213441909013", 
        "description": "Atomic is a NXTventure project with the official thread at https://bitcointalk.org/index.php?topic=780833.msg8800442#msg8800442"
    }, 
    {
        "name": "AutoDiv", 
        "asset": "1434237137246193127", 
        "description": "A steady stream of automatic dividends paid daily. Details here: http://tiny.cc/91oisx"
    }, 
    {
        "name": "AutoDiv3", 
        "asset": "6924643464789677166", 
        "description": "AutoDiv3 is a weekly income fund. Objective (3.0%-6.5%) Details here: http://tiny.cc/91oisx"
    }, 
    {
        "name": "BGCAFFE", 
        "asset": "2978798152942226372", 
        "description": "The first Buongiorno Caffe opened November 2013 in Pretoria, South Africa. We are committed to providing high quality food for our customers in a \r\nsustainable way, doing our best to improve both their well-being and the planet we all live on. Part of this journey is sourcing the best possible ingredients from local producers, ensuring our staff are part of the business and benefit from their energy and creativity and most importantly building a better community.\r\n\r\nWe would love you all to become part of our community and listing on NextCoin AE is the first step in that direction. Lets take this exciting step together and see where our journey takes us :)\r\n\r\nPlease see Buongiorno Caffe's website for more detail: http://www.buongiorno-caffe.co.za\r\n\r\nSPECIAL THANKS!\r\nThe team at Buongiorno Caffe would like to send a heartfelt thanks to the NextCoin developers and community for working so hard to bring the amazing possibilities of crypto currencies into the hands of the people!"
    }, 
    {
        "name": "BearMining", 
        "asset": "16866116529232450550", 
        "description": "No-fee direct mining asset. Please see our discussion thread on the forums for more information."
    }, 
    {
        "name": "Bithaus", 
        "asset": "13926712251908664867", 
        "description": "Each asset represents .0001% of bithaus profits. As profits from bithaus come in, they will be distributed to asset holders. please refer to bithaus themselves for info on their business.\r\nThere are a total of 40% bithaus profit assets issued for a total of 400000, but most are parked in the Parkinglot account 6917879084634468097\r\nThe only bithaus assets that are released from the parkinglot acct are the ones bound to actual bithaus profit shares. Initially it will be comprised of my personal 1.8% (18000) and also some of aldrin's shares. contact jl777 if you want to bind your bithaus profit sharing with this bithaus asset"
    }, 
    {
        "name": "CBOOKING", 
        "asset": "13159456840724391314", 
        "description": "CoinBooking.net - Vacation Rental Listings platform | List your property for cryptocurrency. This project is developed by CoinEvolve.com. Note that this project is separated from SuperNET Partnerhip. This project does not share profit with SuperNET"
    }, 
    {
        "name": "CELL", 
        "asset": "18212211773827322818", 
        "description": "https://asset.cryptomining.farm"
    }, 
    {
        "name": "CNTROPOLIS", 
        "asset": "17321741837176104160", 
        "description": "ConnectTropolis by CoinTropolis is the combination of 4 different services that not only grow our exposure to all 300+ coin communities, but help us work with businesses that could use guidance in marketing, project management or business development.This will also allow us to showcase how Nxt can become the basis for a stable and relevant platform from which to build upon.\r\n\r\nConnectTropolis virtual token holders will be rewarded a percentage based on the number of tokens held. The reward pool will consist of 50% of the coins earned by the ConnectTropolis services outlined in detail in the links below.\r\n\r\nDetails about virtual tokens:\r\nhttps://nxtforum.org/assets-board/official-cointropolis-launch-1pm-today-us-eastern/\r\n\r\nAbout CoinTropolis:\r\nhttp://www.cointropolis.com/"
    }, 
    {
        "name": "CoinoUSD", 
        "asset": "12982485703607823902", 
        "description": "CoinoUSD is a non-dividend paying asset tied to US dollar, one CoinoUSD equals one dollar. In- and out-exchange of it is carried out at Coinomat.com. The objective of CoinoUSD is to create NXT/USD market directly on NXT asset exchange. Besides, it allows for value transfer in USD on NXT blockchain."
    }, 
    {
        "name": "Coinomat", 
        "asset": "6220108297598959542", 
        "description": "Coinomat.com is an instant cryptocurrency exchange service. Coinomat.com seeks external funding through virtual IPO to enhance its operating capital and implement several new services aimed at transaction volume and revenue growth.   IPO is carried out at several platforms, including NXT platform. Our mission consists in offering frictionless customer experience in the area of cryptocurrency transactions. Our business model is built on offering fixed rate services for cryptocurrency exchanges and charging premium for the transaction speed and comfort. Our competitive advantage is the current lack of similar services and our clear profit structure, based on hedging cryptocurrency volatility effects. \r\n\r\nCoinomat.com offers its shareholders profits equal to 1.5% of the total transaction amount. Users can have access to our transactions stats here: http://coinomat.com/globalstat.php\r\n\r\nThe dividend payments are made weekly."
    }, 
    {
        "name": "Coinomat1", 
        "asset": "7474435909229872610", 
        "description": "This is the secondary offering of Coinomat asset. \r\nCoinomat.com is an instant cryptocurrency exchange service. in July of 2014 NXT cryptocurrency transactions have been integrated in Coinomat.com services, including NXT withdrawals to bank cards.\r\n\r\nTotal volume of the initial and secondary IPO is equal to 7000000 NXT.\r\nCoinomat.com offers its shareholders profit equal to 1.5% of the total transaction amount. Users can have access to our transactions stats here: http://coinomat.com/globalstat.php. The dividend payments are made weekly on Mondays."
    }, 
    {
        "name": "ColdHash", 
        "asset": "11632121299907478243", 
        "description": "Diversified cloud mining asset. Details at https://nxtforum.org/asset-exchange-general/(ann)-coldhash/"
    }, 
    {
        "name": "DORCS", 
        "asset": "2318361924203311027", 
        "description": "1. DORCS ASSETS are bearer assets issued via a digitally signed certificate\r\non the NXT AE.\r\n2. The issuer maintains no records of who owns the assets.\r\n3. Ownership is transferred by transferring the digital certificate\r\nrepresenting a particular asset.\r\n4. Whoever can demonstrate ownership of the private-key securing the\r\ncertificate is presumed to own the asset.\r\nFor a more detailed description of the Asset, please refer to http://www.dorcsgames.com/nxtaedescription/"
    }, 
    {
        "name": "DeBuNe", 
        "asset": "6926770479287491943", 
        "description": "DeBuNe, the Decentrilised Business Network, combines the power of Nxt blockchain and powerful software frameworks to a modular, agile, worldwide business network beneficial to both members and clients. Some non core DeBuNe functionalities (centralised in external websites) will require a fee to be used. Dividends will be paid starting July 2015. Info on http://debune.org"
    }, 
    {
        "name": "DroneMine", 
        "asset": "4087414277501042216", 
        "description": "Create drones to mine raw materials from Earth, Ocean & Space. An interactive online overlay environment will be created to allow the drones to be directed by users and interact with the real world.Concept: Interface environ to interact with drones by site users.Drones will be developed to function in a sandbox environment during the alpha. Release C&C centers, Manufacturing Facilities and Material Drop-off point locations. % of raw material sales will be kept as a fee for providing the Drop-off points. Dividends will be paid out to all shareholders after each sale. Shareholders will have voting rights in the company. No other shares will be created unless voted and approved by the majority of shareholders using the voting system in the DAC. Goal is to create a DAC in the NXT ecosystem. Each share of DroneMine represents of 1/1,000,000th of 30% of yearly profits to be paid out as dividends. Initial IPO funds will be used for liquidity.Profit Split: 30% R&D/40% reinvest/30% dividends"
    }, 
    {
        "name": "EVOLVE", 
        "asset": "3574526501061878636", 
        "description": "http://coinevolve.com - A group of developers working full time on developing various services for cryptocurrency. We aim to make your cryptocurrency a bit more useful and generate some profit in the same time"
    }, 
    {
        "name": "EVOLVE2", 
        "asset": "3643966800021258206", 
        "description": "EVOLVE Shares for latecomers - http://coinevolve.com - A group of developers working full time on developing various services for cryptocurrency. We aim to make your cryptocurrency a bit more useful and generate some profit in the same time"
    }, 
    {
        "name": "FIMventure", 
        "asset": "8501115346481349929", 
        "description": "FIMventure makes private investments in promising enterprises and adds value to each investment. FIMventure forging and trading FIM (fork NXT). FIMventure will pay 3-5% monthly dividends in the assets or NXT it acquires, net of trading activities during the all period. Send Message NXT-USCH-VC7D-4EX3-272SG if you are seeking investment."
    }, 
    {
        "name": "ForgeCoin", 
        "asset": "5934798443252900551", 
        "description": "Mine with cheap electricity! \r\nTotal 175 Slots at this phase. 145 Slots (83%) selling at IPO.\r\nEach Asset (Slot) is a 180 GH/s S1 AntMiner in a country with about $0.01/KWh.\r\nROI is about 4 Months from IPO Date. Dividends will pay Weekly. \r\nYou can pay or receive dividends in BTC or NXT.\r\nMore info: http://forgeco.in"
    }, 
    {
        "name": "FreeMarket", 
        "asset": "134138275353332190", 
        "description": "FreeMarket is a decentralized marketplace that supports physical items for an initial fixed listing cost of 7.77 NXT. Please check the official website http://nxtfreemarket.com and the official thread https://nxtforum.org/index.php?topic=5408.0 for any changes and updates. A 20% revenue sharing agreement with SuperNET allows for 80% of the listing fees to be distributed as dividends."
    }, 
    {
        "name": "Freebsrvrs", 
        "asset": "784050511394255426", 
        "description": "Freebieservers is hereby issuing 1 million shares for 5 percent profit shares of freebieservers.com's net profit. Dividends will be paid out on the 15th of every month , 6 months from now. With a clientele that spans across the globe, Freebie Servers is one of the hottest start-ups to be involved in the Nxt Ecosystem. \r\n\r\n\r\nRead more at : https://nxtforum.org/asset-exchange-general/freebieservers-com-75-000-users-and-growing!/"
    }, 
    {
        "name": "FunBotReve", 
        "asset": "3930224606324455741", 
        "description": "This asset will receive 30% of all profits generated through the FunBotV1 project asset: 502090591603781088. More details can be found here: https://nxtforum.org/index.php?topic=5638.0"
    }, 
    {
        "name": "FunBotV1", 
        "asset": "502090591603781088", 
        "description": "This is the official FunBotV1 asset. An automated trading bot is used to generate profits, that are distributed as dividends. More details can be found here: https://nxtforum.org/index.php?topic=5638.0"
    }, 
    {
        "name": "HRLTCGear", 
        "asset": "10890135065820123998", 
        "description": "Hashrate.org LTCGear Shares\r\nPlease see: http://tinyurl.com/HRLTCGear for asset information."
    }, 
    {
        "name": "HRNXTPool", 
        "asset": "17166680677145186899", 
        "description": "Each asset represents .001% fractional ownership of the private Hashrate.org NXT mining pool. Up to date details can be found at http://tiny.cc/9m1yix"
    }, 
    {
        "name": "InstantDEX", 
        "asset": "15344649963748848799", 
        "description": "There are a total of 1 million InstantDEX assets. The goal of InstantDEX is to offer realtime trading of NXT, NXT assets and other cryptos. It will earn fees from commissions on the trades. By keeping costs low by using a decentralized infrastructure, it is expected to be able to distribute approximately half of revenues to asset holders.\r\n\r\nplease refer to nxtforum.org for up to date details"
    }, 
    {
        "name": "Jinn", 
        "asset": "3061160746493230502", 
        "description": "www.jinnlabs.com"
    }, 
    {
        "name": "KPS", 
        "asset": "10941619155761914846", 
        "description": "Kongzi Print Shop"
    }, 
    {
        "name": "LAND", 
        "asset": "11225580336549701867", 
        "description": "Borzalom ! Virtual world turns into reality.\r\nThis is an area developer game.\r\nA total of 33 million shares are released.\r\nA LAND asset is equal to 1 x 1 cm of real land area.\nBefore purchasing read the terms and conditions and up to date details located at borzalom.hu"
    }, 
    {
        "name": "LIQUID", 
        "asset": "4630752101777892988", 
        "description": "Liquid Technologies implements custom software solutions for trading cryptocurrency markets.  Please see http://www.liquidtech.info for more details. LIQUID ASSETS are bearer assets issued via a digitally signed certificate on the NXT AE. The issuer maintains no records of who owns the assets. Ownership is transferred by transferring the digital certificate representing a particular asset. Whoever can demonstrate ownership of the private-key securing the certificate is presumed to own the asset."
    }, 
    {
        "name": "LOVE", 
        "asset": "12358227497921853690", 
        "description": "Love is one of the first and best virtual goods ever! Spend it generously with your loved ones. Love is specifically not for getting rich. It's for spreading, baby! Love is available in huge quantities but still you need to search for it. If you find it you will be amazed by its value."
    }, 
    {
        "name": "LTCshare2G", 
        "asset": "2128300325778905751", 
        "description": "LTCshare2G provides affordable, reliable Scrypt cloud mining and will INCREASE payouts and hashrate over time. Initial hashrate is 2 GH/s mining LTC. 35% of profits will be re-invested to increase hashrate and 65% will be paid out in dividends weekly. This gives the majority of income back to investors for fast ROI and increases hashrate faster than the projected difficulty increase of LTC. This ratio could be adjusted by majority vote. 0.1 MH/s per share at launch, increasing each week. Please see https://nxtforum.org/asset-exchange-general/ann-ltcshares/ for more information and weekly profitability/dividend reports."
    }, 
    {
        "name": "MGW", 
        "asset": "10524562908394749924", 
        "description": "each MGW asset represents .0001% of multigateway\r\nmultigateway will generate minimal fees from deposits and withdraws of cryptos into NXT AE. It uses a separate multisig acct for each depositor. It will have ongoing server costs and to minimize the cost of depositing and withdrawing crypto assets into NXT, it will keep fees as low as possible. Currently its projected revenue source will be via auctions for listing altcoins and altcoin giveaways. Such revenues received net of operating costs will be distributed to asset holders.\r\nmultigateway isnt a non-profit, but it also isnt designed to be a massive profit generator. Any investment in multigateway will help cover operating costs and help the NXT community."
    }, 
    {
        "name": "MIC", 
        "asset": "4469670021276890463", 
        "description": "The most interesting coin in the world"
    }, 
    {
        "name": "MMNXT", 
        "asset": "979292558519844732", 
        "description": "Market-making fund for NXT AE: https://nxtforum.org/assets-board/mmnxt-market-making-and-arbitrage-fund-for-nxt-ae/"
    }, 
    {
        "name": "NEMstake", 
        "asset": "12465186738101000735", 
        "description": "A NEMstake token represents one million NEM receivable after the official launch of NEM blockchain. The token can be traded down to one digit after zero (minimum unit is 1/10 of a token). Our website is www.ournem.com. Please read about NEM, NEMstake token and the conversion rules in our dedicated thread before buying NEMstake. The issuing account is NXT-J62B-CNAR-34YW-4RCFN."
    }, 
    {
        "name": "NHZ", 
        "asset": "3733170523104676119", 
        "description": "This is the (first) official NHZ ( http://nhzcrypto.org ) Asset. \r\n\r\nNHZ is a fork of NXT. The NHZ blockchain started on 03-22-2014. It has the same parameters as NXT and follows NXT releases after a small delay. Our own features will be added over time. \r\n\r\nNHZ is distributed by a bounty system. The current distribution state can be seen on the block explorer. If you want to earn NHZ, take a look at the bounties on our forum. You can of course also come with your own ideas how you could be useful for NHZ.\r\n\r\nWe don't expect all NHZ to end up here, so there are only 100M units of the asset, each worth 1 NHZ.\r\nTo withdraw, send your assets to NXT-S7CP-4FZC-5T8B-H7UPF and add your numeric NHZ account ID - and nothing else! - to the comment field.\r\nFor deposits and further information about the asset as well as the current fee go to http://asx.nhzcrypto.org \r\n\r\nAlways check the issuer and asset ID! Be sure not to buy assets from copycats! The asset issuer account will never sell assets!"
    }, 
    {
        "name": "NNG", 
        "asset": "1013693125509851736", 
        "description": "NNG (NewNxtGames) develops browser games on top of Nxt. For more information visit www.NewNxtGames.com or contact NewNxtGames on NXTforum.org."
    }, 
    {
        "name": "NSC", 
        "asset": "6775372232354238105", 
        "description": "[NSC]\r\nNXT Security Coin:\r\nNSC is created to help securing the network by adding more value to forging fees. NSC is distributed weekly to every Block Generator. Payout is 1 NSC for every forged block by an accout ID. Every account ID have a cap of x NSC per 1440 Blocks, Public Forging Pools don't have a cap! The future value of this first tradeable AE-Coin depends on the community, the more value the more forgers secure the network. The Asset Holder will only sell NSC to cover the Asset transfer fees. To all stake holders, please help to give this Coin a value, thank you! The start value should be around 0.10 EUR. More information on https://nxtforum.org"
    }, 
    {
        "name": "NXTCS", 
        "asset": "12658817572699179955", 
        "description": "NXTCS is a callback service for developers. We will watch your account and call your defined URLs at specific events like receiving payments. You get all infos for processing in a JSON posted to your script. More details at: https://nxtforum.org/index.php?topic=6982.0"
    }, 
    {
        "name": "NXTInspect", 
        "asset": "14273984620270850703", 
        "description": "This asset is represents the right to a share in the profits from the activities of NXTinspect, you can find more information about it here https://nxtforum.org/index.php?topic=5655.msg109465#msg109465"
    }, 
    {
        "name": "NXTMINING", 
        "asset": "15953898000415537360", 
        "description": "Only 18250 virtual tokens issued. Each virtual token corresponds to a value equivalent to a qasic share on ltcgear.com. “NXTMINING\" tokens are redeemable for actual qasic shares on the site. just message me here https://nxtforum.org/index.php?action=profile;area=summary;u=2333. These shares will be sold at 25 NXT each until they are all sold out. Lowest fees on the asset exchange! \"NXTMINING\" tokens are not stocks, bonds or any other kind of financial instrument or security. Investors are expected to perform due diligence."
    }, 
    {
        "name": "NXTautoDAC", 
        "asset": "14347250558295845059", 
        "description": "NXTautoDAC assets represent .0001% of revenues from the family of autoDACs that bluemeanie1 and his team will create. NXTventure has made a private investment and assetized 75% of revenues. Development costs will be funded by the remaining 25% of revenues.\r\n\r\nOnce deployed the automatic Digital Autonomous Corporations will continue to operate in an open and transparent manner with transactions enforced by the NXT blockchain. Due to their automated nature the fees charged to people can be dramatically less than real world equivalents. The much lower fees are expected to entice enough people to try this new technology and thus increasing the customer base.\r\n\r\nThe ability to easily utilize autoDACs will be integrated into NXTservices and this will encourage adoption. While autoDAC's have a tremendous potential, it is still in its infancy and it is expected that it will take a while for people to become comfortable with using autoDACs\r\n\r\nPlease follow updates on the NXTventure section"
    }, 
    {
        "name": "NXTcoinsco", 
        "asset": "17571711292785902558", 
        "description": "There are a total of 1 million NXTcoinsco assets. NXTcoinsco will be creating coins that run on top of NXT, starting with nodecoin. After that it will make SVMcoin and also create a NXTcoins development kit to enable others to make coins easily.\r\nFor internally created coins, NXTcoinsco asset holders will receive 10% of the coins. The percentage for externally developed coins will vary.\r\n\r\nplease refer to nxtforum.org for up to date details"
    }, 
    {
        "name": "NXTmovie", 
        "asset": "2240155853020376741", 
        "description": "Loosely based on real life events, the NXT Film Project (nxtmovie.org) narrates the subversive and often vicious attacks that are conducted using technology. It further aims to educate and inform the masses about these new technologies.\r\n\r\nCurrent round is for pre-production on the NXT Film Project screenplay. All proceeds from the sale or licensing of said screenplay will be distributed to token holders at the time of sale. Token holders will also receive site advertising revenues, which will ensure an early source of ROI. Holders of 5% or more get access to contributors circle.\r\n\r\n*Added Perk*\r\nA substantial portion of the proceeds from the NXTmovie Project will go towards rewarding community member Cadence Jean Morton (aka CobaltSkky) as a form of reparation for the vicious harassment she received while confronting cyberbulling and cyberstalking in our community; this will show that the community rewards such members who stand against acts of cruelty and the invasion of our privacy."
    }, 
    {
        "name": "NXTprivacy", 
        "asset": "17911762572811467637", 
        "description": "NXTprivacy will contain various privacy related projects. It will hold significant percentages of several other privacy related assets, like Privatebet and NXTcard, and it will also create privacyServer software for server hosts to run. Any dividends NXTprivacy receives from assets it holds, will be redistributed to its assetholders on a prorata basis. The privacyServer software will provide services for customers that will allow server hosts to recoup some or all of their costs in maintaining a NXT node. Additionally, NXTprivacy will make a market in privateNXT. Please follow the nxtforum.org section on NXTprivacy for more information."
    }, 
    {
        "name": "NXTventure", 
        "asset": "16212446818542881180", 
        "description": "NXTventure makes private investments in promising enterprises and adds value to each investment by proactively integrating it into NXTservices to add a valuable new service for the NXTcommunity. \r\n\r\nNXTventure will pay monthly dividends in the assets it acquires, net of trading activities during the launch period. This means NXTventure asset will generate a stream of new assets as it launches them. contact jl777 if you are seeking investment"
    }, 
    {
        "name": "NeoDICE", 
        "asset": "18184274154437352348", 
        "description": "100% of the neoDICE revenues will be distributed to assetholders.\r\n\r\nNeoDICE revives the instantaneous gaming experience of the legendary SatoshiDice and brings it to NXT. The game is playable via any NXT client supporting asset transfer and does not require any additional software.\r\n\r\nNeoDice is a provably fair game relying on mathematically verifiable cryptographic hash calculations. To ensure the game's integrity the entire betting history is permanently stored on the NXT blockchain.\r\n\r\nMore info at http://neodice.com"
    }, 
    {
        "name": "NxtAT", 
        "asset": "16365311175761675972", 
        "description": "NxtAT (automated transaction) is a decentralised business that will provide AT solutions for clients wanting to gain the benefits of \"Turing complete\" transactions in the Nxt ecosystem without the complexity of having to understand every detail about how AT works"
    }, 
    {
        "name": "Nxttycoin", 
        "asset": "18128686802152832026", 
        "description": "The official cryptocurrency of the Nxt Mobile Applications Company.  \r\n\r\nOfficial newsfeed: https://twitter.com/cryptomessenger"
    }, 
    {
        "name": "OPALTKN", 
        "asset": "5326942574002986149", 
        "description": "OpalTKN represents a holding in the future earnings of opal products.  Learn more at http://www.opal-coin.com"
    }, 
    {
        "name": "ORA", 
        "asset": "16194910134118257692", 
        "description": "ORA is a leaderless, decentralised 'starfish' community software development project announced on May 22, 2014. 889 people initially registered between June 24 - July 8, 2014 for a FREE stake of 166,666 assets each. The remaining ORA assets were held in trust for later distribution to community members & future developers. ORA asset tokens are issued as bearer assets. Whoever controls the  private keys for an amount of ORA asset tokens will be eligible to redeem an equivalent amount of ORA 'coins' if/when the ORA software and P2P network is completed. The asset issuer is unable to guarantee either the completion of ORA software, or the exchange of ORA asset tokens into ORA coins. Please research the ORA project before purchasing ORA assets. The terms & conditions and date of the redemption will be finalised after community consultation. Total assets: 1,000,000,000. For more details : http://ora.to. Issuing account : NXT-7FPB-3K2S-M9FL-ARP4G"
    }, 
    {
        "name": "Pangea", 
        "asset": "6883271355794806507", 
        "description": "Pangea is SuperNET's decentralized poker that uses provably random numbers and will take advantage of the built in privacy features of SuperNET. 80% of revenues will be distributed to assetholders. 20% of revenues will go to marketing affiliates, with Privatebet handling the SuperNET players for Pangea.\r\n\r\nhttps://nxtforum.org/nxtventures/pangea-poker/ will have the latest information"
    }, 
    {
        "name": "Privatebet", 
        "asset": "17083334802666450484", 
        "description": "Privatebet will allow people to make bets directly with each other in a decentralized way. It will let people create their own personal bet with a designated arbiter in addition to automatically supporting a range of standard events with betting interest, like sports betting. Privatebet will only accept crypto and no personal information will be required from its customers. It will have a fee of 1% to begin with, subject to change to adapt to market forces. The goal is to automate as much of Privatebet as possible and it is expected to be able to payout about 80% of the fees it collects as dividends. Please follow the NXTforum for more detals and up to date information."
    }, 
    {
        "name": "RGDO", 
        "asset": "17140378927644056619", 
        "description": "HK Rigid Petroleum Chemical Group Limited was founded in 2003, the company set the lubricating oil research and development, sales, business wide coverage, Taiwan, Macao, Hongkong, the country, and exported to Japan, India, South Korea and other overseas areas. Fusion leading the world's outstanding enterprise management mode and China efficient kind spirit of service in a body, not only can let the customers use to lubricating material of high end, more be able to enjoy real first-class service. Over the years, we have been committed to the development of new products, long-term close cooperation with scientific research units of international NAC, Institute of petroleum, coal science research institute and other institutions. http://www.rigidlube.com"
    }, 
    {
        "name": "RSUnit", 
        "asset": "14285820955872321553", 
        "description": "RSUnit is the NXT asset that holds the place of RSU, allowing early trading of it, until the Beta release of the Reserve Share wallet. Reserve Share is a cryptocurrency, based on Proof of Reserve block generation method, having a Unique Source Code, which allows the users to keep their Units in reserve, by which they increase their Shares. For detailed information check our White Paper and official thread at Bitcointalk."
    }, 
    {
        "name": "SAAS", 
        "asset": "14225517118742712534", 
        "description": "Scrypt Asic Advanced Shares (SAAS) aims to correct 2 significant drawbacks of mining shares/contracts. 1) diminishing returns and 2) decreasing share value.  50% of revenue generated by SAAS will be re-invested to increasing Hash rate, the other 50% will go back to shareholders via dividend payouts.  As hash rates in SAAS increase so does your dividend and therefore your share value.  All funds generated by initial share offering go directly to purchasing more Hash rate.  As of September 1st the Pool owns 211 MH Scrypt.  First dividend payout is scheduled for Monday September 15th 2014 and every Monday after.  Regular updates on Twitter @SAASonNXTAE"
    }, 
    {
        "name": "STSH", 
        "asset": "2504568464748765731", 
        "description": "STSH is a crypto-currency diversified fund that aims to provide its shareholders above average steady dividends with minimal downside . \r\n\r\n3 income Sources:\r\n\r\nArbitrage Trading\r\nScrypt and SHA-256 Mining\r\nSolid Dividend paying Crypto-stocks\r\n\r\nThree rounds of assets listing on NXT AE\r\n1- 2500 Assets @ 10 NXT\r\n2- 5000 Assets @ 30 NXT\r\n3- 7500 Assets @ 50 NXT\r\nOur weekly guaranteed Dividend is .1 NXT per week for each NXT shareholder.\r\nPlease check our website for latest updates.\r\nwww.satosh1.com"
    }, 
    {
        "name": "SafeHash", 
        "asset": "12699150877111554426", 
        "description": "https://nxtforum.org/asset-exchange-general/safehash/"
    }, 
    {
        "name": "ShortNXT", 
        "asset": "7297711024038530345", 
        "description": "twitter.com/shortnxt\r\n\r\nProtect the value of your NXT holdings and hedge your transaction exposure. If NXT goes down, ShortNXT goes up (and vice versa).\r\n\r\nInitial Price: 100 NXT\r\n\r\nShortNXT aims to generate a daily percentage gain inverse to that of NXT. Issuer will support price target with buy and sell orders on the Asset Exchange.\r\n\r\nShortNXT Target Price equals the most recent ShortNXT Daily Reference Price minus the percentage change in NXT from the most recent NXT Daily Reference Price (in USD). ShortNXT Daily Reference Price is set daily at or around 10 am ET to current ShortNXT Target Price. NXT Daily Reference Price is a weighted average as reported at coinmarketcap.com or comparable substitute, at issuer's discretion, at or around 10 am ET.\r\n\r\nIssuer will maintain price support on a best effort basis and makes no assurances of timeliness or accurate calculation or reporting of involved prices.\r\n\r\nUpdates and reference price history at @shortnxt."
    }, 
    {
        "name": "Sianote", 
        "asset": "11593659039925686857", 
        "description": "Convertible to Siastock upon completion of Sia. 1 Sianote converts to 0.01% siastock. Only 1500 will be sold during pre-IPO."
    }, 
    {
        "name": "SkyNET", 
        "asset": "6854596569382794790", 
        "description": "SkyNET will develop decentralized AI technology using neural nets, SVM and other methods, combined with blockchain technology to create real world solutions that can be monetized. More details available at: https://nxtforum.org/index.php?topic=6826"
    }, 
    {
        "name": "SuperNET", 
        "asset": "12071612744977229797", 
        "description": "Official SuperNET asset, trading symbol on exchanges is UNITY \r\n\r\nOfficial BTT thread is https://bitcointalk.org/index.php?topic=762346.0 \r\n\r\nOfficial website http://supernet.org"
    }, 
    {
        "name": "SuperNETx2", 
        "asset": "13502152099823770958", 
        "description": "SuperNETx2 is backed 1:1 with SuperNET assets in NXT-7HAS-3W8H-BTDY-99BJE account. It will receive passthrough asset and revshare dividends that the SuperNET backing the x2 gets. Additionally it will receive an extra 5% revshare dividends, which doubles the revshare that x2 gets since there are 40803.05 x2 assets, which is 5% of SuperNET assets"
    }, 
    {
        "name": "Supercell", 
        "asset": "15008504503343850630", 
        "description": "Supercell Investments is a diverse investments venture offering multitudes of financial services and investment opportunities. Shares offered here are a total 10 Million shares; They represents 50% of Supercell Investments and entitles the owners to 50% of the revenue."
    }, 
    {
        "name": "TOKEN", 
        "asset": "15641806960898178066", 
        "description": "thesupernet.org Official SuperNET TOKEN, latest info at https://bitcointalk.org/index.php?topic=762346"
    }, 
    {
        "name": "TXTCoinNow", 
        "asset": "17874206509705745796", 
        "description": "What we offer:\r\n\r\n1) Safe and secure online storage of all your coins. Transfers of coins require phone call verification and PIN request.\r\n\r\n2) Simple SMS transfer system opens up mico-payments in local currencies using crypto-coins. Merchants create an account and can instantly start taking payments in any of our supported crypto-coins.\r\n www.txtcoinsnow.com"
    }, 
    {
        "name": "USDbitfnx", 
        "asset": "10294386916428132892", 
        "description": "Each 1 USDbitfnx asset represents 1 USD deposited at bitfinex.com . The USD deposited at bitfinex will be used to provide liquidity to margin traders that pay a fee for that service. This interest is paid daily into our account and is currently hovering at about 0.16% per day(~60% yearly return). This dividend will be distributed proportionally to USDbitfnx holders every two weeks. Details about fees, risks and how to deposit and withdraw, can be found in this thread on nxtforum.org: https://nxtforum.org/index.php?topic=3884.0"
    }, 
    {
        "name": "VULTMINING", 
        "asset": "12419839393546948696", 
        "description": "VULTMINING Labs."
    }, 
    {
        "name": "XDFB", 
        "asset": "288267136544646747", 
        "description": "Domains have been considered digital property for 2 decades now. Every business in the modern world needs it's own estate in cyberspace and that is exactly what domains are. In today’s world new businesses pop up all the time. Every second of every minute of every hour of every day: a new business starts it's journey. Some are good and some are bad, some fail and some succeed, but they all have one thing in common: they all need a domain name. \r\n \r\nDomains were the first assets of the internet, and with the ever rapid and enormous growth of both cryptocurrencies and the domain market, it is almost poetically natural for the two to be joined together. This is exactly what DotsforBits will do!\r\n \r\nCheck out the infographic and prospectus for all the details and FAQ!\r\n\r\nhttps://www.youtube.com/watch?v=_9JAK4TAUvE\r\n\r\nAsset Exchange - Ticker symbol - XDFB\r\n\r\nINFO : http://dotsforbits.com/DfB_VIPO.pdf"
    }, 
    {
        "name": "ach", 
        "asset": "6789385243274909976", 
        "description": "Altcoin Herald is a leading alternative cryptocurrency news website known for its’ well-balanced coverage. Our mission is to continue to offer high-quality coverage of cryptocurrency while growing our revenues and profits at a healthy rate. Each ACH purchased entitles the holder to 40% of our net revenues, as explained here. https://alth.co/rDPPI Dividends will be paid bi-weekly. 5000000 ACH are available for sale. Each ACH costs 1 NXT. Learn more here:"
    }, 
    {
        "name": "cryptocard", 
        "asset": "7110939398145553585", 
        "description": "NXTprivacy is proud to issue the cryptocard asset which will distribute 1% of processed transaction volumes to the assetholders. This card does not require any personal information. All of the processing and handling is outsourced to coinomat.com. Please check NXTprivacy.org for the latest details on fees and limits. Standard ATM fees will apply for cash withdrawals."
    }, 
    {
        "name": "cyberShare", 
        "asset": "18349167062458849940", 
        "description": "cyber•Shares are protoshares which create industry of Polymorphic Decentralised Applications. Official site: http://cybershares.net. Read http://paper.cybershares.net. Get involved http://cybertalks.org. Major news http://blog.cyber.fund. Created by http://cyber.fund. 1000000 cyber•Shares ever existed. Proof-of-Origin cybershares.net/explorer. In accordance with shareholders agreement 148158 cyber•Shares was placed on NXT AE burning 148158 cyber•Shares from Open Assets Protocol. cyber•Shares polymorphic blockchain - is the mailing list for sharedrops to community who build cyber•Shares technology. cyber•Shares is your share in all future industry of decentralized applications."
    }, 
    {
        "name": "fuzon", 
        "asset": "5053136014193078855", 
        "description": "A concoction of carefully selected cryptocurrencies which have been identified as long-term investments. Strong performing cryptocurrencies are being added continuously to the assets holdings. Perfect for investors who are looking for a well rounded investment with diversification. More information can be found at fuzon.io or follow @fuzonXFN on twitter."
    }, 
    {
        "name": "iHash", 
        "asset": "9560963759586239947", 
        "description": "iHash is a 0.2 GH/s Virtual Bitcoin Mining Bond valued at 10 NXT each. At the time of launch, Sep 3, 2014 iHash projected APR is more than 90%. With iHash you can start generating Bitcoin immediately. Your payout rate is pegged to Bitcoin Mining difficulty so there are no  downtimes, power failure or any other surprise expenses.\r\nDividends will be calculated every Friday 00:00 UTC and distributed at Friday 10:00 UTC.\r\nProof of solvency: We will accumulate 6 months future dividends on NXT AE. \r\nFor latest details please check our website <a href=\"http://ihash.biz”>iHash.biz</a>"
    }, 
    {
        "name": "jl777hodl", 
        "asset": "6932037131189568014", 
        "description": "This asset will not pay dividends. It will contain portions of almost all of the assets that I issue, the target percentage is 10%, but actual percentage will vary. Some issues will have more than 10%, some assets I wont be able to put here. Once the assets are in this account they will probably stay there long term, but occasional changes will be made at then current market prices. You can see current hodlings at 18323612891099439610 NXT-2AHU-UXZW-K9Q2-HENLW"
    }, 
    {
        "name": "ltc2nXt", 
        "asset": "8670004015468655281", 
        "description": "ltc2nxt.ihash.biz :: Each virtual token corresponds to a value equivalent to a qasic share on ltcgear.com. ltc2nXt tokens are not redeemable for actual qasic shares.\r\nltc2nXt tokens are not stocks, bonds or any other kind of financial instrument or security. Investors are expected to perform due diligence. For uptodate information please check the official website: http://ltc2nxt.ihash.biz/"
    }, 
    {
        "name": "ltc2nXt3", 
        "asset": "7658325674657936242", 
        "description": "http://ltc2nxt3.ihash.biz :: only 50,000 ltc2nXt3 virtual tokens issued. 100% of your initial NXT purchase is protected. 0% fees and 100% multiplication shares during 100% ROI period. “ltc2nXt3\" tokens are not redeemable for actual qasic shares. “ltc2nXt3\" tokens are not stocks, bonds or any other kind of financial instrument or security. Investors are expected to perform due diligence. For up-to-date information please check the official website: http://ltc2nxt3.ihash.biz"
    }, 
    {
        "name": "ltc2nxt2", 
        "asset": "2388153394586381152", 
        "description": "http://ltc2nXt.net :: only 18250 virtual tokens issued. Each virtual token corresponds to a value equivalent to a qasic share on ltcgear.com. “ltc2nXt2\" tokens are not redeemable for actual qasic shares. “ltc2nXt2\" tokens are not stocks, bonds or any other kind of financial instrument or security. Investors are expected to perform due diligence. For up-to-date information please check the official website: http://ltc2nxt.net/"
    }, 
    {
        "name": "mgwBTC", 
        "asset": "17554243582654188572", 
        "description": "Production Multigateway BTC (mgwBTC) is backed 100% by deposits in the custom multi-signature accounts generated for each user in the Multigateway production servers. Deposits made to the multi-signature accounts will automatically transfer the corresponding amount of mgwBTC assets to the associated NXT account. Withdraws are automatically processed serially only when all Multigateway servers are in agreement. The balances in the multi-signature accounts will change internally and do not represent the amount of BTC in your NXT account, the mgwBTC assets you own do. See https://multigateway.org for more information."
    }, 
    {
        "name": "mgwBTC", 
        "asset": "4551058913252105307", 
        "description": "multigateway BTC is backed 100% by deposits in the custom multisig accounts generated for each user. Deposits made to the multisig account will automatically transfer the corresponding amount of BTC assets to the associated NXT account. Withdraws are automatically processed serially only when all multigateway servers are in agreement. The balances in the multisig accounts will change and do not represent the amount of BTC in your account, the BTC assets do. See forum for more details and fee structure. By configuring NXTservices to monitor multigateway, any NXT node will be able to track the current status of all multigateway transactions and balances."
    }, 
    {
        "name": "mgwBTCD", 
        "asset": "11060861818140490423", 
        "description": "multigateway BTCD is backed 100% by deposits in the custom multisig accounts generated for each user. Deposits made to the multisig account will automatically transfer the corresponding amount of BTCD assets to the associated NXT account. Withdraws are automatically processed serially only when all multigateway servers are in agreement. The balances in the multisig accounts will change and do not represent the amount of BTCD in your account, the BTCD assets do. See forum for more details and fee structure. By configuring NXTservices to monitor multigateway, any NXT node will be able to track the current status of all multigateway transactions and balances. Amounts are rounded down to 4 decimals."
    }, 
    {
        "name": "nXtGenGHS", 
        "asset": "9312536843540017349", 
        "description": "nXtGen Mining is offering mining assets available immediately. Each asset is equivalent to 1 GHS worth of processing power. We will use the profits from mining to buy NXT and distribute it through dividends to all asset holders. By placing an order on this Site for Our Services, You agree to be bound by these Terms and Conditions of Service [ http://nxtmining.com/terms ]. We collect an ongoing variable hosting charge from the virtual currency product produced by all of Our Services. See Terms and Conditions for hosting charges and also for general risk information. WE RESERVE THE RIGHT TO TERMINATE ANY SERVICES WHEN IT BECOMES UNECONOMICAL FOR US OR YOU (IN OUR SOLE DECISION MAKING DISCRETION) TO CONTINUE ON WITH SUCH SERVICES BECAUSE OF CHANGES IN THE VIRTUAL CURRENCY MARKETPLACE, THE FACT MINING EQUIPMENT HAS BECOME OBSOLETE, ETC., EVEN THOUGH THERE IS NO STATED TERMINATION OR EXPIRY DATE ON ‘ASSETS’ or 'SHARES' (ALL SERVICES) WHICH YOU PURCHASE."
    }, 
    {
        "name": "nXtGenGHS", 
        "asset": "12984255659001987157", 
        "description": "nXtGen Mining is offering mining shares valued at 1 GHS per share. nXtGen Mining will be partnering with Knights of the Satoshi Ltd. to facilatate hosting of the equipment at a very competitive rate. This will allow for a more profitable venture. We will merge mine SHA-256 coins on a decentralized pool which will allow us to make a larger ROI. We will use the profits from mining to buy NXT and distrubute it through dividends to all shareholders. There will be a 3% fee to cover expenses such as electricity, hosting, etc. Dividends will be paid on a weekly basis. Further information will be found through the alias nXtGenMining or the website http://nxtmining.com"
    }, 
    {
        "name": "nXtGenKHS", 
        "asset": "12178299813760950396", 
        "description": "nXtGen Mining is offering mining shares valued at 1 KHS per share. nXtGen Mining will be partnering with Knights of the Satoshi Ltd. to facilatate hosting of the equipment at a very competitive rate. This will allow for a more profitable venture. We will merge mine Scrypt coins on a decentralized pool which will allow us to make a larger ROI. We will use the profits from mining to buy NXT and distrubute it through dividends to all shareholders. There will be a 3% fee to cover expenses such as electricity, hosting, etc. Dividends will be paid on a weekly basis. Further information will be found through the alias nXtGenMining or the website http://nxtmining.com"
    }, 
    {
        "name": "nxtegregor", 
        "asset": "15363532072961781727", 
        "description": "Этот актив будет получать прибыль от краткосрочных и среднесрочных инвестиций в Nxt Asset Exchange активы. А также от инвестиций в другие финансовые рынки.\r\nДля успешного старта проекта,держателям этого актива,первоначально будут выплачены высокие дивиденды:\r\n21.12.2014-22.12.2014-будет выплачено 100% прибыли от вложенных средств,т.е.  количество активов nxtegregor  удвоится.\r\n29.12.2014-03.01.2014-будет выплачено 100% \r\nВ январе 2015 года,планируется выплата 50%"
    }, 
    {
        "name": "sharkfund0", 
        "asset": "3006420581923704757", 
        "description": "Each purchased sharkfund0 asset represents a proportional share of the fund's crypto holdings. NXTsharks will actively manage sharkfund0 to maximize its market value. 25% of profits are assetized by the NXTsharks assets, the rest compounds in sharkfund0. The sharkfund0 assets held by NXTsharks are unpurchased assets and are not bound to anything, NXTsharks will never sell unpurchased assets via AE. Initially, the value is set to 10000 NXT per asset. After the initial funding, additions are made at the marked to the market value of all previously purchased sharkfund0 assets. Purchases using non-NXT crypto is done manually on a case by case basis, minimum 10 BTC. It is preferred to make withdrawals simply by selling the asset using AE, but NXTsharks can accomodate requests of larger cashouts manually.\r\nplease check the NXT forum for up to date details"
    }, 
    {
        "name": "silver", 
        "asset": "7819056276221630295", 
        "description": "Before purchasing read the terms and conditions located at alias SilverTerms. - The act of purchasing one of these tokens shall constitute the expression of consent to the terms expressed at alias SilverTerms. - These tokens act as warehouse receipts for 999 Silver Bullion stored in my facilities and may be redeemed for physical silver. For more details read the information located at alias SilverDetails or send me a personal message."
    }, 
    {
        "name": "theRealDAX", 
        "asset": "10014539005191342474", 
        "description": "The Real DAX is not a Game but a real Trade based on Real DAX Rates.every Day in the Morning (Mo-Fr) we cancel our old Sell Orders from the previous Day and make new Sell Orders based on the closing Rates from the previous Day.a certain Sell Orders below the current Rates we will buy to provide a fair Trade of course we can not all Sell Orders buy! All DAX Rates are based on the official Closing Rates from www.finanzen.net/dax  You can also make Real Profits! All Rates are dividends thru Thousend! Happy Trading"
    }, 
    {
        "name": "topDISTR", 
        "asset": "1007341094739630837", 
        "description": "The aim of this asset is to achieve the highest distribution at the NXT AE. I’m putting the funds and the effort to distribute 10000 packages of 1000 shares to whoever has an account on nxtforum.org or on bitcointalk.org, created before 2014-07-30. The priority is on a first come first served basis. The issuing account will never trade a single share and will only have outgoing transactions of 1000 shares and one incoming initial transaction of 11000 NXT for creating and distributing the asset. I will not send shares to the same NXT account twice. Post your account number to the corresponding thread on either forum."
    }
    ]
    
    COINS = [
	    { 'id':"5527630" },
	    { 'id':"17554243582654188572" },
	    { 'id':"4551058913252105307" },
	    { 'id':"12659653638116877017" },
	    { 'id':"11060861818140490423"},
	    { 'id':"6918149200730574743" },
	    { 'id':"13120372057981370228" },
	    { 'id':"2303962892272487643" },
	    { 'id':"16344939950195952527"},
	    { 'id':"6775076774325697454" },
	    { 'id':"7734432159113182240" },
	    { 'id':"9037144112883608562" },
	    { 'id':"1369181773544917037" },
	    { 'id':"17353118525598940144" },
	    { 'id':"2881764795164526882" },
	    { 'id':"7117580438310874759" },
	    { 'id':"275548135983837356" },
	]
    
    
    
    #query_json = {'requestType': 'lottostats'}
	# {'error': 'illegal lotto parms'}
	#{"result":"lottostats","totaltickets":"0","NXT":"8418687609572182360","numtickets":"0","odds":"0.00","topMM":"0"}
    def lotto(self):

        print(5*"\n++++++++++++","lotto call")
        test_RQ_ = {'requestType': 'lottostats'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
		
        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)
        return rpl777
        
        
	##############################################
	##############################################
	#
	#	InstantDEX API Calls
	#
	#
	##############################################
	##############################################
    def placebid(self,volume,price,baseid,relid):
        query_json = {'price': '', 'volume': '', 'requestType': 'placebid', 'baseid': '', 'relid': ''}

        print(5*"\n++++++++++++","test_placebid")
        testRQ_placebid = {'requestType': 'placebid'}

        testRQ_placebid['volume'] = volume
        testRQ_placebid['price'] =  price
        testRQ_placebid['baseid'] = baseid
        testRQ_placebid['relid'] =  relid

        payload= self.qComp_777.make_777POST_Request(testRQ_placebid)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        return rpl777
        
    def allorderbooks(self):
        query_json  = {'requestType': 'allorderbooks'}
		# {'orderbooks': []}

        print(5*"\n++++++++++++","test_allorderbooks")
        test_RQ_ = {'requestType': 'allorderbooks'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)
        
        return rpl777
        
    def openorders(self):
        query_json = {'requestType': 'openorders'}
        # {'result': 'no openorders'}

        print(5*"\n++++++++++++","test_openorders")
        test_RQ_ = {'requestType': 'openorders'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)
        
        return rpl777
        
    #'{"requestType":"orderbook","baseid":"11060861818140490423","relid":"17554243582654188572"}'
    #{'error': 'no bids or asks'}
    #{
	#"key": 		"7646303683960469163",
	#"baseid": 	"11060861818140490423",
	#"relid": 	"17554243582654188572",
	#"bids": 	 	[["0.00550000000", "100.00000000"]],
	#"asks": 	 	[["0.00650000000", "80.00000000"]]
	#}
    def orderbook(self, base, rel):
        test_RQ_orderbook = {
                            'allfields': '1', \
                            'baseid': base, \
                            'relid': rel, \
                            'requestType': 'orderbook', \
                            'oldest': ''
        }

        print(5*"\n++++++++++++","test_orderbook")

        payload= self.qComp_777.make_777POST_Request(test_RQ_orderbook)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)
        
        return rpl777
        
        
    def bid(self, baseid, relid):
        test_RQ_bid = {
                            'requestType': 'bid', \
                            'baseid': baseid, \
                            'relid': relid, \
                            'volume': '1', \
                            'price': '1', \
                            'timestamp': '', \
                            'baseamount': '', \
                            'relamount': '', \
                            'type': '', \

        }
        
        print(5*"\n++++++++++++","test_bid")
        payload= self.qComp_777.make_777POST_Request(test_RQ_bid)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        
        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)
        
        return rpl777
        
        
    def ask(self, baseid, relid):
        test_RQ_orderbook = {
                            'requestType': 'ask', \
                            'baseid': baseid, \
                            'relid': relid, \
                            'volume': '1', \
                            'price': '1', \
                            'timestamp': '', \
                            'baseamount': '', \
                            'relamount': '', \
                            'type': '', \
        }

        print(5*"\n++++++++++++","test_ask")

        payload= self.qComp_777.make_777POST_Request(test_RQ_orderbook)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        
        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)
        
        return rpl777
        
        
    def placeask(self,volume,price,baseid,relid):
        query_json =  {'relid': '', 'requestType': 'placeask', 'baseid': '', 'volume': '', 'price': ''}

        print(5*"\n++++++++++++","test_placeask")
        testRQ_placeask = {'requestType': 'placeask'}

        testRQ_placeask['volume'] = volume
        testRQ_placeask['price'] =  price
        testRQ_placeask['baseid'] = baseid
        testRQ_placeask['relid'] =  relid

        payload= self.qComp_777.make_777POST_Request(testRQ_placeask)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        
        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)
        
        return rpl777
        
        
    def respondtx(self):
        null = None

        print(5*"\n++++++++++++","test_respondtx")
        test_RQ_ = {'requestType': 'respondtx'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)
        
        return rpl777
        
    def processutx(self):
        print(5*"\n++++++++++++","test_processutx")
        test_RQ_ = {'requestType': 'processutx'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)
        
        return rpl777
    #
    # def processutx2(self):
    #
    #     test_RQ_ = {'requestType': 'processutx'}
    #     rpl777 = apicall(test_RQ)
    #
    #     return rpl777
    #
    def apicall(self, query):
        null = None
        print(5*"\n++++++++++++","running API call")

        print("query json is: ", query)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(query), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)
        
        return rpl777
        

    def placebid_full(self,volume,price,baseid,relid):
        #price = '0.00014'
        #volume = '1.00001'

        #baseid = '17554243582654188572'
        #relid = '5527630'
        placebidResponse = self.placebid(volume,price,baseid,relid)
        print('\nCheck if response is ok\n')
        self.assertTrue('quoteid' in placebidResponse.keys())
        #print('\nblaaatest\n');
        #print(placebidResponse['quoteid']);
        
        orderbookResponse = self.orderbook(baseid,relid)
        print('\nCheck orderbook if bid is there\n')
        #print(orderbookResponse);
        
        found = False
        for bid in orderbookResponse['bids']:
            if float(bid['price']) == float(price):
                found = True
        self.assertTrue(found)
        
        
        openordersResponse = self.openorders()
        print('\nCheck if bid is in openorders\n')
        #print(openordersResponse)
        
        found = False
        for openorder in openordersResponse['openorders']:
            if openorder['quoteid'] == placebidResponse['quoteid']:
                found = True
        self.assertTrue(found)
        
        cancelquoteResponse = self.apicall({'requestType': 'cancelquote','quoteid':placebidResponse['quoteid']})
        print('\nCheck cancelquote works\n')
        self.assertTrue(cancelquoteResponse['result']=='quote cancelled')
        
        
        openordersResponse = self.openorders()
        print('\nCheck if bid is not in openorders\n')
        #print(openordersResponse)
        
        found = False
        for openorder in openordersResponse['openorders']:
            if openorder['quoteid'] == placebidResponse['quoteid']:
                found = True
        self.assertFalse(found)
        
        
        

##############################################
##############################################
#
#	InstantDEX Tests
#
#
##############################################
##############################################
#{"requestType":"placeask","baseid":"11060861818140490423","relid":"17554243582654188572","volume":"80","price":"0.0065"}'
#{"result":"success","txid":"15021359626299573695"}
class SNET_idex_placeask(SNET_BaseTest, SNET_apicalls):
	
    def setUp(self):
        print(" test setUp func here")
        pass

    def runTest(self):
        self.test_placeask()
        self.test_placeask_a()
        self.test_placeask_full()

    def test_placeask(self):
        price = '0.014'
        volume = '1.00'

        baseid = '17554243582654188572'
        relid = '5527630'
        apiResponse = self.placeask(volume,price,baseid,relid)
        #print(apiResponse);
        self.assertTrue('quoteid' in apiResponse.keys() )
        
    def test_placeask_a(self):
        price = '0.00014'
        volume = '1.00001'

        baseid = '17554243582654188572'
        relid = '5527630'
        apiResponse = self.placeask(volume,price,baseid,relid)
        self.assertTrue('quoteid' in apiResponse.keys() )
        
        
    def test_placeask_full(self):
        price = '0.00014'
        volume = '1.00001'

        baseid = '17554243582654188572'
        relid = '5527630'
        placeaskResponse = self.placeask(volume,price,baseid,relid)
        print('\nCheck if response is ok\n')
        self.assertTrue('quoteid' in placeaskResponse.keys())
        #print('\nblaaatest\n');
        #print(placeaskResponse['quoteid']);
        
        orderbookResponse = self.orderbook(baseid,relid)
        print('\nCheck orderbook if bid is there\n')
        #print(orderbookResponse);
        
        found = False
        for bid in orderbookResponse['bids']:
            if float(bid['price']) == float(price):
                found = True
        self.assertTrue(found)
        
        
        openordersResponse = self.openorders()
        print('\nCheck if ask is in openorders\n')
        #print(openordersResponse)
        
        found = False
        for openorder in openordersResponse['openorders']:
            if openorder['quoteid'] == placeaskResponse['quoteid']:
                found = True
        self.assertTrue(found)
        
        cancelquoteResponse = self.apicall({'requestType': 'cancelquote','quoteid':placeaskResponse['quoteid']})
        print('\nCheck cancelquote works\n')
        self.assertTrue(cancelquoteResponse['result']=='quote cancelled')
        

        openordersResponse = self.openorders()
        print('\nCheck if ask is not in openorders\n')
        #print(openordersResponse)
        
        found = False
        for openorder in openordersResponse['openorders']:
            if openorder['quoteid'] == placeaskResponse['quoteid']:
                found = True
        self.assertFalse(found)


class SNET_idex_placebid(SNET_BaseTest, SNET_apicalls):

    def setUp(self):
        print("test placebid")
        
    def runTest(self):
        self.test_placebid()
        self.test_placebid_a()
        self.test_placebid_full()
        self.test_placebid_range()
        
    def test_placebid(self):
        price = '0.014'
        volume = '1.00'

        baseid = '17554243582654188572'
        relid = '5527630'
        apiResponse = self.placebid(volume,price,baseid,relid)
        #print(apiResponse);
        self.assertTrue('quoteid' in apiResponse.keys() )
        
    def test_placebid_a(self):
        price = '0.00014'
        volume = '1.00001'

        baseid = '17554243582654188572'
        relid = '5527630'
        apiResponse = self.placebid(volume,price,baseid,relid)
        self.assertTrue('quoteid' in apiResponse.keys() )
        
        
    def test_placebid_full(self):
        price = '0.00014'
        volume = '1.00001'

        baseid = '17554243582654188572'
        relid = '5527630'
        placebidResponse = self.placebid(volume,price,baseid,relid)
        print('\nCheck if response is ok\n')
        self.assertTrue('quoteid' in placebidResponse.keys())
        #print('\nblaaatest\n');
        #print(placebidResponse['quoteid']);
        
        orderbookResponse = self.orderbook(baseid,relid)
        print('\nCheck orderbook if bid is there\n')
        #print(orderbookResponse);
        
        found = False
        for bid in orderbookResponse['bids']:
            if float(bid['price']) == float(price):
                found = True
        self.assertTrue(found)
        
        
        openordersResponse = self.openorders()
        print('\nCheck if bid is in openorders\n')
        #print(openordersResponse)
        
        found = False
        for openorder in openordersResponse['openorders']:
            if openorder['quoteid'] == placebidResponse['quoteid']:
                found = True
        self.assertTrue(found)
        
        cancelquoteResponse = self.apicall({'requestType': 'cancelquote','quoteid':placebidResponse['quoteid']})
        print('\nCheck cancelquote works\n')
        self.assertTrue(cancelquoteResponse['result']=='quote cancelled')
        
        
        openordersResponse = self.openorders()
        print('\nCheck if bid is not in openorders\n')
        #print(openordersResponse)
        
        found = False
        for openorder in openordersResponse['openorders']:
            if openorder['quoteid'] == placebidResponse['quoteid']:
                found = True
        self.assertFalse(found)
        
        
        
class SNET_idex_placebid_full(SNET_BaseTest, SNET_apicalls):

    def setUp(self):
        print("test placebid")
        
    def runTest(self):
        self.test_placebid()
        
    def test_placebid(self):
        #i = 1000
        #while i >= 1:
            #print(round(i,2))
            #self.placebid_full(22,round(i,0),17554243582654188572,5527630)
            #i /= 10
            
        for assetinfo in self.NXTASSETS:
            i = 10
            while i >= 1:
                print(round(i,2))
                self.placebid_full(22,round(i,0),assetinfo['asset'],'5527630')
                i /= 10
            
        #Asset <-> Coin is also hybrid which doesnt work atm
        #for assetinfo in self.NXTASSETS:
            #for coininfo in self.COINS:
                #print(coininfo)
                #if assetinfo['asset']!=coininfo['id']:
                    #i = 1000
                    #while i >= 1:
                        #print(round(i,2))
                        #self.placebid_full(22,round(i,0),assetinfo['asset'],coininfo['id'])
                        #i /= 10
            
        #Asset <-> Asset placebid doesnt work
        #for assetinfo1 in self.NXTASSETS:
            #print(assetinfo1['asset'])
            #for assetinfo2 in self.NXTASSETS:
                #if assetinfo1['asset']!=assetinfo2['asset']:
                    #print(assetinfo2['asset'])
                    #i = 1000
                    #while i >= 1:
                        #print(round(i,2))
                        #self.placebid_full(22,round(i,0),assetinfo1['asset'],assetinfo2['asset'])
                        #i /= 10
        
        
        
class SNET_idex_allorderbooks(SNET_BaseTest, SNET_apicalls):

    def setUp(self):
        print(" test setUp func here")
        pass

    def runTest(self):
        self.test_allorderbooks()

    def test_allorderbooks(self):

        rpl777 = self.allorderbooks()
        # good reply:
        # {'orderbooks': [{'rel': 'NET', 'relid': '12071612744977229797', 'baseid': '11060861818140490423', 'base': 'BTCD', 'numquotes': 7}]}

        self.assertTrue('orderbooks' in rpl777.keys() )


class SNET_idex_openorders(SNET_BaseTest, SNET_apicalls):

    def setUp(self):
        print(" test setUp func here")
        pass

    def runTest(self):
        self.test_openorders()

    def test_openorders(self):
		
        rpl777 = self.openorders()
        #{'result': 'no openorders'}
        self.assertTrue('openorders' in rpl777.keys() )



class SNET_idex_orderbook(SNET_BaseTest, SNET_apicalls):

    def setUp(self):
        print(" test setUp func here")
        pass

    def runTest(self):
        self.test_orderbook()

    def test_orderbook(self):
        baseid = '11060861818140490423'
        relid = '17554243582654188572'
        
        rpl777 = self.orderbook(baseid, relid)

        self.assertTrue('NXT' in rpl777.keys() )


#ask and bid are internal calls
#only use them if you are debugging internal calls 
class SNET_idex_bid(SNET_BaseTest, SNET_apicalls):

    def setUp(self):
        print(" test setUp func here")
        pass

    def runTest(self):
        self.test_bid()

	# {'txid': '14590711946411376684', 'result': 'success'}
	# static char *bid[] = { (char *)bid_func, "bid", "V", "baseid", "relid", "volume", "price", "timestamp", "baseamount", "relamount", "type", 0 };
    def test_bid(self):
        
        baseid = '11060861818140490423'
        relid = '17554243582654188572'
        
        rpl777 = self.bid(baseid, relid)

        if 'error' in rpl777:
            print(5*"\n~~~~~~~~~~~~","error in SuperNET rpl777y:\n\n", rpl777)
            self.assertTrue(False)
        else:
            self.assertTrue('result' in rpl777.keys() )


#ask and bid are internal calls
#only use them if you are debugging internal calls
# static char *ask[] = { (char *)ask_func, "ask", "V", "baseid", "relid", "volume", "price", "timestamp", "baseamount", "relamount", "type", 0 };
#{'txid': '11713518629359241926', 'result': 'success'}
class SNET_idex_ask(SNET_BaseTest, SNET_apicalls):

    def setUp(self):
        print(" test setUp func here")
        pass

    def runTest(self):
        self.test_ask()

    def test_ask(self):
        
        baseid = '11060861818140490423'
        relid = '17554243582654188572'
        
        rpl777 = self.ask(baseid, relid)

        if 'error' in rpl777.keys():
            self.fail("Got an Error Response!")
        else:
            self.assertTrue('result' in rpl777.keys() )


class SNET_idex_allsignals(SNET_BaseTest, SNET_apicalls):

    def setUp(self):
        print(" test allsignals setUp func here")
        pass

    def runTest(self):
        self.test_allsignals()

    def test_allsignals(self):
        rpl777 = self.apicall({'requestType': 'allsignals'})

        self.assertTrue('signals' in rpl777.keys() )



class SNET_idex_lottostats(SNET_BaseTest, SNET_apicalls):

    def setUp(self):
        print(" test lottostats setUp func here")
        pass

    def runTest(self):
        self.test_lottostats()

    def test_lottostats(self):   
        rpl777 = self.apicall({'requestType': 'lottostats'})

        self.assertTrue('result' in rpl777.keys() )



class SNET_idex_tradehistory(SNET_BaseTest, SNET_apicalls):

    def setUp(self):
        print(" test tradehistory setUp func here")
        pass

    def runTest(self):
        self.test_tradehistory()

    def test_tradehistory(self):
        rpl777 = self.apicall({'requestType': 'tradehistory'})

        self.assertTrue('result' in rpl777.keys() )



class SNET_idex_getsignal(SNET_BaseTest, SNET_apicalls):

    def setUp(self):
        print(" test getsignal setUp func here")
        pass

    def runTest(self):
        self.test_getsignal()

    def test_getsignal(self):
        rpl777 = self.apicall({'requestType': 'getsignal'})

        self.assertTrue('result' in rpl777.keys() )



class SNET_idex_cancelquote(SNET_BaseTest, SNET_apicalls):

    def setUp(self):
        print(" test cancelquote setUp func here")
        pass

    def runTest(self):
        self.test_cancelquote()

    def test_cancelquote(self):
        rpl777 = self.apicall({'requestType': 'cancelquote','quoteid':'123'})

        self.assertTrue('result' in rpl777.keys() )


class SNET_idex_processjumptrade(SNET_BaseTest, SNET_apicalls):

    def setUp(self):
        print(" test processjumptrade setUp func here")
        pass

    def runTest(self):
        self.test_processjumptrade()

    def test_processjumptrade(self):
        rpl777 = self.apicall({'requestType': 'processjumptrade'})

        self.assertTrue('result' in rpl777.keys())



class SNET_idex_jumptrades(SNET_BaseTest, SNET_apicalls):

    def setUp(self):
        print(" test jumptrades setUp func here")
        pass

    def runTest(self):
        self.test_jumptrades()

    def test_jumptrades(self):
        rpl777 = self.apicall({'requestType': 'jumptrades'})

        if rpl777:
            print("not empty")
        else:
            print("empty")

        
#query_json = {'signedtx': '', 'requestType': 'respondtx'}
# {'result': 'invalid makeoffer_func request'}
class SNET_idex_respondtx(SNET_BaseTest, SNET_apicalls):

    def setUp(self):
        print(" test setUp func here")
        pass

    def runTest(self):
        self.test_respondtx()

    def test_respondtx(self):
        rpl777 = self.respondtx()

        self.assertTrue('result' in rpl777.keys() )



class SNET_idex_processutx(SNET_BaseTest, SNET_apicalls):

    def setUp(self):
        print(" test setUp func here")
        pass

    def runTest(self):
        self.test_processutx()

    def test_processutx(self):

        rpl777 = self.processutx()

        self.assertTrue('result' in rpl777.keys())
        
        
##############################################
##############################################
#
#	Other SN Tests
#
#
##############################################
##############################################
class SNET_lotto(SNET_BaseTest, SNET_apicalls):

    def setUp(self):
        print(" test setUp func here")
        pass

    def runTest(self):
        self.test_lotto()
        
    def test_lotto(self):
        apiResponse = self.lotto()
        self.assertTrue('' in apiResponse.keys() )
        
        
        
##############################################
##############################################
##############################################
##############################################
##############################################

def suite_idexSuite():
    suite = unittest.TestSuite()
    suite.addTest(SNET_idex_placebid())
    suite.addTest(SNET_idex_placeask())
    suite.addTest(SNET_idex_orderbook())
    suite.addTest(SNET_idex_allorderbooks())
    suite.addTest(SNET_idex_openorders())
    suite.addTest(SNET_idex_respondtx())
    suite.addTest(SNET_idex_processutx())
    suite.addTest(SNET_idex_bid())
    suite.addTest(SNET_idex_ask())
    suite.addTest(SNET_idex_allsignals())
    suite.addTest(SNET_idex_lottostats())
    suite.addTest(SNET_idex_tradehistory())
    suite.addTest(SNET_idex_getsignal())
    suite.addTest(SNET_idex_cancelquote())
    suite.addTest(SNET_idex_processjumptrade())
    suite.addTest(SNET_idex_jumptrades())

    return suite

def suite_baseSetup():
    suite = unittest.TestSuite()
    suite.addTest(SNET_baseSetup('setUp'))
    suite.addTest(SNET_baseSetup('test_SNET_baseSetup'))
    return suite

def suite_getpeers():
    suite = unittest.TestSuite()
    #suite.addTest(SNET_getpeers('setUp'))
    suite.addTest(SNET_getpeers('test_getpeers'))
    return suite

def suite_settings():
    suite = unittest.TestSuite()
    #suite.addTest(SNET_getpeers('setUp'))
    suite.addTest(SNET_settings('test_settings'))

    return suite

def suite_gotjson():
    suite = unittest.TestSuite()
    #suite.addTest(SNET_getpeers('setUp'))
    suite.addTest(SNET_gotjson('test_gotjson'))
    return suite

def suite_SG():
    suite = unittest.TestSuite()
    suite.addTest(SNET_getpeers('test_getpeers'))
    suite.addTest(SNET_settings('test_settings'))
    return suite



class TestCollector(object):

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
        # passth
        testClasses['SNET_passthru'] = SNET_passthru # ?
        testClasses['SNET_remote'] = SNET_remote # ?
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
        testClasses['SNET_restorefile'] = SNET_restorefile # ?
        testClasses['SNET_publish'] = SNET_publish # ?
        # telepa
        testClasses['SNET_getpeers'] = SNET_getpeers # *
        testClasses['SNET_addcontact'] = SNET_addcontact # ?
        testClasses['SNET_removecontact'] = SNET_removecontact # ?
        testClasses['SNET_dispcontact'] = SNET_dispcontact # ?
        testClasses['SNET_telepathy'] = SNET_telepathy # ?
        testClasses['SNET_getdb'] = SNET_getdb # ?
        testClasses['SNET_sendmessage'] = SNET_sendmessage # ?
        testClasses['SNET_sendbinary'] = SNET_sendbinary # ?
        testClasses['SNET_checkmsg'] = SNET_checkmsg # ?
        # telepo
        testClasses['SNET_maketelepods'] = SNET_maketelepods # ?
        testClasses['SNET_telepodacct'] = SNET_telepodacct # ?
        testClasses['SNET_teleport'] = SNET_teleport # ?
        # idex

        testClasses['SNET_idex_allorderbooks'] = SNET_idex_allorderbooks # *
        testClasses['SNET_idex_openorders'] = SNET_idex_openorders       # *
        testClasses['SNET_idex_orderbook'] = SNET_idex_orderbook # *
        testClasses['SNET_idex_placebid'] = SNET_idex_placebid # *
        testClasses['SNET_idex_placeask'] = SNET_idex_placeask # *
        testClasses['SNET_idex_placebid_full'] = SNET_idex_placebid_full
       #testClasses['SNET_idex_makeoffer'] = SNET_idex_makeoffer # *? deprecated
        testClasses['SNET_idex_respondtx'] = SNET_idex_respondtx  # * ?
        testClasses['SNET_idex_processutx'] = SNET_idex_processutx  # * ?
        testClasses['SNET_idex_bid'] = SNET_idex_bid # *
        testClasses['SNET_idex_ask'] = SNET_idex_ask # *
        testClasses['SNET_idex_allsignals'] = SNET_idex_allsignals # *
        testClasses['SNET_idex_lottostats'] = SNET_idex_lottostats # *
        testClasses['SNET_idex_tradehistory'] = SNET_idex_tradehistory # *
        testClasses['SNET_idex_getsignal'] = SNET_idex_getsignal # *
        testClasses['SNET_idex_cancelquote'] = SNET_idex_cancelquote # *
        #testClasses['SNET_idex_makeoffer2'] = SNET_idex_makeoffer2 # * deprecated
        testClasses['SNET_idex_processjumptrade'] = SNET_idex_processjumptrade # *
        testClasses['SNET_idex_jumptrades'] = SNET_idex_jumptrades # *

        # tbot
        testClasses['SNET_pricedb'] = SNET_pricedb   # ?
        testClasses['SNET_getquotes'] = SNET_getquotes   # ?
        testClasses['SNET_tradebot'] = SNET_tradebot   # ?
        # pbet
        testClasses['SNET_lotto'] = SNET_lotto  # ?
        # lang
        testClasses['SNET_python'] = SNET_python  # ? ~
        testClasses['SNET_syscall'] = SNET_syscall  # ? ~

        return testClasses


    def  getTestSuitesDict(self, ):

        testSuites = {}
        #testSuites['base'] = suite_baseSetup
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
                        # passth
                        SNET_passthru ,\
                        SNET_remote ,\
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
                        SNET_checkmsg ,\
                        # telepo
                        SNET_maketelepods ,\
                        SNET_telepodacct ,\
                        SNET_teleport ,\
                        # idex
                        SNET_idex_allorderbooks ,\
                        SNET_idex_openorders       ,\
                        SNET_idex_orderbook ,\
                        SNET_idex_placebid ,\
                        SNET_idex_placeask ,\
                #       SNET_idex_makeoffer ,\ deprecated
                        SNET_idex_respondtx  ,\
                        SNET_idex_processutx  ,\
                        SNET_idex_bid ,\
                        SNET_idex_ask ,\
                        SNET_idex_allsignals ,\
                        SNET_idex_lottostats ,\
                        SNET_idex_tradehistory ,\
                        SNET_idex_getsignal ,\
                        SNET_idex_cancelquote ,\
                #        SNET_idex_makeoffer2 ,\ deprecated
                        SNET_idex_processjumptrade ,\
                        SNET_idex_jumptrades ,\
                        # tbot
                        SNET_pricedb   ,\
                        SNET_getquotes   ,\
                        SNET_tradebot   ,\
                        # pbet
                        SNET_lotto  ,\
                        # lang
                        SNET_python  ,\
                        SNET_syscall  ,\


                        ]

        elif testListName == 'idex':

            testList = [
                        SNET_idex_makeoffer,\
                        SNET_idex_allorderbooks ,\
                        SNET_idex_openorders,\
                        SNET_idex_orderbook,\
                        SNET_idex_placebid,\
                        SNET_idex_placeask,\
                        SNET_idex_bid,\
                        SNET_idex_ask,\
                        SNET_idex_respondtx,\
                        SNET_idex_processutx,\
                        SNET_idex_allsignals ,\
                        SNET_idex_lottostats ,\
                        SNET_idex_tradehistory,\
                        SNET_idex_getsignal,\
                        SNET_idex_cancelquote,\
                        SNET_idex_makeoffer2 ,\
                        SNET_idex_processjumptrade,\
                        SNET_idex_jumptrades
                        ]

        elif testListName == 'contacts':

            testList = [

                       SNET_addcontact,\
                        SNET_dispcontact,\
                        SNET_removecontact
                        ]


        elif testListName == 'errs':

            testList = [

                        SNET_idex_placebid,\
                        SNET_idex_placeask,\
                        SNET_idex_orderbook,\

                        ]



        else:

            testList = []

        return testList





def main():
    """

    uTest1 can be invoked from cmd line with a specific test CLASS as agrument:

    python3 -m unittest -vvv uTest1.py

    python3 -m unittest -vvv uTest1.SNET_baseSetup

    OR

    by itself with a list of test suites and test classes and test lists to be run

    ./uTest1.py sg base settings testList1


    """#

    #argparse later
    testCollector = TestCollector()
    testClasses = testCollector.getTestClassDict()
    testSuites = testCollector.getTestSuitesDict()


    multiSuite = ['sg', 'base'] # extend as needed


    args = sys.argv[1:]


    for  testCase in args:

        if testCase in testClasses:
            runner = unittest.TextTestRunner()
            runner.run(testClasses[testCase]())

        elif testCase in testSuites:
             suite  = testSuites[testCase]()
             runner = unittest.TextTestRunner()
             runner.run(suite)

        elif testCase == 'sList':
            for singleSuite in multiSuite:
                 suite  = testSuites[singleSuite]() # this returns a callable!
                 runner = unittest.TextTestRunner()
                 runner.run(suite)

        else:

            verifTestList = testCollector.getTestList(testCase)
            for test in verifTestList:

                runner = unittest.TextTestRunner()
                runner.run(test())


    try:
        if args[0] == 'all':
            unittest.main()
    except:
        print(main.__doc__)




if __name__ == '__main__':
    main()





    """


char *SuperNET_json_commands(struct NXThandler_info *mp,char *previpaddr,cJSON *origargjson,char *sender,int32_t valid,char *origargstr)
 // local glue 7
    static char *gotjson[] = { (char *)gotjson_func, "BTCDjson", "V", "json", 0 };
    static char *gotpacket[] = { (char *)gotpacket_func, "gotpacket", "V", "msg", "dur", "ip_port", 0 };
    static char *gotnewpeer[] = { (char *)gotnewpeer_func, "gotnewpeer", "V", "ip_port", 0 };
    static char *BTCDpoll[] = { (char *)BTCDpoll_func, "BTCDpoll", "V", 0 };
    static char *GUIpoll[] = { (char *)GUIpoll_func, "GUIpoll", "V", 0 };
    static char *stop[] = { (char *)stop_func, "stop", "V", 0 };
    static char *settings[] = { (char *)settings_func, "settings", "V", "field", "value", "reinit", 0 };

    // passthru 2
    static char *passthru[] = { (char *)passthru_func, "passthru", "V", "coin", "method", "params", "tag", 0 };
    static char *remote[] = { (char *)remote_func, "remote", "V",  "coin", "method", "result", "tag", 0 };


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


    // MGW 7
    static char *genmultisig[] = { (char *)genmultisig_func, "genmultisig", "", "userpubkey", "coin", "refcontact", "M", "N", "contacts", "destip", "destport", "email", "buyNXT", 0 };
    static char *getmsigpubkey[] = { (char *)getmsigpubkey_func, "getmsigpubkey", "V", "coin", "refNXTaddr", "myaddr", "mypubkey", 0 };
    static char *MGWaddr[] = { (char *)MGWaddr_func, "MGWaddr", "V", 0 };
    static char *MGWresponse[] = { (char *)MGWresponse_func, "MGWresponse", "V", 0 };     static char *setmsigpubkey[] = { (char *)setmsigpubkey_func, "setmsigpubkey", "V", "coin", "refNXTaddr", "addr", "userpubkey", 0 };
    static char *cosign[] = { (char *)cosign_func, "cosign", "V", "otheracct", "seed", "text", 0 };
    static char *cosigned[] = { (char *)cosigned_func, "cosigned", "V", "seed", "result", "privacct", "pubacct", 0 };
    static char *setmsigpubkey[] = { (char *)setmsigpubkey_func, "setmsigpubkey", "V", "coin", "refNXTaddr", "addr", "userpubkey", 0 };


    // IP comms 6
    static char *ping[] = { (char *)ping_func, "ping", "V", "pubkey", "ipaddr", "port", "destip", "MMatrix", 0 };
    static char *pong[] = { (char *)pong_func, "pong", "V", "pubkey", "ipaddr", "port", "yourip", "yourport", "tag", "MMatrix", 0 };
    static char *sendfrag[] = { (char *)sendfrag_func, "sendfrag", "V", "pubkey", "name", "fragi", "numfrags", "ipaddr", "totalcrc", "datacrc", "data", "totallen", "blocksize", "handler", 0 };
    static char *gotfrag[] = { (char *)gotfrag_func, "gotfrag", "V", "pubkey", "name", "fragi", "numfrags", "ipaddr", "totalcrc", "datacrc", "totallen", "blocksize", "count", "handler", 0 };
    static char *startxfer[] = { (char *)startxfer_func, "startxfer", "V", "fname", "dest", "data", "timeout", "handler", 0 };
    static char *getfile[] = { (char *)getfile_func, "getfile", "V", "name", "handler", 0 };


    // Kademlia DHT 8
    static char *puzzles[] = { (char *)challenge_func, "puzzles", "V", "reftime", "duration", "threshold", 0 };
    static char *nonces[] = { (char *)response_func, "nonces", "V", "reftime", "threshold", "nonces", 0 };

    static char *store[] = { (char *)store_func, "store", "V", "pubkey", "key", "name", "data", 0 };
    static char *findvalue[] = { (char *)findvalue_func, "findvalue", "V", "pubkey", "key", "name", "data", 0 };
    static char *findnode[] = { (char *)findnode_func, "findnode", "V", "pubkey", "key", "name", "data", 0 };
    static char *havenode[] = { (char *)havenode_func, "havenode", "V", "pubkey", "key", "name", "data", 0 };
    static char *havenodeB[] = { (char *)havenodeB_func, "havenodeB", "V", "pubkey", "key", "name", "data", 0 };
    static char *findaddress[] = { (char *)findaddress_func, "findaddress", "V", "refaddr", "list", "dist", "duration", "numthreads", 0 };

    // MofNfs 3
    static char *savefile[] = { (char *)savefile_func, "savefile", "V", "fname", "L", "M", "N", "backup", "password", "pin", 0 };
    static char *restorefile[] = { (char *)restorefile_func, "restorefile", "V", RESTORE_ARGS, 0 };
    static char *publish[] = { (char *)publish_func, "publish", "V", "files", "L", "M", "N", "backup", "password", "pin", 0  };

    // Telepathy 9
    static char *getpeers[] = { (char *)getpeers_func, "getpeers", "V",  "scan", 0 };
    static char *addcontact[] = { (char *)addcontact_func, "addcontact", "V",  "handle", "acct", 0 };
    static char *removecontact[] = { (char *)removecontact_func, "removecontact", "V",  "contact", 0 };
    static char *dispcontact[] = { (char *)dispcontact_func, "dispcontact", "V",  "contact", 0 };
    static char *telepathy[] = { (char *)telepathy_func, "telepathy", "V",  "contact", "id", "type", "attach", 0 };
    static char *getdb[] = { (char *)getdb_func, "getdb", "V",  "contact", "id", "key", "dir", "destip", 0 };
    static char *sendmsg[] = { (char *)sendmsg_func, "sendmessage", "V", "dest", "msg", "L", 0 };
    static char *sendbinary[] = { (char *)sendbinary_func, "sendbinary", "V", "dest", "data", "L", 0 };
    static char *checkmsg[] = { (char *)checkmsg_func, "checkmessages", "V", "sender", 0 };

    // Teleport 3
    static char *maketelepods[] = { (char *)maketelepods_func, "maketelepods", "V", "amount", "coin", 0 };
    static char *telepodacct[] = { (char *)telepodacct_func, "telepodacct", "V", "amount", "contact", "coin", "comment", "cmd", "withdraw", 0 };
    static char *teleport[] = { (char *)teleport_func, "teleport", "V", "amount", "contact", "coin", "minage", "withdraw", 0 };

    // InstantDEX 8
    static char *allorderbooks[] = { (char *)allorderbooks_func, "allorderbooks", "V", 0 };
    static char *openorders[] = { (char *)openorders_func, "openorders", "V", 0 };
    static char *orderbook[] = { (char *)orderbook_func, "orderbook", "V", "baseid", "relid", "allfields", "oldest", 0 };
    static char *placebid[] = { (char *)placebid_func, "placebid", "V", "baseid", "relid", "volume", "price", 0 };
    static char *placeask[] = { (char *)placeask_func, "placeask", "V", "baseid", "relid", "volume", "price",0 };
    static char *makeoffer[] = { (char *)makeoffer_func, "makeoffer", "V", "baseid", "relid", "baseamount", "relamount", "other", "type", 0 };
    static char *respondtx[] = { (char *)respondtx_func, "respondtx", "V", "signedtx", 0 };
    static char *processutx[] = { (char *)processutx_func, "processutx", "V", "utx", "sig", "full", 0 };
    static char *bid[] = { (char *)bid_func, "bid", "V", "baseid", "relid", "volume", "price", "timestamp", "baseamount", "relamount", "type", 0 };
    static char *ask[] = { (char *)ask_func, "ask", "V", "baseid", "relid", "volume", "price", "timestamp", "baseamount", "relamount", "type", 0 };


    // Tradebot 3
    static char *pricedb[] = { (char *)pricedb_func, "pricedb", "V", "exchange", "base", "rel", "stop", 0 };
    static char *getquotes[] = { (char *)getquotes_func, "getquotes", "V", "exchange", "base", "rel", "oldest", 0 };
    static char *tradebot[] = { (char *)tradebot_func, "tradebot", "V", "code", 0 };

    // Privatbet 1
    static char *lotto[] = { (char *)lotto_func, "lotto", "V", "refacct", "asset", 0 };

    // EmLang 2
    static char *python[] = { (char *)python_func, "python", "V",  "name", 0 };
    static char *syscall[] = { (char *)syscall_func, "syscall", "V",  "name", "cmd", 0 };

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
#
#
#
#
#
#
#
#
# there should be 2 kinds of unit tests
#
# blackyblack [11:15 PM]
# for testing server you test the internals
#
# blackyblack [11:16 PM]
# so no need for POST
#
# blackyblack [11:16 PM]
# for testing client side you create a fake server and test client requets
#
# blackyblack [11:16 PM]11:16
# all networking is removed from testing
#
# blackyblack [11:17 PM]
# for networking you create another test suite and test it separately from client/server


##############################################
##############################################
#
#	DEPRECATED
#
#
##############################################
##############################################
class SNET_idex_makeoffer2(SNET_BaseTest, SNET_apicalls):


    def setUp(self):
        print(" test makeoffer2 setUp func here")
        pass



    def runTest(self):
        self.test_makeoffer2()


    def test_makeoffer2(self):
#
        print(5*"\n++++++++++++","test_makeoffer2")
        test_RQ_makeoffer2 = {'requestType': 'makeoffer2'}
        payload= self.qComp_777.make_777POST_Request(test_RQ_makeoffer2)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )
        
        
##############################################
##############################################
#
#	DEPRECATED
#
#
##############################################
##############################################
class SNET_idex_makeoffer(SNET_BaseTest, SNET_apicalls):
    """makeoffer
Makeoffer is under construction, not currently working.
The orderbook contains additional information required to send a makeoffer call to meet another user's bid/ask. Use allfields in orderbook to show this information for each orderbook entry.
static char makeoffer[] = { (char )makeoffer_func, "makeoffer", "V", "baseid", "relid", "baseamount", "relamount", "other", "type", 0 }'
example
./BitcoinDarkd SuperNET '{"requestType":"orderbook","baseid":"11060861818140490423","relid":"17554243582654188572","allfields":1}'
result
{
	"key":		"7646303683960469163",
	"baseid":	"11060861818140490423",
 	"relid":	"17554243582654188572",
 	"bids":		"0.00550000000", "100.00000000", 0, "'''6249611027680999354'''",
	"asks":		[["0.00500000000", "50.00000000", 0, "6249611027680999354"], ["0.00500000000", "50.00000000", 0, "6249611027680999354"]]
}
Each entry now includes the NXT address of the user that submitted it (here in bold).
For makeoffer, other = the NXT address of the account the posted the bid/ask. Currently type = 0 by default.
example
./BitcoinDarkd SuperNET '{"requestType":"makeoffer","baseid":"11060861818140490423","relid":"17554243582654188572","baseamount":"10","relamount":"0.055","other":"6249611027680999354","type":0 }'
result
{"error":"illegal parameter","descr":"NXT.6249611027680999354 makeoffer to NXT.11060861818140490423 10.00000000 asset.17554243582654188572 for 0.00000000 asset.0, type.0 }'"""

    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_makeoffer()


    def test_makeoffer(self):

        query_json = {
                        'requestType': 'makeoffer',\
                        'relid': '17554243582654188572',\
                        'other': '8279528579993996036', \
                        'baseamount': '101111100',\
                        'relamount': '617900', \
                        'type': '', \
                        'baseid': '11060861818140490423',\
                        'subscribe':  1,\
                        }

# {'result': 'invalid makeoffer_func request'}



        print(5*"\n++++++++++++","test_makeoffer")
        test_RQ_ = {'requestType': 'makeoffer'}
        test_RQ_ = query_json
        payload= self.qComp_777.make_777POST_Request(test_RQ_)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        print(testReq.text)

        rpl777_string =testReq.text #  eval(
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777_string:\n\n", rpl777_string)


        self.assertTrue('comment' in rpl777_string )

