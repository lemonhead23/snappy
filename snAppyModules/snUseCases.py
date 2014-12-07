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

        # these need to addressed explicitly by their names in the UC class,
        # and there the names must be known explicitly anyway
        self.target = schedule['target']
        self.lastCallTime = int(time.time() * 1000)



    def callMe(self):
        self.deltaT = int(time.time() * 1000 ) - self.lastCallTime
        print("------> callFreq of this schedule ???: ", self.deltaT ," > ", self.callFreq, self.deltaT > self.callFreq)
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
                self.deferred.addCallback(self.reply777_df1)
                self.deferred.addErrback(self.reply777ERR)
            elif 'SPAM' == 'EGGS':
                pass
    #
    #
    # cascading deferreds here!
    #
    def reply777_df1(self, dataFrom777):
        """ These deferreds are UseCase specific!  """#
        repl=dataFrom777.json()
        next_req_we_want_to_do_in_df1 =    {'requestType':'ping'}

        for thing in repl['whitelist']:
            next_req_we_want_to_do_in_df1['destip'] = thing
            self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(next_req_we_want_to_do_in_df1), headers=POSTHEADERS)
            self.deferred.addCallback(self.reply777_df2)
            self.deferred.addErrback(self.reply777ERR)

    def reply777_df2(self, dataFrom777):

        # we do not have any requester to give anything back to.
        # either another part of the use case or just dump to screen or file.
        print( 1 * "\n---->reply777 deferred here", dataFrom777)
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


    def reply777ERR(self, ERR777):
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
        print( "Scheduler ", self, " MAIN scheduled Heartbeat: ", datetime.now())

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
                self.deferred.addCallback(self.reply777_df1)
                self.deferred.addErrback(self.reply777ERR)
            elif 'SPAM' == 'EGGS':
                pass
    #
    # cascading deferreds here!
    #
    def reply777_df1(self, dataFrom777):
        """"""#
        repl=dataFrom777.json()
        reqPing = {'requestType':'ping'}

        ipsToPing=repl['whitelist'] #[0] # singlecheck
        #ipsToPing = 10* ['178.62.185.131'] # stonefish['80.41.56.181'] # ['85.178.202.108']   #

        for node in ipsToPing:
            reqPing['destip']=node
            self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqPing), headers=POSTHEADERS)
            self.deferred.addCallback(self.reply777_df2)
            self.deferred.addErrback(self.reply777ERR)


    def reply777_df2(self, dataFrom777):
        """"""#
        repl=dataFrom777.json()
        #log.msg( 1 * "\n---->reply777 ping", dataFrom777)
        repl=dataFrom777.content.decode("utf-8")
        repl=eval(repl)
        # for se in repl:
        #     print(se,repl[se]) #85.178.200.167

        reqGUIpoll = {'requestType':'GUIpoll'}

        self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqGUIpoll), headers=POSTHEADERS)
        self.deferred.addCallback(self.reply777_df3)
        self.deferred.addErrback(self.reply777ERR)



    def reply777_df3(self, dataFrom777):
        """
        Note : Use python assert in the future
                Use parse and format for the strings!

        """#

        if dataFrom777.content == b'{"result":"nothing pending"}':
            return {"result":"nothing pending"}

        #log.msg( 1 * "\n---->reply777 GUIpoll", dataFrom777, type(dataFrom777))
        #log.msg( 1 * "\n---->reply777 GUIpoll", dataFrom777.content)

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
                log.msg("resultFull parse except:", resultFull,type(resultFull) )
                resultFull={'SPAM':'EGGS'}
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



    def reply777ERR(self, ERR777):

        print(ERR777)

        raise RuntimeError







class UCTEST_2_ping_findnode(object):

    """



settings - ping whitelist and do findnode

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

        prepSchedules = environ['UCTEST_1_ping_whitelist_777'] # can use same as UC1 for now- extends it
        for sched in prepSchedules.keys():
            sched = prepSchedules[sched]
            self.schedules[ sched['schedName']] = Schedule( sched )

        self.lastCallTime = int(time.time() * 1000)


    def periodic(self, ):
        """ this is the method that is called periodically by the twisted loopingTask.
         This contains the UseCase logic, ie needs to check what to do, and then do it. """#

        schedulesDue =[]
        print( "Scheduler ", self, " MAIN scheduled Heartbeat: ", datetime.now())

        for schedule in self.schedules.keys():
            schedule = self.schedules[schedule]

            if schedule.callMe():
                schedulesDue.append(schedule)

        self.runSchedules(schedulesDue)


    def runSchedules(self,schedulesDue):

        for schedDue in schedulesDue:
            if 'uc1Start_settings' in schedDue.SNrequests.keys():
                reqData = schedDue.SNrequests['uc1Start_settings']
                self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqData), headers=POSTHEADERS)
                self.deferred.addCallback(self.reply777_df1)
                self.deferred.addErrback(self.reply777ERR)
            elif 'SPAM' == 'EGGS':
                pass
    #
    # cascading deferreds here!
    #
    def reply777_df1(self, dataFrom777):
        """"""#
        repl=dataFrom777.json()
        reqPing = {'requestType':'ping'}

        ipsToPing=repl['whitelist'] #[0] # singlecheck
        #ipsToPing = 10* ['178.62.185.131'] # stonefish['80.41.56.181'] # ['85.178.202.108']   #

        for node in ipsToPing:
            reqPing['destip']=node
            self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqPing), headers=POSTHEADERS)
            self.deferred.addCallback(self.reply777_df2)
            self.deferred.addErrback(self.reply777ERR)


    def reply777_df2(self, dataFrom777):
        """"""#
        repl=dataFrom777.json()
        #log.msg( 1 * "\n---->reply777 ping", dataFrom777)
        repl=dataFrom777.content.decode("utf-8")
        repl=eval(repl)
        # for se in repl:
        #     print(se,repl[se]) #85.178.200.167

        reqGUIpoll = {'requestType':'GUIpoll'}

        self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqGUIpoll), headers=POSTHEADERS)
        self.deferred.addCallback(self.reply777_df3)
        self.deferred.addErrback(self.reply777ERR)



    def reply777_df3(self, dataFrom777):
        """
        Note : Use python assert in the future
                Use parse and format for the strings!

        """#

        if dataFrom777.content == b'{"result":"nothing pending"}':
            return {"result":"nothing pending"}

        #log.msg( 1 * "\n---->reply777 GUIpoll", dataFrom777, type(dataFrom777))
        #log.msg( 1 * "\n---->reply777 GUIpoll", dataFrom777.content)

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
                log.msg("resultFull parse except:", resultFull,type(resultFull) )
                resultFull={'SPAM':'EGGS'}
                #log.msg(resultFull,type(resultFull) )



            ptt_PONG = {
                            'fullRequest': fullRequest , \
                            "token":token  ,\
                            'result':resultFull,\
                            'fromPort':fromPort,\
                            'fromIp' : fromIp
                             }
            #
            # print(3*"---------------*") #\n")
            # for key in ptt_PONG.keys():
            #
            #
            #     if key == 'result':
            #         for keyR in ptt_PONG[key].keys():
            #             print( keyR, " - ",ptt_PONG[key][keyR])
            #         continue
            #     print(1*"\n")
            #     if key == 'fullRequest':
            #         for keyR in ptt_PONG[key].keys():
            #             print( keyR, " - ",ptt_PONG[key][keyR])
            #         continue
            #
            #     print("\n", key, " - ",ptt_PONG[key], "\n")



        except Exception as e:
            print("Error {0}".format(str(e)))



        if 'NXT' in fullRequest.keys():
            print("going to findnode on:", fullRequest['NXT'])
            req_findnode = {'requestType':'findnode'}
            req_findnode['key'] = fullRequest['NXT']
            self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(req_findnode), headers=POSTHEADERS)
            self.deferred.addCallback(self.reply777_df4)
            self.deferred.addErrback(self.reply777ERR)




    def reply777_df4(self, dataFrom777):

        print(5*"\n~~+>", dataFrom777.content, type(dataFrom777.content))
        dataFrom777=dataFrom777.content
        # good: findnode on whitelist
        # now parse. a bit awkward.
        # make ad hoc here, put into nice class later.
        # b'{"result":"kademlia_findnode from.(2131686659786462901) previp.() key.(3571143576961987768) datalen.0 txid.1496458648985206585"}'
        try:

            dataFrom777= dataFrom777.decode("utf-8")
            dataFrom777 = dataFrom777.split()
            key = dataFrom777[3]
            key=key.split('(')[1]
            key = key.rstrip(')')

        except Exception as e:

            print("Error parsing findnode:  {0}".format(str(e)))



        reqGUIpoll = {'requestType':'GUIpoll'}

        self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(reqGUIpoll), headers=POSTHEADERS)
        self.deferred.addCallback(self.reply777_df5GP)
        self.deferred.addErrback(self.reply777ERR)




    def reply777_df5GP(self, dataFrom777):

        print(5*"\n+++++++~~+>", dataFrom777.content, type(dataFrom777.content))
        havenodeBytes = dataFrom777.content
        havenodeS = havenodeBytes.decode("utf-8")
        havenodeDi =json.loads(havenodeS) # better than eval
        #                havenodeDi.keas(['from', 'args', 'result', 'port'])
        havenodeRes = havenodeDi['result']



#resultFull

#{"result":"kademlia_havenode from NXT.7108754351996134253 key.(7108754351996134253) value.([["7108754351996134253", "167.114.2.171", "7777", "0"], ["7422772935859746536", "184.175.25.117", "7777", "1417890717"], ["3571143576961987768", "89.212.19.49", "7777", "1417830096"], ["16196432036059823401", "167.114.2.203", "7777", "1417829426"], ["13594896385051583735", "192.99.246.20", "7777", "1417829426"], ["15178638394924629506", "167.114.2.206", "7777", "1417829426"], ["6216883599460291148", "192.99.246.126", "7777", "1417829405"]])"} <class 'str'>

            #
            # try:
            #     #resultFull = eval(resultFull) #<------------- YES this is a str too!
            #     resultFull = json.loads(resultFull) #<------------- YES this is a str too!
            #
            #     port =  resultFull['port']
            #     numpings =  resultFull['numpings']
            #     lag  =  resultFull['lag']
            #     ipaddr  = resultFull['ipaddr']
            #     numpongs =  resultFull['numpongs']
            #     result =   resultFull['result']
            #     ave  =  resultFull['ave']
            #     NXT  = resultFull['NXT']
            #     #log.msg("resultFull", resultFull,type(resultFull))


#
# havenodeDi['from']  '209.126.70.170'
#
# havenodeDi['args']   '[{"requestType":"pong","NXT":"10694781281555936856","time":1417959171,"yourip":"178.62.185.131","yourport":7777,"ipaddr":"209.126.70.170","pubkey":"603043fc438bb7047fe4a0bc3734ccc56ca34a1e5db1d7b4b702eff3e0fc3e18","ver":"0.256"},{"token":"8fu46c30shvg9dsbpgq3ff503p5a6r65muqdfcatvjgf7ro2u9mc861u5kkts0o1rlq86puqhi744tsfvkt9qj1lo8hn1ujkn1vjavnc4um0vd1map6pi0qh92u107vm0bja5gtqqehn0etpn13e1e59tglb25gh"}]'
#
# havenodeDi['port']  0
#
# havenodeDi['result']  '{"result":"kademlia_pong","tag":"","NXT":"10694781281555936856","ipaddr":"209.126.70.170","port":0,"lag":"284.500","numpings":118,"numpongs":75,"ave":"14973.824"}'
#


# b'{"result":"kademlia_havenode from NXT.13434315136155299987 key.(13434315136155299987) value.([["13434315136155299987", "209.126.70.159", "7777", "0"], ["12315166155634751985", "167.114.2.205", "7777", "1417927353"], ["13594896385051583735", "192.99.246.20", "7777", "1417927128"], ["2131686659786462901", "178.62.185.131", "7777", "1417943077"], ["3571143576961987768", "89.212.19.49", "7777", "1417927101"], ["8894667849638377372", "209.126.70.156", "7777", "1417929362"], ["7067340061344084047", "94.102.50.70", "7777", "1417927162"]])"} <class 'str'>

# b'{"result":"{\\"result\\":\\"kademlia_pong\\",\\"tag\\":\\"\\",\\"NXT\\":\\"10694781281555936856\\",\\"ipaddr\\":\\"209.126.70.170\\",\\"port\\":0,\\"lag\\":\\"284.500\\",\\"numpings\\":118,\\"numpongs\\":75,\\"ave\\":\\"14973.824\\"}","from":"209.126.70.170","port":0,"args":"[{\\"requestType\\":\\"pong\\",\\"NXT\\":\\"10694781281555936856\\",\\"time\\":1417959171,\\"yourip\\":\\"178.62.185.131\\",\\"yourport\\":7777,\\"ipaddr\\":\\"209.126.70.170\\",\\"pubkey\\":\\"603043fc438bb7047fe4a0bc3734ccc56ca34a1e5db1d7b4b702eff3e0fc3e18\\",\\"ver\\":\\"0.256\\"},{\\"token\\":\\"8fu46c30shvg9dsbpgq3ff503p5a6r65muqdfcatvjgf7ro2u9mc861u5kkts0o1rlq86puqhi744tsfvkt9qj1lo8hn1ujkn1vjavnc4um0vd1map6pi0qh92u107vm0bja5gtqqehn0etpn13e1e59tglb25gh\\"}]"}'

# successfull HAVENODE but snatched by wrong GUIpoll!

# resultFull parse except:
# #
# #
# # {"result":"kademlia_havenode from NXT.7108754351996134253 key.(7108754351996134253) value.([["7108754351996134253", "167.114.2.171", "7777", "0"], ["7422772935859746536", "184.175.25.117", "7777", "1417890717"], ["3571143576961987768", "89.212.19.49", "7777", "1417830096"], ["16196432036059823401", "167.114.2.203", "7777", "1417829426"], ["13594896385051583735", "192.99.246.20", "7777", "1417829426"], ["6216883599460291148", "192.99.246.126", "7777", "1417829405"], ["15178638394924629506", "167.114.2.206", "7777", "1417829426"]])"} <class 'str'>
# Error parsing fullRequest:  'pubkey'
#2014-12-07 14:32:35+0100 [-] resultFull parse except: {'result': 'kademlia_findnode from.(7108754351996134253) previp.(167.114.2.171) key.(2131686659786462901) datalen.0 txid.17606717170707944813'} <class 'dict'>
#2014-12-07 14:32:35+0100 [-] Error parsing fullRequest:  'pubkey'
#2014-12-07 14:32:35+0100 [-] resultFull parse except:

#  {"result":"kademlia_havenode from NXT.7108754351996134253 key.(7108754351996134253) value.([["7108754351996134253", "167.114.2.171", "7777", "0"], ["7422772935859746536", "184.175.25.117", "7777", "1417890717"], ["3571143576961987768", "89.212.19.49", "7777", "1417830096"], ["16196432036059823401", "167.114.2.203", "7777", "1417829426"], ["13594896385051583735", "192.99.246.20", "7777", "1417829426"], ["6216883599460291148", "192.99.246.126", "7777", "1417829405"], ["15178638394924629506", "167.114.2.206", "7777", "1417829426"]])"} <class 'str'>

#
# 2014-12-07 14:37:16+0100 [-] +++++++~~+>
# 2014-12-07 14:37:16+0100 [-] +++++++~~+>
# 2014-12-07 14:37:16+0100 [-] +++++++~~+> b'{"result":"{\\"result\\":\\"kademlia_pong\\",\\"tag\\":\\"\\",\\"NXT\\":\\"10694781281555936856\\",\\"ipaddr\\":\\"209.126.70.170\\",\\"port\\":0,\\"lag\\":\\"1381.000\\",\\"numpings\\":168,\\"numpongs\\":118,\\"ave\\":\\"10356.752\\"}","from":"209.126.70.170","port":0,"args":"[{\\"requestType\\":\\"pong\\",\\"NXT\\":\\"10694781281555936856\\",\\"time\\":1417959371,\\"yourip\\":\\"178.62.185.131\\",\\"yourport\\":7777,\\"ipaddr\\":\\"209.126.70.170\\",\\"pubkey\\":\\"603043fc438bb7047fe4a0bc3734ccc56ca34a1e5db1d7b4b702eff3e0fc3e18\\",\\"ver\\":\\"0.256\\"},{\\"token\\":\\"8fu46c30shvg9dsbpgq3ff503p5a6r65muqdfcatvjgf7ro2u9moo61u66cdnr81muu5ang1cls58asvepjvttc9jei8h3j109bbdu0qgktg9lhimu1iimnomhun082es94raqm7vl1ej8ij31qjbuela8iqrljs\\"}]"}' <class 'bytes'>
# 2014-12-07 14:37:18+0100 [-] Scheduler  <snAppyModules.snUseCases.UCTEST_2_ping_findnode object at 0x7f4026e48e80>  MAIN scheduled Heartbeat:  2014-12-07 14:37:18.765234
# 2014-12-07 14:37:18+0100 [-] ------> callFreq of this
# #addnode
#7108754351996134253


# findnode comed from GUIpoll.
# s back nice through the reular return channel.
        # havenode and PONG get snrafe





    def reply777ERR(self, ERR777):

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
        print( "Scheduler ", self, " MAIN scheduled Heartbeat: ", datetime.now())

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

