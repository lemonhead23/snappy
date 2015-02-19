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




    def test_SNET_baseSetup(self):

        print(5*"\ntest_SNET_baseSetup")
        time.sleep(3)
        #self.assertTrue(self.SNET_baseSetupOK)
        self.failUnless(self.SNET_baseSetupOK)


    # GUIpoll reply: kademlia_pong ------->
    # {'result': '{"result":"kademlia_pong","tag":"","isMM":"0","NXT":"1978065578067355462","ipaddr":"127.0.0.1","port":0,"lag":"143.250","numpings":5,"numpongs":24,"ave":"366301.170"}', 'from': '89.212.19.49', 'args': '[{"requestType":"pong","NXT":"1978065578067355462","time":1424204548,"MMatrix":0,"yourip":"178.62.185.131","yourport":35671,"ipaddr":"127.0.0.1","pubkey":"c269a8b4567c0b3062e6c4be859d845c4b808a405dd03d0d1ac7b4d9cb725b40","ver":"0.599"},{"token":"aqqagqe2sph302rsgieobfm482580iqs386jrk2teb5tjd67a6scag2ricaddi82i9cgd2qokv9147cqp2aqbtoogldjbaofuoga3cb3r2m06qjmfu5gpl8s63m6hn2gfahl3l4o7t0eds96d78t4eiclm5psims"}]', 'port': 0}
    # {'args': '[{"requestType":"pong","NXT":"1978065578067355462","time":1424241662,"MMatrix":0,"yourip":"178.62.185.131","yourport":33978,"ipaddr":"89.212.19.49","pubkey":"c269a8b4567c0b3062e6c4be859d845c4b808a405dd03d0d1ac7b4d9cb725b40","ver":"0.599"},{"token":"aqqagqe2sph302rsgieobfm482580iqs386jrk2teb5tjd67a94rsg2r93ggu7o2va245utlbcftdrfqkm74cjnc4nomh0tsrbe3iupfn2mg2r2ii6k40iki6b70ppfo3naq2vcmndtab86m036r22g3ka2f2a4f"}]', 'from': '89.212.19.49', 'result': '{"result":"kademlia_pong","tag":"","isMM":"0","NXT":"1978065578067355462","ipaddr":"89.212.19.49","port":0,"lag":"84380.922","numpings":0,"numpongs":2,"ave":"70919.423"}', 'port': 0}
    # {'result': 'nothing pending'}



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
        #
        # print(rpl777['Numnxtaccts'])
        # print(rpl777['Numpservers'])
        # print(rpl777['num'])
        #
        # for peer in rpl777['peers']:#
        #     for dat in peer:
        #         print(dat, " - ", peer[dat])
        #     print("\n")

        self.assertTrue('peers' in rpl777.keys())

    #
    # def test_getpeers(self):
    #
    #     print(5*"\n++++++++++++**","test_getpeers")
    #     reqType = {'requestType': 'getpeers'}
    #     payload= self.qComp_777.make_777POST_Request(reqType)
    #     print("query json is: ", payload)
    #     headers = {'content-type': 'application/json'}
    #     testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
    #
    #     rpl777 = eval(testReq.text)
    #     print(15*"\n~~~~~~~~~~~~","SuperNET rpl777y:",rpl777)
    #
    #
    #     print(rpl777['Numnxtaccts'])
    #     print(rpl777['Numpservers'])
    #     print(rpl777['num'])
    #
    #     for peer in rpl777['peers']:#
    #         for dat in peer:
    #             print(dat, " - ", peer[dat])
    #         print("\n")
    #
    #     self.assertGreater(rpl777['num'],1)

#
        #
        #
        #
        #
        #
        #
        #



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



    def test_gotjson(self):
        null = None #  b'{"result":null}' for when null is sent back, which py doenst know
        print(5*"\n++++++++++++","test_gotjson")
        reqType = {'requestType': 'gotjson'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:", testReq.content) #  b'{"result":null}'


        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777) # rpl777)

# azure@boxfish:~/workbench/nxtDev/TEAM/snappy$ curl   -H 'content-type: text/plain;' 'http://127/nxt?requestType=gotjson'
# {'result': None}
#


        self.assertTrue(True)



class SNET_gotpacket(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_gotpacket(self):

        print(5*"\n++++++++++++","test_gotpacket")
        reqType = {'requestType': 'gotpacket'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)
# {'result': None}
#


        self.assertTrue(True)



class SNET_gotnewpeer(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_gotnewpeer(self):

        print(5*"\n++++++++++++","test_gotnewpeer")
        reqType = {'requestType': 'gotnewpeer'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)




    #// passthru


class SNET_BTCDpoll(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_BTCDpoll(self):

        print(5*"\n++++++++++++","test_BTCDpoll")
        reqType = {'requestType': 'BTCDpoll'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)

        self.assertTrue(True)
# settings

#GUIpoll


class SNET_passthru(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_passthru(self):

        print(5*"\n++++++++++++","test_passthru")
        reqType = {'requestType': 'passthru'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)





    #// ramchains   13


class SNET_remote(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_remote(self):

        print(5*"\n++++++++++++","test_remote")
        reqType = {'requestType': 'remote'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_ramstatus(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_ramstatus(self):

        print(5*"\n++++++++++++","test_ramstatus")
        reqType = {'requestType': 'ramstatus'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_ramaddrlist(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_ramaddrlist(self):

        print(5*"\n++++++++++++","test_ramaddrlist")
        reqType = {'requestType': 'ramaddrlist'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_ramstring(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_ramstring(self):

        print(5*"\n++++++++++++","test_ramstring")
        reqType = {'requestType': 'ramstring'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_ramrawind(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_ramrawind(self):

        print(5*"\n++++++++++++","test_ramrawind")
        reqType = {'requestType': 'ramrawind'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_ramblock(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_ramblock(self):

        print(5*"\n++++++++++++","test_ramblock")
        reqType = {'requestType': 'ramblock'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_ramscript(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_ramscript(self):

        print(5*"\n++++++++++++","test_ramscript")
        reqType = {'requestType': 'ramscript'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_ramtxlist(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_ramtxlist(self):

        print(5*"\n++++++++++++","test_ramtxlist")
        reqType = {'requestType': 'ramtxlist'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_ramrichlist(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_ramrichlist(self):

        print(5*"\n++++++++++++","test_ramrichlist")
        reqType = {'requestType': 'ramrichlist'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_remoramcompresste(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_ramcompress(self):

        print(5*"\n++++++++++++","test_x1")
        reqType = {'requestType': 'test_ramcompress'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_ramexpand(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_ramexpand(self):

        print(5*"\n++++++++++++","test_ramexpand")
        reqType = {'requestType': 'ramexpand'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_rambalances(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_rambalances(self):

        print(5*"\n++++++++++++","test_rambalances")
        reqType = {'requestType': 'rambalances'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_rampyramid(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_rampyramid(self):

        print(5*"\n++++++++++++","test_rampyramid")
        reqType = {'requestType': 'rampyramid'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)






    # // MGW


class SNET_ramresponse(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_ramresponse(self):

        print(5*"\n++++++++++++","test_ramresponse")
        reqType = {'requestType': 'ramresponse'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_genmultisig(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_genmultisig(self):

        print(5*"\n++++++++++++","test_genmultisig")
        reqType = {'requestType': 'genmultisig'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)

        self.assertTrue(True)



class SNET_getmsigpubkey(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_getmsigpubkey(self):

        print(5*"\n++++++++++++","test_getmsigpubkey")
        reqType = {'requestType': 'getmsigpubkey'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_MGWaddr(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_MGWaddr(self):

        print(5*"\n++++++++++++","test_MGWaddr")
        reqType = {'requestType': 'MGWaddr'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)

        self.assertTrue(True)



class SNET_MGWresponse(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_MGWresponse(self):

        print(5*"\n++++++++++++","test_MGWresponse")
        reqType = {'requestType': 'MGWresponse'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_setmsigpubkey(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_setmsigpubkey(self):

        print(5*"\n++++++++++++","test_setmsigpubkey")
        reqType = {'requestType': 'setmsigpubkey'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_MGW(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_MGW(self):

        print(5*"\n++++++++++++","test_MGW")
        reqType = {'requestType': 'MGW'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_cosign(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_cosign(self):

        print(5*"\n++++++++++++","test_cosign")
        reqType = {'requestType': 'cosign'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)






    # // IPcomms(MGW)


class SNET_cosigned(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_cosigned(self):

        print(5*"\n++++++++++++","test_cosigned")
        reqType = {'requestType': 'cosigned'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)

#ping

class SNET_pong(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_pong(self):

        print(5*"\n++++++++++++","test_pong")
        reqType = {'requestType': 'pong'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_sendfrag(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_sendfrag(self):

        print(5*"\n++++++++++++","test_sendfrag")
        reqType = {'requestType': 'sendfrag'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_gotfrag(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_gotfrag(self):

        print(5*"\n++++++++++++","test_gotfrag")
        reqType = {'requestType': 'gotfrag'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)







    # // Kademlia DHT

class SNET_startxfer(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_startxfer(self):

        print(5*"\n++++++++++++","test_startxfer")
        reqType = {'requestType': 'startxfer'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)

#findvalue

class SNET_store(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_store(self):

        print(5*"\n++++++++++++","test_store")
        reqType = {'requestType': 'store'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_findnode(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_findnode(self):

        print(5*"\n++++++++++++","test_findnode")
        reqType = {'requestType': 'findnode'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_havenode(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_havenode(self):

        print(5*"\n++++++++++++","test_havenode")
        reqType = {'requestType': 'havenode'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)

#findaddress

class SNET_havenodeB(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_havenodeB(self):

        print(5*"\n++++++++++++","test_havenodeB")
        reqType = {'requestType': 'havenodeB'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)





    # // MofNfs

class SNET_savefile(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_savefile(self):

        print(5*"\n++++++++++++","test_savefile")
        reqType = {'requestType': 'savefile'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_restorefile(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_restorefile(self):

        print(5*"\n++++++++++++","test_restorefile")
        reqType = {'requestType': 'restorefile'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_publish(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_publish(self):

        print(5*"\n++++++++++++","test_publish")
        reqType = {'requestType': 'publish'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)





    # // Telepathy
##############getpeers


class SNET_getpeers___DOUBLE__1(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_getpeers(self):

        print(5*"\n++++++++++++","test_getpeers")
        reqType = {'requestType': 'getpeers'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:", rpl777)

        print(rpl777['Numnxtaccts'])
        print(rpl777['Numpservers'])
        print(rpl777['num'])

        for peer in rpl777['peers']:#
            for dat in peer:
                print(dat, " - ", peer[dat])
            print("\n")

        self.assertTrue('peers' in rpl777.keys())



class SNET_addcontact(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_addcontact(self):

        print(5*"\n++++++++++++","test_addcontact")
        reqType = {'requestType': 'addcontact'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)

        self.assertTrue(True)



class SNET_removecontact(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_removecontact(self):

        print(5*"\n++++++++++++","test_removecontact")
        reqType = {'requestType': 'removecontact'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_dispcontact(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_dispcontact(self):

        print(5*"\n++++++++++++","test_dispcontact")
        reqType = {'requestType': 'dispcontact'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_telepathy(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_telepathy(self):

        print(5*"\n++++++++++++","test_telepathy")
        reqType = {'requestType': 'telepathy'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_getdb(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_getdb(self):

        print(5*"\n++++++++++++","test_getdb")
        reqType = {'requestType': 'getdb'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_sendmessage(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_sendmessage(self):

        print(5*"\n++++++++++++","test_sendmessage")
        reqType = {'requestType': 'sendmessage'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_sendbinary(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_sendbinary(self):

        print(5*"\n++++++++++++","test_sendbinary")
        reqType = {'requestType': 'sendbinary'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_checkmsg(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_checkmsg(self):

        print(5*"\n++++++++++++","test_checkmsg")
        reqType = {'requestType': 'checkmsg'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



    # // Teleport



class SNET_maketelepods(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_maketelepods(self):

        print(5*"\n++++++++++++","test_maketelepods")
        reqType = {'requestType': 'maketelepods'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_telepodacct(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_telepodacct(self):

        print(5*"\n++++++++++++","test_telepodacct")
        reqType = {'requestType': 'telepodacct'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_teleport(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_teleport(self):

        print(5*"\n++++++++++++","test_teleport")
        reqType = {'requestType': 'teleport'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)

        self.assertTrue(True)



    # // InstantDEX

class SNET_orderbook(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_orderbook(self):

        print(5*"\n++++++++++++","test_orderbook")
        reqType = {'requestType': 'orderbook'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_placebid(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_placebid(self):

        print(5*"\n++++++++++++","test_placebid")
        reqType = {'requestType': 'placebid'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)

        self.assertTrue(True)



class SNET_placeask(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_placeask(self):

        print(5*"\n++++++++++++","test_placeask")
        reqType = {'requestType': 'placeask'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)

        self.assertTrue(True)



class SNET_makeoffer(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_makeoffer(self):

        print(5*"\n++++++++++++","test_makeoffer")
        reqType = {'requestType': 'makeoffer'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_respondtx(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_respondtx(self):

        print(5*"\n++++++++++++","test_respondtx")
        reqType = {'requestType': 'respondtx'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_processutx(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_processutx(self):

        print(5*"\n++++++++++++","test_processutx")
        reqType = {'requestType': 'processutx'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)

        self.assertTrue(True)




    # // Tradebot


class SNET_pricedb(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_pricedb(self):

        print(5*"\n++++++++++++","test_pricedb")
        reqType = {'requestType': 'pricedb'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)


        self.assertTrue(True)



class SNET_getquotes(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_getquotes(self):

        print(5*"\n++++++++++++","test_getquotes")
        reqType = {'requestType': 'getquotes'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)

        self.assertTrue(True)



class SNET_tradebot(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_tradebot(self):

        print(5*"\n++++++++++++","test_tradebot")
        reqType = {'requestType': 'tradebot'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)

        self.assertTrue(True)




    # // # privatebet

class SNET_lotto(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_lotto(self):

        print(5*"\n++++++++++++","test_lotto")
        reqType = {'requestType': 'lotto'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)

        self.assertTrue(True)



    # // Embedded Langs


class SNET_python(SNET_BaseTest):


    def setUp(self):
        print(" test setUp func here")
        pass



    def test_python(self):

        print(5*"\n++++++++++++","test_python")
        reqType = {'requestType': 'python'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)

        self.assertTrue(True)



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
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)

        self.assertTrue(True)



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



def main():
    """

    can be invoked from cmd line with a specific test CLASS as agrument:

    python3 -m unittest -vvv uTest1.SNET_baseSetup


    OR

    by itself with a list of test suites and test classes and test lists to be run

    ./uTest1.py sg base settings testList1


    """#

    #argparse later

    testClasses = {}
    testClasses['settings'] = SNET_settings


    testSuites = {}
    testSuites['base'] = suite_baseSetup
    testSuites['base1'] = suite_baseSetup
    testSuites['base2'] = suite_baseSetup
    testSuites['base3'] = suite_baseSetup
    testSuites['base4'] = suite_baseSetup
    testSuites['base5'] = suite_baseSetup
    testSuites['base6'] = suite_baseSetup
    testSuites['sg'] = suite_SG

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
    self.assertTrue('peers' in rpl777.keys())

    """ #

# ALSO: failIf etc!

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

