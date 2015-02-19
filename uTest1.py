#!/usr/bin/env python3

#import random
import unittest
import requests
import json

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
        reqType = {'requestType': 'settings'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        for setting in rpl777:
            print(setting, " - ", rpl777[setting])




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
        self.settingsPassed=True

        req_getpeers = {'requestType': 'getpeers'}
        payload = self.qComp_777.make_777POST_Request(req_getpeers)

        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)

        print(rpl777)
        self.localpeers=rpl777['peers']

        establishNetwork = True
        while establishNetwork:

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
                #print(payload)
                time.sleep(0.2)
                testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
                rpl777 = eval(testReq.text)
                print("req_findnode rpl777: ",rpl777)


            time.sleep(0.1)

            reqType = {'requestType': 'GUIpoll'}
            payload= self.qComp_777.make_777POST_Request(reqType)

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


    def setUp(self):
        print("SNET_getpeers setUp here- NOP")
        pass


    def runTest(self):
        self.test_getpeers()


    def test_getpeers(self):

        """
        self.assertTrue('peers' in rpl777.keys())

        """ #

        print(5*"\n++++++++++++","test_getpeers")
        reqType = {'requestType': 'getpeers'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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
        print(5*"\n++++++++++++","test_gotjson")
        reqType = {'requestType': 'gotjson'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_gotpacket")
        reqType = {'requestType': 'gotpacket'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        print(rpl777['error'])
        if 'error' in rpl777.keys():
            self.Assert(False)
        else:
            self.assertTrue('result' in rpl777.keys() )



class SNET_gotnewpeer(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_gotnewpeer()


    def test_gotnewpeer(self):

        print(5*"\n++++++++++++","test_gotnewpeer")
        reqType = {'requestType': 'gotnewpeer'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        null = None # to be determined
        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )





    #// passthru


class SNET_BTCDpoll(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_BTCDpoll()


    def test_BTCDpoll(self):

        print(5*"\n++++++++++++","test_BTCDpoll")
        reqType = {'requestType': 'BTCDpoll'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )


class SNET_GUIpoll(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_GUIpoll()


    def test_GUIpoll(self):

        print(5*"\n++++++++++++","test_GUIpoll")
        reqType = {'requestType': 'GUIpoll'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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
        print(5*"\n++++++++++++","test_settings")
        reqType = {'requestType': 'settings'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_passthru")
        reqType = {'requestType': 'passthru'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue(True)





    #// ramchains   13


class SNET_remote(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_remote()


    def test_remote(self):

        print(5*"\n++++++++++++","test_remote")
        reqType = {'requestType': 'remote'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )


    #########################



    #     // ramchains 13
    #########################



class ___Ramchains():
    pass


class SNET_ramstatus(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass


    def runTest(self):
        self.test_ramstatus()



    def test_ramstatus(self):

        print(5*"\n++++++++++++","test_ramstatus")
        reqType = {'requestType': 'ramstatus'}
        reqType['coin'] = 'BTCD' #

        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_ramaddrlist")
        reqType = {'requestType': 'ramaddrlist'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_ramstring(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass




    def runTest(self):
        self.test_ramstring()

    def test_ramstring(self):

        print(5*"\n++++++++++++","test_ramstring")
        reqType = {'requestType': 'ramstring'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_ramrawind(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_ramrawind()


    def test_ramrawind(self):

        print(5*"\n++++++++++++","test_ramrawind")
        reqType = {'requestType': 'ramrawind'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_ramblock(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass


    def runTest(self):
        self.test_ramblock()



    def test_ramblock(self):

        print(5*"\n++++++++++++","test_ramblock")
        reqType = {'requestType': 'ramblock'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_ramscript(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_ramscript()


    def test_ramscript(self):

        print(5*"\n++++++++++++","test_ramscript")
        reqType = {'requestType': 'ramscript'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_ramtxlist(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_ramtxlist()


    def test_ramtxlist(self):

        print(5*"\n++++++++++++","test_ramtxlist")
        reqType = {'requestType': 'ramtxlist'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_ramrichlist")
        reqType = {'requestType': 'ramrichlist'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_x1")
        reqType = {'requestType': 'test_ramcompress'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_ramexpand")
        reqType = {'requestType': 'ramexpand'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_rambalances")
        reqType = {'requestType': 'rambalances'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_rampyramid")
        reqType = {'requestType': 'rampyramid'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_ramresponse")
        reqType = {'requestType': 'ramresponse'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_genmultisig")
        reqType = {'requestType': 'genmultisig'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_getmsigpubkey")
        reqType = {'requestType': 'getmsigpubkey'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_MGWaddr")
        reqType = {'requestType': 'MGWaddr'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_MGWresponse")
        reqType = {'requestType': 'MGWresponse'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_setmsigpubkey")
        reqType = {'requestType': 'setmsigpubkey'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_cosign")
        reqType = {'requestType': 'cosign'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_cosigned")
        reqType = {'requestType': 'cosigned'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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


class SNET_ping(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_ping()


    def test_ping(self):

        print(5*"\n++++++++++++","test_ping")
        reqType = {'requestType': 'ping'}
        reqType['destip'] = 'localhost'
        payload= self.qComp_777.make_777POST_Request(reqType)
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
        print(5*"\n++++++++++++","test_pong")
        reqType = {'requestType': 'pong'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )




class SNET_sendfrag(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_sendfrag()


    def test_sendfrag(self):

        print(5*"\n++++++++++++","test_sendfrag")
        reqType = {'requestType': 'sendfrag'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_gotfrag")
        reqType = {'requestType': 'gotfrag'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )







    # // Kademlia DHT


class SNET_startxfer(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass


    def runTest(self):
        self.test_startxfer()



    def test_startxfer(self):

        print(5*"\n++++++++++++","test_startxfer")
        reqType = {'requestType': 'startxfer'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )

#findvalue


    #########################




    #     // Kademlia DHT  6

    #########################

class __Kademlia():
    pass

class SNET_store(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_store()


    def test_store(self):

        print(5*"\n++++++++++++","test_store")
        reqType = {'requestType': 'store'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_findnode(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_findnode()


    def test_findnode(self):

        print(5*"\n++++++++++++","test_findnode")
        reqType = {'requestType': 'findnode'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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
        reqType = {'requestType': 'havenode'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_findnode")
        reqType = {'requestType': 'findnode'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_havenodeB")
        reqType = {'requestType': 'havenodeB'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_savefile")
        reqType = {'requestType': 'savefile'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_restorefile")
        reqType = {'requestType': 'restorefile'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_publish")
        reqType = {'requestType': 'publish'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )





    # // Telepathy
##############getpeers

    #########################
    #     // Telepathy 9
    #########################




class SNET_addcontact(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_addcontact()


    def test_addcontact(self):

        print(5*"\n++++++++++++","test_addcontact")
        reqType = {'requestType': 'addcontact'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )


class ___Telepathy():
    pass

class SNET_removecontact(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_removecontact()


    def test_removecontact(self):

        print(5*"\n++++++++++++","test_removecontact")
        reqType = {'requestType': 'removecontact'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_dispcontact(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_dispcontact()


    def test_dispcontact(self):

        print(5*"\n++++++++++++","test_dispcontact")
        reqType = {'requestType': 'dispcontact'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_telepathy(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_telepathy()


    def test_telepathy(self):

        print(5*"\n++++++++++++","test_telepathy")
        reqType = {'requestType': 'telepathy'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_getdb(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_getdb()


    def test_getdb(self):

        print(5*"\n++++++++++++","test_getdb")
        reqType = {'requestType': 'getdb'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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



    def runTest(self):
        self.test_sendmessage()


    def test_sendmessage(self):

        print(5*"\n++++++++++++","test_sendmessage")
        reqType = {'requestType': 'sendmessage'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_sendbinary(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_sendbinary()


    def test_sendbinary(self):

        print(5*"\n++++++++++++","test_sendbinary")
        reqType = {'requestType': 'sendbinary'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_checkmsg(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_checkmsg()


    def test_checkmsg(self):

        print(5*"\n++++++++++++","test_checkmsg")
        reqType = {'requestType': 'checkmsg'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_maketelepods")
        reqType = {'requestType': 'maketelepods'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_telepodacct")
        reqType = {'requestType': 'telepodacct'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_teleport")
        reqType = {'requestType': 'teleport'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )



    # // InstantDEX


    #########################





    #     // InstantDEX 8
    #########################

class ___InstantDex():
    pass

class SNET_allorderbooks(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_allorderbooks()


    def test_allorderbooks(self):

        print(5*"\n++++++++++++","test_allorderbooks")
        reqType = {'requestType': 'allorderbooks'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        # good reply:
        # SuperNET rpl777y:
        # {'orderbooks': [{'rel': 'NET', 'relid': '12071612744977229797', 'baseid': '11060861818140490423', 'base': 'BTCD', 'numquotes': 7}]}


        self.assertTrue('orderbooks' in rpl777.keys() )


class SNET_openorders(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_openorders()


    def test_openorders(self):

        print(5*"\n++++++++++++","test_openorders")
        reqType = {'requestType': 'openorders'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        #         {'result': 'no openorders'}

        self.assertTrue('result' in rpl777.keys() )



class SNET_orderbook(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_orderbook()


    def test_orderbook(self):

        print(5*"\n++++++++++++","test_orderbook")
        reqType = {'requestType': 'orderbook'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

# {'error': 'no such orderbook.(0 ^ 0)'}

        self.assertTrue('result' in rpl777.keys() )



class SNET_placebid(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_placebid()


    def test_placebid(self):

        print(5*"\n++++++++++++","test_placebid")
        reqType = {'requestType': 'placebid'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )



class SNET_placeask(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_placeask()


    def test_placeask(self):

        print(5*"\n++++++++++++","test_placeask")
        reqType = {'requestType': 'placeask'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )



class SNET_makeoffer(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_makeoffer()


    def test_makeoffer(self):

        print(5*"\n++++++++++++","test_makeoffer")
        reqType = {'requestType': 'makeoffer'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_respondtx(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_respondtx()


    def test_respondtx(self):

        print(5*"\n++++++++++++","test_respondtx")
        reqType = {'requestType': 'respondtx'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)


        self.assertTrue('result' in rpl777.keys() )



class SNET_processutx(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_processutx()


    def test_processutx(self):

        print(5*"\n++++++++++++","test_processutx")
        reqType = {'requestType': 'processutx'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )




    # // Tradebot
    #########################





    #     // Tradebot 3
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

        print(5*"\n++++++++++++","test_pricedb")
        reqType = {'requestType': 'pricedb'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_getquotes")
        reqType = {'requestType': 'getquotes'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_tradebot")
        reqType = {'requestType': 'tradebot'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )




    # // # privatebet

class ___Privatebet():
    pass

class SNET_lotto(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def runTest(self):
        self.test_lotto()


    def test_lotto(self):

        print(5*"\n++++++++++++","test_lotto")
        reqType = {'requestType': 'lotto'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )



    # // Embedded Langs
class ___EmLang():
    pass


class SNET_python(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass


    def runTest(self):
        self.test_python()



    def test_python(self):

        print(5*"\n++++++++++++","test_python")
        reqType = {'requestType': 'python'}
        payload= self.qComp_777.make_777POST_Request(reqType)
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

        print(5*"\n++++++++++++","test_syscall")
        reqType = {'requestType': 'syscall'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}

        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:\n\n", rpl777)

        self.assertTrue('result' in rpl777.keys() )



##############################################
##############################################
##############################################
##############################################
##############################################



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

        testClasses = {}
        #
        testClasses['SNET_baseSetup'] = SNET_baseSetup #
        #
        testClasses['SNET_gotjson'] = SNET_gotjson     #
        testClasses['SNET_gotpacket'] = SNET_gotpacket #
        testClasses['SNET_gotnewpeer'] = SNET_gotnewpeer #
        testClasses['SNET_BTCDpoll'] = SNET_BTCDpoll #
        testClasses['SNET_GUIpoll'] = SNET_GUIpoll    #
        testClasses['SNET_settings'] = SNET_settings  #
        #
        testClasses['SNET_passthru'] = SNET_passthru
        testClasses['SNET_remote'] = SNET_remote
        #
        testClasses['SNET_ramstatus'] = SNET_ramstatus ##
        testClasses['SNET_ramaddrlist'] = SNET_ramaddrlist
        testClasses['SNET_ramstring'] = SNET_ramstring
        testClasses['SNET_ramrawind'] = SNET_ramrawind
        testClasses['SNET_ramblock'] = SNET_ramblock
        testClasses['SNET_ramscript'] = SNET_ramscript
        testClasses['SNET_ramtxlist'] = SNET_ramtxlist
        testClasses['SNET_ramrichlist'] = SNET_ramrichlist
        testClasses['SNET_ramcompress'] = SNET_ramcompress
        testClasses['SNET_ramexpand'] = SNET_ramexpand
        testClasses['SNET_rambalances'] = SNET_rambalances
        testClasses['SNET_rampyramid'] = SNET_rampyramid
        testClasses['SNET_ramresponse'] = SNET_ramresponse
        #
        testClasses['SNET_genmultisig'] = SNET_genmultisig
        testClasses['SNET_getmsigpubkey'] = SNET_getmsigpubkey
        testClasses['SNET_MGWaddr'] = SNET_MGWaddr
        testClasses['SNET_MGWresponse'] = SNET_MGWresponse
        testClasses['SNET_setmsigpubkey'] = SNET_setmsigpubkey
        testClasses['SNET_cosign'] = SNET_cosign
        testClasses['SNET_cosigned'] = SNET_cosigned
        #
        testClasses['SNET_ping'] = SNET_ping #
        testClasses['SNET_pong'] = SNET_pong # [#]
        testClasses['SNET_sendfrag'] = SNET_sendfrag
        testClasses['SNET_gotfrag'] = SNET_gotfrag
        testClasses['SNET_startxfer'] = SNET_startxfer
        #
        testClasses['SNET_store'] = SNET_store
        testClasses['SNET_findnode'] = SNET_findnode #
        testClasses['SNET_havenode'] = SNET_havenode
        testClasses['SNET_findaddress'] = SNET_findaddress
        testClasses['SNET_havenodeB'] = SNET_havenodeB
        #
        testClasses['SNET_savefile'] = SNET_savefile
        testClasses['SNET_restorefile'] = SNET_restorefile
        testClasses['SNET_publish'] = SNET_publish
        #
        testClasses['SNET_getpeers'] = SNET_getpeers          #
        testClasses['SNET_addcontact'] = SNET_addcontact
        testClasses['SNET_removecontact'] = SNET_removecontact
        testClasses['SNET_dispcontact'] = SNET_dispcontact
        testClasses['SNET_telepathy'] = SNET_telepathy
        testClasses['SNET_getdb'] = SNET_getdb
        testClasses['SNET_sendmessage'] = SNET_sendmessage
        testClasses['SNET_sendbinary'] = SNET_sendbinary
        testClasses['SNET_checkmsg'] = SNET_checkmsg
        #
        testClasses['SNET_maketelepods'] = SNET_maketelepods
        testClasses['SNET_telepodacct'] = SNET_telepodacct
        testClasses['SNET_teleport'] = SNET_teleport
        #
        testClasses['SNET_allorderbooks'] = SNET_allorderbooks #
        testClasses['SNET_openorders'] = SNET_openorders       #
        testClasses['SNET_orderbook'] = SNET_orderbook
        testClasses['SNET_placebid'] = SNET_placebid
        testClasses['SNET_placeask'] = SNET_placeask
        testClasses['SNET_makeoffer'] = SNET_makeoffer
        testClasses['SNET_respondtx'] = SNET_respondtx
        testClasses['SNET_processutx'] = SNET_processutx
        #
        testClasses['SNET_pricedb'] = SNET_pricedb
        testClasses['SNET_getquotes'] = SNET_getquotes
        testClasses['SNET_tradebot'] = SNET_tradebot
        #
        testClasses['SNET_lotto'] = SNET_lotto
        #
        testClasses['SNET_python'] = SNET_python
        testClasses['SNET_syscall'] = SNET_syscall

        return testClasses


    def  getTestSuitesDict(self, ):

        testSuites = {}
        testSuites['base'] = suite_baseSetup
        testSuites['base1'] = suite_baseSetup
        testSuites['base2'] = suite_baseSetup
        testSuites['base3'] = suite_baseSetup
        testSuites['base4'] = suite_baseSetup
        testSuites['base5'] = suite_baseSetup
        testSuites['base6'] = suite_baseSetup
        testSuites['sg'] = suite_SG
        return testSuites

    def getTestList(self):
        pass

def main():
    """

    uTest1 can be invoked from cmd line with a specific test CLASS as agrument:

    python3 -m unittest -vvv uTest1.SNET_baseSetup

    OR

    by itself with a list of test suites and test classes and test lists to be run

    ./uTest1.py sg base settings testList1


    """#

    #argparse later
    testCollector = TestCollector()
    testClasses = testCollector.getTestClassDict()
    testSuites = testCollector.getTestSuitesDict()
    testList1 = [ SNET_settings, SNET_getpeers ]

    args = sys.argv[1:]

    for  test in args:

        if test in testClasses:

            runner = unittest.TextTestRunner()
            runner.run(testClasses[test]())


        elif test in testSuites:

             suite  = testSuites[test]()
             runner = unittest.TextTestRunner()
             runner.run(suite)

        elif test == 'tl1':
            for test in testList1:

                runner = unittest.TextTestRunner()
                runner.run(test())

    try:
        if args[0] == 'all':
            unittest.main()
    except:
        print(main.__doc__)




if __name__ == '__main__':
    main()





# List of tests and what they do:

# getpeers:

    """


char *SuperNET_json_commands(struct NXThandler_info *mp,char *previpaddr,cJSON *origargjson,char *sender,int32_t valid,char *origargstr)
{
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

    // ramchains   13
    static char *ramstatus[] = { (char *)ramstatus_func, "ramstatus", "V", "destip", "coin", 0 };
    static char *ramaddrlist[] = { (char *)ramaddrlist_func, "ramaddrlist", "V", "coin", 0 };
    static char *ramstring[] = { (char *)ramstring_func, "ramstring", "V", "destip", "coin", "type", "rawind", 0 };
    static char *ramrawind[] = { (char *)ramrawind_func, "ramrawind", "V", "destip", "coin", "type", "string", 0 };
    static char *ramblock[] = { (char *)ramblock_func, "ramblock", "V", "destip", "coin", "blocknum", 0 };
    static char *ramscript[] = { (char *)ramscript_func, "ramscript", "V", "destip", "coin", "txid", "vout", "blocknum", "txind", "v", 0 };
    static char *ramtxlist[] = { (char *)ramtxlist_func, "ramtxlist", "V", "destip", "coin", "address", "unspent", 0 };
    static char *ramrichlist[] = { (char *)ramrichlist_func, "ramrichlist", "V", "destip", "coin", "numwhales", "recalc", 0 };
    static char *ramcompress[] = { (char *)ramcompress_func, "ramcompress", "V", "destip", "coin", "data", 0 };
    static char *ramexpand[] = { (char *)ramexpand_func, "ramexpand", "V", "destip", "coin", "data", 0 };
    static char *rambalances[] = { (char *)rambalances_func, "rambalances", "V", "destip", "coin", "coins", "rates", 0 };
    static char *ramresponse[] = { (char *)ramresponse_func, "ramresponse", "V", "coin", "origcmd", "data", 0 };
    static char *rampyramid[] = { (char *)rampyramid_func, "rampyramid", "V", "destip", "port", "coin", "blocknum", "type", 0 };

    // MGW 7
    static char *genmultisig[] = { (char *)genmultisig_func, "genmultisig", "", "userpubkey", "coin", "refcontact", "M", "N", "contacts", "destip", "destport", "email", "buyNXT", 0 };
    static char *getmsigpubkey[] = { (char *)getmsigpubkey_func, "getmsigpubkey", "V", "coin", "refNXTaddr", "myaddr", "mypubkey", 0 };
    static char *MGWaddr[] = { (char *)MGWaddr_func, "MGWaddr", "V", 0 };
    static char *MGWresponse[] = { (char *)MGWresponse_func, "MGWresponse", "V", 0 };     static char *setmsigpubkey[] = { (char *)setmsigpubkey_func, "setmsigpubkey", "V", "coin", "refNXTaddr", "addr", "userpubkey", 0 };
    static char *cosign[] = { (char *)cosign_func, "cosign", "V", "otheracct", "seed", "text", 0 };
    static char *cosigned[] = { (char *)cosigned_func, "cosigned", "V", "seed", "result", "privacct", "pubacct", 0 };

    // IP comms 5
  *  static char *ping[] = { (char *)ping_func, "ping", "V", "pubkey", "ipaddr", "port", "destip", "MMatrix", 0 };
    static char *pong[] = { (char *)pong_func, "pong", "V", "pubkey", "ipaddr", "port", "yourip", "yourport", "tag", "MMatrix", 0 };
    static char *sendfrag[] = { (char *)sendfrag_func, "sendfrag", "V", "pubkey", "name", "fragi", "numfrags", "ipaddr", "totalcrc", "datacrc", "data", "totallen", "blocksize", "handler", 0 };
    static char *gotfrag[] = { (char *)gotfrag_func, "gotfrag", "V", "pubkey", "name", "fragi", "numfrags", "ipaddr", "totalcrc", "datacrc", "totallen", "blocksize", "count", "handler", 0 };
    static char *startxfer[] = { (char *)startxfer_func, "startxfer", "V", "fname", "dest", "data", "timeout", "handler", 0 };

    // Kademlia DHT 6
    static char *store[] = { (char *)store_func, "store", "V", "pubkey", "key", "name", "data", 0 };
  *  static char *findvalue[] = { (char *)findvalue_func, "findvalue", "V", "pubkey", "key", "name", "data", 0 };
    static char *findnode[] = { (char *)findnode_func, "findnode", "V", "pubkey", "key", "name", "data", 0 };
    static char *havenode[] = { (char *)havenode_func, "havenode", "V", "pubkey", "key", "name", "data", 0 };
    static char *havenodeB[] = { (char *)havenodeB_func, "havenodeB", "V", "pubkey", "key", "name", "data", 0 };
    static char *findaddress[] = { (char *)findaddress_func, "findaddress", "V", "refaddr", "list", "dist", "duration", "numthreads", 0 };

    // MofNfs 3
    static char *savefile[] = { (char *)savefile_func, "savefile", "V", "fname", "L", "M", "N", "backup", "password", "pin", 0 };
    static char *restorefile[] = { (char *)restorefile_func, "restorefile", "V", RESTORE_ARGS, 0 };
    static char *publish[] = { (char *)publish_func, "publish", "V", "files", "L", "M", "N", "backup", "password", "pin", 0  };

    // Telepathy 9
  *  static char *getpeers[] = { (char *)getpeers_func, "getpeers", "V",  "scan", 0 };
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

