#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
#



"""#

from twisted.internet import reactor

import sys, time
import os
from snAppyModules.snUseCases import *

#from snAppyTests.snTests import *
from snAppyModules.snQueryComposers import *
from snAppyModules.snParsers import *
from snAppyModules.snAppyConfig import *
from snAppyModules.pyDaemon3 import Daemon3

from twisted.internet import task
from twisted.python import threadpool as tp



class nxtClientFactory(ClientFactory):
    
    def __init__(self, ):
        super(nxtClientFactory, self).__init__()
        #log.msg("2c --nxtClientFactory---->  build Client Protocol" )
        self.ok=True



class nxtServerFactory(ServerFactory):

    def __init__(self, queryComposers, parsers, environ):
        super(nxtServerFactory, self).__init__()
        self.ok=True
        #print(environ)

        self.parser_XML = parsers['parser_XML']
        self.parser_777 = parsers['parser_777']
        self.parser_RPC = parsers['parser_RPC']
        self.parser_LOC = parsers['parser_LOC']
        self.parser_LOC.environ = environ

        self.qComp_777 = queryComposers['qComp_777']    # .API_calls
        self.qComp_XML = queryComposers['qComp_XML']
        self.qComp_LOC = queryComposers['qComp_LOC']


    def buildProtocol(self, addr):
        proto = ProxyServerProtocolSuperNET()
        # this is where we plug this namespace into the Protocol!
        proto.proxyServerFactory = self #
        log.msg(1*"\n1 nxtServerFactory---->  builds a  Protocol", str(proto), '@',str(addr))
        return proto


# Adapted from http://stackoverflow.com/a/15645169/221061
class ProxyServerProtocolSuperNET(protocol.Protocol):
    """# Client => Proxy
        # Here we receive the initial request.
        # Here we parse the request
        # Here we route the request to the client that sends the specific query to the remote server.
    """#

    def __init__(self):

        self.buffer = None
        self.client = None





    def connectionMade(self):
        """  here we must connect to EITHER jl777 OR some external data feed
             so either we do this as a deferred OR we move this into the GET processing routine where we find out what API is called
            Instantiate CLientFactory here, but not yet the Protocoal, because the Req needs to be parsed first in order to decide which Prot.
        """ #
        #log.msg("ProxyServerProtocolSuperNET 1 ----> build Protocol: connectionMade")
        self.clientFactory = nxtClientFactory()
        # NOTE: the nxtServerFactory instance is always the same, but the nxtClientFactory is a new one every time.

    def dataReceived(self, rawRequest):
        """ Protocol ONLY knows dataReceived. dataReceived Has to be overridden, and the processing pipeline added:
        render_GET, etc... """ #
        # ToDo: check mechnism: - self.client? this has to do with connection status somehow.
        if self.client:
            log.msg("ProxyServerProtocolSuperNET 2a::\n\n", str(rawRequest))
            self.client.write(rawRequest)
        else:
            #log.msg("ProxyServerProtocolSuperNET 2b--dataReceived- ", str(rawRequest))
            self.identify_req_type(rawRequest)


    def identify_req_type(self, rawRequest):
        """- this is low level as opposed to the Site API
            Doing this low level stuff myself is a bit tedious but it offers flexibility for custom mods.
            
        Called whenever data is received.
        
        Use this method to translate to a higher-level message.  Usually, some
        callback will be made upon the receipt of each complete protocol
        message.
        We can process both, GET and POST! (POST not implemented yet)

        """ #
        POST = rawRequest[:4]==bytes('POST',"utf-8")
        GET = rawRequest[:3]==bytes('GET',"utf-8") 

        if POST:
            self.render_POST(rawRequest)
        elif GET:
            self.render_GET(rawRequest)
            #log.msg("ProxyServerProtocolSuperNET 3--parse_request-- ", str(rawRequest), " time: "  ,str(time.time()))
        else:
            self.transport.loseConnection()
            raise RuntimeError( ("request: "+str(rawRequest) ))
 
        return None



    def render_GET(self, request):
        """
        The requests are received here as raw bytestrings.
        Example: rawrequst:  <class 'bytes'>
        b'GET /nxt?requestType=getpeers HTTP/1.1\r\nUser-Agent: curl/7.35.0\r\nHost: 127.0.0.1:7777\r\nAccept: */*\r\ncontent-type: text/plain;\r\n\r\n'

        We don't use a lib here because it is very easy and we can't get into trouble with libs.

        Here we do all kinds of parsing. Can be modified at will to adapt.
        """ #

        #log.msg("ProxyServerProtocolSuperNET 4 render_GET GET. time---> ",str(time.time()))
        reqMeth = request.split()[1]

        ###################################################################
        #
        # here we have some internal contollers to start and stop use cases, and to stop the whole api
        #
        ###################################################################
        stopSelf = ( reqMeth[:6].decode("utf-8")  == '/stop?')
        if stopSelf:
            log.msg("snApi caught stop- shutting down @ time: "  ,str(time.time()))
            self.transport.loseConnection()
            os.kill(os.getpid(),15)

        startUC = ( reqMeth[:6].decode("utf-8")  == '/ucstart?')
        if startUC:
            log.msg("snApi caught startUC-   @ time: "  ,str(time.time()))
            self.transport.loseConnection()
            return None
        stopUC = ( reqMeth[:6].decode("utf-8")  == '/ucstop?')
        if startUC:
            log.msg("snApi caught stopUC-   @ time: "  ,str(time.time()))
            self.transport.loseConnection()
            return None

        reqOK = ( reqMeth[:5].decode("utf-8")  == '/nxt?') # drop all else snAp.py
        if not reqOK:
            self.transport.write(b'unspecific error in ProxyServerProtocolSuperNET.render_GET')
            self.transport.loseConnection()
            return None

        reqMeth = reqMeth[5:]
        reqMeth = reqMeth.decode()

        reqLi = reqMeth.split('&')
        reqDict = {}

        if len(reqLi) < 1:
            raise LookupError(str(request))
            self.transport.loseConnection()
            return None
            
        for req in reqLi:
            try:
                reqDict[req.split('=')[0]] = req.split('=')[1]
            except:
                raise LookupError(str(request))
                self.transport.loseConnection()

        if 'requestType' not in reqDict.keys():
            self.transport.loseConnection()
            return None

        #
        # This invokes different Client Server/Factory instances depending on what calls are requested.
        # port, parser, qcomposer
        #

        if reqDict['requestType'] in self.proxyServerFactory.qComp_777.API_calls:
            # send to the 777Composer
            # self.clientFactory.protocol - the 'protocol' MUST remain GENERIC!!! keep this Note here.
            self.clientFactory.protocol = ProxyClientProtocol777
            self.clientFactory.protocol.parser_777 = self.proxyServerFactory.parser_777
            self.clientFactory.server = self #
            self.clientFactory.requestType = reqDict['requestType'] # just put it in here to be available for the Parser!
            reactor.connectTCP( SERVER_ADDR_jl777, SERVER_PORT_SUPERNETHTTP, self.clientFactory)
            print(6*"\nreqDict:", reqDict)

            self.newQuery = self.proxyServerFactory.qComp_777.make_777POST_Request(reqDict)
            print(6*"\nquery:", self.newQuery)


        elif reqDict['requestType'] in  ["start","stop" ]:
        # direct to BTCD RPC, use that parser ONLY for START and stop call that must go through BTCD
        # Note: there is a 'passthrough' call in the api to talk to RPC coins.
        # only 'start' and 'stop' can't be issued to SuperNET directly.
            # self.clientFactory.protocol - the 'protocol' MUST remain GENERIC!!! keep this Note here.
            self.clientFactory.protocol = ProxyClientProtocolRPC
            self.clientFactory.protocol.parser_RPC = self.proxyServerFactory.parser_RPC
            self.clientFactory.server = self #
            self.clientFactory.requestType = reqDict['requestType'] # just put it in here to be available for the Parser!
            reactor.connectTCP( SERVER_ADDR_jl777, SERVER_PORT_BTCD_RPC, self.clientFactory)
            # NOTE: this uses the same querycomposer that 777 also uses!!!
            self.newQuery = self.proxyServerFactory.qComp_777.make_rawBytes_Request(reqDict)
            self.transport.loseConnection() # this is because we won't get a reply afte stoppping and we must close ourself!

        elif reqDict['requestType'] in self.proxyServerFactory.qComp_XML.API_calls:
            # self.clientFactory.protocol - the 'protocol' MUST remain GENERIC!!! keep this Note here.
            self.clientFactory.protocol = ProxyClientProtocolXML
            self.clientFactory.protocol.parser_XML = self.proxyServerFactory.parser_XML
            self.clientFactory.server = self #
            self.clientFactory.requestType = reqDict['requestType'] # just put it in here to be available for the Parser!
            reactor.connectTCP(SERVER_ADDR_xmlFeed1, SERVER_PORT_xmlFeed1, self.clientFactory)
            self.newQuery = self.proxyServerFactory.qComp_XML.make_XML_Request(reqDict)

        elif reqDict['requestType'] in self.proxyServerFactory.qComp_LOC.API_calls:
            self.clientFactory.protocol = ProxyClientProtocolLOC
            self.clientFactory.protocol.parser_LOC = self.proxyServerFactory.parser_LOC
            self.clientFactory.server = self #
            self.clientFactory.requestType = reqDict['requestType'] # just put it in here to be available for the Parser!
            #
            # LOCAL handling is different, we don't use POST or GET, but do other stuff as load files or so.
            #
            # use deferToThread in UCclasses
            #
            dataLocalCacheBytes = self.proxyServerFactory.qComp_LOC.make_LOC_Request(reqDict)
            dataLocalCacheParsedBytes = self.proxyServerFactory.parser_LOC.parse_XML( dataLocalCacheBytes, reqDict)
            self.write(dataLocalCacheParsedBytes)
            # call the ClientReceiving Function DIRECTLY here, we don't send the request through the interwebz
            self.newQuery = 'dummyUpForLocCache'
            return None # MAYBE GOOD to do this here because we go to self.write() DIRECTLY FROM HERE!?!?!

        else:
            raise LookupError(str(request))
            self.transport.loseConnection()
            return None

        if self.newQuery == 'error':
            raise LookupError(str(request))
            self.transport.loseConnection()
            return None


    def write(self, data):
        """ Here the processed reply finally leaves the proxy again and goes back to the requester:
            ServerPartOfProxy => WebClient
            This function expects fully processed and formatted reply data, it only returns the data w/o any further processing.
        """ #

        log.msg("ProxyServerProtocolSuperNET 5: proxy returns to client:", str(len(data)), str(type(data)), str((data)[:100]))#
        self.transport.write(data)
        self.transport.loseConnection()


class ProxyClientProtocolLOC(protocol.Protocol):
    """ This ProxyClient does local stuff """#
    pass

class ProxyClientProtocolRPC(protocol.Protocol):
    """ This ProxyClient queries the SuperNET server using POST DIRECTLY RPC """#

    def connectionMade(self):
        self.factory.server.client = self
        try:
            requestOUT = self.factory.server.newQuery     #.decode("utf-8")
        except:
            self.transport.loseConnection()
            return None
        # two end Protocol: here we WRITE out to the remote.
        # we expect the dataReceived back. What if that doenst happen? as in stop or start?
        self.transport.write(requestOUT)
        self.factory.server.requestOUT = '' # cleanup

    def read_raw_ERR(self):
        pass

    # NEED A DEFERRED TO READ RAW
    def read_raw_POST(self, data_RPC):
        print("**** data_777 --->", str(data_RPC))
        pass

    def dataReceived(self, data_RPC):
        """ this receives the RAW reply from the jl777lib. POSTprocessing needs to be done. """ #
        log.msg("ProxyClientProtocolRPC dataReceived - from remoteServer LENGTH:: ", str(len(data_RPC)))
        log.msg("ProxyClientProtocolRPC - from remoteServer data_777: ", str((data_RPC)))
        data_RPC_parsed = self.parser_RPC.parse_RPC(data_RPC, self.factory.requestType )
        self.factory.server.write(data_RPC_parsed)
        self.transport.loseConnection()
        return None

class ProxyClientProtocol777(protocol.Protocol):
    """ This ProxyClient queries the SuperNET server using POST DIRECTLY """#

    def connectionMade(self):

        self.factory.server.client = self
        #log.msg(15*"\n~~~~~~~~~~~~~>", self.factory.server.newQuery)
        try:
            preppedReq777 = self.factory.server.newQuery
        except:
            self.transport.write(b'ERROR in ProxyClientProtocol777.connectionMade')
            self.transport.loseConnection()
            return None
        #log.msg(15*"\n~~~~~~~~~~~~~>", preppedReq777)
        self.deferred = deferToThread(requests.post, FULL_URL, data=json.dumps(preppedReq777), headers= POSTHEADERS)
        self.deferred.addCallback(self.rcvPOST)
        self.deferred.addErrback(self.rcvPOSTERR)

        # stat1 = reactor.threadpool.waiters
        # stat2 = reactor.threadpool.workers
        # stat3 = reactor.threadpool.threads
        # stat4 = reactor.threadpool.q.queue
        #
        # log.msg("waiters: ", stat1)
        # log.msg("workers: ", stat2)
        # log.msg("threads: ", stat3)
        # log.msg("queue: ", stat4)

        # putting this into a Session() object fails miserabley due to some threading!
        # this is for raw transport level bytes writing!
        # self.transport.write(requestOUT)
        # self.factory.server.requestOUT = '' # cleanup

    def rcvPOSTERR(self,retPOSTERR):
        log.msg(10*"\n++++++++++ERRR in ProxyClientProtocol777+++", retPOSTERR, str(retPOSTERR))
        self.factory.server.write("rcvPOSTERR() ERROR")
        self.transport.loseConnection()
        return None


    def rcvPOST(self, data_777):
        """ this receives the RAW reply from the jl777lib. POSTprocessing needs to be done. """ #
        log.msg("ProxyClientProtocol777 dataReceived - from remoteServer type:: ", type(data_777))
        # here we receive the prepared data for sending back through the port to the GET requester
        data_777_parsedBytes = self.parser_777.parse_777(data_777, self.factory.requestType )
        #print(data_777_parsedBytes)
        self.factory.server.write(data_777_parsedBytes) #data_777_parsed)
        self.transport.loseConnection()
        return None


class ProxyClientProtocolXML(protocol.Protocol):
    """ This ProxyClient is using the TWISTED getPage function """#

    def connectionMade(self):
        self.factory.server.client = self

        try:

            requestOUT = self.factory.server.newQuery     #.decode("utf-8")

        except:
            self.transport.loseConnection()
            return None

        self.getPage_deferred =  getPage(requestOUT)
        # """can I do multiple here??"""

        self.getPage_deferred.addCallback(self.pageReceived)
        self.getPage_deferred.addErrback(self.handleFailure)
        self.factory.server.requestOUT = ''
        self.query_xmlFeed1 = False
        log.msg("-2e--ProxyClientProtocolXML----requestOUT   -----register deferred ---------->:",requestOUT) # only for GET , ppOST is different

 
    # Server => Proxy
    def handleFailure(self, err):
        raise RuntimeError(str(err))
                
    # this will be the deferreed
    def pageReceived(self, data_XML):

        log.msg("3 ProxyClientProtocolXML dataReceived - from remoteServer: ", str(len(data_XML)))
        log.msg(1*"\n3a dataReceived - from remoteServer: ", str(data_XML)[:200])

        print(self.parser_XML)
        print(self.parser_XML.parse_XML)
        print(self.factory.requestType)
        data_XML_parsed = self.parser_XML.parse_XML(data_XML,  self.factory.requestType)

        self.factory.server.write(data_XML_parsed)
        self.transport.loseConnection()
        return None





class SuperNETApiD(Daemon3):


    """ This is the SuperNET API Main class.
         This is instantiated by the DEMON controller app.
         This is supposed to be a singleton,
        and so are the class objects that are declared up here.  """#



    # instead of doing this in the class head here, we could also make a local method 'def makeContext'
    environ['snApiDir'] = os.getcwd()
    environ['localCacheDir'] = os.getcwd() + environ['CACHE_DIR']
    # note: there is something really unpleasant going on with the 'environ name here!
    # this creates the ApiCOntext!

    qComp_777 = QueryComposer_777(environ) # Querycomposer is part of the SERVER part, composes the query, and hands the Q to the CLIENT part.
    qComp_XML = QueryComposer_XML(environ)
    qComp_LOC = QueryComposer_LOC(environ)
    #qComp_RPC = QueryComposer_RPC(environ)


    parser_XML = Parser_XML(environ)
    parser_777 = Parser_777(environ)
    parser_RPC = Parser_RPC(environ)
    parser_LOC = Parser_LOC(environ)

    parsers = {
                'parser_XML':  parser_XML,\
                'parser_777':  parser_777,\
                'parser_RPC':  Parser_RPC,\
                'parser_LOC':  parser_LOC
                }

    queryComposers = {
                        'qComp_777': qComp_777,\
                        'qComp_XML': qComp_XML,\
                        'qComp_LOC': qComp_LOC
                        }




    UCs = [
            'start', 'stop', 'restart',
            'UC1', 'UC2', 'UC3', 'UC4', 'UC5', 'UC6',
            'UC7', 'UC8', 'UC9', 'UC10', 'UC11','UC12',
            ]


    def __init__(self, pidfile):
        self.environ = environ
        super(SuperNETApiD, self).__init__(pidfile)




    def run(self):
        log.msg("calling init")
        self.init()
        log.msg("init() done. starting reactor.run()")
        reactor.run()



    def init(self):
        """
        serverfactory gets all parsers and qcomps, and builds the clientFactories according to what is supposed to happen
        name scoping is very tricky here. In case of problems, check the object instance identities by print(self) here!
        The SERVERfactory always the same object! It does NOT get re-instantiated with each new call.
        Factory is somewhat flexible as to what argument types it gets! """#

        log.startLogging(sys.stdout) # check: logfile or other output ?
        # factory for ad hoc requests received from external sources
        serverFactory = nxtServerFactory(SuperNETApiD.queryComposers, SuperNETApiD.parsers, self.environ)
        serverFactory.protocol = ProxyServerProtocolSuperNET # <- this is not an instance this is the CLASS!!!!

        reactor.suggestThreadPoolSize(500) # should be ok
        log.msg("stats: ",reactor.threadpool.dumpStats())
        log.msg("workers: ", tp.ThreadPool.workers)

        serverFactory.reactor = reactor

        uc_scd_XML_SportsdataLLC = UC_Scheduler_XML(serverFactory,  self.environ ) # environ has the credentials and all
        timer1 = task.LoopingCall(uc_scd_XML_SportsdataLLC.periodic,  )
        timer1.start( TIMER_15000, now=True ) # slow heartbeat, start now TODO: the NOW does not seem to work!
        reactor.listenTCP(LISTEN_PORT_SNT, serverFactory)

        # can make as many as we want here with specific timers and tasks







    def runUC(self, UC):
        log.msg( 1 * "start UC: ", UC)


        if UC in self.UCs:
            print("UC1 - 0")
            self.initUC(UC)
        else:
            log.msg("UC name error")


        log.msg("initUC() done. starting reactor.run()")
        reactor.run()


    def initUC(self, UC):
        """
        serverfactory gets all parsers and qcomps, and builds the clientFactories according to what is supposed to happen
        name scoping is very tricky here. In case of problems, check the object instance identities by print(self) here!
        The SERVERfactory always the same object! It does NOT get re-instantiated with each new call.
        Factory is somewhat flexible as to what argument types it gets!
        """#

        self.UC_results = {'here we can collect results for individual test cases' : True}

        if UC == 'UC1':
            self.startUC1()
        elif UC == 'UC2':
            self.startUC2()
        elif UC == 'UC3':
            self.startUC3()
        elif UC == 'UC4':
            self.startUC4()
        elif UC == 'UC5':
            self.startUC5()
        elif UC == 'UC6':
            self.startUC6()
        elif UC == 'UC7':
            self.startUC7()
        elif UC == 'UC8':
            self.startUC8()
        elif UC == 'UC9':
            self.startUC9()
        elif UC == 'UC10':
            self.startUC10()
        elif UC == 'UC11':
            self.startUC11()
        elif UC == 'UC12':
            self.startUC12()

        else:
            log.msg("UC name error")



    def startUC1(self):
        log.startLogging(sys.stdout)
        serverFactory = nxtServerFactory(SuperNETApiD.queryComposers, SuperNETApiD.parsers, self.environ)
        serverFactory.protocol = ProxyServerProtocolSuperNET # <- this is not an instance this is the CLASS!!!!
        log.msg(1*"initUC1")
        uc1_pingPong = UC1_pingPong(serverFactory,  self, self.environ ,  ) # also hand in 'self' here as a means to stop self
        self.timer1 = task.LoopingCall(uc1_pingPong.periodic,  )
        self.timer1.start( TIMER_850 , now=True )
        reactor.suggestThreadPoolSize(500)
        reactor.listenTCP(LISTEN_PORT_SNT, serverFactory)

    def stopUC1(self, result):
        log.msg(1*"\n                           STOP UC1 with result: ", result, "\n")
        self.timer1.stop( )
        #self.stop()
        self.startUC2()


    def startUC2(self):
        log.startLogging(sys.stdout)
        serverFactory = nxtServerFactory(SuperNETApiD.queryComposers, SuperNETApiD.parsers, self.environ)
        serverFactory.protocol = ProxyServerProtocolSuperNET # <- this is not an instance this is the CLASS!!!!
        log.msg(1*"initUC2")
        uc2_havenode = UC2_havenode(serverFactory, self, self.environ )
        reactor.suggestThreadPoolSize(500)
        serverFactory.reactor = reactor # this # is only used ATM to access to access thread stats
        try:
            reactor.listenTCP(LISTEN_PORT_SNT, serverFactory)
        except Exception as e:
            log.msg("already listening, continue.{0}".format(str(e)))

        self.timer2 = task.LoopingCall(uc2_havenode.periodic,  )
        self.timer2.start( TIMER_850 , now=True )


    def stopUC2(self, result):
        log.msg(5*"\n\n                           STOP UC2 with result:  ", result, "\n")
        self.timer2.stop( )
        #self.stop()
        self.startUC3()


    def startUC3(self):
        log.startLogging(sys.stdout)
        serverFactory = nxtServerFactory(SuperNETApiD.queryComposers, SuperNETApiD.parsers, self.environ)
        serverFactory.protocol = ProxyServerProtocolSuperNET # <- this is not an instance this is the CLASS!!!!
        log.msg(10*"\ninitUC3")
        uc3_store_findvalue = UC3_store_findvalue(serverFactory, self, self.environ )
        serverFactory.reactor = reactor # this # is only used ATM to access to access thread stats
        reactor.suggestThreadPoolSize(500)
        try:
            reactor.listenTCP(LISTEN_PORT_SNT, serverFactory)
        except Exception as e:
            log.msg("already listening, continue.{0}".format(str(e)))

        self.timer3 = task.LoopingCall(uc3_store_findvalue.periodic,  )
        self.timer3.start( TIMER_850 , now=True )


    def stopUC3(self, result):
        log.msg(5*"\n\n                           STOP UC3 with result:  ", result, "\n")
        self.timer3.stop( )
        log.msg("STOP snappyDaemon")
        #self.stop()
        self.startUC4()


    def startUC4(self):
        log.startLogging(sys.stdout)
        serverFactory = nxtServerFactory(SuperNETApiD.queryComposers, SuperNETApiD.parsers, self.environ)
        serverFactory.protocol = ProxyServerProtocolSuperNET # <- this is not an instance this is the CLASS!!!!
        log.msg(1*"initUC4")
        reactor.suggestThreadPoolSize(500) # should be ok
        serverFactory.reactor = reactor # this # is only used ATM to access to access thread stats
        try:
            reactor.listenTCP(LISTEN_PORT_SNT, serverFactory) # this is needed to also recevies GET queries
        except Exception as e:
            log.msg("already listening, continue.{0}".format(str(e)))

        uc4_sendMSG = UC4_sendMSG(serverFactory, self,  self.environ )

        self.timer4 = task.LoopingCall(uc4_sendMSG.periodic,  )
        self.timer4.start( TIMER_850, now=True )



    def stopUC4(self,result):
        log.msg(5*"\n\n                           STOP UC4 with result:  ", result, "\n")
        self.timer4.stop( )
        log.msg("STOP snappyDaemon")
        #self.stop()
        self.startUC5()


    def startUC5(self):
        log.startLogging(sys.stdout)
        serverFactory = nxtServerFactory(SuperNETApiD.queryComposers, SuperNETApiD.parsers, self.environ)
        serverFactory.protocol = ProxyServerProtocolSuperNET # <- this is not an instance this is the CLASS!!!!
        log.msg(1*"initUC5")
        reactor.suggestThreadPoolSize(500) # should be ok
        serverFactory.reactor = reactor # this # is only used ATM to access to access thread stats
        try:
            reactor.listenTCP(LISTEN_PORT_SNT, serverFactory) # this is needed to also recevies GET queries
        except Exception as e:
            log.msg("already listening, continue.{0}".format(str(e)))

        uc5_sendBIN = UC5_sendBIN(serverFactory, self,  self.environ )

        self.timer5 = task.LoopingCall(uc5_sendBIN.periodic,  )
        self.timer5.start( TIMER_850 , now=True )


    def stopUC5(self,result):
        log.msg(5*"\n\n                           STOP UC5 with result:  ", result, "\n")
        self.timer5.stop( )
        log.msg("STOP snappyDaemon")
        #self.stop()
        self.startUC6()




    def startUC6(self):
        log.startLogging(sys.stdout)
        serverFactory = nxtServerFactory(SuperNETApiD.queryComposers, SuperNETApiD.parsers, self.environ)
        serverFactory.protocol = ProxyServerProtocolSuperNET # <- this is not an instance this is the CLASS!!!!
        log.msg(1*"initUC6")
        reactor.suggestThreadPoolSize(500) # should be ok
        serverFactory.reactor = reactor # this # is only used ATM to access to access thread stats
        try:
            reactor.listenTCP(LISTEN_PORT_SNT, serverFactory) # this is needed to also recevies GET queries
        except Exception as e:
            log.msg("already listening, continue.{0}".format(str(e)))

        uc6_checkMSG = UC6_checkMSG(serverFactory, self,  self.environ )

        self.timer6 = task.LoopingCall(uc6_checkMSG.periodic,  )
        self.timer6.start( TIMER_850 , now=True )


    def stopUC6(self,result):
        log.msg(5*"\n\n                           STOP UC6 with result:  ", result, "\n")
        self.timer6.stop( )
        log.msg("STOP snappyDaemon")
        #self.stop()
        self.startUC7()





    def startUC7(self):
        log.startLogging(sys.stdout)
        serverFactory = nxtServerFactory(SuperNETApiD.queryComposers, SuperNETApiD.parsers, self.environ)
        serverFactory.protocol = ProxyServerProtocolSuperNET # <- this is not an instance this is the CLASS!!!!
        log.msg(1*"initUC7")
        reactor.suggestThreadPoolSize(500) # should be ok
        serverFactory.reactor = reactor # this # is only used ATM to access to access thread stats
        try:
            reactor.listenTCP(LISTEN_PORT_SNT, serverFactory) # this is needed to also recevies GET queries
        except Exception as e:
            log.msg("already listening, continue.{0}".format(str(e)))

        uc7_findaddress = UC7_findaddress(serverFactory, self,  self.environ )

        self.timer7 = task.LoopingCall(uc7_findaddress.periodic,  )
        self.timer7.start( TIMER_850 , now=True )

    def stopUC7(self,result):
        log.msg(5*"\n\n                           STOP UC7 with result:  ", result, "\n")
        self.timer7.stop( )
        log.msg("STOP snappyDaemon")
        self.stop()
        #self.startUC8()




    def startUC8(self):
        log.startLogging(sys.stdout)
        serverFactory = nxtServerFactory(SuperNETApiD.queryComposers, SuperNETApiD.parsers, self.environ)
        serverFactory.protocol = ProxyServerProtocolSuperNET # <- this is not an instance this is the CLASS!!!!
        log.msg(1*"initUC8")
        reactor.suggestThreadPoolSize(500) # should be ok
        serverFactory.reactor = reactor # this # is only used ATM to access to access thread stats
        try:
            reactor.listenTCP(LISTEN_PORT_SNT, serverFactory) # this is needed to also recevies GET queries
        except Exception as e:
            log.msg("already listening, continue.{0}".format(str(e)))

        uc8_contacts = UC8_contacts(serverFactory, self,  self.environ )

        self.timer8 = task.LoopingCall(uc8_contacts.periodic,  )
        self.timer8.start( TIMER_850 , now=True )

    def stopUC8(self,result):
        log.msg(5*"\n\n                           STOP UC8 with result:  ", result, "\n")
        self.timer8.stop( )
        log.msg("STOP snappyDaemon")
        self.stop()





    def startUC9(self):
        log.startLogging(sys.stdout)
        serverFactory = nxtServerFactory(SuperNETApiD.queryComposers, SuperNETApiD.parsers, self.environ)
        serverFactory.protocol = ProxyServerProtocolSuperNET # <- this is not an instance this is the CLASS!!!!
        log.msg(1*"initUC9")
        reactor.suggestThreadPoolSize(500) # should be ok
        serverFactory.reactor = reactor # this # is only used ATM to access to access thread stats
        try:
            reactor.listenTCP(LISTEN_PORT_SNT, serverFactory) # this is needed to also recevies GET queries
        except Exception as e:
            log.msg("already listening, continue.{0}".format(str(e)))

        uc9_getdb = UC9_getdb(serverFactory, self,  self.environ )

        self.timer9 = task.LoopingCall(uc9_getdb.periodic,  )
        self.timer9.start( TIMER_850 , now=True )

    def stopUC9(self,result):
        log.msg(5*"\n\n                           STOP UC9 with result:  ", result, "\n")
        self.timer9.stop( )
        log.msg("STOP snappyDaemon")
        self.stop()



    def startUC10(self):
        log.startLogging(sys.stdout)
        serverFactory = nxtServerFactory(SuperNETApiD.queryComposers, SuperNETApiD.parsers, self.environ)
        serverFactory.protocol = ProxyServerProtocolSuperNET # <- this is not an instance this is the CLASS!!!!
        log.msg(1*"initUC10")
        reactor.suggestThreadPoolSize(500) # should be ok
        serverFactory.reactor = reactor # this # is only used ATM to access to access thread stats
        try:
            reactor.listenTCP(LISTEN_PORT_SNT, serverFactory) # this is needed to also recevies GET queries
        except Exception as e:
            log.msg("already listening, continue.{0}".format(str(e)))

        uc10_IDEX_placeAB  = UC10_IDEX_placeAB(serverFactory, self,  self.environ )

        self.timer10 = task.LoopingCall(uc10_IDEX_placeAB.periodic,  )
        self.timer10.start( TIMER_850 , now=True )

    def stopUC10(self,result):
        log.msg(5*"\n\n                           STOP UC10 with result:  ", result, "\n")
        self.timer10.stop( )
        log.msg("STOP snappyDaemon")
        self.stop()



    def startUC11(self):
        log.startLogging(sys.stdout)
        serverFactory = nxtServerFactory(SuperNETApiD.queryComposers, SuperNETApiD.parsers, self.environ)
        serverFactory.protocol = ProxyServerProtocolSuperNET # <- this is not an instance this is the CLASS!!!!
        log.msg(1*"initUC11")
        reactor.suggestThreadPoolSize(500) # should be ok
        serverFactory.reactor = reactor # this # is only used ATM to access to access thread stats
        try:
            reactor.listenTCP(LISTEN_PORT_SNT, serverFactory) # this is needed to also recevies GET queries
        except Exception as e:
            log.msg("already listening, continue.{0}".format(str(e)))

        uc11_priceDB  = UC11_priceDB(serverFactory, self,  self.environ )

        self.timer11 = task.LoopingCall(uc11_priceDB.periodic,  )
        self.timer11.start( TIMER_850 , now=True )

    def stopUC11(self,result):
        log.msg(5*"\n\n                           STOP UC11 with result:  ", result, "\n")
        self.timer11.stop( )
        log.msg("STOP snappyDaemon")
        self.stop()




    def startUC12(self):
        log.startLogging(sys.stdout)
        serverFactory = nxtServerFactory(SuperNETApiD.queryComposers, SuperNETApiD.parsers, self.environ)
        serverFactory.protocol = ProxyServerProtocolSuperNET # <- this is not an instance this is the CLASS!!!!
        log.msg(1*"initUC12")
        reactor.suggestThreadPoolSize(500) # should be ok
        serverFactory.reactor = reactor # this # is only used ATM to access to access thread stats
        try:
            reactor.listenTCP(LISTEN_PORT_SNT, serverFactory) # this is needed to also recevies GET queries
        except Exception as e:
            log.msg("already listening, continue.{0}".format(str(e)))

        uc12_save_restore_File = UC12_save_restore_File(serverFactory, self,  self.environ )

        self.timer12 = task.LoopingCall(uc12_save_restore_File.periodic,  )
        self.timer12.start( TIMER_850 , now=True )

    def stopUC12(self,result):
        log.msg(5*"\n\n                           STOP UC12 with result:  ", result, "\n")
        self.timer12.stop( )
        log.msg("STOP snappyDaemon")
        self.stop()



if __name__ == "__main__":


    pidFileName = '/tmp/SuperNET_API.pid'
    superNetApiD = SuperNETApiD(pidFileName) # '/tmp/daemon-example.pid')
    #
    # Note:
    # we are using standard Daemonization here and NOT twistd,
    # becasue that seems to be not properly ported to python3 yet.
    # Also, it is difficult to understand and badly documented.
    # It is better to do it with the standard python recipe, and have opportunity of intervention.
    #
    # Also, the sequence of starting reactor and Daemon is sensitive!


    UCs = [
            'start', 'stop', 'restart',
            'UC1', 'UC2', 'UC3', 'UC4', 'UC5', 'UC6',
            'UC7', 'UC8','UC9', 'UC10', 'UC11','UC12',
            ]



    if len(sys.argv) == 2:
        UC=sys.argv[1]
        if UC not in UCs:
            print("Unknown command")
            sys.exit(2)

        if 'start' == sys.argv[1]:
            superNetApiD.start()
        elif 'stop' == sys.argv[1]:
            superNetApiD.stop()
        elif 'restart' == sys.argv[1]:
            superNetApiD.restart()

        else:
            superNetApiD.startUC(UC)




        sys.exit(0)

    else:
        print("usage: %s start|stop|restart|UC" % sys.argv[0])
        sys.exit(2)
