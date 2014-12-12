#!/usr/bin/python3
# -*- coding: utf-8 -*-


from twisted.internet import protocol #, # ClientFactory
from twisted.internet.protocol  import ClientFactory

from twisted.python import log
from twisted.web.client import getPage
from datetime import datetime
import json
import requests
from twisted.internet.threads import deferToThread
import time
from snAppyModules.snAppyConfig import *
#from requests import Request, Session
#from twisted.internet.defer import Deferred
from twisted.internet.protocol import ClientFactory, ServerFactory




class Schedule(object):
    """ container class to contain schedule info for each cached data feed
        This gets the simpl dicts from the snApiConfig module"""#
    def __init__(self, schedule, ):

        self.schedule = schedule
        self.callFreq = schedule['callFreq']
        self.SNrequests = schedule['SNreqTypes']

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







class UC_templateEXAMPLE(object):

    """

each UC can have MULTIPLE schedule timers!
each schedule timer can init different conditional request sequences of deferreds!
each t
        This handles scheduled tasks such as pulling XML data to update the local cache.


        We enter the Scheduled DATA by way of a structure form instantiation to be more flexible.

        A single schedule needs a name, a callFreq and a target. Then multiple schedules can be wrapped into an outer schedules dict.
        from this they are unwrapped here and the Scheduler instance can serve multiple schedules.

        So Schedulers have a callFreq, and Schedules have their own callFreq.

    Note: schedulers can use different methods to do their deferred work:
    1: use a client proxy to get stuff from the internet,
    2: use a simple deferredToThread to do local things like caching or SuperNET communication
    3: SuperNET controller apps have their business logic in classes of this type.

    Schedulers that use deferToThread do NOT need a Protocol!
    But a protocol CAN be used to organize internal logic.


    DESIGN:

    This allows to run MULTIPLPE timer schedules in ONE useCase!

    It may be better to build tailor made classes for specific tests and UCs
    instead of using one class and feed different schedules to it.

    These can either instantiate their own custom client protocols,
    or they can use the standard protocols that are provided in the main serveFactory.

    Or they don't use protocols at all.

    Many UCs will use cascading calls where the reply sequence is UC specific.
    Hence, it is better to make a Scheduler class for each UC,
    and use cascading deferreds to implement the use case logic.

    Thes UCs can be made with or without PROTOCOL/FACTORY.
    A Protocol provides a transport layer AND a deferred.
    When using python.requests, we do the transport and the deferred ourselves here.
    Both seems possible. Don't know if one is always better, so let's try both.

    """#
    def __init__(self, serverFactory , environ = {} ): # prepSchedules = {},

        self.environ = environ
        self.schedules = {}    # this contains the schedules


        #
        # This is just a template. If needed, all kind of things can be hardcoded into the UC class!
        # This provides facilities to take the schedules (PLURAL!) from the config,
        # and reqTypes if it is better to have those in the config.
        # can introduce the schedules explicitly here!!
        # because the UC classes do contain explicit and hard coded UC logic,
        # they can also unpack their schedules here explicitly!

        prepSchedules = environ['template'] # create a schedule in snAppyConfig.py !!!
        for sched in prepSchedules.keys():
            sched = prepSchedules[sched]
            self.schedules[ sched['schedName']   ] = Schedule( sched )

        self.lastCallTime = int(time.time() * 1000)
        # These obejcts may be used:
        # self.clientFactory = protocol.ClientFactory
        # self.qComp_777 = serverFactory.qComp_777
        # self.parser_777 = serverFactory.parser_777
        # self.parser_FOR_PRICEDATA = serverFactory.parser_FOR_PRICEDATA !!!!!!!!!!!!!!!!!!!!

        # we only keep the timers in the config file?!?!

    def periodic(self, ):
        """ this is the method that is called periodically by the twisted loopingTask.
         This contains the UseCase logic, ie needs to check what to do, and then do it. """#

        schedulesDue =[]
        print( "Scheduler ", self, " MAIN scheduled Heartbeat: ", datetime.now())

        for schedule in self.schedules.keys():
            schedule = self.schedules[schedule]

            if schedule.callMe():
                schedulesDue.append(schedule)



    def runSchedules(self,schedulesDue):

        for schedDue in schedulesDue:
            if 'uc1Start_settings' in schedDue.SNrequests.keys():
                reqData = schedDue.SNrequests['uc1Start_settings']
                self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqData), headers=POSTHEADERS)
                self.deferred.addCallback(self.rpl777_df1)
                self.deferred.addErrback(self.rpl777ERR)
            elif 'SPAM' == 'EGGS':
                pass
    #
    #
    # cascading deferreds here!
    #
    def rpl777_df1(self, dataFrom777):
        """ These deferreds are UseCase specific!  """#
        repl=dataFrom777.json()
        next_req_we_want_to_do_in_df1 =    {'requestType':'ping'}

        for thing in repl['whitelist']:
            next_req_we_want_to_do_in_df1['destip'] = thing
            self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(next_req_we_want_to_do_in_df1), headers=POSTHEADERS)
            self.deferred.addCallback(self.rpl777_df2)
            self.deferred.addErrback(self.rpl777ERR)

    def rpl777_df2(self, dataFrom777):

        # we do not have any requester to give anything back to.
        # either another part of the use case or just dump to screen or file.
        print( 1 * "\n---->rpl777 deferred here", dataFrom777)
        repl = dataFrom777.content.decode("utf-8")
        repl=eval(repl)
        for se in repl:
            print(se,repl[se])
        # etc
        #
        # from here we can continue with findnode etc
        #
        #

        ####################################################################
        # Important NOTE:
        # IT IS ALSO POSSIBLE TO MAKE CALLBACKS THAT CALL THEMSELVES!
        # this quickly degrades, BUT_ it can be done with an exit condition!
        #####################################################################


    def rpl777ERR(self, ERR777):
        raise RuntimeError

















##########################################################





class UCTEST_1_ping_whitelist_777(object):

    """



settings - ping whitelist

this also documents the api call params and return values



    """#


    def __init__(self, serverFactory , environ = {} ): # prepSchedules = {},

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



        self.environ = environ
        self.schedules = {}    # this contains the schedules

        prepSchedules = environ['UCTEST_1_ping_whitelist_777'] # create a schedule in snAppyConfig.py !!!
        for sched in prepSchedules.keys():
            sched = prepSchedules[sched]
            self.schedules[ sched['schedName']] = Schedule( sched )

        self.lastCallTime = int(time.time() * 1000)


    def periodic(self, ):
        """ this is the method that is called periodically by the twisted loopingTask.
         This contains the UseCase logic, ie needs to check what to do, and then do it. """#

        schedulesDue =[]
        #print( "Scheduler ", self, " MAIN scheduled Heartbeat: ", datetime.now())

        for schedule in self.schedules.keys():
            schedule = self.schedules[schedule]

            if schedule.callMe():
                schedulesDue.append(schedule)

        self.runSchedules(schedulesDue)


    def runSchedules(self,schedulesDue):


#
# RUN GUIPOLL HERE ON A FASTER SCHEDULE THAN THE PAYLOAD CALLS!
#
#

        for schedDue in schedulesDue:
            if 'uc1Start_settings' in schedDue.SNrequests.keys():
                reqData = schedDue.SNrequests['uc1Start_settings']
                self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqData), headers=POSTHEADERS)
                self.deferred.addCallback(self.rpl777_df1)
                self.deferred.addErrback(self.rpl777ERR)
            elif 'SPAM' == 'EGGS':
                pass
    #
    # cascading deferreds here!
    #
    def rpl777_df1(self, dataFrom777):
        """"""#
        repl=dataFrom777.json()
        reqPing = {'requestType':'ping'}

        ipsToPing=repl['whitelist'] #[0] # singlecheck
        #ipsToPing = 10* ['178.62.185.131'] # stonefish['80.41.56.181'] # ['85.178.202.108']   #

        for node in ipsToPing:
            reqPing['destip']=node
            self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqPing), headers=POSTHEADERS)
            self.deferred.addCallback(self.rpl777_df2)
            self.deferred.addErrback(self.rpl777ERR)


    def rpl777_df2(self, dataFrom777):
        """"""#
        repl=dataFrom777.json()
        #log.msg( 1 * "\n---->rpl777 ping", dataFrom777)
        repl=dataFrom777.content.decode("utf-8")
        repl=eval(repl)
        # for se in repl:
        #     print(se,repl[se]) #85.178.200.167

        reqGUIpoll = {'requestType':'GUIpoll'}

        self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqGUIpoll), headers=POSTHEADERS)
        self.deferred.addCallback(self.rpl777_df3)
        self.deferred.addErrback(self.rpl777ERR)



    def rpl777_df3(self, dataFrom777):
        """
        Note : Use python assert in the future
                Use parse and format for the strings!

        """#

        if dataFrom777.content == b'{"result":"nothing pending"}':
            return {"result":"nothing pending"}

        #log.msg( 1 * "\n---->rpl777 GUIpoll", dataFrom777, type(dataFrom777))
        #log.msg( 1 * "\n---->rpl777 GUIpoll", dataFrom777.content)

        try:

            repl=dataFrom777.content.decode("utf-8")
            #repl=eval(repl)
            repl = json.loads(repl)

            # 1 decode bytes to utf8
            # 2 eval to dict
            # 3 separate dict into result, request, aux
            # 4 repeat on request for [ result, token ]
            # 5 repeat on result

            # repl=dataFrom777.json() #.decode("utf-8")
            # print("GUIpoll-->\n",repl)
            # BEFORE EVAL: {"result":"{\"result\":\"kademlia_pong\",\"NXT\":\"3571143576961987768\",\"ipaddr\":\"89.212.19.49\",\"port\":0\",\"lag\":251.188,\"numpings\":13,\"numpongs\":11,\"ave\":1062.435\"}","from":"89.212.19.49","port":0,"args":"[{\"requestType\":\"pong\",\"NXT\":\"3571143576961987768\",\"time\":1417702487,\"yourip\":\"85.178.200.167\",\"yourport\":61234,\"ipaddr\":\"89.212.19.49\",\"pubkey\":\"30d02aec153a5b7c4e606c2f50b7ac9e71ca814328189cac288650af3d114c30\",\"ver\":\"0.199\"},{\"token\":\"2nm2lk1gc177ompqlirl0brc8e0skscu52m9o61824uquk46tq11ec2cjag7fso1hs074kct6vk905lfbvv512adh3rk6hfau383o9vfilrgd3d1telilup7sdnfuce7h0c8nsd2k1kq4ec361d4d3hmf5ae8egr\"}]"}
            # print("GUIpoll-->\n",repl)
            # after eval
            # {'args': '[{"requestType":"pong","NXT":"3571143576961987768","time":1417702487,"yourip":"85.178.200.167","yourport":61234,"ipaddr":"89.212.19.49","pubkey":"30d02aec153a5b7c4e606c2f50b7ac9e71ca814328189cac288650af3d114c30","ver":"0.199"},{"token":"2nm2lk1gc177ompqlirl0brc8e0skscu52m9o61824uquk46tq11ec2cjag7fso1hs074kct6vk905lfbvv512adh3rk6hfau383o9vfilrgd3d1telilup7sdnfuce7h0c8nsd2k1kq4ec361d4d3hmf5ae8egr"}]', 'port': 0, 'result': '{"result":"kademlia_pong","NXT":"3571143576961987768","ipaddr":"89.212.19.49","port":0","lag":251.188,"numpings":13,"numpongs":11,"ave":1062.435"}', 'from': '89.212.19.49'}

            try:
                resultFull = repl['result']

            except:
                resultFull = {'result': 'no_Result_contained'}
                log.msg(resultFull)
                return {'result': 'no_Result_contained'}
            try:
                origRequest = repl['args']
            except:
                origRequest= ({"requestType":'0'}, {"token": '0'})
            try:
                fromPort = repl['port']
            except:
                fromPort = 0
            try:
                fromIp = repl['from']
            except:
                fromIp = '0'

            #print("args", args )
            #print("args type", type(args))

            try:
                origRequest=origRequest.lstrip('[')
                origRequest=origRequest.rstrip(']')
                fullRequest = origRequest.split('},{')[0] + '}'
                token =   '{'+ origRequest.split('},{')[1]
                # log.msg(fullRequest,type(fullRequest))#
                # log.msg(token,type(token))#
                token = json.loads(token)
                fullRequest = json.loads(fullRequest)


                print(fullRequest, type(fullRequest))

                # this eval produces a TUPLE?!?!      yes: '[ {origRequest:origRequest} , {token:token} ]' !!!!!
            except:
                #log.msg("problem with extracting args")#
                origRequest={'no':'args'}
                token = {'token':'NONE'}



# MAKE A GUIPOLL PARSER HERE
#
            #
            # after a really long time I giot a havendoe!
            #
            #
            #
            #

 #{"result":"kademlia_havenode from NXT.5624143003089008155 key.(5624143003089008155) value.([["5624143003089008155", "192.99.212.250", "7777", "0"], ["15178638394924629506", "167.114.2.206", "7777", "1417435953"], ["6249611027680999354", "80.41.56.181", "7777", "1417449705"], ["11910135804814382998", "167.114.2.94", "7777", "1417435991"], ["7581814105672729429", "187.153.194.200", "29693", "1417652256"], ["7108754351996134253", "167.114.2.171", "7777", "1417435991"], ["16196432036059823401", "167.114.2.203", "7777", "1417435957"]])"}

# {"result":"kademlia_havenode from NXT.5624143003089008155 key.(5624143003089008155) value.([["5624143003089008155", "192.99.212.250", "7777", "0"], ["15178638394924629506", "167.114.2.206", "7777", "1417435953"], ["6249611027680999354", "80.41.56.181", "7777", "1417449705"], ["11910135804814382998", "167.114.2.94", "7777", "1417435991"], ["7581814105672729429", "187.153.194.200", "29693", "1417652256"], ["16196432036059823401", "167.114.2.203", "7777", "1417435957"], ["7108754351996134253", "167.114.2.171", "7777", "1417435991"]])"}
            try:
                #log.msg("\n",fullRequest,"\n",)
                pubkey= fullRequest['pubkey'] # check that this is really pubkey and not DHT key
                requestType= fullRequest['requestType']
                ver =fullRequest['ver']
                yourip =fullRequest['yourip']
                yourport =fullRequest['yourport']

                NXT =fullRequest['NXT']
                time =fullRequest['time']
                ipaddr =fullRequest['ipaddr']


            except Exception as e:
                print("Error parsing fullRequest:  {0}".format(str(e)))
                #log.msg("problem with extracting fullRequest")#,fullRequest, type(fullRequest))
                fullRequest =  { "requestType" : "0" }

# result :
# {"result":"kademlia_havenode from NXT.8894667849638377372 key.(10694781281555936856) value.([["10694781281555936856", "209.126.70.170", "7777", "1417935711"], ["11910135804814382998", "167.114.2.94", "7777", "1417934979"], ["8894667849638377372", "209.126.70.156", "7777", "0"], ["6216883599460291148", "192.99.246.126", "7777", "1417935166"], ["15178638394924629506", "167.114.2.206", "7777", "1417934954"], ["13594896385051583735", "192.99.246.20", "7777", "1417934951"], ["2131686659786462901", "178.62.185.131", "7777", "1417943077"]])"}


            try:
                #resultFull = eval(resultFull) #<------------- YES this is a str too!
                resultFull = json.loads(resultFull) #<------------- YES this is a str too!

                port =  resultFull['port']
                numpings =  resultFull['numpings']
                lag  =  resultFull['lag']
                ipaddr  = resultFull['ipaddr']
                numpongs =  resultFull['numpongs']
                result =   resultFull['result']
                ave  =  resultFull['ave']
                NXT  = resultFull['NXT']
                #log.msg("resultFull", resultFull,type(resultFull))


            except:
                log.msg("resultFull oops- wrong GUIpoll!:", resultFull,type(resultFull) )
                resultFull={'wrong':'poll'}
                #log.msg(resultFull,type(resultFull) )



            ptt_PONG = {
                            'fullRequest': fullRequest , \
                            "token":token  ,\
                            'result':resultFull,\
                            'fromPort':fromPort,\
                            'fromIp' : fromIp
                            }

            print(3*"---------------*") #\n")
            for key in ptt_PONG.keys():


                if key == 'result':
                    for keyR in ptt_PONG[key].keys():
                        print( keyR, " - ",ptt_PONG[key][keyR])
                    continue
                print(1*"\n")
                if key == 'fullRequest':
                    for keyR in ptt_PONG[key].keys():
                        print( keyR, " - ",ptt_PONG[key][keyR])
                    continue

                print("\n", key, " - ",ptt_PONG[key], "\n")



        except Exception as e:
            print("Error {0}".format(str(e)))



    def rpl777ERR(self, ERR777):

        print(ERR777)

        raise RuntimeError





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





class UCTEST_2_ping_findnode(object):

    """



settings - ping whitelist and do findnode

this also documents the api call params and return values

differentiate two types of replies:

1- the replies that are given back by the SuperNET server regularly
2- the replies that are taken from the internal GUIpoll


    """#


    def __init__(self, serverFactory , environ = {} ): # prepSchedules = {},



        self.environ = environ
        self.schedules = {}    # this contains the schedules

        self.nodeDi = {}

        prepSchedules = environ['UCTEST_1_ping_whitelist_777'] # can use same as UC1 for now- extends it
        for sched in prepSchedules.keys():
            sched = prepSchedules[sched]
            self.schedules[ sched['schedName']] = Schedule( sched )

        self.lastCallTime = int(time.time() * 1000)


    def periodic(self, ):
        """ this is the method that is called periodically by the twisted loopingTask.
         This contains the UseCase logic, ie needs to check what to do, and then do it. """#

        schedulesDue =[]
        #print( "Scheduler ", self, " MAIN scheduled Heartbeat: ", datetime.now())

        for schedule in self.schedules.keys():
            schedule = self.schedules[schedule]

            if schedule.callMe():
                schedulesDue.append(schedule)

        self.runSchedules(schedulesDue)


    def runSchedules(self,schedulesDue):
        """ here we get through all the due schedules and call them on SuperNET server
             Here we explicitly check the name and send them to the first callback of their callback sequence."""#


        for schedDue in schedulesDue:
            if 'uc1Start_settings' in schedDue.SNrequests.keys():
                log.msg("ping: IPs ", self.nodeDi.keys())
                log.msg("ping: NXTs", self.nodeDi.values())


                reqData = schedDue.SNrequests['uc1Start_settings']
                self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqData), headers=POSTHEADERS)
                self.deferred.addCallback(self.rpl777_settings_df1)
                self.deferred.addErrback(self.rpl777ERR)

            elif 'GUIpoll' in schedDue.SNrequests.keys():
                log.msg("do GUIpoll")
                reqData = schedDue.SNrequests['GUIpoll'] # this has 0.9 sec
                self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqData), headers=POSTHEADERS)
                self.deferred.addCallback(self.rpl777_df0_GUIpoll)
                self.deferred.addErrback(self.rpl777ERR)




    def rpl777_df0_GUIpoll(self, dataFrom777):
        """
         Distribute to their processing points!

         list what we can catch here from the GUIpoll

        This is the jump point to direct the returns from GUIpoll to their specific parsing functions.
        The formats sometimes change, and the parsing is better done individually!
        This has been a source of confusion!

-------------------

kademlia_store




2014-12-12 15:01:06+0100 [-] do GUIpoll
2014-12-12 15:01:06+0100 [-] GUIpoll ---> kademlia_store {'result': '{"result":"kademlia_store","key":"5420018378925390393","data":"489b81f54869a9bd7986d5e938fecc5677fdd3f8d389ce2f5616f1927f602a725038a2457abd5ff58aa3b3245bbaf3342b6cf9dd08ea93a721727aac165a77c0b79c0b28080440350af365aa","len":76,"txid":"3283676187569738843"}', 'port': 0, 'from': '184.175.25.117', 'args': '[{"requestType":"store","NXT":"17265504311777286118","time":1418334721,"key":"5420018378925390393","data":76},{"token":"4sjc45u1mu6lfbkt4crqchc8440s7coei94dt438hvsn919qv0js487fatka3981br5ro6n0gcq4nq8b9c4q2ioj8d33sggln4uo7kafj61gf7nr5rp5q8q5o49becep1sjr6atj9ih4vhto8jfrn68vd24g6iol"}]'} <class 'dict'>




dataFrom777.json()

 {'from': '192.99.212.250', 'port': 0, 'result': '{"result":"kademlia_store","key":"9939847310395454864","data":"755bf9a38466d016c9874e8203bffe0886d1c2fdbaa97e2fe178d295107c684286e0bfdc21e713a63b149202752ad7a404e4e93800ee611514cce90ff79c6339c5b06516b23fdd746a8bd7cb","len":76,"txid":"0"}', 'args': '[{"requestType":"store","NXT":"5624143003089008155","time":1418374116,"key":"9939847310395454864","data":76},{"token":"vgh0rqnc1ggigvl7nms0aj0bsk1o1vomsvq0in066673i19hv30q83s4p1nbsgo18jalqgivg3561nrdnbm418ru848p3it67681citv13hg6i06stbon01l63o6pcnrivfnaiu19s1adscfqmbd70b8fvpfsnor"}]'} <class 'dict'>


replRes_kademlia_store = 'result': '{"result":"kademlia_store","key":"6714102804552450255","data":"1234","len":2,"txid":"0"}', 'args': '[{"requestType":"store","NXT":"104575166425568823","time":1418299946,"key":"6714102804552450255","data":2},{"token":"accfcmm2avpcc6155tba1pacdmamqnjiq07abeh8uqomcomtuufuk3gtm7rrkvo1f081du5lofoqdnal2rtq70ir6sp510thb2mo018nmsrg57k9fdl4ma77lq07up2l4jhj1328keng15rtuilpl9vp92mantdc"}]'

repl_1 = {
             'port': 0,
             'from': '184.175.25.117',
             'result': '{"result":"kademlia_store","key":"6714102804552450255","data":"1234","len":2,"txid":"0"}', 'args': '[{"requestType":"store","NXT":"104575166425568823","time":1418299946,"key":"6714102804552450255","data":2},{"token":"accfcmm2avpcc6155tba1pacdmamqnjiq07abeh8uqomcomtuufuk3gtm7rrkvo1f081du5lofoqdnal2rtq70ir6sp510thb2mo018nmsrg57k9fdl4ma77lq07up2l4jhj1328keng15rtuilpl9vp92mantdc"}]'

         }


-----------------------

kademlia_havenode


GUIpoll ---> kademlia_havenode {'result': '{"result":"kademlia_havenode from NXT.16196432036059823401 key.(16196432036059823401) value.([["16196432036059823401", "167.114.2.203", "7777", "0"], ["15178638394924629506", "167.114.2.206", "7777", "1418308962"], ["7108754351996134253", "167.114.2.171", "7777", "1418308926"], ["12315166155634751985", "167.114.2.205", "7777", "1418308932"], ["11634703838614499263", "69.90.132.106", "7777", "1418309115"], ["11910135804814382998", "167.114.2.94", "7777", "1418308909"], ["5624143003089008155", "192.99.212.250", "7777", "1418308915"]])"}', 'from': '167.114.2.203', 'port': 0, 'args': '[{"requestType":"havenode","NXT":"16196432036059823401","time":1418318194,"key":"16196432036059823401","data":[["16196432036059823401", "167.114.2.203", "7777", "0"], ["15178638394924629506", "167.114.2.206", "7777", "1418308962"], ["7108754351996134253", "167.114.2.171", "7777", "1418308926"], ["12315166155634751985", "167.114.2.205", "7777", "1418308932"], ["11634703838614499263", "69.90.132.106", "7777", "1418309115"], ["11910135804814382998", "167.114.2.94", "7777", "1418308909"], ["5624143003089008155", "192.99.212.250", "7777", "1418308915"]]},{"token":"ratb2fdulus9a3mr7nqvbseibjgnr0vnadt9vs0k8svpki0suvjj6go5j619p2816f3621bm9ncmp0auu5ojtoive3rp9tg5ecd8cv05pn10098dumvlvotqskq62339il35eo1tq8e304lioj4u80f88lc0ve5g"}]'} <class 'dict'>







----------------------

GUIpoll ---> findnode {'result': '{"result":"kademlia_findnode from.(7108754351996134253) previp.(167.114.2.171) key.(2131686659786462901) datalen.0 txid.4621598500260051131"}', 'from': '167.114.2.171', 'port': 0, 'args': '[{"requestType":"findnode","NXT":"7108754351996134253","time":1418318210,"key":"2131686659786462901"},{"token":"j8edkcsu69k3e3e0ru9p4f6fepega7dijt24dh71h9kfqsg6uvjk4vp3jm6i0m0101ag1me1dubc7cere1tmhahvcc11scjkbmv37ql6gm40vr3gem13gt7jt33l71ro32eu3c37kd90e51cddlb9tnb9eacmgu9"}]'} <class 'dict'>






parsing the GUIpoll is a two step process:

1  extract the standard contents and its standard sub contents
1
2
3
4
5

2 extract the specifics form the sub contents
details




         """#

        # test on string and send there!
        # maybe this can be done more elegant later, but probably not.

        #log.msg("GUIpoll entry--->  ",dataFrom777, type(dataFrom777),"\n")

        rpl777=dataFrom777.json()
        #log.msg("GUIpoll entry--->  ",rpl777, type(rpl777),"\n")

        if 'nothing pending' in str(rpl777):
            pass#log.msg("GUIpoll --->  ",rpl777, type(rpl777),"\n")

        elif 'kademlia_store' in str(rpl777):
            self.rpl777_GUIpoll_kademlia_store(rpl777)
            #log.msg("GUIpoll ---> kademlia_store",rpl777, type(rpl777),"\n")

        elif 'kademlia_pong' in str(rpl777):
            #log.msg("GUIpoll ---> kademlia_pong",rpl777, type(rpl777),"\n")
            self.rpl777_GUIpoll_kademlia_pong(rpl777)

        elif 'kademlia_havenode' in str(rpl777):
            #log.msg("GUIpoll ---> kademlia_havenode",rpl777, type(rpl777),"\n")
            self.rpl777_GUIpoll_kademlia_havenode(rpl777)

        elif 'kademlia_findnode' in str(rpl777):
            #log.msg("GUIpoll ---> findnode",rpl777, type(rpl777),"\n")
            self.rpl777_GUIpoll_findnode(rpl777)


        else:
            log.msg(20*"GUIpoll ---> CALL not caught yet: ",rpl777, type(rpl777),"\n")

        return 0







    def rpl777_GUIpoll_kademlia_store(self, rpl777): #dataFrom777):
        pass #print(5*"\n+++++rpl777_GUIpoll_kademlia_store ")






    def rpl777_GUIpoll_findnode(self, rpl777): #dataFrom777):
        """
        GUIpoll --->   {'result': '{"result":"kademlia_findnode from.(7067340061344084047) previp.(94.102.50.70) key.(2131686659786462901) datalen.0 txid.12611969529750120048"}', 'port': 0, 'from': '94.102.50.70', 'args': '[{"requestType":"findnode","NXT":"7067340061344084047","time":1418391191,"key":"2131686659786462901"},{"token":"197njl2bp54ijkjnfadmvua4irii342267l8taa4n53vqhg5v425eg3455h836g1in2v8sunh9j9mf4hnr7fmhsbdhsb8qk1kp18m6a77gq0d6s57151c1mejh29j3fcpg3jsvidjkbva8g896hjbss5ub7482ms"}]'} <class 'dict'>
        GUIpoll --->   {'from': '167.114.2.171', 'result': '{"result":"kademlia_findnode from.(7108754351996134253) previp.(167.114.2.171) key.(2131686659786462901) datalen.0 txid.14645060032929148909"}', 'port': 0, 'args': '[{"requestType":"findnode","NXT":"7108754351996134253","time":1418320475,"key":"2131686659786462901"},{"token":"j8edkcsu69k3e3e0ru9p4f6fepega7dijt24dh71h9kfqsg6uvo1ovp37gquc4g1ssnvc81804v9pipdo8al5iihmpmls4n9ici5hbe5m0rgveg8fek61lpihnn5k9cne28m9p8b71o918vkeelei1lpaljpn8n4"}]'} <class 'dict'>
        """#
        #log.msg("GUIpoll ---> rpl777_GUIpoll_findnode",rpl777, type(rpl777),"\n")
        pass
        note=""" here we can answer with a findnode or a ping """


 # rpl777_GUIpoll_findnode
 # # {
 # 'from': '167.114.2.94',
 # 'args': '[{"requestType":"findnode","NXT":"11910135804814382998","time":1418385453,"key":"2131686659786462901"},{"token":"crhllp9ko5ehtcf8j46plskln4hn2lkp2ph4kbm0e9edtp00v3muqttr8v90ma81pb3iaqaft4vb3qqp1739i4c98a41885d60ba3mpqd6mg78i8cf6nmp1fsdcrjpi1gs9beh4kvlpq5fq7nscmo6n6dsegr00v"}]',
 # 'port': 0,
 # 'result': '{"result":"kademlia_findnode from.(11910135804814382998) previp.(167.114.2.94) key.(2131686659786462901) datalen.0 txid.9930066001546457017"}'} <class 'dict'>



# INTERESTING!!

            # !! this seems to be a FINDNODE THAT HAS BEEN SENT BY ANOTHER NODE!!!!!!!
# 2014-12-12 11:11:56+0100 [-] GUIpoll ---> findnode {'port': 0, 'args': '[{"requestType":"findnode","NXT":"7067340061344084047","time":1418385386,"key":"2131686659786462901"},{"token":"197njl2bp54ijkjnfadmvua4irii342267l8taa4n53vqhg5v3mqkg34apub5o81hn53tomkpanlirnf8iabbf053v857igan717aumatom0ii2u9c0l5knsffje7n8ade3c3fn9i8eudqi9v3vimgovlquocbn2"}]', 'result': '{"result":"kademlia_findnode from.(7067340061344084047) previp.(94.102.50.70) key.(2131686659786462901) datalen.0 txid.6517719273900935436"}', 'from': '94.102.50.70'} <class 'dict'>
#




    def rpl777_GUIpoll_kademlia_pong(self, rpl777): #dataFrom777):
        """
        Note : Use python assert in the future
                Use parse and format for the strings!


@l8orre: if you get a findnode you will send the findnode to the nodes that are closer to dest

jl777 [12:10 PM]
all the samples are in the list

jl777 [12:10 PM]
this is the raw data

l8orre [12:11 PM]
ah ok so this is autonomous SUperNET server behaviour?

jl777 [12:11 PM]
I will add a field so you can get the open/high/low/close/ave per time period minute, 2 min, 5 min, 1hr etc



findnodes spawn more findnodes and also sends back a havenode

so 1 findnode can cascade through the network

@l8orre: now imagine the attacker's predicament!

only seeing 1400 byte encrypted packets without any visibility into the internals

args ok  [{'key': '6216883599460291148', 'requestType': 'havenode', 'data': [['6216883599460291148', '192.99.246.126', '7777', '0'], ['7067340061344084047', '94.102.50.70', '7777', '1418360786'], ['10694781281555936856', '209.126.70.170', '7777', '1418355574'], ['1978065578067355462', '89.212.19.49', '7777', '1418355275'], ['17265504311777286118', '184.175.25.117', '7777', '1418357608'], ['7108754351996134253', '167.114.2.171', '7777', '1418355385'], ['5624143003089008155', '192.99.212.250', '7777', '1418355291']], 'NXT': '6216883599460291148', 'time': 1418380319}, {'token': '7meqnnpffqh9272utch79ra8rvlih9mevl901qhml0phabmmv3cu07blu76g1681id5qgp3k8lsf9tqhv9glkk6i9u1fluohu919kb6qm8d0kpuk9af13dp684jud4u10iriovu36q2kj21l2js923v7tu6i02gf'}] <class 'list'>

confetti in a blizzard



that is the reeturn data


the nodes closest to the key you are searching for


maybe sender and receiver differences

the findnode call that is received by a node can be locally initiated or remotely


if locally started it is treated differently


for a remote, if it finds it, it returns a store for findvalue



otherwise it is sending back havenode or havenodeB

now when it sends back this havenode or havenodeB, it arrives back at the node that sent the find

so for the recipient of the find node, the result is havenode

to the sender of the find, it comes back as a new havenode command


----------------------
 GUIpoll ---> kademlia_pong

 {'result': '{"result":"kademlia_pong","tag":"","NXT":"10694781281555936856","ipaddr":"209.126.70.170","port":0,"lag":"408186.000","numpings":104,"numpongs":45,"ave":"122765.867"}', 'from': '209.126.70.170', 'port': 0, 'args': '[{"requestType":"pong","NXT":"10694781281555936856","time":1418318212,"yourip":"178.62.185.131","yourport":7777,"ipaddr":"209.126.70.170","pubkey":"603043fc438bb7047fe4a0bc3734ccc56ca34a1e5db1d7b4b702eff3e0fc3e18","ver":"0.256"},{"token":"8fu46c30shvg9dsbpgq3ff503p5a6r65muqdfcatvjgf7ro2uvjka61u4eqtstg1n7q903t7cjoh0f1fr1shlrful8aeajc7o2dvm5grlg2ghl87jqafadd4nt7fup0kf6i0vat4nonj9cqj1kdf46ej8f62luvd"}]'} <class 'dict'>


 {'result':
 '{"result":"kademlia_pong","tag":"","NXT":"10694781281555936856","ipaddr":"209.126.70.170","port":0,"lag":"408186.000","numpings":104,"numpongs":45,"ave":"122765.867"}',
  'from': '209.126.70.170',
   'port': 0,
   'args': '[{"requestType":"pong","NXT":"10694781281555936856","time":1418318212,"yourip":"178.62.185.131","yourport":7777,"ipaddr":"209.126.70.170","pubkey":"603043fc438bb7047fe4a0bc3734ccc56ca34a1e5db1d7b4b702eff3e0fc3e18","ver":"0.256"},{"token":"8fu46c30shvg9dsbpgq3ff503p5a6r65muqdfcatvjgf7ro2uvjka61u4eqtstg1n7q903t7cjoh0f1fr1shlrful8aeajc7o2dvm5grlg2ghl87jqafadd4nt7fup0kf6i0vat4nonj9cqj1kdf46ej8f62luvd"}]'} <class 'dict'>


# b'{"result":"{\\"result\\":\\"kademlia_pong\\",\\"tag\\":\\"\\",\\"NXT\\":\\"10694781281555936856\\",\\"ipaddr\\":\\"209.126.70.170\\",\\"port\\":0,\\"lag\\":\\"284.500\\",\\"numpings\\":118,\\"numpongs\\":75,\\"ave\\":\\"14973.824\\"}","from":"209.126.70.170","port":0,"args":"[{\\"requestType\\":\\"pong\\",\\"NXT\\":\\"10694781281555936856\\",\\"time\\":1417959171,\\"yourip\\":\\"178.62.185.131\\",\\"yourport\\":7777,\\"ipaddr\\":\\"209.126.70.170\\",\\"pubkey\\":\\"603043fc438bb7047fe4a0bc3734ccc56ca34a1e5db1d7b4b702eff3e0fc3e18\\",\\"ver\\":\\"0.256\\"},{\\"token\\":\\"8fu46c30shvg9dsbpgq3ff503p5a6r65muqdfcatvjgf7ro2u9mc861u5kkts0o1rlq86puqhi744tsfvkt9qj1lo8hn1ujkn1vjavnc4um0vd1map6pi0qh92u107vm0bja5gtqqehn0etpn13e1e59tglb25gh\\"}]"}'



This contains FOUR / FIVE top components:

from
port
args [request,token]
result


request
{'requestType': 'pong', 'NXT': '1978065578067355462', 'yourip': '85.178.204.233', 'ipaddr': '89.212.19.49', 'pubkey': 'c269a8b4567c0b3062e6c4be859d845c4b808a405dd03d0d1ac7b4d9cb725b40', 'time': 1418376753, 'ver': '0.256', 'yourport': 63929} <class 'dict'>
2014-12-12 10:57:48+0100 [-] {'token': 'aqqagqe2sph302rsgieobfm482580iqs386jrk2teb5tjd67v35v4g2rsabl7d81uqdsm3grj4us9gef6vtlef9i4gtasb8726mgkdh8q040g1of6221f9bp5i58v5op9ifckla9ng8c268lm7m25i4lte2tdupd'} <class 'dict'>


token
 {'token': 'aqqagqe2sph302rsgieobfm482580iqs386jrk2teb5tjd67v35v4g2rsabl7d81uqdsm3grj4us9gef6vtlef9i4gtasb8726mgkdh8q040g1of6221f9bp5i58v5op9ifckla9ng8c268lm7m25i4lte2tdupd'} <class 'dict'>


result
 'result': '{"result":"kademlia_pong","tag":"","NXT":"1978065578067355462","ipaddr":"89.212.19.49","port":0,"lag":"72083.500","numpings":58,"numpongs":38,"ave":"161029.515"}',


b'{"result":"{\\"result\\":\\"kademlia_pong\\",\\"tag\\":\\"\\",\\"NXT\\":\\"10694781281555936856\\",\\"ipaddr\\":\\"209.126.70.170\\",\\"port\\":0,\\"lag\\":\\"1381.000\\",\\"numpings\\":168,\\"numpongs\\":118,\\"ave\\":\\"10356.752\\"}","from":"209.126.70.170","port":0,"args":"[{\\"requestType\\":\\"pong\\",\\"NXT\\":\\"10694781281555936856\\",\\"time\\":1417959371,\\"yourip\\":\\"178.62.185.131\\",\\"yourport\\":7777,\\"ipaddr\\":\\"209.126.70.170\\",\\"pubkey\\":\\"603043fc438bb7047fe4a0bc3734ccc56ca34a1e5db1d7b4b702eff3e0fc3e18\\",\\"ver\\":\\"0.256\\"},{\\"token\\":\\"8fu46c30shvg9dsbpgq3ff503p5a6r65muqdfcatvjgf7ro2u9moo61u66cdnr81muu5ang1cls58asvepjvttc9jei8h3j109bbdu0qgktg9lhimu1iimnomhun082es94raqm7vl1ej8ij31qjbuela8iqrljs\\"}]"}' <class 'bytes'>



        """#

        #log.msg("GUIpoll ---> kademlia_pong",rpl777, type(rpl777),"\n")

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


        rplArgs = json.loads(args) # <class 'list'> !!
        rplArgsRQ = rplArgs[0] # <class 'dict'>
        rplArgsTK = rplArgs[1]   #<class 'dict'>


        #log.msg(rplArgsTK, type(rplArgsTK))
        #log.msg(1*"kademlia_pong ",rpl777, type(rpl777))



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
            #
            # occasional EXCEPT here!! check!
            #
            #

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
        note= """ from here, we can go the next step, which is the findnode  TODO"""
        reqFindnode = {'requestType':'findnode'}


        reqFindnode['key']= NXT # the rea conf will be the havenode in uipoll
        self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqFindnode), headers=POSTHEADERS)
        self.deferred.addCallback(self.rpl777_df3_findnode ) # this is just for conf that we sent it
        self.deferred.addErrback(self.rpl777ERR)


        self.nodesDi = {}







    def rpl777_GUIpoll_kademlia_havenode(self, rpl777): #parse777_step1
        """

#got HAVENODE.([["7108754351996134253", "167.114.2.171", "7777", "0"], ["8566622688401875656", "37.59.108.92", "7777", "1418355409"], ["16196432036059823401", "167.114.2.203", "7777", "1418355386"], ["7067340061344084047", "94.102.50.70", "7777", "1418355591"], ["11634703838614499263", "69.90.132.106", "7777", "1418356230"], ["13594896385051583735", "192.99.246.20", "7777", "1418355386"], ["1978065578067355462", "89.212.19.49", "7777", "1418355370"]]) for key.(7108754351996134253) from 7108754351996134253



 GUIpoll ---> kademlia_havenode {'args': '[{"requestType":"havenode","NXT":"11910135804814382998","time":1418378252,"key":"11910135804814382998","data":[["11910135804814382998", "167.114.2.94", "7777", "0"], ["2131686659786462901", "85.178.204.233", "61312", "1418374115"], ["11634703838614499263", "69.90.132.106", "7777", "1418355887"], ["10694781281555936856", "209.126.70.170", "7777", "1418355569"], ["17265504311777286118", "184.175.25.117", "7777", "1418355277"], ["5624143003089008155", "192.99.212.250", "7777", "1418355253"], ["8894667849638377372", "209.126.70.156", "7777", "1418355643"]]},{"token":"crhllp9ko5ehtcf8j46plskln4hn2lkp2ph4kbm0e9edtp00v38sqttrls1eh801smc20bj8ebllvob2qn9vnotj5i4952fl450o08pmsbr03liiaftu4ljmbh7ofajod0tvl87edal1k5drbeemj4ul4b42j99c"}]', 'result': '{"result":"kademlia_havenode from NXT.11910135804814382998 key.(11910135804814382998) value.([["11910135804814382998", "167.114.2.94", "7777", "0"], ["2131686659786462901", "85.178.204.233", "61312", "1418374115"], ["11634703838614499263", "69.90.132.106", "7777", "1418355887"], ["10694781281555936856", "209.126.70.170", "7777", "1418355569"], ["17265504311777286118", "184.175.25.117", "7777", "1418355277"], ["5624143003089008155", "192.99.212.250", "7777", "1418355253"], ["8894667849638377372", "209.126.70.156", "7777", "1418355643"]])"}', 'port': 0, 'from': '167.114.2.94'} <class 'dict'>



 #{"result":"kademlia_havenode from NXT.5624143003089008155 key.(5624143003089008155) value.([["5624143003089008155", "192.99.212.250", "7777", "0"], ["15178638394924629506", "167.114.2.206", "7777", "1417435953"], ["6249611027680999354", "80.41.56.181", "7777", "1417449705"], ["11910135804814382998", "167.114.2.94", "7777", "1417435991"], ["7581814105672729429", "187.153.194.200", "29693", "1417652256"], ["7108754351996134253", "167.114.2.171", "7777", "1417435991"], ["16196432036059823401", "167.114.2.203", "7777", "1417435957"]])"}

# {"result":"kademlia_havenode from NXT.5624143003089008155 key.(5624143003089008155) value.([["5624143003089008155", "192.99.212.250", "7777", "0"], ["15178638394924629506", "167.114.2.206", "7777", "1417435953"], ["6249611027680999354", "80.41.56.181", "7777", "1417449705"], ["11910135804814382998", "167.114.2.94", "7777", "1417435991"], ["7581814105672729429", "187.153.194.200", "29693", "1417652256"], ["16196432036059823401", "167.114.2.203", "7777", "1417435957"], ["7108754351996134253", "167.114.2.171", "7777", "1417435991"]])"}


#{"result":"kademlia_havenode from NXT.12315166155634751985 key.(12315166155634751985) value.([["12315166155634751985", "167.114.2.205", "7777", "0"], ["13594896385051583735", "192.99.246.20", "7777", "1418309439"], ["16196432036059823401", "167.114.2.203", "7777", "1418308928"], ["8923034930361863607", "192.99.246.33", "7777", "1418308929"], ["7581814105672729429", "187.153.143.36", "27190", "1418308969"], ["7108754351996134253", "167.114.2.171", "7777", "1418308950"], ["11634703838614499263", "69.90.132.106", "7777", "1418308973"]])"} <class 'str'>
#{"result":"kademlia_havenode from NXT.12315166155634751985 key.(12315166155634751985) value.([["12315166155634751985", "167.114.2.205", "7777", "0"], ["13594896385051583735", "192.99.246.20", "7777", "1418309439"], ["16196432036059823401", "167.114.2.203", "7777", "1418308928"], ["8923034930361863607", "192.99.246.33", "7777", "1418308929"], ["7581814105672729429", "187.153.143.36", "27190", "1418308969"], ["7108754351996134253", "167.114.2.171", "7777", "1418308950"], ["11634703838614499263", "69.90.132.106", "7777", "1418308973"]])"} <class 'str'>

# make ad hoc here, put into nice class later.
        # b'{"result":"kademlia_findnode from.(2131686659786462901) previp.() key.(3571143576961987768) datalen.0 txid.1496458648985206585"}'




GUIpoll ---> kademlia_havenode



{'port': 0, 'args': '[{"requestType":"havenode","NXT":"11910135804814382998","time":1418378474,"key":"11910135804814382998","data":[["11910135804814382998", "167.114.2.94", "7777", "0"], ["2131686659786462901", "85.178.204.233", "61312", "1418374115"], ["11634703838614499263", "69.90.132.106", "7777", "1418355887"], ["10694781281555936856", "209.126.70.170", "7777", "1418355569"], ["17265504311777286118", "184.175.25.117", "7777", "1418355277"], ["5624143003089008155", "192.99.212.250", "7777", "1418355253"], ["8894667849638377372", "209.126.70.156", "7777", "1418355643"]]},{"token":"crhllp9ko5ehtcf8j46plskln4hn2lkp2ph4kbm0e9edtp00v39akttr3oogmkg1nadgia072k06a9nggjaab7fj8mkhl0bqr364sskelrk0gihn85f3rqlriekbdub8vudcs1k27kkgetsmq8u53qoedjgaujep"}]', 'result': '{"result":"kademlia_havenode from NXT.11910135804814382998 key.(11910135804814382998) value.([["11910135804814382998", "167.114.2.94", "7777", "0"], ["2131686659786462901", "85.178.204.233", "61312", "1418374115"], ["11634703838614499263", "69.90.132.106", "7777", "1418355887"], ["10694781281555936856", "209.126.70.170", "7777", "1418355569"], ["17265504311777286118", "184.175.25.117", "7777", "1418355277"], ["5624143003089008155", "192.99.212.250", "7777", "1418355253"], ["8894667849638377372", "209.126.70.156", "7777", "1418355643"]])"}', 'from': '167.114.2.94'} <class 'dict'>



so for the recipient of the find node, the result is havenode

jl777 [12:19 PM]12:19
to the sender of the find, it comes back as a new havenode command

    """#

        #log.msg("GUIpoll ---> kademlia_havenode",rpl777, type(rpl777),"\n")

        try:
            fromIp = rpl777['from']
            port = rpl777['port']
            rplArgs = rpl777['args']
            try:
                rplArgs=json.loads(rplArgs)

            except Exception as e:
                log.msg("Error args {0}".format(str(e)))
                log.msg("args NOT ok",rplArgs, type(rplArgs))
            #log.msg(12*"\nargs ok ",rplArgs, type(rplArgs))
            # [{"requestType":"havenode","NXT":"7067340061344084047","time":1418387237,"key":"7067340061344084047","data":[["7067340061344084047", "94.102.50.70", "7777", "0"], ["5624143003089008155", "192.99.212.250", "7777", "1417906278"], ["7108754351996134253", "167.114.2.171", "7777", "1417855494"], ["7837143510182070614", "62.194.6.163", "7777", "1417012372"], ["7422772935859746536", "184.175.25.117", "55045", "1417951862"], ["8923034930361863607", "192.99.246.33", "7777", "1418263800"], ["11634703838614499263", "69.90.132.106", "7777", "1418231950"]]},{"token":"197njl2bp54ijkjnfadmvua4irii342267l8taa4n53vqhg5v3qeag341hfbkf81p042d8ap8pqtqabfc1u0pn38tiiob79ltvf4utt207dg81r8992jlkovj4b8q84bnln14esjbktd81phnhs51taogbajptre"}]
            #<class 'str'>
            rpl777 = rpl777['result'] # this is a string!
            #log.msg("2",rpl777, type(rpl777))
            #{"result":"kademlia_havenode from NXT.7067340061344084047 key.(7067340061344084047) value.([["7067340061344084047", "94.102.50.70", "7777", "0"], ["5624143003089008155", "192.99.212.250", "7777", "1417906278"], ["7108754351996134253", "167.114.2.171", "7777", "1417855494"], ["7837143510182070614", "62.194.6.163", "7777", "1417012372"], ["7422772935859746536", "184.175.25.117", "55045", "1417951862"], ["8923034930361863607", "192.99.246.33", "7777", "1418263800"], ["11634703838614499263", "69.90.132.106", "7777", "1418231950"]])"}
            #<class 'str'>
            try:
                #print(5*"\n~rpl777_GUIpoll_kademlia_havenode ~+>", rpl777, type(rpl777))
                rpl777SPL=rpl777.split('([')
                prefix = rpl777SPL[0]
                #'{"result":"kademlia_havenode from NXT.11910135804814382998 key.(11910135804814382998) value.'
                # can extract NXT and key from here if need be
                havenodesStr=rpl777SPL[1].split('])')[0]
                # nice str now:
                #'["11910135804814382998", "167.114.2.94", "7777", "0"], ["2131686659786462901", "85.178.204.233", "61312", "1418374115"], ["10694781281555936856", "209.126.70.170", "7777", "1418355569"], ["11634703838614499263", "69.90.132.106", "7777", "1418355887"], ["17265504311777286118", "184.175.25.117", "7777", "1418355277"], ["5624143003089008155", "192.99.212.250", "7777", "1418355253"], ["8894667849638377372", "209.126.70.156", "7777", "1418355643"]'
                rpl777Li=eval(havenodesStr)
                # list now:
                # (['11910135804814382998', '167.114.2.94', '7777', '0'],
                #  ['2131686659786462901', '85.178.204.233', '61312', '1418374115'],
                #  ['10694781281555936856', '209.126.70.170', '7777', '1418355569'],
                #  ['11634703838614499263', '69.90.132.106', '7777', '1418355887'],
                #  ['17265504311777286118', '184.175.25.117', '7777', '1418355277'],
                #  ['5624143003089008155', '192.99.212.250', '7777', '1418355253'],
                #  ['8894667849638377372', '209.126.70.156', '7777', '1418355643'])
                rpl777 = {'havenodes':rpl777Li}

            except Exception as e:
                log.msg("Error args {0}".format(str(e)))
                log.msg("2",rpl777, type(rpl777))

        except Exception as e:
            #log.msg("GUIpoll ---> kademlia_pong",rpl777, type(rpl777),"\n")
            log.msg("Error rpl777_GUIpoll_kademlia_havenode {0}".format(str(e)))

        rplArgsRQ = rplArgs[0] # <class 'dict'>
        rplArgsTK = rplArgs[1]   #<class 'dict'>
        #log.msg(5*"\nargs ----> ",rplArgsRQ, type(rplArgsRQ))

        # There are two types of havendoe

        #
        # for key in rplArgsRQ.keys():
        #     print(key, " - " , rplArgsRQ[key])

 #{'time': 1418380620, 'requestType': 'havenode', 'NXT': '5624143003089008155', 'key': '5624143003089008155', 'data': [['5624143003089008155', '192.99.212.250', '7777', '0'], ['7067340061344084047', '94.102.50.70', '7777', '1418355322'], ['15178638394924629506', '167.114.2.206', '7777', '1418355261'], ['6249611027680999354', '80.41.56.181', '7777', '1418375808'], ['11910135804814382998', '167.114.2.94', '7777', '1418355255'], ['6216883599460291148', '192.99.246.126', '7777', '1418355291'], ['16196432036059823401', '167.114.2.203', '7777', '1418355258']]}

        try:
            data = rplArgsRQ['data']

        except Exception as e:
            #log.msg("GUIpoll ---> kademlia_pong",rpl777, type(rpl777),"\n")
            log.msg("Error data = rplArgsRQ['data']   {0}".format(str(e)))

        #log.msg(rplArgsTK, type(rplArgsTK))
        #log.msg(5*"\n++++++++++++++++kademlia_havenode",rpl777, type(rpl777))
        #log.msg(1*"\n              data",data, type(data))

# THIS MAYB EBE BG ACTIVITY
#
# {'havenodes': (['7067340061344084047', '94.102.50.70', '7777', '0'], ['5624143003089008155', '192.99.212.250', '7777', '1417906278'], ['7108754351996134253', '167.114.2.171', '7777', '1417855494'], ['7837143510182070614', '62.194.6.163', '7777', '1417012372'], ['7422772935859746536', '184.175.25.117', '55045', '1417951862'], ['8923034930361863607', '192.99.246.33', '7777', '1418263800'], ['11634703838614499263', '69.90.132.106', '7777', '1418231950'])} <class 'dict'>
#
#              [['7067340061344084047', '94.102.50.70', '7777', '0'], ['5624143003089008155', '192.99.212.250', '7777', '1417906278'], ['7108754351996134253', '167.114.2.171', '7777', '1417855494'], ['7837143510182070614', '62.194.6.163', '7777', '1417012372'], ['7422772935859746536', '184.175.25.117', '55045', '1417951862'], ['8923034930361863607', '192.99.246.33', '7777', '1418263800'], ['11634703838614499263', '69.90.132.106', '7777', '1418231950']] <class 'list'>
#
        reqPing = {'requestType':'ping'}
        reqFindnode = {'requestType':'findnode'}
        log.msg(1*"\n FINDNODE & PING all:", rpl777Li)
        for node in rpl777Li:
#            ping and findnode!

            if node[1] not in self.nodeDi.keys():
                self.nodeDi[node[1]] = node[0]

            reqPing['destip']=node[1]
            self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqPing), headers=POSTHEADERS)
            self.deferred.addCallback(self.rpl777_df2_ping)
            self.deferred.addErrback(self.rpl777ERR)

            reqFindnode['key']=node[0]
            self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqPing), headers=POSTHEADERS)
            self.deferred.addCallback(self.rpl777_df2_ping)
            self.deferred.addErrback(self.rpl777ERR)







        note=""" data in RQ is the same as in havenodes! ?!?!?! : now do the findonde and poing thing fronm here! """









###################################
###################################
###################################
###################################
###################################
###################################

        #
        #
        # non GUIpoll api talk here
        #
        #

    def rpl777_settings_df1(self, dataFrom777): #these are the basic pings from the whitlist
        """"""#
        repl=dataFrom777.json()
        reqPing = {'requestType':'ping'}

        # self.nodeDi[node[1]] = node[0]
        #'one' in dict.values() easy

        ipsToPing=repl['whitelist'] #[0] # singlecheck
        #ipsToPing = 10* ['178.62.185.131'] # stonefish['80.41.56.181'] # ['85.178.202.108']   #

        for node in ipsToPing:
            reqPing['destip']=node
            self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqPing), headers=POSTHEADERS)
            self.deferred.addCallback(self.rpl777_df2_ping)
            self.deferred.addErrback(self.rpl777ERR)

        self.rpl777_pingDB_df1()


    def rpl777_pingDB_df1(self, ):#dataFrom777):
        """"""#
        #repl=dataFrom777.json()
        reqPing = {'requestType':'ping'}

        # create internal peerlist,
        # init that with the whitelist and extend

        #'one' in dict.values() easy


        # create internal peerlist,
        #log.msg(1*"\npinging these nodeDi",self.nodeDi.keys())
        for node in self.nodeDi.keys():
            reqPing['destip']=node
            self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqPing), headers=POSTHEADERS)
            self.deferred.addCallback(self.rpl777_df2_ping)
            self.deferred.addErrback(self.rpl777ERR)




    def rpl777_df2_ping(self, dataFrom777):
        """
        ---->rpl777 ping {'result': 'kademlia_ping to 100.79.14.220', 'txid': '0'}
        when we have done ping it does not init a callback, because that is PONG we have to wait for

        """#
        repl=dataFrom777.json()
        repl=dataFrom777.content.decode("utf-8")
        repl=eval(repl)
        #log.msg( 1 * "ping sent", repl)




    def rpl777_df3_findnode(self, dataFrom777):
        """
        ---->rpl777_df3_findnode

        """#
        repl=dataFrom777.json()
        repl=dataFrom777.content.decode("utf-8")
        repl=eval(repl)
        log.msg( 1 * "\ndone findnode", repl)








    def rpl777ERR(self, ERR777):

        print(ERR777)

        raise RuntimeError










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

            time.sleep(1.01) # constraint on demo account sportsdataLLC
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

