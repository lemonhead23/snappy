#!/usr/bin/env python3

#import random
import unittest
import requests
import json

from snAppyModules.snQueryComposers import QueryComposer_777
from snAppyModules.snTestConfig import *

import time


class SNET_BaseTest(unittest.TestCase):

    """


    """#
    url = SNET_url # environ['SNET_url']
    qComp_777 = QueryComposer_777(environ)
    numPongers = 1
    numHavenoders = 1

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

        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)

        self.whitelist = rpl777['whitelist']
        self.settingsPassed=True


        req_getpeers = {'requestType': 'getpeers'}
        payload = self.qComp_777.make_777POST_Request(req_getpeers)

        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)

        self.localpeers=rpl777['peers']
        self.getpeersPassed=True


        establishNetwork = True
        while establishNetwork:

            for ip in self.whitelist:
                req_ping = {'requestType': 'ping'}
                payload= self.qComp_777.make_777POST_Request(req_ping)
                payload['destip'] = ip
                #print(payload)
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
                testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
                rpl777 = eval(testReq.text)
                print("req_findnode rpl777: ",rpl777)


            time.sleep(0.1)

            reqType = {'requestType': 'GUIpoll'}
            payload= self.qComp_777.make_777POST_Request(reqType)

            headers = {'content-type': 'application/json'}
            testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

            rpl777 = eval(testReq.text)
            #print(rpl777['result'])
            self.pollsDone+=1
            #
            # if 'nothing pending' in rpl777['result']:
            #     print(1*"GUIpoll : ",rpl777  )
            #
            if 'kademlia_pong' in rpl777['result']:
                print("kademlia_pong -------> ", rpl777)
                self.has_pong=True
            elif 'kademlia_havenode' in rpl777['result']:
                self.has_havenode=True
                print("kademlia_havenode------->", rpl777)
            else:
                #log.msg(1*"GUIpoll ---> misc.  ", rpl777, type(rpl777))
                print(1*"GUIpoll ---> misc.  ", rpl777)

            print("base setup- has ponger:", self.has_pong)
            print("base setup- has havenoder:",self.has_havenode,"\n")

            if self.has_pong and self.has_havenode:
                establishNetwork = False
                self.SNET_baseSetupOK = True

            if self.pollsDone > self.maxPolls:
                establishNetwork = False # give up
                self.SNET_baseSetupOK = False




    def test_SNET_baseSetup(self):

        self.assertTrue(self.SNET_baseSetupOK)

    #
    # def test_ping(self):
    #
    #     """ for each testXYZ method in a test class, the setUp is executed again!!!""" #
    #
    #     print(5*"\n++++++++++++","SNET_baseSetup test_ping" )
    #     req_ping = {'requestType': 'ping'}
    #     payload= self.qComp_777.make_777POST_Request(req_ping) # pull the whole dict for this req
    #     payload['destip'] = self.whitelist[0] # only one needed, did that before ip
    #     testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)
    #     rpl777 = eval(testReq.text)
    #     #print("ping rpl777: ",rpl777)
    #
    #     for setting in rpl777:
    #         print(setting, " - ",rpl777[setting])
    #     self.assertIn('kademlia_ping' , rpl777['result'])








class SNET_settings(SNET_BaseTest): #unittest.TestCase):


    def setUp(self):
        print("SNET_settings setUp here- NOP")
        pass

    def test_settings(self):
        print(5*"\n++++++++++++","test_settings")
        reqType = {'requestType': 'settings'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)

        # here we can add individual params to the request dict

        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        for setting in rpl777:
            print(setting, " - ",rpl777[setting])
        print("\n")

        self.assertGreater(3,2)

        settingsReply="""
        query json is:  {'value': '', 'requestType': 'settings', 'field': '', 'reinit': ''}
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



    def test_getpeers(self):

        print(5*"\n++++++++++++","test_getpeers")
        reqType = {'requestType': 'getpeers'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)

        print(rpl777['Numnxtaccts'])
        print(rpl777['Numpservers'])
        print(rpl777['num'])

        for peer in rpl777['peers']:#
            for dat in peer:
                print(dat, " - ", peer[dat])
            print("\n")

        self.assertGreater(rpl777['num'],1)

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



##############################################
##############################################
##############################################
##############################################
##############################################



# copy this over for every api call


class SNET_(SNET_BaseTest):


    def setUp(self):
        print("SNET_ t setUp here- NOP")
        pass



    def test_(self):

        print(5*"\n++++++++++++","test_x1")
        reqType = {'requestType': 'getpeers'}
        payload= self.qComp_777.make_777POST_Request(reqType)
        print("query json is: ", payload)
        headers = {'content-type': 'application/json'}
        testReq = requests.post(self.url, data=json.dumps(payload), headers=self.headers)

        rpl777 = eval(testReq.text)
        print(5*"\n~~~~~~~~~~~~","SuperNET rpl777y:") # rpl777)

        print(rpl777['Numnxtaccts'])
        print(rpl777['Numpservers'])
        print(rpl777['num'])

        for peer in rpl777['peers']:#
            for dat in peer:
                print(dat, " - ", peer[dat])
            print("\n")

        self.assertTrue(False)






##############################################
##############################################
##############################################
##############################################
##############################################



def suite_1():
    suite = unittest.TestSuite()
    suite.addTest(SNET_baseSetup('setUp'))

    return suite




if __name__ == '__main__':

    runSuite = False
    mainOnly = True

    if mainOnly:
        unittest.main()
    elif runSuite:
        suite1 = suite_1()
        runner = unittest.TextTestRunner()
        runner.run(suite1)




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

