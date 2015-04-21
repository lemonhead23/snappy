#!/usr/bin/env python3

import requests
import unittest
import json
import math


class SNET_BaseTest(unittest.TestCase):

    url = 'http://localhost:7777'
    
    numPongers = 1
    numHavenoders = 1
    # can count pongers and havenoders just as in snappey
    # and other basic state

    null = None

    def setUp(self):
        print("this test using generic setUp function")
        

    def test_base(self):
        query = {'requestType': 'settings'}
        headers = {'content-type': 'application/json'}
        
        testReq = requests.post(self.url, data=json.dumps(query), headers=headers)

        rpl777 = eval(testReq.text)
        for setting in rpl777:
            print(setting, " - ", rpl777[setting])


if __name__ == '__main__':
    unittest.main()
