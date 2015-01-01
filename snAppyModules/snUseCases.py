#!/usr/bin/python3
# -*- coding: utf-8 -*-


from twisted.internet import protocol #, # ClientFactory
from twisted.internet.protocol  import ClientFactory


import binascii

from twisted.python import threadpool as tp



from twisted.python import log
from twisted.web.client import getPage
from datetime import datetime
import json
import requests
from twisted.internet.threads import deferToThread
from random import randint
import time
from time import sleep

from snAppyModules.snAppyConfig import *
#from requests import Request, Session
#from twisted.internet.defer import Deferred
from twisted.internet.protocol import ClientFactory, ServerFactory




class Schedule(object):
    """ container class to contain schedule info for each cached data feed
        This gets the simpl dicts from the snApiConfig module"""#
    def __init__(self, schedule, ):

        print(schedule)
        self.schedule = schedule
        self.callFreq = schedule['callFreq']
        self.SNrequests = schedule['schedReqTypes']

        self.name = schedule['schedName']  # sched_GUIpoll['schedName']

        # these need to addressed explicitly by their names in the UC class,
        # and there the names must be known explicitly anyway
        self.target = schedule['target']
        self.lastCallTime = int(time.time() * 1000)



    def callMe(self):
        self.deltaT = int(time.time() * 1000 ) - self.lastCallTime
        #log.msg("callFreq schedule ", self.name," ???: ", self.deltaT ," > ", self.callFreq, self.deltaT > self.callFreq)
        if self.deltaT > self.callFreq:
            self.lastCallTime = int(time.time() * 1000 )
            return True
        else:
            return False





class Parser(object):


    ptt_PONGstringStage1 = {
                    'args': '[ {"requestType":"pong", "NXT":"","time":,"yourip":"","yourport":,"ipaddr":"","pubkey":"","ver":"0.199"} , {"token":"" }]' ,\
                    'result': '{"result":"kademlia_pong","NXT":"","ipaddr":"","port":0","lag":0,"numpings":0,"numpongs":0,"ave":0}',\
                    'port':0,\
                    'from' : ''
                    }

    ptt_PONG = {
                    'fullRequest': {"requestType":"pong", "NXT":"","time":"","yourip":"","yourport":"","ipaddr":"","pubkey":"","ver":"0.199"} , \
                    "token":""  ,\
                    'result': {"result":"kademlia_pong","NXT":"","ipaddr":"","port":0 ,"lag":0,"numpings":0,"numpongs":0,"ave":0},\
                    'fromPort':0,\
                    'from' : ''
                    }


#  {'from': '192.99.246.126', 'port': 0, 'args': '[{"requestType":"havenode","NXT":"6216883599460291148","time":1418307717,"key":"5624143003089008155","data":[["5624143003089008155", "192.99.212.250", "7777", "1418256837"], ["15178638394924629506", "167.114.2.206", "7777", "1418256815"], ["11910135804814382998", "167.114.2.94", "7777", "1418256815"], ["6216883599460291148", "192.99.246.126", "7777", "0"], ["7108754351996134253", "167.114.2.171", "7777", "1418256939"], ["16196432036059823401", "167.114.2.203", "7777", "1418256827"], ["7581814105672729429", "187.153.143.36", "27190", "1418266908"]]},{"token":"7meqnnpffqh9272utch79ra8rvlih9mevl901qhml0phabmmuuv4a7blsqnoqh01pc3d6rgrmrrul935mv5fhk877p6mu0h8cfplsqs8e2p0njtuhj5oct8js9qlob3q3c7vggui0rej3bdsprtrtuajhvt8pjhs"}]', 'result': '{"result":"kademlia_havenode from NXT.6216883599460291148 key.(5624143003089008155) value.([["5624143003089008155", "192.99.212.250", "7777", "1418256837"], ["15178638394924629506", "167.114.2.206", "7777", "1418256815"], ["11910135804814382998", "167.114.2.94", "7777", "1418256815"], ["6216883599460291148", "192.99.246.126", "7777", "0"], ["7108754351996134253", "167.114.2.171", "7777", "1418256939"], ["16196432036059823401", "167.114.2.203", "7777", "1418256827"], ["7581814105672729429", "187.153.143.36", "27190", "1418266908"]])"}'} <class 'dict'>


    def __init__(self):
        pass








class UC_TEMPLATE(object):


    def __init__(self, serverFactory , environ = {} ): # prepSchedules = {},

        self.environ = environ
        self.schedules = {}    # this contains the schedules

        # local state information UC dependent
        self.spec1 = {}
        self.spec2 = {} # etc..

        prepSchedules = environ['scheduleContainer'] # can use same as UC1 for now- extends it
        for sched in prepSchedules.keys():
            sched = prepSchedules[sched]
            self.schedules[ sched['schedName']] = Schedule( sched )
        self.lastCallTime = int(time.time() * 1000)



    def periodic(self, ):
        """ This is the method that is called periodically by the twisted loopingTask.
         It iterates over all schedules in the UseCase class, checks if they are due to be called,
         adds the ones due to a list and passes that list on to runSchedules(). """#

        schedulesDue =[]

        for schedule in self.schedules.keys():
            schedule = self.schedules[schedule]

            if schedule.callMe():
                schedulesDue.append(schedule)

        self.runSchedules(schedulesDue)


    def runSchedules(self,schedulesDue):
        """ here we get through all the due schedules and call them on SuperNET server
             Here we explicitly check the name and send them to the first callback of their callback sequence."""#

        for schedDue in schedulesDue:
            if 'sched_xy' in schedDue.SNrequests.keys():
                reqData1 = schedDue.SNrequests['sched_xy']
                for key in self.storedVals.keys():
                    reqData1['key'] = self.storedVals[key]
                    self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqData1), headers=POSTHEADERS)
                    self.deferred.addCallback(self.rpl777_findvalue)
                    self.deferred.addErrback(self.rpl777ERR)
            elif 'sched_yz' in schedDue.SNrequests.keys():
                reqData = schedDue.SNrequests['sched_store'] # this has 0.9 sec
                reqData['name'] = 'myStoreName' + str(int(time.time())) #n1
                reqData['data'] = "x"
                self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqData), headers=POSTHEADERS)
                self.deferred.addCallback(self.rpl777_store)
                self.deferred.addErrback(self.rpl777ERR)


    def rpl777_GUIpoll(self, dataFrom777):
        """



         """#
        rpl777=dataFrom777.json()
        if 'nothing pending' in str(rpl777):
            pass#
        elif 'kademlia_xy' in str(rpl777):
            self.rpl777_GUIpoll_kademlia_store(rpl777)
        else:
            log.msg(1*"GUIpoll ---> CALL not caught yet: ",rpl777, type(rpl777),"\n")
        return 0


    def rpl777_df2_ping(self, dataFrom777):
        """


        """#
        repl=dataFrom777.json()
        repl=dataFrom777.content.decode("utf-8")
        repl=eval(repl)







class UC1_pingPong(object):


    def __init__(self, serverFactory , superNET_daemon , environ = {}, ): # prepSchedules = {},
        # uc1_pingPong = UC1_pingPong(serverFactory,  self.environ ,  self )
        #  also hand in 'self' here as a means to stop self
        # log.msg(superNET_daemon)

        self.environ = environ
        self.schedules = {}    # this contains the schedules

        self.superNET_daemon = superNET_daemon

        # local state information UC dependent
        self.pongers =  {} # etc..

        prepSchedules = environ['UCsched_1'] # can use same as UC1 for now- extends it
        for sched in prepSchedules.keys():
            sched = prepSchedules[sched]
            self.schedules[ sched['schedName']] = Schedule( sched )
        self.lastCallTime = int(time.time() * 1000)


    def periodic(self, ):
        """ This is the method that is called periodically by the twisted loopingTask.
         It iterates over all schedules in the UseCase class, checks if they are due to be called,
         adds the ones due to a list and passes that list on to runSchedules(). """#

        schedulesDue =[]

        for schedule in self.schedules.keys():
            schedule = self.schedules[schedule]

            if schedule.callMe():
                schedulesDue.append(schedule)

        self.runSchedules(schedulesDue)


    def runSchedules(self,schedulesDue):
        """ here we get through all the due schedules and call them on SuperNET server
             Here we explicitly check the name and send them to the first callback of their callback sequence."""#

        for schedDue in schedulesDue:
            if 'uc_settings' in schedDue.SNrequests.keys():
                reqData1 = schedDue.SNrequests['uc_settings']
                self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqData1), headers=POSTHEADERS)
                self.deferred.addCallback(self.rpl777_df1_settings)
                self.deferred.addErrback(self.rpl777ERR)

            elif 'uc_getpeers' in schedDue.SNrequests.keys():
                reqData1 = schedDue.SNrequests['uc_getpeers']
                self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqData1), headers=POSTHEADERS)
                self.deferred.addCallback(self.rpl777_df1_getpeers)
                self.deferred.addErrback(self.rpl777ERR)

            elif 'GUIpoll' in schedDue.SNrequests.keys():
                reqData = schedDue.SNrequests['GUIpoll']
                self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqData), headers=POSTHEADERS)
                self.deferred.addCallback(self.rpl777_GUIpoll)
                self.deferred.addErrback(self.rpl777ERR)


    def rpl777_GUIpoll(self, dataFrom777):
        """

         """#
        rpl777=dataFrom777.json()
        log.msg("UC1 tests for pongers: ", len(self.pongers))
        if 'nothing pending' in str(rpl777):
            log.msg(1*"GUIpoll : ",rpl777  ) #pass#
        elif 'kademlia_pong' in str(rpl777):
            self.rpl777_GUIpoll_kademlia_pong(rpl777)
        else:
            #log.msg(1*"GUIpoll ---> misc.  ", rpl777, type(rpl777))
            log.msg(1*"GUIpoll ---> misc.  ",)

        return 0


    def rpl777_GUIpoll_kademlia_pong(self, rpl777): #dataFrom777):
        """

        see PONG details in snAppy_doku

        """#

        #log.msg(1*"GUIpoll -----> kademlia_pong",rpl777, type(rpl777))

        try:
            fromIp = rpl777['from']
            port = rpl777['port']
            args = rpl777['args']
            rpl777 = rpl777['result']
            rpl777 = json.loads(rpl777)

        except Exception as e:
            #log.msg("GUIpoll ---> kademlia_pong",rpl777, type(rpl777),"\n")
            log.msg("Error rpl777_GUIpoll_kademlia_pong {0}".format(str(e)))

        try:
            rplArgs = json.loads(args) # <class 'list'> !!
            rplArgsRQ = rplArgs[0] # <class 'dict'>
            rplArgsTK = rplArgs[1]   #<class 'dict'>
        except Exception as e:
            log.msg("Error rpl777_GUIpoll_kademlia_pong {0}".format(str(e)))

        try:
            #log.msg(1*"\n~~~~ rplArgsRQ", rplArgsRQ)
            pubkey= rplArgsRQ['pubkey'] # check that this is really pubkey and not DHT key
            requestType= rplArgsRQ['requestType']
            ver =rplArgsRQ['ver']
            yourip =rplArgsRQ['yourip']
            yourport =rplArgsRQ['yourport']

            NXT =rplArgsRQ['NXT']
            time =rplArgsRQ['time']
            ipaddr =rplArgsRQ['ipaddr']

        except Exception as e:
            log.msg("GUIpoll ---> kademlia_pong",rpl777, type(rpl777),"\n")
            log.msg("Error rplArgsRQ {0}".format(str(e)))

        try:
            port =  rpl777['port']
            numpings =  rpl777['numpings']
            lag  =  rpl777['lag']
            ipaddr  = rpl777['ipaddr']
            numpongs =  rpl777['numpongs']
            result =   rpl777['result']
            ave  =  rpl777['ave']
            NXT  = rpl777['NXT']
            log.msg("GUIpoll ---> rpl777", rpl777,type(rpl777))

        except Exception as e:
            #log.msg("GUIpoll ---> kademlia_pong",rpl777, type(rpl777),"\n")
            log.msg("Error rpl777 {0}".format(str(e)))

        ponger = rpl777['ipaddr']

        #log.msg("pongers: ", (self.pongers),"\n")

        if not ponger  in self.pongers.keys():
            log.msg(ponger)

            self.pongers[ponger] =  rpl777

        log.msg("pongers: ", len(self.pongers))

        numPongers =  len(self.pongers)

        for pongerr in self.pongers:
            log.msg(self.pongers[pongerr]['ipaddr'])

        if numPongers >3:
            self.superNET_daemon.stopUC1(True)

        # 2014-12-29 12:10:41+0100 [-] GUIpoll ---> rpl777 {'tag': '', 'numpongs': 144, 'lag': '344.375', 'ave': '1259.662', 'numpings': 143, 'result': 'kademlia_pong', 'isMM': '0', 'ipaddr': '<nullstr>', 'NXT': '15178638394924629506', 'port': 0} <class 'dict'>

            # ToDo : check for how often nullst is ipaddr!!

        # kademlia_pong {'args': '[{"requestType":"pong","NXT":"1978065578067355462","time":1419845114,"MMatrix":0,"yourip":"79.245.5.160","yourport":34365,"ipaddr":"89.212.19.49","pubkey":"c269a8b4567c0b3062e6c4be859d845c4b808a405dd03d0d1ac7b4d9cb725b40","ver":"0.399"},{"token":"aqqagqe2sph302rsgieobfm482580iqs386jrk2teb5tjd671sprkg2r7qe3r1821bfds7marsagn15srbn8p447s8oqon5r6a38r21j9q205fiai54r7dtjdfjongdrpp2gsgopa8f7cum3999h5q1t0jl6fjhb"}]', 'from': '89.212.19.49', 'port': 0, 'result': '{"result":"kademlia_pong","tag":"","isMM":"0","NXT":"1978065578067355462","ipaddr":"89.212.19.49","port":0,"lag":"630.578","numpings":63,"numpongs":65,"ave":"1026.539"}'} <class 'dict'>
        # GUIpoll ---> rpl777 {'ave': '1026.539', 'lag': '630.578', 'NXT': '1978065578067355462', 'port': 0, 'result': 'kademlia_pong', 'ipaddr': '89.212.19.49', 'numpings': 63, 'numpongs': 65, 'tag': '', 'isMM': '0'} <class 'dict'>



    def rpl777_df1_settings(self, dataFrom777): #these are the basic pings from the whitlist
        """
         this sends pings

          """#
        repl=dataFrom777.json()
        reqPing = {'requestType':'ping'}

        # self.peersDiLoc[node[1]] = node[0]

        ipsToPing=repl['whitelist'] #[0] # singlecheck
        # manual tests:
        #ipsToPing = 20* ['88.179.105.82'] # ['178.62.185.131'] # stonefish['80.41.56.181'] # ['85.178.202.108']   #

        log.msg(1*"ping to whitelist:")#, reqPing['destip'])
        for node in ipsToPing:
            reqPing['destip']=node
            sleep(0.25)
            #log.msg("ping to whitelist:", reqPing['destip'])
            self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqPing), headers=POSTHEADERS)
            self.deferred.addCallback(self.rpl777_df2_ping)
            self.deferred.addErrback(self.rpl777ERR)



    def rpl777_df1_getpeers(self, dataFrom777):
        """

         peers [{'pubkey': '05a7612d54d14c21be9baa654ad50b4ba423eea0735185ac732ada2332315c3f', 'RS': 'NXT-8AF7-ESB7-GHFM-896JY', 'privateNXT': '8016556209183334821'}, {'RS': 'NXT-7PPP-R6AJ-VSJ7-37C7V', 'pserver': {'recv': 8, 'lastrecv': 14.0111578, 'lastsent': 14.01127447, 'pings': 1, 'sent': 8}, 'srvipaddr': '178.62.185.131', 'recv': 8, 'srvNXT': '2131686659786462901', 'pubkey': '849c97e5b1e8c50429249eff867de5e6ded39d34a6ccc9c42ea720d927a12d18', 'sent': 8}, {'RS': 'NXT-EZJ4-8F5T-8VX4-FVCB7', 'pserver': {'lastrecv': 0.6551996, 'lastsent': 0.06295793, 'pingtime': 231, 'avetime': 3893.46431672, 'recv': 155, 'pings': 63, 'pongs': 63, 'sent': 178}, 'srvipaddr': '167.114.2.206', 'recv': 155, 'srvNXT': '15178638394924629506', 'pubkey': '52e3524b5392a2ecba9e702a0c9c04d3d73dc4f93008977e1bcd15ea5bd5b376', 'sent': 178}, {'RS': 'NXT-5TU8-78XL-W2CW-32WWQ', 'pserver': {'lastrecv': 0.07671293, 'lastsent': 0.00977127, 'pingtime': 176.5, 'avetime': 18793.97457429, 'recv': 188, 'pings': 83, 'pongs': 84, 'sent': 205}, 'srvipaddr': '89.212.19.49', 'recv': 188, 'srvNXT': '1978065578067355462', 'pubkey': 'c269a8b4567c0b3062e6c4be859d845c4b808a405dd03d0d1ac7b4d9cb725b40', 'sent': 205}, {'RS': 'NXT-A4NA-7P8Y-MDMZ-3K4AZ', 'pserver': {'lastrecv': 0.07303403, 'lastsent': 0.07965903, 'pingtime': 327.75, 'avetime': 33324.18828125, 'recv': 35, 'pings': 9, 'pongs': 11, 'sent': 81}, 'srvipaddr': '167.114.2.204', 'recv': 35, 'srvNXT': '2278910666471639688', 'pubkey': '47faa8a876ae56be36a1d214515d0ef3f9ff99b06f4d2702acf0380cab7ccc5e', 'sent': 81}, {'RS': 'NXT-JNLE-Q9XW-MG8P-7GQKE', 'pserver': {'lastrecv': 0.05130237, 'lastsent': 0.0543357, 'pingtime': 36882.25, 'avetime': 13861.70690789, 'recv': 127, 'pings': 47, 'pongs': 48, 'sent': 174}, 'srvipaddr': '192.99.246.126', 'recv': 127, 'srvNXT': '6216883599460291148', 'pubkey': '2fdfab9d3d5e1c91a27e48ed7422ebcea628ebdf36ea0052fdd62e1533a8751d', 'sent': 174}, {'RS': 'NXT-YPWQ-F7SB-WCD7-CFCLC', 'pserver': {'lastrecv': 0.01943838, 'lastsent': 0.02329255, 'pingtime': 295, 'avetime': 7594.5688101, 'recv': 104, 'pings': 38, 'pongs': 40, 'sent': 131}, 'srvipaddr': '167.114.2.94', 'recv': 104, 'srvNXT': '11910135804814382998', 'pubkey': '34e55ae366e8b11e5dc195f29a0d9999567123b9c02e4a621600e4de5c72bb77', 'sent': 131}, {'RS': 'NXT-NHBB-5ZF3-4WTB-GBCK3', 'pserver': {'lastrecv': 2.37580073, 'lastsent': 0.0236049, 'pingtime': 52420.75, 'avetime': 7924.83104292, 'recv': 193, 'pings': 84, 'pongs': 82, 'sent': 181}, 'srvipaddr': '167.114.2.203', 'recv': 193, 'srvNXT': '16196432036059823401', 'pubkey': 'be3db1badadb0e95b8afd2f1f5f53df7837de15c14f09f7a531c489a3f470543', 'sent': 181}, {'RS': 'NXT-Y5FR-ZSRB-BQWC-9W9PR', 'pserver': {'lastrecv': 1.36517293, 'lastsent': 0.03602293, 'pingtime': 93572, 'avetime': 20840.15337171, 'recv': 96, 'pings': 37, 'pongs': 39, 'sent': 104}, 'srvipaddr': '192.99.246.33', 'recv': 96, 'srvNXT': '8923034930361863607', 'pubkey': 'ea83e39d553470725960180afb25afffe3de1fe0019979236b96536e22e1ed29', 'sent': 104}, {'RS': 'NXT-VSVF-FFF5-M4EX-8YUB7', 'pserver': {'lastrecv': 0.04354165, 'lastsent': 0.00936665, 'pingtime': 36595.5, 'avetime': 9679.23729884, 'recv': 188, 'pings': 90, 'pongs': 77, 'sent': 224}, 'srvipaddr': '167.114.2.171', 'recv': 188, 'srvNXT': '7108754351996134253', 'pubkey': '9e33da1c9ac00d376832cf3c9293dfb21d055d76e1c446449f0672fd688a237f', 'sent': 224}, {'RS': 'NXT-DGHK-DUWA-2MRL-C44UP', 'pserver': {'lastrecv': 1.73030202, 'lastsent': 0.00871452, 'pingtime': 45173.25, 'avetime': 9300.74114583, 'recv': 134, 'pings': 62, 'pongs': 58, 'sent': 130}, 'srvipaddr': '167.114.2.205', 'recv': 134, 'srvNXT': '12315166155634751985', 'pubkey': 'eef155b7c8c50dc62ae45f40c30d2b1a0874ca5f5f11adeef7637933d863583b', 'sent': 130}, {'RS': 'NXT-WXJV-AFNK-YW5D-6S95W', 'pserver': {'lastrecv': 1.77902338, 'lastsent': 0.02744422, 'pingtime': -156179, 'avetime': 10604.32024083, 'recv': 114, 'pings': 63, 'pongs': 46, 'sent': 157}, 'srvipaddr': '192.99.212.250', 'recv': 114, 'srvNXT': '5624143003089008155', 'pubkey': 'ecea0d22fca77e28210c0b4c05b8bd16ff8003e5065c09f4e73105398e31840f', 'sent': 157}, {'RS': 'NXT-VT9R-9GYM-YLJF-D8QCT', 'pserver': {'lastrecv': 1.15555233, 'lastsent': 0.01185233, 'pingtime': 223334, 'avetime': 39925.74770221, 'recv': 123, 'pings': 50, 'pongs': 52, 'sent': 134}, 'srvipaddr': '192.99.246.20', 'recv': 123, 'srvNXT': '13594896385051583735', 'pubkey': '430695694b02bb71e8222e1e5d20b1c985afd9ba899e25fe2d52ee1be92f532c', 'sent': 134}, {'RS': 'NXT-UE4H-CXMN-HR75-8W376', 'pserver': {'lastrecv': 4.86252565, 'lastsent': 0.02568398, 'pingtime': -3670675.75, 'avetime': 12546.13709677, 'recv': 14, 'pings': 30, 'pongs': 1, 'sent': 158}, 'srvipaddr': '94.102.50.70', 'recv': 14, 'srvNXT': '7067340061344084047', 'pubkey': '4bd4794f0a77d22949c944f96f9b7a429021e59644a98eea310546fd47b96440', 'sent': 158}, {'RS': 'NXT-XSQA-YBXH-CW2M-93QSF', 'pserver': {'lastrecv': 1.1530546, 'lastsent': 0.05522543, 'pingtime': 371363.25, 'avetime': 83528.03227459, 'recv': 54, 'pings': 41, 'pongs': 20, 'sent': 143}, 'srvipaddr': '37.59.108.92', 'recv': 54, 'srvNXT': '8566622688401875656', 'pubkey': '5a1c33c1e00cec3beecb9a9fcd8379fe61d6a661566875cf0cff89726b27b76f', 'sent': 143}]
         peers is a LIST!

         [

         {'pubkey': '05a7612d54d14c21be9baa654ad50b4ba423eea0735185ac732ada2332315c3f', 'RS': 'NXT-8AF7-ESB7-GHFM-896JY', 'privateNXT': '8016556209183334821'},

         {'RS': 'NXT-7PPP-R6AJ-VSJ7-37C7V', 'pserver': {'recv': 8, 'lastrecv': 14.0111578, 'lastsent': 14.01127447, 'pings': 1, 'sent': 8},
         'srvipaddr': '178.62.185.131', 'recv': 8, 'srvNXT': '2131686659786462901', 'pubkey': '849c97e5b1e8c50429249eff867de5e6ded39d34a6ccc9c42ea720d927a12d18', 'sent': 8},

         {'RS': 'NXT-EZJ4-8F5T-8VX4-FVCB7', 'pserver': {'lastrecv': 0.6551996, 'lastsent': 0.06295793, 'pingtime': 231, 'avetime': 3893.46431672, 'recv': 155, 'pings': 63, 'pongs': 63, 'sent': 178},
          'srvipaddr': '167.114.2.206', 'recv': 155, 'srvNXT': '15178638394924629506', 'pubkey': '52e3524b5392a2ecba9e702a0c9c04d3d73dc4f93008977e1bcd15ea5bd5b376', 'sent': 178},

          {'RS': 'NXT-5TU8-78XL-W2CW-32WWQ', 'pserver': {'lastrecv': 0.07671293, 'lastsent': 0.00977127, 'pingtime': 176.5, 'avetime': 18793.97457429, 'recv': 188, 'pings': 83, 'pongs': 84, 'sent': 205}, 'srvipaddr': '89.212.19.49', 'recv': 188, 'srvNXT': '1978065578067355462', 'pubkey': 'c269a8b4567c0b3062e6c4be859d845c4b808a405dd03d0d1ac7b4d9cb725b40', 'sent': 205},
          {'RS': 'NXT-A4NA-7P8Y-MDMZ-3K4AZ', 'pserver': {'lastrecv': 0.07303403, 'lastsent': 0.07965903, 'pingtime': 327.75, 'avetime': 33324.18828125, 'recv': 35, 'pings': 9, 'pongs': 11, 'sent': 81}, 'srvipaddr': '167.114.2.204', 'recv': 35, 'srvNXT': '2278910666471639688', 'pubkey': '47faa8a876ae56be36a1d214515d0ef3f9ff99b06f4d2702acf0380cab7ccc5e', 'sent': 81},

          ]


        """#

        repl=dataFrom777.json()

        Numnxtaccts = repl['Numnxtaccts']
        peers = repl['peers']
        Numpservers = repl['Numpservers']
        num = repl['num']
        log.msg("Numnxtaccts", Numnxtaccts)
        #log.msg("peers", peers)
        log.msg("Numpservers", Numpservers)
        log.msg("num", num)

        reqFindnode = {'requestType':'findnode'}


        #log.msg(1*" rpl777_df1_getpeers  :",repl)

        reqPing = {'requestType':'ping'}

        for peer in peers[2:]:
            #log.msg(1*"\n\npeer:", peer, type(peer))
            ipaddr = peer['srvipaddr']
            reqPing['destip'] = ipaddr
            #log.msg(1*"peer:", ipaddr)

            sleep(0.25)

            #log.msg("ping to peer:", reqPing['destip'])
            self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqPing), headers=POSTHEADERS)
            self.deferred.addCallback(self.rpl777_df2_ping)
            self.deferred.addErrback(self.rpl777ERR)

            # reqFindnode['key']=srvNXT
            # self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqFindnode), headers=POSTHEADERS)
            # self.deferred.addCallback(self.rpl777_df3_findnode )
            # self.deferred.addErrback(self.rpl777ERR)



    def rpl777_df2_ping(self, dataFrom777):
        """


        """#
        repl=dataFrom777.json()
        repl=dataFrom777.content.decode("utf-8")
        repl=eval(repl)
        #log.msg( 1 * "ping sent", repl)




    def rpl777ERR(self, ERR777):

        log.msg("ERR777 1", ERR777, type(ERR777)) #.printDetailedTraceback())
        log.msg("ERR777 2", ERR777.value, type(ERR777.value)) #.printDetailedTraceback())
        raise RuntimeError(ERR777.printDetailedTraceback())



######################################
######################################
######################################
######################################
######################################
######################################
######################################
######################################




class UC2_havenode(object):


    def __init__(self, serverFactory , superNET_daemon , environ = {}, ): # prepSchedules = {},
        # uc1_pingPong = UC1_pingPong(serverFactory,  self.environ ,  self )
        #  also hand in 'self' here as a means to stop self
        # log.msg(superNET_daemon)

        self.environ = environ
        self.schedules = {}    # this contains the schedules

        self.superNET_daemon = superNET_daemon

        # local state information UC dependent
        self.pongers =  {} # etc..
        self.havenoders =  {} # etc..
        self.peersDiLoc = {}


        prepSchedules = environ['UCsched_1'] # can use same as UC1 for now- extends it
        for sched in prepSchedules.keys():
            sched = prepSchedules[sched]
            self.schedules[ sched['schedName']] = Schedule( sched )
        self.lastCallTime = int(time.time() * 1000)



    def periodic(self, ):
        """ This is the method that is called periodically by the twisted loopingTask.
         It iterates over all schedules in the UseCase class, checks if they are due to be called,
         adds the ones due to a list and passes that list on to runSchedules(). """#

        schedulesDue =[]

        for schedule in self.schedules.keys():
            schedule = self.schedules[schedule]

            if schedule.callMe():
                schedulesDue.append(schedule)

        self.runSchedules(schedulesDue)



    def runSchedules(self,schedulesDue):
        """ here we get through all the due schedules and call them on SuperNET server
             Here we explicitly check the name and send them to the first callback of their callback sequence."""#

        for schedDue in schedulesDue:
            if 'uc_settings' in schedDue.SNrequests.keys():
                reqData1 = schedDue.SNrequests['uc_settings']
                self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqData1), headers=POSTHEADERS)
                self.deferred.addCallback(self.rpl777_df1_settings)
                self.deferred.addErrback(self.rpl777ERR)

            elif 'uc_getpeers' in schedDue.SNrequests.keys():
                reqData1 = schedDue.SNrequests['uc_getpeers']
                self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqData1), headers=POSTHEADERS)
                self.deferred.addCallback(self.rpl777_df1_getpeers)
                self.deferred.addErrback(self.rpl777ERR)
            #
            #
            # elif 'uc_findnode' in schedDue.SNrequests.keys():
            #     reqFindnode = {'requestType':'findnode'}
            #     #log.msg(11*"\n rpl777_df1_getpeers & reqFindnode all:", self.peersDiLoc, type(self.peersDiLoc))
            #     for peer in self.peersDiLoc.keys():
            #         reqFindnode['key']=self.peersDiLoc[peer]
            #         sleep(0.1)
            #         self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqFindnode), headers=POSTHEADERS)
            #         self.deferred.addCallback(self.rpl777_df1_findnode )
            #         self.deferred.addErrback(self.rpl777ERR)



            elif 'GUIpoll' in schedDue.SNrequests.keys():
                reqData = schedDue.SNrequests['GUIpoll']
                self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqData), headers=POSTHEADERS)
                self.deferred.addCallback(self.rpl777_GUIpoll)
                self.deferred.addErrback(self.rpl777ERR)


    def rpl777_GUIpoll(self, dataFrom777):
        """

         """#
        rpl777=dataFrom777.json()
        if 'nothing pending' in str(rpl777):
            log.msg(1*"GUIpoll : ",rpl777  ) #pass#
        elif 'kademlia_pong' in str(rpl777):
            self.rpl777_GUIpoll_kademlia_pong(rpl777)
        elif 'kademlia_havenode' in str(rpl777):
            self.rpl777_GUIpoll_kademlia_havenode(rpl777)
        else:
            #log.msg(1*"GUIpoll ---> misc.  ", rpl777, type(rpl777))
            log.msg(1*"GUIpoll ---> misc.  ", )

        return 0





    def rpl777_GUIpoll_kademlia_havenode(self, rpl777): #parse777_step1
        """


FULL load 1st stage
  GUIpoll ---> kademlia_havenode {'result': '{"result":"kademlia_havenode from NXT.7108754351996134253 key.(11634703838614499263) value.([["11634703838614499263", "69.90.132.106", "7777", "1418404283"], ["13594896385051583735", "192.99.246.20", "7777", "1418404029"], ["11765334723692129557", "176.181.162.180", "7777", "1418443218"], ["8923034930361863607", "192.99.246.33", "7777", "1418404029"], ["7108754351996134253", "167.114.2.171", "7777", "0"], ["4424090804522645439", "54.76.226.59", "7777", "1418429678"], ["11910135804814382998", "167.114.2.94", "7777", "1418404026"]])"}', 'from': '167.114.2.171', 'port': 0, 'args': '[{"requestType":"havenode","NXT":"7108754351996134253","time":1418552795,"key":"11634703838614499263","data":[["11634703838614499263", "69.90.132.106", "7777", "1418404283"], ["13594896385051583735", "192.99.246.20", "7777", "1418404029"], ["11765334723692129557", "176.181.162.180", "7777", "1418443218"], ["8923034930361863607", "192.99.246.33", "7777", "1418404029"], ["7108754351996134253", "167.114.2.171", "7777", "0"], ["4424090804522645439", "54.76.226.59", "7777", "1418429678"], ["11910135804814382998", "167.114.2.94", "7777", "1418404026"]]},{"token":"j8edkcsu69k3e3e0ru9p4f6fepega7dijt24dh71h9kfqsg6vdtpmvp3ve3f6s019fc6pfhll1v0tu0sr4gpbahd3s9pejhg8383rbdmqfc0ironorsv379da2jpe10p5an8cq9ji51mg0vq8sb59sq0fqnugo6m"}]'} <class 'dict'>

args
port
from
result


GUIpoll --->

NOTE: the havenode return is wrapped extremely tight.

It contains the results twice, once as DATA: and once as value([

the result is contained double in here, as orig RQ and as value

kademlia_havenode {'args': '[{"requestType":"havenode","NXT":"11910135804814382998","time":1418378252,"key":"11910135804814382998","data":[["11910135804814382998", "167.114.2.94", "7777", "0"], ["2131686659786462901", "85.178.204.233", "61312", "1418374115"], ["11634703838614499263", "69.90.132.106", "7777", "1418355887"], ["10694781281555936856", "209.126.70.170", "7777", "1418355569"], ["17265504311777286118", "184.175.25.117", "7777", "1418355277"], ["5624143003089008155", "192.99.212.250", "7777", "1418355253"], ["8894667849638377372", "209.126.70.156", "7777", "1418355643"]]},{"token":"crhllp9ko5ehtcf8j46plskln4hn2lkp2ph4kbm0e9edtp00v38sqttrls1eh801smc20bj8ebllvob2qn9vnotj5i4952fl450o08pmsbr03liiaftu4ljmbh7ofajod0tvl87edal1k5drbeemj4ul4b42j99c"}]', 'result': '{"result":"kademlia_havenode from NXT.11910135804814382998 key.(11910135804814382998) value.([["11910135804814382998", "167.114.2.94", "7777", "0"], ["2131686659786462901", "85.178.204.233", "61312", "1418374115"], ["11634703838614499263", "69.90.132.106", "7777", "1418355887"], ["10694781281555936856", "209.126.70.170", "7777", "1418355569"], ["17265504311777286118", "184.175.25.117", "7777", "1418355277"], ["5624143003089008155", "192.99.212.250", "7777", "1418355253"], ["8894667849638377372", "209.126.70.156", "7777", "1418355643"]])"}', 'port': 0, 'from': '167.114.2.94'} <class 'dict'>

  {"result":"kademlia_havenode from NXT.12315166155634751985 key.(12315166155634751985) value.([["12315166155634751985", "167.114.2.205", "7777", "0"], ["13594896385051583735", "192.99.246.20", "7777", "1418309439"], ["16196432036059823401", "167.114.2.203", "7777", "1418308928"], ["8923034930361863607", "192.99.246.33", "7777", "1418308929"], ["7581814105672729429", "187.153.143.36", "27190", "1418308969"], ["7108754351996134253", "167.114.2.171", "7777", "1418308950"], ["11634703838614499263", "69.90.132.106", "7777", "1418308973"]])"} <class 'str'>



kademlia_havenode

{'args':

     '['
     '{'
     '"requestType":"havenode",'
     '"NXT":"1978065578067355462",'
     '"time":1418551919,'
     '"key":"1978065578067355462",'
     '"data":'
     '[["1978065578067355462", "89.212.19.49", "7777", "0"], '
     '["4424090804522645439", "54.76.226.59", "7777", "1418477776"],'
     ' ["13594896385051583735", "192.99.246.20", "7777", "1418477795"], '
     '["13434315136155299987", "209.126.70.159", "7777", "1418492016"], '
     '["104575166425568823", "184.175.25.117", "7777", "1418514417"],'
     ' ["6216883599460291148", "192.99.246.126", "7777", "1418477796"], '
     '["7108754351996134253", "167.114.2.171", "7777", "1418477947"]]},'
     '{"token":"aqqagqe2sph302rsgieobfm482580iqs386jrk2teb5tjd67vds30g2rne1uhug16psce0ts5bmvhjfss9269o6c12g0asq0d373rjg0vrqgqosvi095pod746o2npc29gpabm72ufi1gpk1j8vlm7elu7agv13d"}]',

'port': 0,
'result':

     '{"result":"kademlia_havenode from NXT.1978065578067355462 key.(1978065578067355462)'
     ' value.([["1978065578067355462", "89.212.19.49", "7777", "0"], '
     '["4424090804522645439", "54.76.226.59", "7777", "1418477776"], ["13594896385051583735", "192.99.246.20", "7777", "1418477795"], ["13434315136155299987", "209.126.70.159", "7777", "1418492016"], ["104575166425568823", "184.175.25.117", "7777", "1418514417"], ["6216883599460291148", "192.99.246.126", "7777", "1418477796"], ["7108754351996134253", "167.114.2.171", "7777", "1418477947"]])"}'

    , 'from': '89.212.19.49'}





    """#

        #log.msg("GUIpoll ---> kademlia_havenode",rpl777, type(rpl777),"\n")


        try:
            fromIp = rpl777['from']
            port = rpl777['port']
            rplArgs = rpl777['args']
            result = rpl777['result'] #'result': '{"result":"kademlia_havenode from NXT.13594896385051583735 key.(1978065578067355462) value.([["1978065578067355462", "89.212.19.49", "7777", "1418404057"], ["4
            # result is the internal raw string part
            try:
                rplArgsLi=json.loads(rplArgs)

                token = rplArgsLi[1]
                rplArgs = rplArgsLi[0]
                #
                fromNXT = rplArgs['NXT']
                requestType = rplArgs['requestType']
                data = rplArgs['data']
                key = rplArgs['key']
                time = rplArgs['time']
                peersList = rplArgs['data']
                #log.msg("\nGUIpoll -+--> kademlia_havenode peersList",peersList, type(peersList),"\n")


            except Exception as e:
                log.msg("Error args {0}".format(str(e)))
                log.msg("args NOT ok",rplArgs, type(rplArgs))

            try:
                rpl777 = rpl777['result'] # this is a string!
            except Exception as e:
                log.msg("Error args {0}".format(str(e)))
                log.msg("rpl777 NOT ok",rpl777, type(rpl777))

            #log.msg("\nGUIpoll -+--> kademlia_havenode rpl777",rpl777, type(rpl777),"\n")

        except Exception as e:
            #log.msg("GUIpoll ---> kademlia_pong",rpl777, type(rpl777),"\n")
            log.msg("Error rpl777_GUIpoll_kademlia_havenode >>> {0}".format(str(e)))



        for peer in peersList:
        #            ping and findnode!

            if peer[1] not in self.peersDiLoc.keys():
                self.peersDiLoc[peer[1]] = peer[0] # add this to the internal list of known nodes
                log.msg(1*" NEW PEER FOR LOCAL LIST:", peer)


        log.msg("GUIpoll ---> kademlia_havenode from ", fromNXT, " -- " , fromIp)


        log.msg(1*"              local peers :", len(self.peersDiLoc))
        log.msg(1*"              local havenoders :", len(self.havenoders))

        num_havenoders =  len(self.havenoders)
        for peer in self.peersDiLoc.keys():
            log.msg(peer, " - ", self.peersDiLoc[peer] )


        if not fromNXT  in self.havenoders.keys():
            log.msg(fromNXT)

            self.havenoders[fromNXT] =  rpl777

        if  num_havenoders > 4:
            log.msg(1*"\nhavenode finsish OK")
            self.superNET_daemon.stopUC2(True)





    def rpl777_GUIpoll_kademlia_pong(self, rpl777): #dataFrom777):
        """

        see PONG details in snAppy_doku

        """#

        #log.msg(1*"GUIpoll -----> kademlia_pong",rpl777, type(rpl777))

        try:
            fromIp = rpl777['from']
            port = rpl777['port']
            args = rpl777['args']
            rpl777 = rpl777['result']
            rpl777 = json.loads(rpl777)

        except Exception as e:
            #log.msg("GUIpoll ---> kademlia_pong",rpl777, type(rpl777),"\n")
            log.msg("Error rpl777_GUIpoll_kademlia_pong {0}".format(str(e)))

        try:
            rplArgs = json.loads(args) # <class 'list'> !!
            rplArgsRQ = rplArgs[0] # <class 'dict'>
            rplArgsTK = rplArgs[1]   #<class 'dict'>
        except Exception as e:
            log.msg("Error rpl777_GUIpoll_kademlia_pong {0}".format(str(e)))

        try:
            #log.msg(1*"\n~~~~ rplArgsRQ", rplArgsRQ)
            pubkey= rplArgsRQ['pubkey'] # check that this is really pubkey and not DHT key
            requestType= rplArgsRQ['requestType']
            ver =rplArgsRQ['ver']
            yourip =rplArgsRQ['yourip']
            yourport =rplArgsRQ['yourport']

            NXT =rplArgsRQ['NXT']
            time =rplArgsRQ['time']
            ipaddr =rplArgsRQ['ipaddr']

        except Exception as e:
            log.msg("GUIpoll ---> kademlia_pong",rpl777, type(rpl777),"\n")
            log.msg("Error rplArgsRQ {0}".format(str(e)))

        try:
            port =  rpl777['port']
            numpings =  rpl777['numpings']
            lag  =  rpl777['lag']
            ipaddr  = rpl777['ipaddr']
            numpongs =  rpl777['numpongs']
            result =   rpl777['result']
            ave  =  rpl777['ave']
            NXT  = rpl777['NXT']
            #
            #log.msg("GUIpoll ---> rpl777", rpl777,type(rpl777))

        except Exception as e:
            log.msg("GUIpoll ---> kademlia_pong ERR",rpl777, type(rpl777),"\n")
            log.msg("Error rpl777 {0}".format(str(e)))

        #log.msg("pongers: ", (self.pongers),"\n")

        if not ipaddr  in self.pongers.keys():
            log.msg(ipaddr)
            log.msg(type(ipaddr))

            if ipaddr == '<nullstr':
                print(12*"\n###########", rpl777)

            self.pongers[ipaddr] =  rpl777

        log.msg("pongers: ", len(self.ipaddr))

        numPongers =  len(self.ipaddr)



        # 2014-12-29 12:10:41+0100 [-] GUIpoll ---> rpl777 {'tag': '', 'numpongs': 144, 'lag': '344.375', 'ave': '1259.662', 'numpings': 143, 'result': 'kademlia_pong', 'isMM': '0', 'ipaddr': '<nullstr>', 'NXT': '15178638394924629506', 'port': 0} <class 'dict'>

            # ToDo : check for how often nullst is ipaddr!!

        # kademlia_pong {'args': '[{"requestType":"pong","NXT":"1978065578067355462","time":1419845114,"MMatrix":0,"yourip":"79.245.5.160","yourport":34365,"ipaddr":"89.212.19.49","pubkey":"c269a8b4567c0b3062e6c4be859d845c4b808a405dd03d0d1ac7b4d9cb725b40","ver":"0.399"},{"token":"aqqagqe2sph302rsgieobfm482580iqs386jrk2teb5tjd671sprkg2r7qe3r1821bfds7marsagn15srbn8p447s8oqon5r6a38r21j9q205fiai54r7dtjdfjongdrpp2gsgopa8f7cum3999h5q1t0jl6fjhb"}]', 'from': '89.212.19.49', 'port': 0, 'result': '{"result":"kademlia_pong","tag":"","isMM":"0","NXT":"1978065578067355462","ipaddr":"89.212.19.49","port":0,"lag":"630.578","numpings":63,"numpongs":65,"ave":"1026.539"}'} <class 'dict'>
        # GUIpoll ---> rpl777 {'ave': '1026.539', 'lag': '630.578', 'NXT': '1978065578067355462', 'port': 0, 'result': 'kademlia_pong', 'ipaddr': '89.212.19.49', 'numpings': 63, 'numpongs': 65, 'tag': '', 'isMM': '0'} <class 'dict'>





    def rpl777_df1_settings(self, dataFrom777): #these are the basic pings from the whitlist
        """
         this sends pings

          """#
        repl=dataFrom777.json()
        reqPing = {'requestType':'ping'}

        # self.peersDiLoc[node[1]] = node[0]

        ipsToPing=repl['whitelist'] #[0] # singlecheck
        # manual tests:
        #ipsToPing = 20* ['88.179.105.82'] # ['178.62.185.131'] # stonefish['80.41.56.181'] # ['85.178.202.108']   #

        log.msg(1*"ping to whitelist:")#, reqPing['destip'])
        for node in ipsToPing:
            reqPing['destip']=node
            sleep(0.25)
            #log.msg("ping to whitelist:", reqPing['destip'])
            self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqPing), headers=POSTHEADERS)
            self.deferred.addCallback(self.rpl777_df2_ping)
            self.deferred.addErrback(self.rpl777ERR)



    def rpl777_df1_getpeers(self, dataFrom777):
        """

         peers [{'pubkey': '05a7612d54d14c21be9baa654ad50b4ba423eea0735185ac732ada2332315c3f', 'RS': 'NXT-8AF7-ESB7-GHFM-896JY', 'privateNXT': '8016556209183334821'}, {'RS': 'NXT-7PPP-R6AJ-VSJ7-37C7V', 'pserver': {'recv': 8, 'lastrecv': 14.0111578, 'lastsent': 14.01127447, 'pings': 1, 'sent': 8}, 'srvipaddr': '178.62.185.131', 'recv': 8, 'srvNXT': '2131686659786462901', 'pubkey': '849c97e5b1e8c50429249eff867de5e6ded39d34a6ccc9c42ea720d927a12d18', 'sent': 8}, {'RS': 'NXT-EZJ4-8F5T-8VX4-FVCB7', 'pserver': {'lastrecv': 0.6551996, 'lastsent': 0.06295793, 'pingtime': 231, 'avetime': 3893.46431672, 'recv': 155, 'pings': 63, 'pongs': 63, 'sent': 178}, 'srvipaddr': '167.114.2.206', 'recv': 155, 'srvNXT': '15178638394924629506', 'pubkey': '52e3524b5392a2ecba9e702a0c9c04d3d73dc4f93008977e1bcd15ea5bd5b376', 'sent': 178}, {'RS': 'NXT-5TU8-78XL-W2CW-32WWQ', 'pserver': {'lastrecv': 0.07671293, 'lastsent': 0.00977127, 'pingtime': 176.5, 'avetime': 18793.97457429, 'recv': 188, 'pings': 83, 'pongs': 84, 'sent': 205}, 'srvipaddr': '89.212.19.49', 'recv': 188, 'srvNXT': '1978065578067355462', 'pubkey': 'c269a8b4567c0b3062e6c4be859d845c4b808a405dd03d0d1ac7b4d9cb725b40', 'sent': 205}, {'RS': 'NXT-A4NA-7P8Y-MDMZ-3K4AZ', 'pserver': {'lastrecv': 0.07303403, 'lastsent': 0.07965903, 'pingtime': 327.75, 'avetime': 33324.18828125, 'recv': 35, 'pings': 9, 'pongs': 11, 'sent': 81}, 'srvipaddr': '167.114.2.204', 'recv': 35, 'srvNXT': '2278910666471639688', 'pubkey': '47faa8a876ae56be36a1d214515d0ef3f9ff99b06f4d2702acf0380cab7ccc5e', 'sent': 81}, {'RS': 'NXT-JNLE-Q9XW-MG8P-7GQKE', 'pserver': {'lastrecv': 0.05130237, 'lastsent': 0.0543357, 'pingtime': 36882.25, 'avetime': 13861.70690789, 'recv': 127, 'pings': 47, 'pongs': 48, 'sent': 174}, 'srvipaddr': '192.99.246.126', 'recv': 127, 'srvNXT': '6216883599460291148', 'pubkey': '2fdfab9d3d5e1c91a27e48ed7422ebcea628ebdf36ea0052fdd62e1533a8751d', 'sent': 174}, {'RS': 'NXT-YPWQ-F7SB-WCD7-CFCLC', 'pserver': {'lastrecv': 0.01943838, 'lastsent': 0.02329255, 'pingtime': 295, 'avetime': 7594.5688101, 'recv': 104, 'pings': 38, 'pongs': 40, 'sent': 131}, 'srvipaddr': '167.114.2.94', 'recv': 104, 'srvNXT': '11910135804814382998', 'pubkey': '34e55ae366e8b11e5dc195f29a0d9999567123b9c02e4a621600e4de5c72bb77', 'sent': 131}, {'RS': 'NXT-NHBB-5ZF3-4WTB-GBCK3', 'pserver': {'lastrecv': 2.37580073, 'lastsent': 0.0236049, 'pingtime': 52420.75, 'avetime': 7924.83104292, 'recv': 193, 'pings': 84, 'pongs': 82, 'sent': 181}, 'srvipaddr': '167.114.2.203', 'recv': 193, 'srvNXT': '16196432036059823401', 'pubkey': 'be3db1badadb0e95b8afd2f1f5f53df7837de15c14f09f7a531c489a3f470543', 'sent': 181}, {'RS': 'NXT-Y5FR-ZSRB-BQWC-9W9PR', 'pserver': {'lastrecv': 1.36517293, 'lastsent': 0.03602293, 'pingtime': 93572, 'avetime': 20840.15337171, 'recv': 96, 'pings': 37, 'pongs': 39, 'sent': 104}, 'srvipaddr': '192.99.246.33', 'recv': 96, 'srvNXT': '8923034930361863607', 'pubkey': 'ea83e39d553470725960180afb25afffe3de1fe0019979236b96536e22e1ed29', 'sent': 104}, {'RS': 'NXT-VSVF-FFF5-M4EX-8YUB7', 'pserver': {'lastrecv': 0.04354165, 'lastsent': 0.00936665, 'pingtime': 36595.5, 'avetime': 9679.23729884, 'recv': 188, 'pings': 90, 'pongs': 77, 'sent': 224}, 'srvipaddr': '167.114.2.171', 'recv': 188, 'srvNXT': '7108754351996134253', 'pubkey': '9e33da1c9ac00d376832cf3c9293dfb21d055d76e1c446449f0672fd688a237f', 'sent': 224}, {'RS': 'NXT-DGHK-DUWA-2MRL-C44UP', 'pserver': {'lastrecv': 1.73030202, 'lastsent': 0.00871452, 'pingtime': 45173.25, 'avetime': 9300.74114583, 'recv': 134, 'pings': 62, 'pongs': 58, 'sent': 130}, 'srvipaddr': '167.114.2.205', 'recv': 134, 'srvNXT': '12315166155634751985', 'pubkey': 'eef155b7c8c50dc62ae45f40c30d2b1a0874ca5f5f11adeef7637933d863583b', 'sent': 130}, {'RS': 'NXT-WXJV-AFNK-YW5D-6S95W', 'pserver': {'lastrecv': 1.77902338, 'lastsent': 0.02744422, 'pingtime': -156179, 'avetime': 10604.32024083, 'recv': 114, 'pings': 63, 'pongs': 46, 'sent': 157}, 'srvipaddr': '192.99.212.250', 'recv': 114, 'srvNXT': '5624143003089008155', 'pubkey': 'ecea0d22fca77e28210c0b4c05b8bd16ff8003e5065c09f4e73105398e31840f', 'sent': 157}, {'RS': 'NXT-VT9R-9GYM-YLJF-D8QCT', 'pserver': {'lastrecv': 1.15555233, 'lastsent': 0.01185233, 'pingtime': 223334, 'avetime': 39925.74770221, 'recv': 123, 'pings': 50, 'pongs': 52, 'sent': 134}, 'srvipaddr': '192.99.246.20', 'recv': 123, 'srvNXT': '13594896385051583735', 'pubkey': '430695694b02bb71e8222e1e5d20b1c985afd9ba899e25fe2d52ee1be92f532c', 'sent': 134}, {'RS': 'NXT-UE4H-CXMN-HR75-8W376', 'pserver': {'lastrecv': 4.86252565, 'lastsent': 0.02568398, 'pingtime': -3670675.75, 'avetime': 12546.13709677, 'recv': 14, 'pings': 30, 'pongs': 1, 'sent': 158}, 'srvipaddr': '94.102.50.70', 'recv': 14, 'srvNXT': '7067340061344084047', 'pubkey': '4bd4794f0a77d22949c944f96f9b7a429021e59644a98eea310546fd47b96440', 'sent': 158}, {'RS': 'NXT-XSQA-YBXH-CW2M-93QSF', 'pserver': {'lastrecv': 1.1530546, 'lastsent': 0.05522543, 'pingtime': 371363.25, 'avetime': 83528.03227459, 'recv': 54, 'pings': 41, 'pongs': 20, 'sent': 143}, 'srvipaddr': '37.59.108.92', 'recv': 54, 'srvNXT': '8566622688401875656', 'pubkey': '5a1c33c1e00cec3beecb9a9fcd8379fe61d6a661566875cf0cff89726b27b76f', 'sent': 143}]
         peers is a LIST!

         [

         {'pubkey': '05a7612d54d14c21be9baa654ad50b4ba423eea0735185ac732ada2332315c3f', 'RS': 'NXT-8AF7-ESB7-GHFM-896JY', 'privateNXT': '8016556209183334821'},

         {'RS': 'NXT-7PPP-R6AJ-VSJ7-37C7V', 'pserver': {'recv': 8, 'lastrecv': 14.0111578, 'lastsent': 14.01127447, 'pings': 1, 'sent': 8},
         'srvipaddr': '178.62.185.131', 'recv': 8, 'srvNXT': '2131686659786462901', 'pubkey': '849c97e5b1e8c50429249eff867de5e6ded39d34a6ccc9c42ea720d927a12d18', 'sent': 8},

         {'RS': 'NXT-EZJ4-8F5T-8VX4-FVCB7', 'pserver': {'lastrecv': 0.6551996, 'lastsent': 0.06295793, 'pingtime': 231, 'avetime': 3893.46431672, 'recv': 155, 'pings': 63, 'pongs': 63, 'sent': 178},
          'srvipaddr': '167.114.2.206', 'recv': 155, 'srvNXT': '15178638394924629506', 'pubkey': '52e3524b5392a2ecba9e702a0c9c04d3d73dc4f93008977e1bcd15ea5bd5b376', 'sent': 178},

          {'RS': 'NXT-5TU8-78XL-W2CW-32WWQ', 'pserver': {'lastrecv': 0.07671293, 'lastsent': 0.00977127, 'pingtime': 176.5, 'avetime': 18793.97457429, 'recv': 188, 'pings': 83, 'pongs': 84, 'sent': 205}, 'srvipaddr': '89.212.19.49', 'recv': 188, 'srvNXT': '1978065578067355462', 'pubkey': 'c269a8b4567c0b3062e6c4be859d845c4b808a405dd03d0d1ac7b4d9cb725b40', 'sent': 205},
          {'RS': 'NXT-A4NA-7P8Y-MDMZ-3K4AZ', 'pserver': {'lastrecv': 0.07303403, 'lastsent': 0.07965903, 'pingtime': 327.75, 'avetime': 33324.18828125, 'recv': 35, 'pings': 9, 'pongs': 11, 'sent': 81}, 'srvipaddr': '167.114.2.204', 'recv': 35, 'srvNXT': '2278910666471639688', 'pubkey': '47faa8a876ae56be36a1d214515d0ef3f9ff99b06f4d2702acf0380cab7ccc5e', 'sent': 81},

          ]


        """#

        repl=dataFrom777.json()

        Numnxtaccts = repl['Numnxtaccts']
        peers = repl['peers']
        Numpservers = repl['Numpservers']
        num = repl['num']
        log.msg("Numnxtaccts", Numnxtaccts)
        #log.msg("peers", peers)
        log.msg("Numpservers", Numpservers)
        log.msg("num", num)

        reqFindnode = {'requestType':'findnode'}

        reqPing = {'requestType':'ping'}

        for peer in peers[2:]:
            #log.msg(1*"\n\npeer:", peer, type(peer))
            ipaddr = peer['srvipaddr']
            reqPing['destip'] = ipaddr

            # #log.msg("ping to peer:", reqPing['destip'])
            self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqPing), headers=POSTHEADERS)
            self.deferred.addCallback(self.rpl777_df2_ping)
            self.deferred.addErrback(self.rpl777ERR)

            pserv = peer['pserver']
            srvNXT = peer['srvNXT']
            sleep(0.25)
            reqFindnode['key']=srvNXT
            self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqFindnode), headers=POSTHEADERS)
            self.deferred.addCallback(self.rpl777_df2_findnode )
            self.deferred.addErrback(self.rpl777ERR)



    def rpl777_df2_ping(self, dataFrom777):
        """


        """#
        repl=dataFrom777.json()
        repl=dataFrom777.content.decode("utf-8")
        repl=eval(repl)
        #log.msg( 1 * "ping sent", repl)



    def rpl777_df2_findnode(self, dataFrom777):

        repl=dataFrom777.json()
        repl=dataFrom777.content.decode("utf-8")
        repl=eval(repl)
        log.msg( 1 * "rpl777_df2_findnode sent", repl)




    def rpl777ERR(self, ERR777): # ERR777 is of type exception

        log.msg("ERR777 UC2", ERR777.value, type(ERR777.value)) #.printDetailedTraceback())
        raise RuntimeError(ERR777.printDetailedTraceback())










######################   UC2_havenode fin
######################
######################
######################
######################
######################
######################











class UCTEST_3_store_findvalue(object):
    """

    import binascii
  ss="asdfasfreGJHGJHGKJGoo769875tkzg"

  ss1=ss.encode("utf-8")

Out[48]: b'asdfasfreGJHGJHGKJGoo769875tkzg'

  test =  ss1.hexlify(ss1)

In [50]: test
Out[50]: b'617364666173667265474a48474a48474b4a476f6f373639383735746b7a67'




"""#


    def __init__(self, serverFactory , environ = {} ): # prepSchedules = {},



        self.MSGfrags = [
                        'Eight, sir; seven, sir;',
                        'Six, sir; five, sir;',
                        'Four, sir; three, sir;',
                        'Two, sir; one!',
                        'Tenser, said the Tensor.',
                        'Tenser, said the Tensor.',
                        'Tension, apprehension,',
                        'And dissension have begun.',
                        ]


        self.environ = environ
        self.schedules = {}    # this contains the schedules

        self.peersDiLoc = {}
        #self.peers = {}

        self.storedVals = {} # name:data !

        prepSchedules = environ['UCTEST_3_store_findvalue'] # can use same as UC1 for now- extends it
        for sched in prepSchedules.keys():
            sched = prepSchedules[sched]
            self.schedules[ sched['schedName']] = Schedule( sched )

        self.lastCallTime = int(time.time() * 1000)


    def periodic(self, ):
        """ This is the method that is called periodically by the twisted loopingTask.
         It iterates over all schedules in the UseCase class, checks if they are due to be called,
         adds the ones due to a list and passes that list on to runSchedules(). """#

        schedulesDue =[]

# curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=store&name=starbucks&data=c0ffee'
#{'key': '1031470952125437106', 'txid': '0', 'len': 3, 'data': 'c0ffee', 'result': 'kademlia_store'}
#curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=findvalue&key=1031470952125437106'
#{'key': '1031470952125437106', 'len': '3', 'data': 'c0ffee'}





#./BitcoinDarkd SuperNET '{"requestType":"store","key":"116876777391303227","data":"deadbee32f"}'
#./BitcoinDarkd SuperNET '{"requestType":"findvalue","key":"116876777391303227"}'
# havenodeB ???

#./BitcoinDarkd SuperNET '{"requestType":"store","key":"116876777391303227","data":"deadbee32f"}'
#./BitcoinDarkd SuperNET '{"requestType":"findvalue","key":"116876777391303227"}'
# havenodeB ???





        for schedule in self.schedules.keys():
            schedule = self.schedules[schedule]

            if schedule.callMe():
                schedulesDue.append(schedule)

        self.runSchedules(schedulesDue)


    def runSchedules(self,schedulesDue):
        """ here we get through all the due schedules and call them on SuperNET server
             Here we explicitly check the name and send them to the first callback of their callback sequence."""#




        def msg():
            msg = ''
            for frag in range(randint(4,7)):
                msg +=  self.MSGfrags[randint(0,7)]
            return msg

        for schedDue in schedulesDue:
            if 'sched_findvalue' in schedDue.SNrequests.keys():

                reqData1 = schedDue.SNrequests['sched_findvalue']

                for key in self.storedVals.keys():
                    reqData1['key'] = self.storedVals[key]
                    print(1*"\nreqData1 try to FINDVALUE", reqData1)

                    self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqData1), headers=POSTHEADERS)
                    self.deferred.addCallback(self.rpl777_findvalue)
                    self.deferred.addErrback(self.rpl777ERR)



            elif 'sched_store' in schedDue.SNrequests.keys():
                log.msg("do sched_store")
                reqData = schedDue.SNrequests['sched_store'] # this has 0.9 sec



                n1=msg()
                n2=n1.encode("utf-8")
                n2 = binascii.hexlify(n2)
                n3 = n2.decode("utf-8")



                reqData['name'] = 'myStoreName' + str(int(time.time())) #n1


                reqData['data'] = n3


                log.msg("do reqData", reqData)


                self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqData), headers=POSTHEADERS)
                self.deferred.addCallback(self.rpl777_store)
                self.deferred.addErrback(self.rpl777ERR)

            elif 'GUIpoll' in schedDue.SNrequests.keys():
                log.msg("do GUIpoll")
                reqData = schedDue.SNrequests['GUIpoll'] # this has 0.9 sec
                self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqData), headers=POSTHEADERS)
                self.deferred.addCallback(self.rpl777_GUIpoll)
                self.deferred.addErrback(self.rpl777ERR)


    def rpl777_store(self, dataFrom777):

        rpl777=dataFrom777.json()
        print("rpl777_stored a data val", rpl777, type(rpl777))
        #stored = {}

        self.storedVals[rpl777['key']] = rpl777['key']

#
# reqData STORE {'name': 'myStoreName1418569814', 'data': 'myStoreData1418569814', 'requestType': 'store'}
# 2014-12-14 16:10:14+0100 [-] do GUIpoll
# 2014-12-14 16:10:15+0100 [-] rpl777_stored a data val {'txid': '13689646989932326452', 'result': 'kademlia_store', 'data': 'fffffffefafa1418569814', 'len': 11, 'key': '270615323620844315'} <class 'dict'>

# okokokokokokok

        #
        # {'data': 'myStoreData1418569169', 'name': 'myStoreName1418569169', 'requestType': 'store'}




    def rpl777_findvalue(self, dataFrom777):

        rpl777=dataFrom777.json()
        print(1 * "\nrpl777_findvalue got this:", rpl777)

#rpl="{'len': '112', 'key': '16442637354607720438', 'data': '5369782c207369723b20666976652c207369723b54656e7365722c2073616964207468652054656e736f722e45696768742c207369723b20736576656e2c207369723b45696768742c207369723b20736576656e2c207369723b466f75722c207369723b2074687265652c207369723b'}"

        #foundVal=eval(rpl777)
        foundVal=rpl777['data']
        #foundVal = foundVal.decode("utf-8")
        foundVal = binascii.a2b_hex(foundVal)

        print(1 * "\nrpl777_findvalue got this:", foundVal)



    def rpl777_havenodeB(self, dataFrom777):

        rpl777=dataFrom777.json()
        print(1*"\nrpl777_havenodeB", rpl777, type(rpl777))


    def rpl777_GUIpoll(self, dataFrom777):
        """



         """#

        # test on string and send there!
        # maybe this can be done more elegant later, but probably not.

        #log.msg("GUIpoll entry--->  ",dataFrom777, type(dataFrom777),"\n")

        rpl777=dataFrom777.json()
        #log.msg("GUIpoll entry--->  ",rpl777, type(rpl777),"\n")

        if 'nothing pending' in str(rpl777):
            pass#
            log.msg("GUIpoll --->  ",rpl777, type(rpl777),"\n")

        elif 'kademlia_store' in str(rpl777):
            self.rpl777_GUIpoll_kademlia_store(rpl777)
            #log.msg("GUIpoll ---> kademlia_store",rpl777, type(rpl777),"\n")

        elif 'kademlia_findvalue' in str(rpl777):
            #log.msg("GUIpoll ---> findnode",rpl777, type(rpl777),"\n")
            self.rpl777_GUIpoll_findvalue(rpl777)

        elif 'kademlia_havenodeB' in str(rpl777):
            log.msg("GUIpoll ---> kademlia_havenodeB",rpl777, type(rpl777),"\n")
            self.rpl777_GUIpoll_havenodeB(rpl777)



        else:
            log.msg(1*"GUIpoll ---> CALL not caught yet: ",rpl777, type(rpl777),"\n")

        return 0



    def rpl777_GUIpoll_havenodeB(self,rpl777):

        log.msg(1*"\n  ---> rpl777_GUIpoll_havenodeB",rpl777, type(rpl777),"\n")


    def rpl777_GUIpoll_findvalue(self,rpl777):

        log.msg(1*"\n  ---> rpl777_GUIpoll_findvalue",rpl777, type(rpl777),"\n")

    def rpl777_GUIpoll_kademlia_store(self,rpl777):

        log.msg(1*"\n  ---> rpl777_GUIpoll_kademlia_store",rpl777, type(rpl777),"\n")



    def rpl777ERR(self, ERR777):
        print("ERR", ERR777)





####################################
####################################
####################################
####################################
####################################
####################################






class UC_4_sendMSGs(object):

    """
differentiate two types of replies:

1- the replies that are given back by the SuperNET server regularly
2- the replies that are taken from the internal GUIpoll
3- this UC maintains a local dict of peers from doing getpeers and from all HAVENODEs

    """#



    def __init__(self, serverFactory , environ = {} ):

        self.serverFactory = serverFactory

        self.MSGfrags = [
                        'Eight, sir; seven, sir;',
                        'Six, sir; five, sir;',
                        'Four, sir; three, sir;',
                        'Two, sir; one!',
                        'Tenser, said the Tensor.',
                        'Tenser, said the Tensor.',
                        'Tension, apprehension,',
                        'And dissension have begun.',
                        ]
        # #
        # self.MSGfrags = [' PING SPIKES GALORE',
        #                  ' anybody can see this???',
        #                  ' Noth Korean Hacker Attack',
        #                  ' (c) Sony Motion Pictures',
        #                  ' looks like the heat is on now!',
        #                  ' Three Two One Liftoff..',
        #                  ' any banks in trouble??',
        #                  ' SuperNET messages tunnel under ping spikes ']

        self.environ = environ
        self.schedules = {}    # this contains the schedules

        self.peersDiLoc = {}
        #self.peers = {}

        self.numCalls = 0
        # can collect the RQs used here for neatness
        self.RQsendmsg =  {'requestType':'sendmessage'}
        # each UC only has one ONE master schedule, and the sub-schedules are contained in that
        prepSchedules = environ['UCsched_1'] # can use same as UC1 for now- extends it
        for sched in prepSchedules.keys():
            sched = prepSchedules[sched]
            self.schedules[ sched['schedName']] = Schedule( sched )

        self.lastCallTime = int(time.time() * 1000)



    def periodic(self, ):
        """ This is the method that is called periodically by the twisted loopingTask.
         It iterates over all schedules in the UseCase class, checks if they are due to be called,
         adds the ones due to a list and passes that list on to runSchedules(). """#

        schedulesDue =[]
        for schedule in self.schedules.keys():
            schedule = self.schedules[schedule]

            if schedule.callMe():
                schedulesDue.append(schedule)

        self.runSchedules(schedulesDue)



    def runSchedules(self,schedulesDue):
        """ here we get through all the due schedules and call them on SuperNET server
             Here we explicitly check the name and send them to the first callback of their callback sequence."""#

        self.numCalls+=1
        for schedDue in schedulesDue:
            if 'uc_settings' in schedDue.SNrequests.keys():
                log.msg("peersDiLoc: IPs ", self.peersDiLoc.keys())
                log.msg("peersDiLoc: NXTs", self.peersDiLoc.values())

                reqData1 = schedDue.SNrequests['uc_settings']
                self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqData1), headers=POSTHEADERS)
                self.deferred.addCallback(self.rpl777_df1_settings)
                self.deferred.addErrback(self.rpl777ERR)

                #
                #
                # reqData2 = {"requestType":"getpeers"}
                # self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqData2), headers=POSTHEADERS)
                # self.deferred.addCallback(self.rpl777_df1_getpeers) #rpl777_pingDB_df1
                # self.deferred.addErrback(self.rpl777ERR)



            elif 'uc_findnode' in schedDue.SNrequests.keys():
                reqFindnode = {'requestType':'findnode'}
                log.msg(1*"\n reqFindnode all local peers:", self.peersDiLoc, type(self.peersDiLoc))
                for peer in self.peersDiLoc.keys():
                    reqFindnode['key']=self.peersDiLoc[peer]
                    sleep(0.25)
                    self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqFindnode), headers=POSTHEADERS)
                    self.deferred.addCallback(self.rpl777_df3_findnode )
                    self.deferred.addErrback(self.rpl777ERR)

            elif 'GUIpoll' in schedDue.SNrequests.keys():
                reqData = schedDue.SNrequests['GUIpoll'] # this has 0.9 sec
                self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqData), headers=POSTHEADERS)
                self.deferred.addCallback(self.rpl777_GUIpoll)
                self.deferred.addErrback(self.rpl777ERR)




    def rpl777_GUIpoll(self, dataFrom777):
        """

         """#

        rpl777=dataFrom777.json()
        #log.msg("GUIpoll entry--->  ",rpl777, type(rpl777))

        if 'nothing pending' in str(rpl777):
            log.msg("GUIpoll  ",rpl777)

        elif 'kademlia_store' in str(rpl777):
            self.rpl777_GUIpoll_kademlia_store(rpl777)

        elif 'kademlia_pong' in str(rpl777):
             self.rpl777_GUIpoll_kademlia_pong(rpl777)

        elif 'kademlia_havenode' in str(rpl777):
             self.rpl777_GUIpoll_kademlia_havenode(rpl777)

        elif 'kademlia_findnode' in str(rpl777):
             self.rpl777_GUIpoll_findnode(rpl777)

        else:
            log.msg(20*"GUIpoll ---> CALL not caught yet: ",rpl777, type(rpl777),"\n")

        return 0



    def rpl777_df1_getpeers(self, dataFrom777): #these are the basic pings from the whitlist
        """

         peers [{'pubkey': '05a7612d54d14c21be9baa654ad50b4ba423eea0735185ac732ada2332315c3f', 'RS': 'NXT-8AF7-ESB7-GHFM-896JY', 'privateNXT': '8016556209183334821'}, {'RS': 'NXT-7PPP-R6AJ-VSJ7-37C7V', 'pserver': {'recv': 8, 'lastrecv': 14.0111578, 'lastsent': 14.01127447, 'pings': 1, 'sent': 8}, 'srvipaddr': '178.62.185.131', 'recv': 8, 'srvNXT': '2131686659786462901', 'pubkey': '849c97e5b1e8c50429249eff867de5e6ded39d34a6ccc9c42ea720d927a12d18', 'sent': 8}, {'RS': 'NXT-EZJ4-8F5T-8VX4-FVCB7', 'pserver': {'lastrecv': 0.6551996, 'lastsent': 0.06295793, 'pingtime': 231, 'avetime': 3893.46431672, 'recv': 155, 'pings': 63, 'pongs': 63, 'sent': 178}, 'srvipaddr': '167.114.2.206', 'recv': 155, 'srvNXT': '15178638394924629506', 'pubkey': '52e3524b5392a2ecba9e702a0c9c04d3d73dc4f93008977e1bcd15ea5bd5b376', 'sent': 178}, {'RS': 'NXT-5TU8-78XL-W2CW-32WWQ', 'pserver': {'lastrecv': 0.07671293, 'lastsent': 0.00977127, 'pingtime': 176.5, 'avetime': 18793.97457429, 'recv': 188, 'pings': 83, 'pongs': 84, 'sent': 205}, 'srvipaddr': '89.212.19.49', 'recv': 188, 'srvNXT': '1978065578067355462', 'pubkey': 'c269a8b4567c0b3062e6c4be859d845c4b808a405dd03d0d1ac7b4d9cb725b40', 'sent': 205}, {'RS': 'NXT-A4NA-7P8Y-MDMZ-3K4AZ', 'pserver': {'lastrecv': 0.07303403, 'lastsent': 0.07965903, 'pingtime': 327.75, 'avetime': 33324.18828125, 'recv': 35, 'pings': 9, 'pongs': 11, 'sent': 81}, 'srvipaddr': '167.114.2.204', 'recv': 35, 'srvNXT': '2278910666471639688', 'pubkey': '47faa8a876ae56be36a1d214515d0ef3f9ff99b06f4d2702acf0380cab7ccc5e', 'sent': 81}, {'RS': 'NXT-JNLE-Q9XW-MG8P-7GQKE', 'pserver': {'lastrecv': 0.05130237, 'lastsent': 0.0543357, 'pingtime': 36882.25, 'avetime': 13861.70690789, 'recv': 127, 'pings': 47, 'pongs': 48, 'sent': 174}, 'srvipaddr': '192.99.246.126', 'recv': 127, 'srvNXT': '6216883599460291148', 'pubkey': '2fdfab9d3d5e1c91a27e48ed7422ebcea628ebdf36ea0052fdd62e1533a8751d', 'sent': 174}, {'RS': 'NXT-YPWQ-F7SB-WCD7-CFCLC', 'pserver': {'lastrecv': 0.01943838, 'lastsent': 0.02329255, 'pingtime': 295, 'avetime': 7594.5688101, 'recv': 104, 'pings': 38, 'pongs': 40, 'sent': 131}, 'srvipaddr': '167.114.2.94', 'recv': 104, 'srvNXT': '11910135804814382998', 'pubkey': '34e55ae366e8b11e5dc195f29a0d9999567123b9c02e4a621600e4de5c72bb77', 'sent': 131}, {'RS': 'NXT-NHBB-5ZF3-4WTB-GBCK3', 'pserver': {'lastrecv': 2.37580073, 'lastsent': 0.0236049, 'pingtime': 52420.75, 'avetime': 7924.83104292, 'recv': 193, 'pings': 84, 'pongs': 82, 'sent': 181}, 'srvipaddr': '167.114.2.203', 'recv': 193, 'srvNXT': '16196432036059823401', 'pubkey': 'be3db1badadb0e95b8afd2f1f5f53df7837de15c14f09f7a531c489a3f470543', 'sent': 181}, {'RS': 'NXT-Y5FR-ZSRB-BQWC-9W9PR', 'pserver': {'lastrecv': 1.36517293, 'lastsent': 0.03602293, 'pingtime': 93572, 'avetime': 20840.15337171, 'recv': 96, 'pings': 37, 'pongs': 39, 'sent': 104}, 'srvipaddr': '192.99.246.33', 'recv': 96, 'srvNXT': '8923034930361863607', 'pubkey': 'ea83e39d553470725960180afb25afffe3de1fe0019979236b96536e22e1ed29', 'sent': 104}, {'RS': 'NXT-VSVF-FFF5-M4EX-8YUB7', 'pserver': {'lastrecv': 0.04354165, 'lastsent': 0.00936665, 'pingtime': 36595.5, 'avetime': 9679.23729884, 'recv': 188, 'pings': 90, 'pongs': 77, 'sent': 224}, 'srvipaddr': '167.114.2.171', 'recv': 188, 'srvNXT': '7108754351996134253', 'pubkey': '9e33da1c9ac00d376832cf3c9293dfb21d055d76e1c446449f0672fd688a237f', 'sent': 224}, {'RS': 'NXT-DGHK-DUWA-2MRL-C44UP', 'pserver': {'lastrecv': 1.73030202, 'lastsent': 0.00871452, 'pingtime': 45173.25, 'avetime': 9300.74114583, 'recv': 134, 'pings': 62, 'pongs': 58, 'sent': 130}, 'srvipaddr': '167.114.2.205', 'recv': 134, 'srvNXT': '12315166155634751985', 'pubkey': 'eef155b7c8c50dc62ae45f40c30d2b1a0874ca5f5f11adeef7637933d863583b', 'sent': 130}, {'RS': 'NXT-WXJV-AFNK-YW5D-6S95W', 'pserver': {'lastrecv': 1.77902338, 'lastsent': 0.02744422, 'pingtime': -156179, 'avetime': 10604.32024083, 'recv': 114, 'pings': 63, 'pongs': 46, 'sent': 157}, 'srvipaddr': '192.99.212.250', 'recv': 114, 'srvNXT': '5624143003089008155', 'pubkey': 'ecea0d22fca77e28210c0b4c05b8bd16ff8003e5065c09f4e73105398e31840f', 'sent': 157}, {'RS': 'NXT-VT9R-9GYM-YLJF-D8QCT', 'pserver': {'lastrecv': 1.15555233, 'lastsent': 0.01185233, 'pingtime': 223334, 'avetime': 39925.74770221, 'recv': 123, 'pings': 50, 'pongs': 52, 'sent': 134}, 'srvipaddr': '192.99.246.20', 'recv': 123, 'srvNXT': '13594896385051583735', 'pubkey': '430695694b02bb71e8222e1e5d20b1c985afd9ba899e25fe2d52ee1be92f532c', 'sent': 134}, {'RS': 'NXT-UE4H-CXMN-HR75-8W376', 'pserver': {'lastrecv': 4.86252565, 'lastsent': 0.02568398, 'pingtime': -3670675.75, 'avetime': 12546.13709677, 'recv': 14, 'pings': 30, 'pongs': 1, 'sent': 158}, 'srvipaddr': '94.102.50.70', 'recv': 14, 'srvNXT': '7067340061344084047', 'pubkey': '4bd4794f0a77d22949c944f96f9b7a429021e59644a98eea310546fd47b96440', 'sent': 158}, {'RS': 'NXT-XSQA-YBXH-CW2M-93QSF', 'pserver': {'lastrecv': 1.1530546, 'lastsent': 0.05522543, 'pingtime': 371363.25, 'avetime': 83528.03227459, 'recv': 54, 'pings': 41, 'pongs': 20, 'sent': 143}, 'srvipaddr': '37.59.108.92', 'recv': 54, 'srvNXT': '8566622688401875656', 'pubkey': '5a1c33c1e00cec3beecb9a9fcd8379fe61d6a661566875cf0cff89726b27b76f', 'sent': 143}]
         peers is a LIST!

         [

         {'pubkey': '05a7612d54d14c21be9baa654ad50b4ba423eea0735185ac732ada2332315c3f', 'RS': 'NXT-8AF7-ESB7-GHFM-896JY', 'privateNXT': '8016556209183334821'},

         {'RS': 'NXT-7PPP-R6AJ-VSJ7-37C7V', 'pserver': {'recv': 8, 'lastrecv': 14.0111578, 'lastsent': 14.01127447, 'pings': 1, 'sent': 8},
         'srvipaddr': '178.62.185.131', 'recv': 8, 'srvNXT': '2131686659786462901', 'pubkey': '849c97e5b1e8c50429249eff867de5e6ded39d34a6ccc9c42ea720d927a12d18', 'sent': 8},

         {'RS': 'NXT-EZJ4-8F5T-8VX4-FVCB7', 'pserver': {'lastrecv': 0.6551996, 'lastsent': 0.06295793, 'pingtime': 231, 'avetime': 3893.46431672, 'recv': 155, 'pings': 63, 'pongs': 63, 'sent': 178},
          'srvipaddr': '167.114.2.206', 'recv': 155, 'srvNXT': '15178638394924629506', 'pubkey': '52e3524b5392a2ecba9e702a0c9c04d3d73dc4f93008977e1bcd15ea5bd5b376', 'sent': 178},

          {'RS': 'NXT-5TU8-78XL-W2CW-32WWQ', 'pserver': {'lastrecv': 0.07671293, 'lastsent': 0.00977127, 'pingtime': 176.5, 'avetime': 18793.97457429, 'recv': 188, 'pings': 83, 'pongs': 84, 'sent': 205}, 'srvipaddr': '89.212.19.49', 'recv': 188, 'srvNXT': '1978065578067355462', 'pubkey': 'c269a8b4567c0b3062e6c4be859d845c4b808a405dd03d0d1ac7b4d9cb725b40', 'sent': 205},
          {'RS': 'NXT-A4NA-7P8Y-MDMZ-3K4AZ', 'pserver': {'lastrecv': 0.07303403, 'lastsent': 0.07965903, 'pingtime': 327.75, 'avetime': 33324.18828125, 'recv': 35, 'pings': 9, 'pongs': 11, 'sent': 81}, 'srvipaddr': '167.114.2.204', 'recv': 35, 'srvNXT': '2278910666471639688', 'pubkey': '47faa8a876ae56be36a1d214515d0ef3f9ff99b06f4d2702acf0380cab7ccc5e', 'sent': 81},

          ]


        """#

        repl=dataFrom777.json()

        Numnxtaccts = repl['Numnxtaccts']
        peers = repl['peers']
        Numpservers = repl['Numpservers']
        num = repl['num']
        log.msg("Numnxtaccts", Numnxtaccts)
        #log.msg("peers", peers)
        log.msg("Numpservers", Numpservers)
        log.msg("num", num)

        reqFindnode = {'requestType':'findnode'}


        log.msg(1*"\n rpl777_df1_getpeers & peers all:")#, peers, type(peers))


        for peer in peers[2:]:
            #log.msg(5*"\n rpl777_df1_getpeers & PING all:", peer, type(peer))

            pserv = peer['pserver']
            srvNXT = peer['srvNXT']
            #log.msg(1*"\n FINDNODE peer:", srvNXT)
            reqFindnode['key']=srvNXT

            sleep(0.25)

            self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqFindnode), headers=POSTHEADERS)
            self.deferred.addCallback(self.rpl777_df3_findnode )
            self.deferred.addErrback(self.rpl777ERR)



#        GUIpoll ---> kademlia_pong {'result': '{"result":"kademlia_pong","tag":"","isMM":"0","NXT":"16451506450525369985","ipaddr":"92.222.160.77","port":0,"lag":"1904.809","numpings":1,"numpongs":1,"ave":"1269.872"}', 'args': '[{"requestType":"pong","NXT":"16451506450525369985","time":1419198740,"MMatrix":0,"yourip":"178.62.185.131","yourport":50472,"ipaddr":"92.222.160.77","pubkey":"b8b3105deb570c745e78edd43773b6183b76d000224ed9468b8a75b600ab0869","ver":"0.299"},{"token":"tdeh1ctof1f7832nmppjfl7d0387ceoohd3dijh2lc0bctca0lbd8q88a0p9j4g2qjknqf3kk5b11pn82epr79k05ibufjh00gjjuk4dvig0v2pk4ijoioir4ig6t8gesbq9h26ldr13r0bbvjbjq4922a0j79so"}]', 'from': '92.222.160.77', 'port': 0} <class 'dict'>

#>
#2014-12-21 22:53:52+0100 [-] GUIpoll entry--->   {'from': '167.114.2.205', 'result': '{"result":"kademlia_havenode from NXT.12315166155634751985 key.(13594896385051583735) value.([["13594896385051583735", "192.99.246.20", "56745", "1419123113"], ["12315166155634751985", "167.114.2.205", "55912", "0"], ["11634703838614499263", "69.90.132.106", "40225", "1419131956"], ["1978065578067355462", "89.212.19.49", "50444", "1419123113"], ["7108754351996134253", "167.114.2.171", "37131", "1419123116"], ["2131686659786462901", "178.62.185.131", "60626", "1419157351"], ["7837143510182070614", "62.194.6.163", "35416", "1419185505"]])"}', 'port': 0, 'args': '[{"requestType":"havenode","NXT":"12315166155634751985","time":1419198801,"key":"13594896385051583735","data":[["13594896385051583735", "192.99.246.20", "56745", "1419123113"], ["12315166155634751985", "167.114.2.205", "55912", "0"], ["11634703838614499263", "69.90.132.106", "40225", "1419131956"], ["1978065578067355462", "89.212.19.49", "50444", "1419123113"], ["7108754351996134253", "167.114.2.171", "37131", "1419123116"], ["2131686659786462901", "178.62.185.131", "60626", "1419157351"], ["7837143510182070614", "62.194.6.163", "35416", "1419185505"]]},{"token":"p2rlbsfesglcc3e55c6s6g2vbv57820quvnaq4avcfc36ub30lbh4eqo47s68dg2vc0mm449f5srp4rfndsuvvufj906o89mhid8am91sa4g6n45enqlkvg95vrjigl3ndf6s7hhbsl9bv8ap6c7nam0svi6va8s"}]'} <class 'dict'>






    def rpl777_df1_settings(self, dataFrom777): #these are the basic pings from the whitlist
        """"""#
        repl=dataFrom777.json()
        reqPing = {'requestType':'ping'}

        ipsToPing = repl['whitelist']



        #ipsToPing = 10*['88.179.105.82']   #  ['79.245.52.39']  #[ STONEFISH_IP] #[']  #['178.62.185.131'] # ["69.90.132.106"]

        log.msg("ping to whitelist:", len(ipsToPing))

        for node in ipsToPing:
            reqPing['destip']=node

            #log.msg("dumpStats: ",   self.serverFactory.reactor.threadpool.dumpStats())
            #log.msg("workers: ", tp.ThreadPool.workers)
            #
            # stat1 = len(self.serverFactory.reactor.threadpool.waiters)
            # stat2 = self.serverFactory.reactor.threadpool.workers
            # stat3 = len(self.serverFactory.reactor.threadpool.threads)
            # stat4 = len(self.serverFactory.reactor.threadpool.q.queue)
            #
            # log.msg("waiters: ", stat1)
            # log.msg("workers1: ", stat2)
            # log.msg("threads: ", stat3)
            # log.msg("queue: ", stat4)
            # log.msg("workers2: ", tp.ThreadPool.workers)

            sleep(0.25)

            log.msg("ping to whitelist:", reqPing['destip'])
            self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqPing), headers=POSTHEADERS)
            self.deferred.addCallback(self.rpl777_df2_ping)
            self.deferred.addErrback(self.rpl777ERR)


    def rpl777_df2_ping(self, dataFrom777):
        """


        """#
        repl=dataFrom777.json()
        repl=dataFrom777.content.decode("utf-8")
        repl=eval(repl)
        #log.msg( 1 * "ping sent", repl)



    def rpl777_df3_findnode(self, dataFrom777):
        repl=dataFrom777.json()
        log.msg("rpl777_df3_findnode",repl)



    def rpl777_GUIpoll_kademlia_store(self, rpl777): #dataFrom777):
        pass


    def rpl777_GUIpoll_findnode(self, rpl777): #dataFrom777):
        """
        GUIpoll --->   {'result': '{"result":"kademlia_findnode from.(7067340061344084047) previp.(94.102.50.70) key.(2131686659786462901) datalen.0 txid.12611969529750120048"}', 'port': 0, 'from': '94.102.50.70', 'args': '[{"requestType":"findnode","NXT":"7067340061344084047","time":1418391191,"key":"2131686659786462901"},{"token":"197njl2bp54ijkjnfadmvua4irii342267l8taa4n53vqhg5v425eg3455h836g1in2v8sunh9j9mf4hnr7fmhsbdhsb8qk1kp18m6a77gq0d6s57151c1mejh29j3fcpg3jsvidjkbva8g896hjbss5ub7482ms"}]'} <class 'dict'>
        GUIpoll --->   {'from': '167.114.2.171', 'result': '{"result":"kademlia_findnode from.(7108754351996134253) previp.(167.114.2.171) key.(2131686659786462901) datalen.0 txid.14645060032929148909"}', 'port': 0, 'args': '[{"requestType":"findnode","NXT":"7108754351996134253","time":1418320475,"key":"2131686659786462901"},{"token":"j8edkcsu69k3e3e0ru9p4f6fepega7dijt24dh71h9kfqsg6uvo1ovp37gquc4g1ssnvc81804v9pipdo8al5iihmpmls4n9ici5hbe5m0rgveg8fek61lpihnn5k9cne28m9p8b71o918vkeelei1lpaljpn8n4"}]'} <class 'dict'>
        """#
        #log.msg("GUIpoll ---> rpl777_GUIpoll_findnode",rpl777, type(rpl777),"\n")
        pass
        note=""" here we can answer with a findnode or a ping """



    def rpl777_GUIpoll_kademlia_pong(self, rpl777): #dataFrom777):
        """

This catches ALL pings as PONGs - see PONG details in snAppy_doku

        """#
        log.msg(1*"\nGUIpoll ---> kademlia_pong",rpl777, type(rpl777),"\n")
        try:
            fromIp = rpl777['from']
            port = rpl777['port']
            args = rpl777['args']
            #log.msg(args, type(args))
            rpl777 = rpl777['result'] # this is a string!
            rpl777 = json.loads(rpl777)

        except Exception as e:
            #log.msg("GUIpoll ---> kademlia_pong",rpl777, type(rpl777),"\n")
            log.msg("Error rpl777_GUIpoll_kademlia_pong {0}".format(str(e)))

        try:
            rplArgs = json.loads(args) # <class 'list'> !!
            rplArgsRQ = rplArgs[0] # <class 'dict'>
            rplArgsTK = rplArgs[1]   #<class 'dict'>
        except Exception as e:
            log.msg("Error rpl777_GUIpoll_kademlia_pong {0}".format(str(e)))

        try:
            #log.msg(1*"\n~~~~ rplArgsRQ", rplArgsRQ)
            pubkey= rplArgsRQ['pubkey'] # check that this is really pubkey and not DHT key
            requestType= rplArgsRQ['requestType']
            ver =rplArgsRQ['ver']
            yourip =rplArgsRQ['yourip']
            yourport =rplArgsRQ['yourport']

            NXT =rplArgsRQ['NXT']
            time =rplArgsRQ['time']
            ipaddr =rplArgsRQ['ipaddr']

        except Exception as e:
            log.msg("GUIpoll ---> kademlia_pong",rpl777, type(rpl777),"\n")
            log.msg("Error rplArgsRQ {0}".format(str(e)))

        try:
            port =  rpl777['port']
            numpings =  rpl777['numpings']
            lag  =  rpl777['lag']
            ipaddr  = rpl777['ipaddr']
            numpongs =  rpl777['numpongs']
            result =   rpl777['result']
            ave  =  rpl777['ave']
            NXT  = rpl777['NXT']
            log.msg("rpl777", rpl777,type(rpl777))

        except Exception as e:
            #log.msg("GUIpoll ---> kademlia_pong",rpl777, type(rpl777),"\n")
            log.msg("Error rpl777 {0}".format(str(e)))

        # further ACTION from here
        note= """ from here, we can go the next step, which is the findnode   """
        reqFindnode = {'requestType':'findnode'}
        reqFindnode['key']= NXT # the rea conf will be the havenode in uipoll
        self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqFindnode), headers=POSTHEADERS)
        self.deferred.addCallback(self.rpl777_df3_findnode ) # this is just for conf that we sent it
        self.deferred.addErrback(self.rpl777ERR)




    def rpl777_GUIpoll_kademlia_havenode(self, rpl777):
        """

    """#

        #log.msg("GUIpoll ---> kademlia_havenode",rpl777, type(rpl777),"\n")
        log.msg("GUIpoll ---> kademlia_havenode from ",rpl777['from'])

        try:
            fromIp = rpl777['from']
            port = rpl777['port']
            rplArgs = rpl777['args']
            result = rpl777['result'] #'result': '{"result":"kademlia_havenode from NXT.13594896385051583735 key.(1978065578067355462) value.([["1978065578067355462", "89.212.19.49", "7777", "1418404057"], ["4
            # result is the internal raw string part
            try:
                rplArgsLi=json.loads(rplArgs)
                token = rplArgsLi[1]
                rplArgs = rplArgsLi[0]
                fromNXT = rplArgs['NXT']
                requestType = rplArgs['requestType']
                data = rplArgs['data']
                key = rplArgs['key']
                time = rplArgs['time']
                peersList = rplArgs['data']

            except Exception as e:
                log.msg("Error args {0}".format(str(e)))
                log.msg("args NOT ok",rplArgs, type(rplArgs))

            try:
                rpl777 = rpl777['result'] # this is a string!
            except Exception as e:
                log.msg("Error args {0}".format(str(e)))
                log.msg("rpl777 NOT ok",rpl777, type(rpl777))

            #log.msg("\nGUIpoll -+--> kademlia_havenode rpl777",rpl777, type(rpl777),"\n")

        except Exception as e:
            #log.msg("GUIpoll ---> kademlia_pong",rpl777, type(rpl777),"\n")
            log.msg("Error rpl777_GUIpoll_kademlia_havenode >>> {0}".format(str(e)))


        def msg():
            msg = ''
            for frag in range(randint(4,7)):
                msg +=  self.MSGfrags[randint(0,7)]
            return msg

        log.msg(1*"num peers in peersList", len(peersList))




        for peer in peersList:

            self.peersDiLoc[peer[1]] = peer[0] # add this to the internal list of known nodes
            #log.msg(1*"\n NEW msg FOR LOCAL peer:", peer)
            self.RQsendmsg['dest'] = peer[0] #'16451506450525369985'    # peer[0]


          #  if peer[1] == '79.245.52.39':  # '88.179.105.82': # '178.62.185.131': #'62.194.6.163': '88.179.105.82
          #      for sp in range(10):
            log.msg(1*"\n NEW msg FOR LOCAL peer:", peer)

            spam = msg()

            self.RQsendmsg['msg'] = spam

            stat1 = len(self.serverFactory.reactor.threadpool.waiters)
            stat2 = self.serverFactory.reactor.threadpool.workers
            stat3 = len(self.serverFactory.reactor.threadpool.threads)
            stat4 = len(self.serverFactory.reactor.threadpool.q.queue)

            log.msg("waiters: ", stat1)
            log.msg("workers1: ", stat2)
            log.msg("threads: ", stat3)
            log.msg("queue: ", stat4)
            log.msg("workers2: ", tp.ThreadPool.workers)

            sleep(0.25)
            self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(self.RQsendmsg), headers=POSTHEADERS)
            self.deferred.addCallback(self.rpl777_sndMSG ) # this is just for conf that we sent it
            self.deferred.addErrback(self.rpl777ERR)





    def rpl777_sndMSG(self, dataFrom777):
        rpl777=dataFrom777.json()
        print("rpl777_sndMSG SENT!!!", rpl777, type(rpl777))

        if self.numCalls > 5:
            self.superNET_daemon.stopUC4(True)


    def rpl777ERR(self, ERR777):
        log.msg("ERR777 1", ERR777, type(ERR777)) #.printDetailedTraceback())
        log.msg("ERR777 2", ERR777.value, type(ERR777.value)) #.printDetailedTraceback())

        #raise RuntimeError(ERR777.printDetailedTraceback())
















class UC_Scheduler_XML(object):
    """
    demo for xml. fetches three hardcoded xml oages from sportsdatallc.

    """#

    def __init__(self, serverFactory ,  environ = {} ):

        # ToDo: the schedules and their details must be registered in the ENVIROINMENT! - including the filenames where they go to
        #
        self.environ = environ
        self.schedules = {} #schedules # this contains the schedules

        prepSchedules = environ['envSportsData']
        for sched in prepSchedules.keys():
            sched = prepSchedules[sched]
            self.schedules[ sched['schedName']   ] = Schedule( sched )

        self.proxyServerFactory = serverFactory #probably not needed

        self.ucFactory = ClientFactory()

        self.qComp_XML = serverFactory.qComp_XML
        self.parser_XML = serverFactory.parser_XML
        # self.schedulerProtocol_XML = SchedulerProtocol_XML(self)
        # this probably only gets me ONE self.schedulerProtocol_XML ONLY! ?!?!



    def periodic(self, ):
        """ this is the method that is called periodically by the twisted loopingTask.
         This contains the UseCase logic, ie needs to check what to do, and then do it. """#

        scheduledReqs =[]
        #print( "Scheduler ", self, " MAIN scheduled Heartbeat: ", datetime.now())

        for schedule in self.schedules.keys():
            schedule = self.schedules[schedule]

            if schedule.callMe():
                scheduledReqs.append(schedule)

        self.makeScheduledRequests(scheduledReqs)


    def makeScheduledRequests(self,scheduledReqs):

        for req in scheduledReqs:

            sleep(0.25) # constraint on demo account sportsdataLLC
            requestOUT = req.schedule['target'].encode("utf-8")
            #
            self.uc_Factory = ClientFactory()
            self.uc_Factory.protocol = SchedulerProtocol_XML()
            self.uc_Factory.protocol.connectionMade(requestOUT)
            #self.schedulerProtocol_XML.connectionMade(requestOUT)# only using a proto may yield errs?!


    def receiveFromProtocol(self, dataFromProto):

        print(1 * "\nscheduled refresh of data here. update to file by saving it")
        self.result = dataFromProto
        log.msg(1 * "----> **** SchedulerProtocol_XML dataReceived - from remoteServer: ", dataFromProto[:200], str(len(dataFromProto)),"\n-----",time.time(),"\n\n")
        # ToDo SAVE HERE TO FILES- look up files in environ


# ENABLE THE SCHEDULERS TO OPERATE THE SERVERFACTORY JUST AS REQUESTS
# make a new class for each scheduler.
# maybe later concentrae functionality in a superclass to be subclassed





#
#
# class SchedulerProtocol_777(protocol.Protocol):
#     """ this can be used for scheduled SuperNET tasks
#     """#
#
#     def __init__(self,  scheduler):
#         super(SchedulerProtocol_777, self).__init__()
#         self.scheduler = scheduler
#
#
#     def connectionMade(self, requestOUT = None):
#         """ connection made here means that we are called by the scheduler  """#
#         print(1*"\n++++++++++SchedulerProtocol_777 connectionMade - Scheduled Check")
#         try:
#             self.requestOUT = requestOUT
#         except:
#             self.transport.loseConnection()
#             return None
#         self.getPage_deferred =  getPage(self.requestOUT)
#         print(1*"\n++++++++++SchedulerProtocol_777 connectionMade - Scheduled Check", self.requestOUT)
#         self.getPage_deferred.addCallback(self.pageReceived)
#         self.getPage_deferred.addErrback(self.handleFailure)
#         self.requestOUT = ''
#
#     # Server => Proxy
#     def handleFailure(self, err):
#         raise RuntimeError(str(err))
#
#     # this will be the deferreed
#     def pageReceived(self, data):
#         log.msg(1*"\n scheduled pageReceived - from remoteServer: ", data[:200], str(len(data)),"\n\n")
#         self.scheduler.receiveFromProtocol(data)
#         return None









class SchedulerProtocol_XML(protocol.Protocol):
    """
    This works but there is a number of things I am unsure about.
        I don't know if this is a singleton or throwaway Proto like with the others.
        Also, I don't quite know about the contorl flow, I call a method on the scheduler to get rid of the data
        that has jus tbeen recevied, and I don't know if we ever get back in to the deferred 'pagereceived.
        Normally, Protocols use the 'loseConnection'. When I do this I get execptions because I jump out of here when throwing out the data,
        and the connection is not not closed. so if we just do it like this it may be hunky dory. lets see.
        Maybe it IS neccessary to loseconnection() ???? it does not appear so atm"""#

    def __init__(self,  ):#scheduler):
        super(SchedulerProtocol_XML, self).__init__()
        #self.scheduler = scheduler

# SchedulerProtocol_XML connectionMade:  None b'http://api.sportsdatallc.org/soccer-t2/eu/schema/matches-schedule.xml?api_key=fv37s4rd2arqqxav774wb2kc'

    def connectionMade(self, requestOUT ):
        """ connection made here means that we are called by the scheduler  """#
        print(10*"\nSchedulerProtocol_XML connectionMade: ", requestOUT, self )
        try:
            self.requestOUT = requestOUT
        except:
            self.transport.loseConnection()
            return None

        self.getPage_deferred =  getPage(self.requestOUT)
        print(3*"\nSchedulerProtocol_XML connectionMade - Scheduled Check", self.requestOUT)

        self.getPage_deferred.addCallback(self.pageReceived)
        self.getPage_deferred.addErrback(self.handleFailure)
        self.requestOUT = ''
        self.query_xmlFeed1 = False
        #log.msg("-SchedulerProtocol_XML-- sending scheduled request out----->:", self.requestOUT) # only for GET , ppOST is different

    # Server => Proxy
    def handleFailure(self, err):
        raise RuntimeError(str(err))

    # this will be the deferreed
    def pageReceived(self, data):
        log.msg(12*"\n scheduled pageReceived - from remoteServer: ", data[:1200], str(len(data)),"\n\n")
        #self.scheduler.receiveFromProtocol(data)
        #b'http://api.sportsdatallc.org/soccer-t2/eu/matches/2014/08/21/summary.xml?api_key=fv37s4rd2arqqxav774wb2kc'>
        return None










#
#
#
# class UCsched_1(object):
#
#
#     """
#
#
#
# settings - ping whitelist
#
# this also documents the api call params and return values
#
#
#
#     """#
#
#
#     def __init__(self, serverFactory , environ = {} ): # prepSchedules = {},
#
#
#
#         self.environ = environ
#         self.schedules = {}    # this contains the schedules
#
#         prepSchedules = environ['UCsched_1'] # create a schedule in snAppyConfig.py !!!
#         for sched in prepSchedules.keys():
#             sched = prepSchedules[sched]
#             self.schedules[ sched['schedName']] = Schedule( sched )
#
#         self.lastCallTime = int(time.time() * 1000)
#
#
#     def periodic(self, ):
#         """ this is the method that is called periodically by the twisted loopingTask.
#          This contains the UseCase logic, ie needs to check what to do, and then do it. """#
#
#         schedulesDue =[]
#         #print( "Scheduler ", self, " MAIN scheduled Heartbeat: ", datetime.now())
#
#         for schedule in self.schedules.keys():
#             schedule = self.schedules[schedule]
#
#             if schedule.callMe():
#                 schedulesDue.append(schedule)
#
#         self.runSchedules(schedulesDue)
#
#
#     def runSchedules(self,schedulesDue):
#
#
# #
# # RUN GUIPOLL HERE ON A FASTER SCHEDULE THAN THE PAYLOAD CALLS!
# #
# #
#
#         for schedDue in schedulesDue:
#             if 'uc_settings' in schedDue.SNrequests.keys():
#                 reqData = schedDue.SNrequests['uc_settings']
#                 self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqData), headers=POSTHEADERS)
#                 self.deferred.addCallback(self.rpl777_df1)
#                 self.deferred.addErrback(self.rpl777ERR)
#             elif 'SPAM' == 'EGGS':
#                 pass
#     #
#     # cascading deferreds here!
#     #
#     def rpl777_df1(self, dataFrom777):
#         """"""#
#         repl=dataFrom777.json()
#         reqPing = {'requestType':'ping'}
#
#         ipsToPing=repl['whitelist'] #[0] # singlecheck
#         #ipsToPing = 10* ['178.62.185.131'] # stonefish['80.41.56.181'] # ['85.178.202.108']   #
#
#         for node in ipsToPing:
#             reqPing['destip']=node
#             self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqPing), headers=POSTHEADERS)
#             self.deferred.addCallback(self.rpl777_df2)
#             self.deferred.addErrback(self.rpl777ERR)
#
#
#     def rpl777_df2(self, dataFrom777):
#         """"""#
#         repl=dataFrom777.json()
#         #log.msg( 1 * "\n---->rpl777 ping", dataFrom777)
#         repl=dataFrom777.content.decode("utf-8")
#         repl=eval(repl)
#         # for se in repl:
#         #     print(se,repl[se]) #85.178.200.167
#
#         reqGUIpoll = {'requestType':'GUIpoll'}
#
#         self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqGUIpoll), headers=POSTHEADERS)
#         self.deferred.addCallback(self.rpl777_df3)
#         self.deferred.addErrback(self.rpl777ERR)
#
#
#
#     def rpl777_df3(self, dataFrom777):
#         """
#         Note : Use python assert in the future
#                 Use parse and format for the strings!
#
#         """#
#
#         if dataFrom777.content == b'{"result":"nothing pending"}':
#             return {"result":"nothing pending"}
#
#         #log.msg( 1 * "\n---->rpl777 GUIpoll", dataFrom777, type(dataFrom777))
#         #log.msg( 1 * "\n---->rpl777 GUIpoll", dataFrom777.content)
#
#         try:
#
#             repl=dataFrom777.content.decode("utf-8")
#             #repl=eval(repl)
#             repl = json.loads(repl)
#
#             # 1 decode bytes to utf8
#             # 2 eval to dict
#             # 3 separate dict into result, request, aux
#             # 4 repeat on request for [ result, token ]
#             # 5 repeat on result
#
#             # repl=dataFrom777.json() #.decode("utf-8")
#             # print("GUIpoll-->\n",repl)
#             # BEFORE EVAL: {"result":"{\"result\":\"kademlia_pong\",\"NXT\":\"3571143576961987768\",\"ipaddr\":\"89.212.19.49\",\"port\":0\",\"lag\":251.188,\"numpings\":13,\"numpongs\":11,\"ave\":1062.435\"}","from":"89.212.19.49","port":0,"args":"[{\"requestType\":\"pong\",\"NXT\":\"3571143576961987768\",\"time\":1417702487,\"yourip\":\"85.178.200.167\",\"yourport\":61234,\"ipaddr\":\"89.212.19.49\",\"pubkey\":\"30d02aec153a5b7c4e606c2f50b7ac9e71ca814328189cac288650af3d114c30\",\"ver\":\"0.199\"},{\"token\":\"2nm2lk1gc177ompqlirl0brc8e0skscu52m9o61824uquk46tq11ec2cjag7fso1hs074kct6vk905lfbvv512adh3rk6hfau383o9vfilrgd3d1telilup7sdnfuce7h0c8nsd2k1kq4ec361d4d3hmf5ae8egr\"}]"}
#             # print("GUIpoll-->\n",repl)
#             # after eval
#             # {'args': '[{"requestType":"pong","NXT":"3571143576961987768","time":1417702487,"yourip":"85.178.200.167","yourport":61234,"ipaddr":"89.212.19.49","pubkey":"30d02aec153a5b7c4e606c2f50b7ac9e71ca814328189cac288650af3d114c30","ver":"0.199"},{"token":"2nm2lk1gc177ompqlirl0brc8e0skscu52m9o61824uquk46tq11ec2cjag7fso1hs074kct6vk905lfbvv512adh3rk6hfau383o9vfilrgd3d1telilup7sdnfuce7h0c8nsd2k1kq4ec361d4d3hmf5ae8egr"}]', 'port': 0, 'result': '{"result":"kademlia_pong","NXT":"3571143576961987768","ipaddr":"89.212.19.49","port":0","lag":251.188,"numpings":13,"numpongs":11,"ave":1062.435"}', 'from': '89.212.19.49'}
#
#             try:
#                 resultFull = repl['result']
#
#             except:
#                 resultFull = {'result': 'no_Result_contained'}
#                 log.msg(resultFull)
#                 return {'result': 'no_Result_contained'}
#             try:
#                 origRequest = repl['args']
#             except:
#                 origRequest= ({"requestType":'0'}, {"token": '0'})
#             try:
#                 fromPort = repl['port']
#             except:
#                 fromPort = 0
#             try:
#                 fromIp = repl['from']
#             except:
#                 fromIp = '0'
#
#             #print("args", args )
#             #print("args type", type(args))
#
#             try:
#                 origRequest=origRequest.lstrip('[')
#                 origRequest=origRequest.rstrip(']')
#                 fullRequest = origRequest.split('},{')[0] + '}'
#                 token =   '{'+ origRequest.split('},{')[1]
#                 # log.msg(fullRequest,type(fullRequest))#
#                 # log.msg(token,type(token))#
#                 token = json.loads(token)
#                 fullRequest = json.loads(fullRequest)
#
#
#                 print(fullRequest, type(fullRequest))
#
#                 # this eval produces a TUPLE?!?!      yes: '[ {origRequest:origRequest} , {token:token} ]' !!!!!
#             except:
#                 #log.msg("problem with extracting args")#
#                 origRequest={'no':'args'}
#                 token = {'token':'NONE'}
#
#
#  #{"result":"kademlia_havenode from NXT.5624143003089008155 key.(5624143003089008155) value.([["5624143003089008155", "192.99.212.250", "7777", "0"], ["15178638394924629506", "167.114.2.206", "7777", "1417435953"], ["6249611027680999354", "80.41.56.181", "7777", "1417449705"], ["11910135804814382998", "167.114.2.94", "7777", "1417435991"], ["7581814105672729429", "187.153.194.200", "29693", "1417652256"], ["7108754351996134253", "167.114.2.171", "7777", "1417435991"], ["16196432036059823401", "167.114.2.203", "7777", "1417435957"]])"}
#
# # {"result":"kademlia_havenode from NXT.5624143003089008155 key.(5624143003089008155) value.([["5624143003089008155", "192.99.212.250", "7777", "0"], ["15178638394924629506", "167.114.2.206", "7777", "1417435953"], ["6249611027680999354", "80.41.56.181", "7777", "1417449705"], ["11910135804814382998", "167.114.2.94", "7777", "1417435991"], ["7581814105672729429", "187.153.194.200", "29693", "1417652256"], ["16196432036059823401", "167.114.2.203", "7777", "1417435957"], ["7108754351996134253", "167.114.2.171", "7777", "1417435991"]])"}
#             try:
#                 #log.msg("\n",fullRequest,"\n",)
#                 pubkey= fullRequest['pubkey'] # check that this is really pubkey and not DHT key
#                 requestType= fullRequest['requestType']
#                 ver =fullRequest['ver']
#                 yourip =fullRequest['yourip']
#                 yourport =fullRequest['yourport']
#
#                 NXT =fullRequest['NXT']
#                 time =fullRequest['time']
#                 ipaddr =fullRequest['ipaddr']
#
#
#             except Exception as e:
#                 print("Error parsing fullRequest:  {0}".format(str(e)))
#                 #log.msg("problem with extracting fullRequest")#,fullRequest, type(fullRequest))
#                 fullRequest =  { "requestType" : "0" }
#
# # result :
# # {"result":"kademlia_havenode from NXT.8894667849638377372 key.(10694781281555936856) value.([["10694781281555936856", "209.126.70.170", "7777", "1417935711"], ["11910135804814382998", "167.114.2.94", "7777", "1417934979"], ["8894667849638377372", "209.126.70.156", "7777", "0"], ["6216883599460291148", "192.99.246.126", "7777", "1417935166"], ["15178638394924629506", "167.114.2.206", "7777", "1417934954"], ["13594896385051583735", "192.99.246.20", "7777", "1417934951"], ["2131686659786462901", "178.62.185.131", "7777", "1417943077"]])"}
#
#
#             try:
#                 #resultFull = eval(resultFull) #<------------- YES this is a str too!
#                 resultFull = json.loads(resultFull) #<------------- YES this is a str too!
#
#                 port =  resultFull['port']
#                 numpings =  resultFull['numpings']
#                 lag  =  resultFull['lag']
#                 ipaddr  = resultFull['ipaddr']
#                 numpongs =  resultFull['numpongs']
#                 result =   resultFull['result']
#                 ave  =  resultFull['ave']
#                 NXT  = resultFull['NXT']
#                 #log.msg("resultFull", resultFull,type(resultFull))
#
#
#             except:
#                 log.msg("resultFull oops- wrong GUIpoll!:", resultFull,type(resultFull) )
#                 resultFull={'wrong':'poll'}
#                 #log.msg(resultFull,type(resultFull) )
#
#
#
#             ptt_PONG = {
#                             'fullRequest': fullRequest , \
#                             "token":token  ,\
#                             'result':resultFull,\
#                             'fromPort':fromPort,\
#                             'fromIp' : fromIp
#                             }
#
#             print(3*"---------------*") #\n")
#             for key in ptt_PONG.keys():
#
#
#                 if key == 'result':
#                     for keyR in ptt_PONG[key].keys():
#                         print( keyR, " - ",ptt_PONG[key][keyR])
#                     continue
#                 print(1*"\n")
#                 if key == 'fullRequest':
#                     for keyR in ptt_PONG[key].keys():
#                         print( keyR, " - ",ptt_PONG[key][keyR])
#                     continue
#
#                 print("\n", key, " - ",ptt_PONG[key], "\n")
#
#
#
#         except Exception as e:
#             print("Error {0}".format(str(e)))
#
#
#
#     def rpl777ERR(self, ERR777):
#
#         log.msg("ERR777", ERR777.printDetailedTraceback())
#         #raise RuntimeError(ERR777.printDetailedTraceback())
#
#
