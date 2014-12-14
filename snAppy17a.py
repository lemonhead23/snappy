#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
#



"""#

from twisted.internet import reactor
#from twisted.internet.protocol import ClientFactory, ServerFactory

from twisted.internet import task

import sys, time
import os
from snAppyModules.snUseCases import *
from snAppyModules.snQueryComposers import *
from snAppyModules.snParsers import *
from snAppyModules.snAppyConfig import *
from snAppyModules.pyDaemon3 import Daemon3

#from snAppyModules.snApiConfig import environ
#import requests
#from twisted.internet.defer import Deferred
#import twisted.web.client as cli
#from twisted.web.client import getPage
#from io import StringIO # io.BytesIO
#from lxml import etree
#from datetime import datetime
#from twisted.python import log




class nxtClientFactory(ClientFactory):
    
    def __init__(self, ):
        super(nxtClientFactory, self).__init__()
        #log.msg("2c --nxtClientFactory---->  build Client Protocol" )
        self.ok=True



class nxtServerFactory(ServerFactory):

    def __init__(self,queryComposers, parsers, environ):
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
            #log.msg("ProxyServerProtocolSuperNET 2a::\n\n", str(rawRequest))
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
            self.newQuery = self.proxyServerFactory.qComp_777.make_777POST_Request(reqDict)

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
        # putting this into a Session() object fails miserabley due to some threading!
        # this is for raw transport level bytes writing!
        # self.transport.write(requestOUT)
        # self.factory.server.requestOUT = '' # cleanup

    def rcvPOSTERR(self,retPOSTERR):
        log.msg(30*"\n++++++++++ERRR+++++", retPOSTERR)

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





class SuperNETApiD(Daemon3): #object):


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
    parser_RPC = Parser_RPC(environ) #TODO
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


    def __init__(self, pidfile):
        self.environ = environ
        super(SuperNETApiD, self).__init__(pidfile)


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

        uc_scd_XML_SportsdataLLC = UC_Scheduler_XML(serverFactory,  self.environ ) # environ has the credentials and all
        timer1 = task.LoopingCall(uc_scd_XML_SportsdataLLC.periodic,  )
        timer1.start( TIMER1_SportsdataLLC_SECS, now=True ) # slow heartbeat, start now TODO: the NOW does not seem to work!
        # can make as many as we want here with specific timers and tasks

        reactor.suggestThreadPoolSize(500) # should be ok
        reactor.listenTCP(LISTEN_PORT_SNT, serverFactory)

        # a scheduler for statusInfo




    def run(self):
        print("calling init")
        self.init()
        print("going hot: reactor.run()")
        reactor.run()

    def runUC(self, UC):
        print(1*"\ncalling initTests")

        if UC == 'UC1':
            self.initUC1()
        elif UC == 'UC2':
            self.initUC2()
        elif UC == 'UC3':
            self.initUC3()
        print("going hot: reactor.run()")
        reactor.run()



    def initUC1(self):
        """
        serverfactory gets all parsers and qcomps, and builds the clientFactories according to what is supposed to happen
        name scoping is very tricky here. In case of problems, check the object instance identities by print(self) here!
        The SERVERfactory always the same object! It does NOT get re-instantiated with each new call.
        Factory is somewhat flexible as to what argument types it gets!
        """#

        log.startLogging(sys.stdout)
        serverFactory = nxtServerFactory(SuperNETApiD.queryComposers, SuperNETApiD.parsers, self.environ)
        serverFactory.protocol = ProxyServerProtocolSuperNET # <- this is not an instance this is the CLASS!!!!
        print(1*"\ninitUC1")
        #
        #  here we can build as many different schedulers as we want!
        #
        ucTEST_1_pingWhtList = UCTEST_1_ping_whitelist_777(serverFactory,  self.environ )
        timer2 = task.LoopingCall(ucTEST_1_pingWhtList.periodic,  )
        timer2.start( TIMER2_Freq , now=True )
        #
        reactor.suggestThreadPoolSize(500) # should be ok
        reactor.listenTCP(LISTEN_PORT_SNT, serverFactory)

    def initUC2(self):
        """
        serverfactory gets all parsers and qcomps, and builds the clientFactories according to what is supposed to happen
        name scoping is very tricky here. In case of problems, check the object instance identities by print(self) here!
        The SERVERfactory always the same object! It does NOT get re-instantiated with each new call.
        Factory is somewhat flexible as to what argument types it gets!
        """#

        log.startLogging(sys.stdout)
        serverFactory = nxtServerFactory(SuperNETApiD.queryComposers, SuperNETApiD.parsers, self.environ)
        serverFactory.protocol = ProxyServerProtocolSuperNET # <- this is not an instance this is the CLASS!!!!
        print(1*"\ninitUC2")
        #
        #  here we can build as many different schedulers as we want!
        #
        ucTEST_2 = UCTEST_2_ping_findnode(serverFactory,  self.environ )
        timer2 = task.LoopingCall(ucTEST_2.periodic,  )
        timer2.start( TIMER2_Freq , now=True )

        #
        reactor.suggestThreadPoolSize(500) # should be ok
        reactor.listenTCP(LISTEN_PORT_SNT, serverFactory)



    def initUC3(self):
        """
        serverfactory gets all parsers and qcomps, and builds the clientFactories according to what is supposed to happen
        name scoping is very tricky here. In case of problems, check the object instance identities by print(self) here!
        The SERVERfactory always the same object! It does NOT get re-instantiated with each new call.
        Factory is somewhat flexible as to what argument types it gets!
        """#

        log.startLogging(sys.stdout)
        serverFactory = nxtServerFactory(SuperNETApiD.queryComposers, SuperNETApiD.parsers, self.environ)
        serverFactory.protocol = ProxyServerProtocolSuperNET # <- this is not an instance this is the CLASS!!!!
        print(1*"\ninitUC3")
        #
        #  here we can build as many different schedulers as we want!
        #
        ucTEST_3 = UCTEST_3_store_findvalue(serverFactory,  self.environ )
        timer3 = task.LoopingCall(ucTEST_3.periodic,  )
        timer3.start( TIMER3_Freq , now=True )

        #
        reactor.suggestThreadPoolSize(500) # should be ok
        reactor.listenTCP(LISTEN_PORT_SNT, serverFactory)






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

    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            superNetApiD.start()
        elif 'stop' == sys.argv[1]:
            superNetApiD.stop()
        elif 'restart' == sys.argv[1]:
            superNetApiD.restart()
        elif 'UC1' == sys.argv[1]:
            superNetApiD.startUC('UC1')
        elif 'UC2' == sys.argv[1]:
            superNetApiD.startUC('UC2')
        elif 'UC3' == sys.argv[1]:
            superNetApiD.startUC('UC3')

        #...
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)

    else:
        print("usage: %s start|stop|restart" % sys.argv[0])
        sys.exit(2)
