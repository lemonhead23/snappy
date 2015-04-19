#!/usr/bin/python3
# -*- coding: utf-8 -*-

import base64


##################
##################
##################

class QC_XMLBase(object):
    """ The base class can be used for common functions and declarations if needed """#
    pass


##################
##################
##################


class QC_XML_Golf1(QC_XMLBase):
    example = True


class QC_XML_Soccer1(QC_XMLBase):
    """ this class has all particulars for ONE xml data source - FEED or market.
         Other Data sources have their own classes
         THIS CAN BE SPLIT INTO CLASSES TOO!!!
         SOCCER BASE CLASS with details, and the calls inherit from that
        """#

# #ToDo: systematically organize the data feed details: credentials and paths and variables as IDs and dates
# ToDo: get this from CONFIG!!!!!

    baseURL = 'http://api.sportsdatallc.org'
    category = 'soccer-t2/eu'
    match = 'matches/2014/08/22/summary.xml'
    apiKey = '?api_key=fv37s4rd2arqqxav774wb2kc'

    def __init__(self):
        super(QC_XML_Soccer1, self).__init__()
        self.OK = True

    def assembleQuery(self, fragments):
        """ fragments is a tuple """#
        qString = ''
        for fragment in fragments:
            qString += (fragment + '/')
        qString = qString[:-1] # drop trailing '/'
        qString += self.apiKey
        requestOUT = qString.encode("utf-8")
        return requestOUT
    # this needs to be made much more robust and modular, but works as it is

    def getMatchSummary(self, params):
        """ compose the specific request from the particulars HERE! """#

        fragments  = (self.baseURL , self.category, self.match,  )
        if params:
            pass
        requestOUT = self.assembleQuery(fragments)
        return requestOUT

    def getAllCategories(self, params):
        """ compose the specific request from the particulars HERE! """#
        fragments  = ()
        if params:
            pass
        #requestOUT = self.assembleQuery(fragments)
        requestOUT = 'http://api.sportsdatallc.org/soccer-t2/eu/matches/2014/08/22/summary.xml?api_key=fv37s4rd2arqqxav774wb2kc'.encode("utf-8")
        return requestOUT

    def getNewsFeed(self, params):
        """ compose the specific request from the particulars HERE! """#
        fragments  = ()
        if params:
            pass
        #requestOUT = self.assembleQuery(fragments)
        requestOUT = 'http://api.sportsdatallc.org/soccer-t2/eu/matches/2014/08/22/summary.xml?api_key=fv37s4rd2arqqxav774wb2kc'.encode("utf-8")
        return requestOUT


##################
##################
##################
##################
#
# wrapper class below
#
##################
##################
##################


class QueryComposer_XML(QC_XMLBase):
    """ This is the wrapper class to compose the specific details of the query that is sent to the data provider service
        The detail classes will need all the specifics as configurations, credentials, paths etc on the data sources.

    """ #
    # not used but may be helpful


    API_calls = [
                    'getNewsFeed',
                    'getAllCategories',
                    'getSubCategoriesByCategories',
                    'getMatchSummary',
                    'MOAR!'
                ]

    xml_Soccer1 = QC_XML_Soccer1()
    xml_Golf1 = QC_XML_Golf1()

    def __init__(self, environ = {}):
        self.environ = environ
        super(QueryComposer_XML, self).__init__()
        #self.scheduler = scheduler
        print("here we compose the specific details of the query that is sent to the data provider service")
        ok=True


    # the calls must be routed to the particular FEEDS depending on their params,
    # IE getSOCCER goes to a different class than getGOLF!!!

    def make_XML_Request(self, reqDict):
        """ Route the request to the proper composer class with the feed particulars """ #

        #log.msg("----QueryComposer---------> composeGET")
        if reqDict['requestType'] == 'getAllCategories':    # getAllCategories -> this may be a LOC !?!?!?!!!!!!!
            params = None
            requestOUT = self.xml_Soccer1.getAllCategories(params)
            return requestOUT

        elif reqDict['requestType'] == 'getNewsFeed':
            params = None
            requestOUT = self.xml_Soccer1.getNewsFeed(params)
            return requestOUT

        elif reqDict['requestType'] == 'getMatchSummary':
            params = None
            requestOUT = self.xml_Soccer1.getMatchSummary(params)
            return requestOUT

        elif reqDict['requestType'] == 'getGolfTest':
            params = None
            requestOUT = self.xml_Golf1.getMatchSummary(params)
            return requestOUT

        else:
            raise LookupError




##########################
##########################
##########################
##########################
##
## in this modular manner, we can use MULTIPLE XML sources!
##
##########################
##########################
##########################
##########################




class QC_777Base(object):
    """ The base class can be used for common functions and declarations if needed
    This can maybe be changed to use normal PST requests and deferToThreadPool

    """#
    # ToDo: USE deferToThread here- better! but not critical atm
    #
    def __init__(self, environ):
        #print( environ)
    #    def create_base64_encoded_Creds(self):
        self.BitcoinDarkRPCCreds = environ['BitcoinDarkRPCCreds']
        user = self.BitcoinDarkRPCCreds['user']
        rpcPw = self.BitcoinDarkRPCCreds['rpcPw']
        creds = user + ':' + rpcPw
        encoded = base64.b64encode(creds.encode("utf-8"))
        self.BTCDCreds =  encoded.decode()
        #self.reqBaseOld = 'POST / HTTP/1.1\r\nAuthorization: Basic YXp1cmU6SXI5cURtaWNudFR4SDhD\r\nUser-Agent: curl/7.35.0\r\nHost: 127.0.0.1:14632\r\nAccept: */*\r\ncontent-type: text/plain;\r\nContent-Length: '
        self.reqBase1 = 'POST / HTTP/1.1\r\nAuthorization: Basic '
        self.reqBase2 = '\r\nUser-Agent: curl/7.35.0\r\nHost: 127.0.0.1:14632\r\nAccept: */*\r\ncontent-type: text/plain;\r\nContent-Length: '
        self.reqBase = self.reqBase1 + self.BTCDCreds +  self.reqBase2


    def assembleQuery(self, parms):
        """ fragments is a tuple    # ToDo: tune later!
         """# # ToDo: this may be possible to be done much more elegant

        jsonSpecs = ''
        try:
            for parm in parms:
                jsonSpecs += self.quot + parm[0] + self.quot + self.colon + self.quot + parm[1] + self.quot + ','
                # first add then drop trailing comma of last kv pair later general
        except:
             error = 'error: parameter composition for query: ' + "K0"
             return error
        jsonSpecs = jsonSpecs[:-1] # drop trailing ','


        print(1*"\n***********jsonSpecs ", jsonSpecs)
        return jsonSpecs


##################
##################
##################



class QC_777_iDex(QC_777Base):

    colon = ':'
    quot = '\\"'


class QC_777_aAll(QC_777Base):

    colon = ':'
    quot = '\\"'


    """
        //  privatebet 1
        // glue 7
        // passthru 2
        // ramchains 11
        // MGW 8
        // IPcomms 5
        // Kademlia DHT  6
        // MofNfs 3
        // Telepathy 9
        // Teleport 3
        // InstantDEX 6
        // Tradebot 3
        // privatebet 1


Parameters of api calls as extracted from api.h:

several calls are internal only, nit be to be called by the user
"V" is just a flag to verify not a real param

so skip the first three and the zero at the end

can use more soph. exception handling later
    """

    #########################





    #     // glue 7
    ######################### reqDict['']


    def gotjson(self, reqDict):
        """ individual treatment of requests and their parms here
    static char *gotjson[] = { (char *)gotjson_func, "BTCDjson", "", "json", 0 };

    """#
        K0 = 'requestType'
        P0 = 'gotjson'

        try:
            K1 = 'json'
            P1 = reqDict['json']
        except:
            P1 = ''

        #parms = ( (K0,P0), (K1,P1),)
        #jsonSpecs = self.assembleQuery(parms)

        return  { K0 : P0 , K1 : P1 ,  }



    def gotpacket(self, reqDict):
        """ individual treatment of requests and their parms here static char *gotpacket[] = { (char *)gotpacket_func, "gotpacket", "", "msg", "dur", "ip_port", 0 };
"""#
        K0 = 'requestType'
        P0 = 'gotpacket'
        try:
            K1 = 'msg'
            P1 = reqDict['msg']
        except:
            P1 = ''
        try:
            K2 = 'dur'
            P2= reqDict['dur']
        except:
            P2 = ''


        try:
            K3 = 'ip_port'
            P3 = reqDict['ip_port']
        except:
            P3 = ''


        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,}

            #
            # parms = ( (K0,P0), (K1,P1), (K2,P2), (K3,P3), )
            # jsonSpecs = self.assembleQuery(parms)
            #
            # return jsonSpecs


    def gotnewpeer(self, reqDict):
        """ individual treatment of requests and their parms here     static char *gotnewpeer[] = { (char *)gotnewpeer_func, "gotnewpeer", "", "ip_port", 0 };
"""#
        K0 = 'requestType'
        P0 = 'gotnewpeer'
        try:
            K1 = 'ip_port'
            P1 = reqDict['ip_port']
        except:
            P1 = ''

        return  { K0 : P0 , K1 : P1 , }
        #
        # parms = ( (K0,P0),  (K1,P1), )
        # jsonSpecs = self.assembleQuery(parms)
        #
        # return jsonSpecs


    def BTCDpoll(self, reqDict):
        """ individual treatment of requests and their parms here
    static char *BTCDpoll[] = { (char *)BTCDpoll_func, "BTCDpoll", "", 0 };
 """#
        K0 = 'requestType'
        P0 = 'BTCDpoll'

        return  { K0 : P0 ,  }


    def GUIpoll(self, reqDict):
        """ individual treatment of requests and their parms here
    static char *GUIpoll[] = { (char *)GUIpoll_func, "GUIpoll", "", 0 };

curl -k --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "SuperNET", "params": ["{\"requestType\":\"GUIpoll\"}"]  }' -H 'content-type: text/plain;' https://127.0.0.1:7777/

{"result":"nothing pending"}


curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=GUIpoll'
 """#

        K0 = 'requestType'
        P0 = 'GUIpoll'
        return  { K0 : P0 ,  }



    def stop(self, reqDict):
        """ individual treatment of requests and their parms here
    static char *stop[] = { (char *)stop_func, "stop", "", 0 };
"""#
        K0 = 'requestType'
        P0 = 'stop'
        # THIS IS GOING TO RPC ONLY TO BTCD NOT TO SUPERNET SERVER!
        parms = ( (K0,P0),   )
        jsonSpecs = self.assembleQuery(parms)
        return jsonSpecs
        # this has to use OLD raw style for BTCD! return  { K0 : P0 ,  }


    def start(self, reqDict):
        """ individual treatment of requests and their parms here
    static char *stop[] = { (char *)stop_func, "stop", "", 0 };
"""#
        K0 = 'requestType'
        P0 = 'start'
        parms = ( (K0,P0),   )
        jsonSpecs = self.assembleQuery(parms)
        return jsonSpecs
        # this has to use OLD raw style for BTCD! return  { K0 : P0 ,  }



    def settings(self, reqDict):
        """ individual treatment of requests and their parms here
        OK using snApi @7800
        curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=settings'
        OK direct
        ./BitcoinDarkd  SuperNET '{"requestType":"settings"}'

    static char *settings[] = { (char *)settings_func, "settings", "", "field", "value", "reinit", 0 };
 """#
        K0 = 'requestType'
        P0 = 'settings'
        try:
            K1 = 'field'
            P1 = reqDict['field']
        except:
            P1 = ''

        try:
            K2 = 'value'
            P2 = reqDict['value']
        except:
            P2 = ''

        try:
            K3 = 'reinit'
            P3 = reqDict['reinit']
        except:
            P3 = ''


        return  { K0 : P0 , K1 : P1 ,K2 : P2,  K3 : P3,  }
        #
        # # unwrap into tuple here, and pass into the relevant function!
        # parms = ( (K0,P0),  (K1,P1), (K2,P2), (K3,P3),) # NB: need the extra comma to force len(parms)==1 for ONE tuple
        # jsonSpecs = self.assembleQuery(parms)
        # print("\n\n\n",jsonSpecs)
        # return jsonSpecs




    #########################



    #     // ramchains 13
    #########################



    def ramstatus(self, reqDict):
        """ individual treatment of requests and their parms here


CHECK!



    static char *ramstatus[] = { (char *)ramstatus_func, "ramstatus", "V", "destip", "coin", 0 };


"""#
        K0 = 'requestType'
        P0 = 'ramstatus'
        try:
            K1 = 'destip'
            P1 = reqDict['destip']
        except:
            P1 = ''


        try:
            K2 = 'coin'
            P2 = reqDict['coin']
        except:
            P2 = ''


        return  { K0 : P0 , K1 : P1 ,K2 : P2 }




    def ramaddrlist(self, reqDict):
        """ individual treatment of requests and their parms here


    static char *ramaddrlist[] = { (char *)ramaddrlist_func, "ramaddrlist", "V", "coin", 0 };



"""#
        K0 = 'requestType'
        P0 = 'ramaddrlist'
        try:
            K1 = 'coin'
            P1 = reqDict['coin']
        except:
            P1 = ''


        return  { K0 : P0 , K1 : P1 }



    def ramstring(self, reqDict):
        """ individual treatment of requests and their parms here



    static char *ramstring[] = { (char *)ramstring_func, "ramstring", "V", "destip", "coin", "type", "rawind", 0 };


"""#
        K0 = 'requestType'
        P0 = 'ramstring'
        try:
            K1 = 'destip'
            P1 = reqDict['destip']
        except:
            P1 = ''


        try:
            K2 = 'type'
            P2 = reqDict['type']
        except:
            P2 = ''


        try:
            K3 = 'rawind'
            P3 = reqDict['rawind']
        except:
            P3 = ''




        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3}



    def ramrawind(self, reqDict):
        """ individual treatment of requests and their parms here



    static char *ramrawind[] = { (char *)ramrawind_func, "ramrawind", "V", "destip", "coin", "type", "string", 0 };


"""#
        K0 = 'requestType'
        P0 = 'ramrawind'
        try:
            K1 = 'destip'
            P1 = reqDict['destip']
        except:
            P1 = ''


        try:
            K2 = 'coin'
            P2 = reqDict['coin']
        except:
            P2 = ''


        try:
            K3 = 'type'
            P3 = reqDict['type']
        except:
            P3 = ''


        try:
            K4 = 'string'
            P4 = reqDict['string']
        except:
            P4 = ''




        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4 }


    def ramblock(self, reqDict):
        """ individual treatment of requests and their parms here



    static char *ramblock[] = { (char *)ramblock_func, "ramblock", "V", "destip", "coin", "blocknum", 0 };


"""#
        K0 = 'requestType'
        P0 = 'ramblock'
        try:
            K1 = 'destip'
            P1 = reqDict['destip']
        except:
            P1 = ''


        try:
            K2 = 'coin'
            P2 = reqDict['coin']
        except:
            P2 = ''


        try:
            K3 = 'blocknum'
            P3 = reqDict['blocknum']
        except:
            P3 = ''




        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3 }



    def ramscript(self, reqDict):
        """ individual treatment of requests and their parms here


    static char *ramscript[] = { (char *)ramscript_func, "ramscript", "V", "destip", "coin", "txid", "vout", "blocknum", "txind", "v", 0 };

"""#
        K0 = 'requestType'
        P0 = 'ramscript'
        try:
            K1 = 'destip'
            P1 = reqDict['destip']
        except:
            P1 = ''


        try:
            K2 = 'txid'
            P2 = reqDict['txid']
        except:
            P2 = ''


        try:
            K3 = 'vout'
            P3 = reqDict['vout']
        except:
            P3 = ''


        try:
            K4 = 'blocknum'
            P4 = reqDict['blocknum']
        except:
            P4 = ''


        try:
            K5 = 'txind'
            P5 = reqDict['txind']
        except:
            P5 = ''


        try:
            K6 = 'v'
            P6 = reqDict['v']
        except:
            P6 = ''



        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  K5 : P5, K6 : P6}



    def ramtxlist(self, reqDict):
        """ individual treatment of requests and their parms here


    static char *ramtxlist[] = { (char *)ramtxlist_func, "ramtxlist", "V", "destip", "coin", "address", "unspent", 0 };

"""#
        K0 = 'requestType'
        P0 = 'ramtxlist'
        try:
            K1 = 'destip'
            P1 = reqDict['destip']
        except:
            P1 = ''


        try:
            K2 = 'coin'
            P2 = reqDict['coin']
        except:
            P2 = ''


        try:
            K3 = 'address'
            P3 = reqDict['address']
        except:
            P3 = ''


        try:
            K4 = 'unspent'
            P4 = reqDict['unspent']
        except:
            P4 = ''



        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4 }


    def ramrichlist(self, reqDict):
        """ individual treatment of requests and their parms here


    static char *ramrichlist[] = { (char *)ramrichlist_func, "ramrichlist", "V", "destip", "coin", "numwhales", "recalc", 0 };


"""#
        K0 = 'requestType'
        P0 = 'ramrichlist'
        try:
            K1 = 'destip'
            P1 = reqDict['destip']
        except:
            P1 = ''


        try:
            K2 = 'coin'
            P2 = reqDict['coin']
        except:
            P2 = ''


        try:
            K3 = 'numwhales'
            P3 = reqDict['numwhales']
        except:
            P3 = ''


        try:
            K4 = 'recalc'
            P4 = reqDict['recalc']
        except:
            P4 = ''


        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4 }


    def ramcompress(self, reqDict):
        """ individual treatment of requests and their parms here



    static char *ramcompress[] = { (char *)ramcompress_func, "ramcompress", "V", "destip", "coin", "data", 0 };


"""#
        K0 = 'requestType'
        P0 = 'ramcompress'
        try:
            K1 = 'destip'
            P1 = reqDict['destip']
        except:
            P1 = ''


        try:
            K2 = 'coin'
            P2 = reqDict['coin']
        except:
            P2 = ''


        try:
            K3 = 'data'
            P3 = reqDict['data']
        except:
            P3 = ''




        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3 }



    def ramexpand(self, reqDict):
        """ individual treatment of requests and their parms here


    static char *ramexpand[] = { (char *)ramexpand_func, "ramexpand", "V", "destip", "coin", "data", 0 };

"""#
        K0 = 'requestType'
        P0 = 'ramexpand'
        try:
            K1 = 'destip'
            P1 = reqDict['destip']
        except:
            P1 = ''


        try:
            K2 = 'coin'
            P2 = reqDict['coin']
        except:
            P2 = ''


        try:
            K3 = 'data'
            P3 = reqDict['data']
        except:
            P3 = ''



        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3 }




    def rambalances(self, reqDict):
        """ individual treatment of requests and their parms here



    static char *rambalances[] = { (char *)rambalances_func, "rambalances", "V", "destip", "coin", "coins", "rates", 0 };

"""#
        K0 = 'requestType'
        P0 = 'rambalances'
        try:
            K1 = 'destip'
            P1 = reqDict['destip']
        except:
            P1 = ''


        try:
            K2 = 'coin'
            P2 = reqDict['coin']
        except:
            P2 = ''


        try:
            K3 = 'coins'
            P3 = reqDict['coins']
        except:
            P3 = ''


        try:
            K4 = 'rates'
            P4 = reqDict['rates']
        except:
            P4 = ''




        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4 }



    #// remotable ramchains
    #


    def ramresponse(self, reqDict):
        """ individual treatment of requests and their parms here
 #static char *ramresponse[] = { (char *)ramresponse_func, "ramresponse", "V", "coin", "origcmd", "data", 0 };



"""#
        K0 = 'requestType'
        P0 = 'ramresponse'
        try:
            K1 = 'coin'
            P1 = reqDict['coin']
        except:
            P1 = ''


        try:
            K2 = 'origcmd'
            P2 = reqDict['origcmd']
        except:
            P2 = ''


        try:
            K3 = 'data'
            P3 = reqDict['data']
        except:
            P3 = ''



        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3 }




    def rampyramid(self, reqDict):
        """ individual treatment of requests and their parms here

static char *rampyramid[] = { (char *)rampyramid_func, "rampyramid", "V", "destip", "port", "coin", "blocknum", "type", 0 };
    """#
        K0 = 'requestType'
        P0 = 'rampyramid'
        try:
            K1 = 'destip'
            P1 = reqDict['destip']
        except:
            P1 = ''


        try:
            K2 = 'port'
            P2 = reqDict['port']
        except:
            P2 = ''


        try:
            K3 = 'coin'
            P3 = reqDict['coin']
        except:
            P3 = ''


        try:
            K4 = 'blocknum'
            P4 = reqDict['blocknum']
        except:
            P4 = ''


        try:
            K5 = 'type'
            P5 = reqDict['type']
        except:
            P5 = ''




        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  K5 : P5 }




    #########################



    #     // MGW 6
    #########################





    def genmultisig(self, reqDict):
        """ individual treatment of requests and their parms here
 static char *genmultisig[] = { (char *)genmultisig_func, "genmultisig", "V", "coin", "refcontact", "M", "N", "contacts", "destip", 0 };
   """#
        K0 = 'requestType'
        P0 = 'genmultisig'


        try:
            K1 = 'coin'
            P1 = reqDict['coin']
        except:
            P1 = ''

        try:
            K2 = 'refcontact'
            P2 = reqDict['refcontact']
        except:
            P2 = ''

        try:
            K3 = 'M'
            P3 = reqDict['M']
        except:
            P3= ''

        try:
            K3 = 'N'
            P3 = reqDict['N']
        except:
            P3= ''


        try:
            K4 = 'contacts'
            P4 = reqDict['contacts']
        except:
            P4= ''

        try:
            K5 = 'destip'
            P5 = reqDict['destip']
        except:
            P5= ''


        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,K4 : P4, K5 : P5, }


    def getmsigpubkey(self, reqDict):
        """ individual treatment of requests and their parms here
   static char *getmsigpubkey[] = { (char *)getmsigpubkey_func, "getmsigpubkey", "V", "coin", "refNXTaddr", "myaddr", "mypubkey", 0 };
  """#
        K0 = 'requestType'
        P0 = 'getmsigpubkey'


        try:
            K1 = 'coin'
            P1 = reqDict['coin']
        except:
            P1 = ''

        try:
            K2 = 'refNXTaddr'
            P2 = reqDict['refNXTaddr']
        except:
            P2 = ''

        try:
            K3 = 'myaddr'
            P3 = reqDict['myaddr']
        except:
            P3= ''

        try:
            K4 = 'mypubkey'
            P4 = reqDict['mypubkey']
        except:
            P4= ''

        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3, K4 : P4, }




    def MGWaddr(self, reqDict):
        """ individual treatment of requests and their parms here
static char *MGWaddr[] = { (char *)MGWaddr_func, "MGWaddr", "V", 0 };
 """#
        K0 = 'requestType'
        P0 = 'MGWaddr'


        return  { K0 : P0 ,  }






    def MGWresponse(self, reqDict):
        """ individual treatment of requests and their parms here

static char *MGWresponse[] = { (char *)MGWresponse_func, "MGWresponse", "V", 0 };

 """#
        K0 = 'requestType'
        P0 = 'MGWresponse'


        return  { K0 : P0 ,  }



    def setmsigpubkey(self, reqDict):
        """ individual treatment of requests and their parms here
static char *[] = { (char *)setmsigpubkey_func, "setmsigpubkey", "V", "coin", "refNXTaddr", "addr", "pubkey", 0 };
 """#
        K0 = 'requestType'
        P0 = 'setmsigpubkey'


        try:
            K1 = 'coin'
            P1 = reqDict['coin']
        except:
            P1 = ''

        try:
            K2 = 'refNXTaddr'
            P2 = reqDict['refNXTaddr']
        except:
            P2 = ''

        try:
            K3 = 'addr'
            P3 = reqDict['addr']
        except:
            P3= ''

        try:
            K4 = 'pubkey'
            P4 = reqDict['pubkey']
        except:
            P4= ''

        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3, K4 : P4, }



#################

    def cosign(self, reqDict):
        """ individual treatment of requests and their parms here
    static char *cosign[] = { (char *)cosign_func, "cosign", "V", "otheracct", "seed", "text", 0 };
 """#
        K0 = 'requestType'
        P0 = 'cosign'


        try:
            K1 = 'otheracct'
            P1 = reqDict['otheracct']
        except:
            P1 = ''

        try:
            K2 = 'seed'
            P2 = reqDict['seed']
        except:
            P2 = ''

        try:
            K3 = 'text'
            P3 = reqDict['text']
        except:
            P3= ''

        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3, }




    def cosigned(self, reqDict):
        """ individual treatment of requests and their parms here
    static char *cosigned[] = { (char *)cosigned_func, "cosigned", "V", "seed", "result", "privacct", "pubacct", 0 };

"""#
        K0 = 'requestType'
        P0 = 'cosigned'
        try:
            K1 = 'seed'
            P1 = reqDict['seed']
        except:
            P1 = ''


        try:
            K2 = 'result'
            P2 = reqDict['result']
        except:
            P2 = ''


        try:
            K3 = 'privacct'
            P3 = reqDict['privacct']
        except:
            P3 = ''


        try:
            K4 = 'pubacct'
            P4 = reqDict['pubacct']
        except:
            P4 = ''

        return  { K0 : P0 , K1 : P1 , K2 : P2, K3 : P3,  K4 : P4,}





    #########################




    #     // IPcomms 5

    #########################









    def ping(self, reqDict):
        """ individual treatment of requests and their parms here

        # ./BitcoinDarkd  SuperNET '{"requestType":"ping","destip":"178.62.185.131"}'

        # ./BitcoinDarkd  SuperNET '{"requestType":"ping","destip":"85.178.202.239"}'

        curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=ping&destip=178.62.185.131'
OK!

curl -k --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "SuperNET", "params": [    "{\"requestType\":\"ping\",\"destip\":\"178.62.185.131\" }     "]  }' -H 'content-type: text/plain;' http://127.0.0.1:7776/


static char *ping[] = { (char *)ping_func, "ping", "V", "pubkey", "ipaddr", "port", "destip", 0 };


        """#

        K0 = 'requestType'
        P0 = 'ping'

        try:
            K1 = 'destip'
            P1 = reqDict['destip']
        except:
            P1 = ''
        try:
            K2 = 'pubkey'
            P2 = reqDict['pubkey']
        except:
            P2 = ''

        try:
            K3 = 'ipaddr'
            P3 = reqDict['ipaddr']
        except:
            P3=''

        try:
            K4 = 'port'
            P4 = reqDict['port']
        except:
            P4=''

        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,}




    def pong(self, reqDict):
        """ individual treatment of requests and their parms here

        # ./BitcoinDarkd  SuperNET '{"requestType":"ping","destip":"178.62.185.131"}'

        # ./BitcoinDarkd  SuperNET '{"requestType":"pong","yourip":"85.178.202.239"}'

        curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=pong&yourip=85.178.202.239'
OK!


static char *ping[] = { (char *)ping_func, "ping", "V", "pubkey", "ipaddr", "port", "destip", 0 };
static char *pong[] = { (char *)pong_func, "pong", "V", "pubkey", "ipaddr", "port", "yourip", "yourport", 0 };


    static char *pong[] = { (char *)pong_func, "pong", "V", "pubkey", "ipaddr", "port", "yourip", "yourport", 0 };


        """#

        K0 = 'requestType'
        P0 = 'pong'
        try:
            K1 = 'pubkey'
            P1 = reqDict['pubkey']
        except:
            P1 = ''


        try:
            K2 = 'ipaddr'
            P2 = reqDict['ipaddr']
        except:
            P2 = ''


        try:
            K3 = 'port'
            P3 = reqDict['port']
        except:
            P3 = ''


        try:
            K4 = 'yourip'
            P4 = reqDict['yourip']
        except:
            P4 = ''


        try:
            K5 = 'yourport'
            P5 = reqDict['yourport']
        except:
            P5 = ''



        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  K5 : P5,}



    def sendfrag(self, reqDict):
        """ individual treatment of requests and their parms here

*   static char *sendfrag[] = { (char *)sendfrag_func, "sendfrag", "V", "pubkey", "name", "fragi", "numfrags", "ipaddr", "totalcrc", "datacrc", "data", "totallen", "blocksize", "handler", 0 };


        """#


        K0 = 'requestType'
        P0 = 'sendfrag'

        try:
            K1 = 'pubkey'
            P1 = reqDict['pubkey']
        except:
            P1= ''
        try:
            K2 = 'name'
            P2 = reqDict['name']
        except:
            P2= ''
        try:
            K3 = 'fragi'
            P3 = reqDict['fragi']
        except:
            P3= ''
        try:
            K4 = 'numfrags'
            P4 = reqDict['numfrags']
        except:
            P4= ''
        try:
            K5 = 'ipaddr'
            P5 = reqDict['ipaddr']
        except:
            P5= ''
        try:
            K6 = 'totalcrc'
            P6 = reqDict['totalcrc']
        except:
            P6= ''
        try:
            K7 = 'datacrc'
            P7 = reqDict['datacrc']
        except:
            P7= ''
        try:
            K8 = 'data'
            P8 = reqDict['data']
        except:
            P8= ''
        try:
            K9 = 'totallen'
            P9 = reqDict['totallen']
        except:
            P9= ''
        try:
            K10 = 'blocksize'
            P10 = reqDict['blocksize']
        except:
            P10= ''
        try:
            K11 = 'handler'
            P11 = reqDict['handler']
        except:
            P11= ''


        retVal =  {
                    K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  K5 : P5, K6 : P6,  K7 : P7, \
                    K8 : P8 , K9 : P9 , K10 : P10, K11 : P11
                    }

        return retVal




    def gotfrag(self, reqDict):
        """ individual treatment of requests and their parms here

    *   static char *gotfrag[] = { (char *)gotfrag_func, "gotfrag", "V", "pubkey", "name", "fragi", "numfrags", "ipaddr", "totalcrc", "datacrc", "totallen", "blocksize", "count", "handler", 0 };


        """#


        K0 = 'requestType'
        P0 = 'sendfrag'

        try:
            K1 = 'pubkey'
            P1 = reqDict['pubkey']
        except:
            P1= ''
        try:
            K2 = 'name'
            P2 = reqDict['name']
        except:
            P2= ''
        try:
            K3 = 'fragi'
            P3 = reqDict['fragi']
        except:
            P3= ''
        try:
            K4 = 'numfrags'
            P4 = reqDict['numfrags']
        except:
            P4= ''
        try:
            K5 = 'ipaddr'
            P5 = reqDict['ipaddr']
        except:
            P5= ''
        try:
            K6 = 'totalcrc'
            P6 = reqDict['totalcrc']
        except:
            P6= ''
        try:
            K7 = 'datacrc'
            P7 = reqDict['datacrc']
        except:
            P7= ''
        try:
            K8 = 'count'
            P8 = reqDict['count']
        except:
            P8= ''
        try:
            K9 = 'totallen'
            P9 = reqDict['totallen']
        except:
            P9= ''
        try:
            K10 = 'blocksize'
            P10 = reqDict['blocksize']
        except:
            P10= ''
        try:
            K11 = 'handler'
            P11 = reqDict['handler']
        except:
            P11= ''


        retVal =  {
                    K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  K5 : P5, K6 : P6,  K7 : P7, \
                    K8 : P8 , K9 : P9 , K10 : P10, K11 : P11
                    }

        return retVal


    def startxfer(self, reqDict):
        """ individual treatment of requests and their parms here


 *   static char *startxfer[] = { (char *)startxfer_func, "startxfer", "V", "fname", "dest", "data", "timeout", "handler", 0 };


        """#

        K0 = 'requestType'
        P0 = 'startxfer'
        try:
            K1 = 'timeout'
            P1 = reqDict['timeout']
        except:
            P1 = ''


        try:
            K2 = 'fname'
            P2 = reqDict['fname']
        except:
            P2 = ''


        try:
            K3 = 'dest'
            P3 = reqDict['dest']
        except:
            P3 = ''


        try:
            K4 = 'data'
            P4 = reqDict['data']
        except:
            P4 = ''


        try:
            K5 = 'handler'
            P5 = reqDict['handler']
        except:
            P5 = ''



        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  K5 : P5,}






    def getfile(self, reqDict):
        """ individual treatment of requests and their parms here

!! ip
 static char *getfile[] = { (char *)getfile_func, "getfile", "V", "name", "handler", 0 };


        """#

        K0 = 'requestType'
        P0 = 'getfile'

        try:
            K1 = 'name'
            P1 = reqDict['name']
        except:
            P1 = ''
        try:
            K2 = 'handler'
            P2 = reqDict['handler']
        except:
            P2 = ''

        return  { K0 : P0 , K1 : P1 ,K2 : P2 }









    #########################




    #     // Kademlia DHT 8

    #########################


    def store(self, reqDict):
        """ individual treatment of requests and their parms here
    static char *store[] = { (char *)store_func, "store", "V", "pubkey", "key", "name", "data", 0 };

"""#
        K0 = 'requestType'
        P0 = 'store'
        try:
            K1 = 'pubkey'
            P1 = reqDict['pubkey']
        except:
            P1 = ''


        try:
            K2 = 'key'
            P2 = reqDict['key']
        except:
            P2 = ''


        try:
            K3 = 'name'
            P3 = reqDict['name']
        except:
            P3 = ''


        try:
            K4 = 'data'
            P4 = reqDict['data']
        except:
            P4 = ''


        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  }




    def findvalue(self, reqDict):
        """ individual treatment of requests and their parms here
    static char *findvalue[] = { (char *)findvalue_func, "findvalue", "V", "pubkey", "key", "name", "data", 0 };

 """#
        K0 = 'requestType'
        P0 = 'findvalue'
        try:
            K1 = 'pubkey'
            P1 = reqDict['pubkey']
        except:
            P1 = ''


        try:
            K2 = 'key'
            P2 = reqDict['key']
        except:
            P2 = ''


        try:
            K3 = 'name'
            P3 = reqDict['name']
        except:
            P3 = ''


        try:
            K4 = 'data'
            P4 = reqDict['data']
        except:
            P4 = ''


        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4, }




    def findnode(self, reqDict):
        """ individual treatment of requests and their parms here
    static char *findnode[] = { (char *)findnode_func, "findnode", "V", "pubkey", "key", "name", "data", 0 };

"""#
        K0 = 'requestType'
        P0 = 'findnode'
        try:
            K1 = 'pubkey'
            P1 = reqDict['pubkey']
        except:
            P1 = ''


        try:
            K2 = 'key'
            P2 = reqDict['key']
        except:
            P2 = ''


        try:
            K3 = 'name'
            P3 = reqDict['name']
        except:
            P3 = ''


        try:
            K4 = 'data'
            P4 = reqDict['data']
        except:
            P4 = ''


        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  }



    def havenode(self, reqDict):
        """ individual treatment of requests and their parms here

             static char *havenode[] = { (char *)havenode_func, "havenode", "V", "pubkey", "key", "name", "data", 0 };

"""#
        K0 = 'requestType'
        P0 = 'havenode'
        try:
            K1 = 'pubkey'
            P1 = reqDict['pubkey']
        except:
            P1 = ''


        try:
            K2 = 'key'
            P2 = reqDict['key']
        except:
            P2 = ''


        try:
            K3 = 'name'
            P3 = reqDict['name']
        except:
            P3= ''


        try:
            K4 = 'data'
            P4 = reqDict['data']
        except:
            P4 = ''


        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  }



    def havenodeB(self, reqDict):
        """ individual treatment of requests and their parms here
     static char *havenode[] = { (char *)havenode_func, "havenode", "V", "pubkey", "key", "name", "data", 0 };

"""#
        K0 = 'requestType'
        P0 = 'havenodeB'
        try:
            K1 = 'pubkey'
            P1 = reqDict['pubkey']
        except:
            P1 = ''


        try:
            K2 = 'key'
            P2 = reqDict['key']
        except:
            P2 = ''


        try:
            K3 = 'name'
            P3 = reqDict['name']
        except:
            P3 = ''


        try:
            K4 = 'data'
            P4 = reqDict['data']
        except:
            P4 = ''



        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  }



    def findaddress(self, reqDict):
        """ individual treatment of requests and their parms here
      static char *findaddress[] = { (char *)findaddress_func, "findaddress", "V", "refaddr", "list", "dist", "duration", "numthreads", 0 };

"""#
        K0 = 'requestType'
        P0 = 'findaddress'
        try:
            K1 = 'refaddr'
            P1 = reqDict['refaddr']
        except:
            P1 = ''


        try:
            K2 = 'list'
            P2 = reqDict['list']
        except:
            P2 = ''


        try:
            K3 = 'dist'
            P3 = reqDict['dist']
        except:
            P3 = ''


        try:
            K4 = 'duration'
            P4 = reqDict['duration']
        except:
            P4 = ''


        try:
            K5 = 'numthreads'
            P5 = reqDict['numthreads']
        except:
            P5 = ''


        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  K5 : P5,}




    def nonces(self, reqDict):
        """ individual treatment of requests and their parms here
   static char *nonces[] = { (char *)response_func, "nonces", "V", "reftime", "threshold", "nonces", 0 };

"""#
        K0 = 'requestType'
        P0 = 'nonces'
        try:
            K1 = 'reftime'
            P1 = reqDict['reftime']
        except:
            P1 = ''


        try:
            K2 = 'threshold'
            P2 = reqDict['threshold']
        except:
            P2 = ''


        try:
            K3 = 'nonces'
            P3 = reqDict['nonces']
        except:
            P3 = ''



        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3   }



    def puzzles(self, reqDict):
        """ individual treatment of requests and their parms here



    // Kademlia DHT 8

!!!
static char *puzzles[] = { (char *)challenge_func, "puzzles", "V", "reftime", "duration", "threshold", 0 };


"""#
        K0 = 'requestType'
        P0 = 'puzzles'
        try:
            K1 = 'reftime'
            P1 = reqDict['reftime']
        except:
            P1 = ''


        try:
            K2 = 'duration'
            P2 = reqDict['duration']
        except:
            P2 = ''


        try:
            K3 = 'threshold'
            P3 = reqDict['threshold']
        except:
            P3 = ''




        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3   }


         #########################



    #     // MofNfs 3
    #########################

    def savefile(self, reqDict):
        """ individual treatment of requests and their parms here
  static char *savefile[] = { (char *)savefile_func, "savefile", "V", "filename", "L", "M", "N", "backup", "password", "pin", 0 };
"""#
        K0 = 'requestType'
        P0 = 'savefile'
        try:
            K1 = 'filename'
            P1 = reqDict['filename']
        except:
            P1 = ''


        try:
            K2 = 'L'
            P2 = reqDict['L']
        except:
            P2 = ''


        try:
            K3 = 'M'
            P3 = reqDict['M']
        except:
            P3 = ''


        try:
            K4 = 'N'
            P4 = reqDict['N']
        except:
            P4 = ''


        try:
            K5 = 'backup'
            P5 = reqDict['backup']
        except:
            P5 = ''


        try:
            K6 = 'password'
            P6 = reqDict['password']
        except:
            P6 = ''


        try:
            K7 = 'pin'
            P7 = reqDict['pin']
        except:
            P7 = ''

        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  K5 : P5, K6 : P6,  K7 : P7,}



    def restorefile(self, reqDict):
        """
    static char *restorefile[] = { (char *)restorefile_func, "restorefile", "V", "filename", "L", "M", "N", "backup", "password", "destfile", "sharenrs", "txids", "pin", 0 };

individual treatment of requests and their parms here """#
        K0 = 'requestType'
        P0 = 'restorefile'
        try:
            K1 = 'filename'
            P1 = reqDict['filename']
        except:
            P1 = ''


        try:
            K2 = 'L'
            P2 = reqDict['L']
        except:
            P2 = ''


        try:
            K3 = 'M'
            P3 = reqDict['M']
        except:
            P3 = ''


        try:
            K4 = 'N'
            P4 = reqDict['N']
        except:
            P4 = ''


        try:
            K5 = 'backup'
            P5 = reqDict['backup']
        except:
            P5= ''


        try:
            K6 = 'password'
            P6 = reqDict['password']
        except:
            P6 = ''

        try:
            K7 = 'destfile'
            P7 = reqDict['destfile']
        except:
            P7 = ''


        try:
            K8 = 'sharenrs'
            P8 = reqDict['sharenrs']
        except:
            P8= ''


        try:
            K9 = 'txids'
            P9 = reqDict['txids']
        except:
            P9 = ''


        try:
            K10 = 'pin'
            P10 = reqDict['pin']
        except:
            P10 = ''


        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  K5 : P5, K6 : P6,  K7 : P7, K8 : P8, K9 : P9,  K10 : P10,}




    def publish(self, reqDict):

        """ individual treatment of requests and their parms here
        static char *publish[] = { (char *)publish_func, "publish", "V", "files", "L", "M", "N", "backup", "password", "pin", 0  };

"""#
        K0 = 'requestType'
        P0 = 'publish'

        try:
            K1 = 'files'
            P1 = reqDict['files']
        except:
            P1 = ''

        try:
            K2 = 'L'
            P2 = reqDict['L']
        except:
            P2 = ''


        try:
            K3 = 'M'
            P3 = reqDict['M']
        except:
            P3 = ''


        try:
            K4 = 'N'
            P4 = reqDict['N']
        except:
            P4 = ''


        try:
            K5 = 'backup'
            P5 = reqDict['backup']
        except:
            P5 = ''


        try:
            K6 = 'password'
            P6 = reqDict['password']
        except:
            P6 = ''

        try:
            K6 = 'pin'
            P6 = reqDict['pin']
        except:
            P6 = ''




        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  K5 : P5, K6 : P6,   }



    #########################
    #     // Telepathy 9
    #########################




    def getpeers(self, reqDict):
        """ individual treatment of requests and their parms here

        # ./BitcoinDarkd  SuperNET '{"requestType":"getpeers","scan":1}'

    static char *getpeers[] = { (char *)getpeers_func, "getpeers", "V",  "scan", 0 };
"""#
        K0 = 'requestType'
        P0 = 'getpeers'

        # optional parms handling
        #todo: case handling has to be done for all optional params!
        K1 = 'scan'
        try:
            P1 = reqDict['scan']

        except:
            P1 = ''
        # ./BitcoinDarkd  SuperNET '{"requestType":"getpeers","scan":1}'

        # ./BitcoinDarkd SuperNET '{"requestType":"dispcontact","contact":"*"}' shows 2 peers now

        return  { K0 : P0 , K1 : P1 ,  }




    def addcontact(self, reqDict):
        """ individual treatment of requests and their parms here
    static char *addcontact[] = { (char *)addcontact_func, "addcontact", "V",  "handle", "acct", 0 };
"""#
        K0 = 'requestType'
        P0 = 'addcontact'
        try:
            K1 = 'handle'
            P1 = reqDict['handle']
        except:
            P1 = ''


        try:
            K2 = 'acct'
            P2 = reqDict['acct']
        except:
            P2 = ''


        return  { K0 : P0 , K1 : P1 ,K2 : P2,  }


    def removecontact(self, reqDict):
        """ individual treatment of requests and their parms here
    static char *removecontact[] = { (char *)removecontact_func, "removecontact", "V",  "contact", 0 };
 """#
        K0 = 'requestType'
        P0 = 'removecontact'
        try:
            K1 = 'contact'
            P1 = reqDict['contact']
        except:
            P1 = ''



        return  { K0 : P0 , K1 : P1 , }
        # parms = ( (K0,P0),  (K1,P1),)
        # jsonSpecs = self.assembleQuery(parms)
        #
        # return jsonSpecs


    def dispcontact(self, reqDict):
        """ individual treatment of requests and their parms here
          ./BitcoinDarkd  SuperNET '{"requestType":"dispcontact","contact":"jl777"}'
        """#
        K0 = 'requestType'
        P0 = 'dispcontact'
        try:
            K1 = 'contact'
            P1 = reqDict['contact']
        except:
            P1 = ''


        return  { K0 : P0 , K1 : P1 , }





    def telepathy(self, reqDict):
        """ individual treatment of requests and their parms here
    static char *telepathy[] = { (char *)telepathy_func, "telepathy", "V",  "contact", "id", "type", "attach", 0 };

  """#
        K0 = 'requestType'
        P0 = 'telepathy'
        try:
            K1 = 'contact'
            P1 = reqDict['contact']
        except:
            P1 = ''


        try:
            K2 = 'id'
            P2 = reqDict['id']
        except:
            P2 = ''


        try:
            K3 = 'type'
            P3 = reqDict['type']
        except:
            P3 = ''


        try:
            K4 = 'attach'
            P4 = reqDict['attach']
        except:
            P4 = ''


        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  }




    def getdb(self, reqDict):
        """ individual treatment of requests and their parms here
       static char *getdb[] = { (char *)getdb_func, "getdb", "V",  "contact", "id", "key", "dir", "destip", 0 };

"""#
        K0 = 'requestType'
        P0 = 'getdb'
        try:
            K1 = 'contact'
            P1 = reqDict['contact']
        except:
            P1 = ''


        try:
            K2 = 'id'
            P2 = reqDict['id']
        except:
            P2 = ''


        try:
            K3 = 'key'
            P3 = reqDict['key']
        except:
            P3 = ''


        try:
            K4 = 'dir'
            P4 = reqDict['dir']
        except:
            P4 = ''


        try:
            K5 = 'destip'
            P5 = reqDict['destip']
        except:
            P5 = ''



        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  K5 : P5,  }


    def sendmessage(self, reqDict):
        """ individual treatment of requests and their parms here
        # ./BitcoinDarkd  SuperNET '{"requestType":"sendmessage","dest":"2131686659786462901","msg":"hello---------------------------******************************"}'

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=sendmessage&dest=2131686659786462901&msg=*****HELLLOO*WORLD*'

     static char *sendmsg[] = { (char *)sendmsg_func, "sendmessage", "V", "dest", "msg", "L", 0 };

        #"""# #


# curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=sendmessage&dest=2131686659786462901&msg=aaaaabbbbbccccc'

        print(1*"***********", reqDict)

        K0 = 'requestType'
        P0 = 'sendmessage'
        try:
            K1 = 'L'
            P1 = reqDict['L']
        except:
            P1 = ''


        try:
            K2 = 'dest'
            P2 = reqDict['dest']
        except:
            P2 = ''


        try:
            K3 = 'msg'
            P3 = reqDict['msg']
        except:
            P3 = ''



        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  }



    def sendbinary(self, reqDict):
        """ individual treatment of requests and their parms here
    static char *sendbinary[] = { (char *)sendbinary_func, "sendbinary", "V", "dest", "data", "L", 0 };
 """#
        K0 = 'requestType'
        P0 = 'sendbinary'
        try:
            K1 = 'dest'
            P1 = reqDict['dest']
        except:
            P1 = ''


        try:
            K2 = 'data'
            P2 = reqDict['data']
        except:
            P2 = ''


        try:
            K3 = 'L'
            P3 = reqDict['L']
        except:
            P3 = ''

        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3, }



    #########################





    #     // Teleport 3
    #########################


    def maketelepods(self, reqDict):
        """ individual treatment of requests and their parms here

   static char *maketelepods[] = { (char *)maketelepods_func, "maketelepods", "V", "amount", "coin", 0 };

 """#
        K0 = 'requestType'
        P0 = 'maketelepods'
        try:
            K1 = 'amount'
            P1 = reqDict['amount']
        except:
            P1 = ''


        try:
            K2 = 'coin'

            P2 = reqDict['coin']
        except:
            P2 = ''



        return  { K0 : P0 , K1 : P1 ,K2 : P2, }


    def telepodacct(self, reqDict):
        """ individual treatment of requests and their parms here
      static char *telepodacct[] = { (char *)telepodacct_func, "telepodacct", "V", "amount", "contact", "coin", "comment", "cmd", "withdraw", 0 };
 """#
        K0 = 'requestType'
        P0 = 'telepodacct'
        try:
            K1 = 'amount'
            P1 = reqDict['amount']
        except:
            P1 = ''


        try:
            K2 = 'contact'
            P2 = reqDict['contact']
        except:
            P2 = ''


        try:
            K3 = 'coin'
            P3 = reqDict['coin']
        except:
            P3 = ''


        try:
            K4 = 'comment'
            P4 = reqDict['comment']
        except:
            P4 = ''


        try:
            K5 = 'cmd'
            P5 = reqDict['cmd']
        except:
            P5 = ''


        try:
            K6 = 'withdraw'
            P6 = reqDict['withdraw']
        except:
            P6 = ''



        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  K5 : P5, K6 : P6,   }



    def teleport(self, reqDict):
        """ individual treatment of requests and their parms here
    static char *teleport[] = { (char *)teleport_func, "teleport", "V", "amount", "contact", "coin", "minage", "withdraw", 0 };

 """#
        K0 = 'requestType'
        P0 = 'teleport'
        try:
            K1 = 'amount'
            P1 = reqDict['amount']
        except:
            P1 = ''


        try:
            K2 = 'contact'
            P2 = reqDict['contact']
        except:
            P2 = ''


        try:
            K3 = 'coin'
            P3 = reqDict['coin']
        except:
            P3 = ''


        try:
            K4 = 'minage'
            P4 = reqDict['minage']
        except:
            P4 = ''


        try:
            K5 = 'withdraw'
            P5 = reqDict['withdraw']
        except:
            P5 = ''



        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  K5 : P5, }

    #########################





    #     // InstantDEX 8
    #########################




    def allorderbooks(self, reqDict):
        """ individual treatment of requests and their parms here

static char *allorderbooks[] = { (char *)allorderbooks_func, "allorderbooks", "V", 0 };

    """#
        K0 = 'requestType'
        P0 = 'allorderbooks'


        return  { K0 : P0  }





    def openorders(self, reqDict):
        """ individual treatment of requests and their parms here
 static char *openorders[] = { (char *)openorders_func, "openorders", "V", 0 };

   static char *openorders[] = { (char *)openorders_func, "openorders", "V", 0 };


    """#
        K0 = 'requestType'
        P0 = 'openorders'


        return  { K0 : P0   }





    def orderbook(self, reqDict):
        """ individual treatment of requests and their parms here
    static char *orderbook[] = { (char *)orderbook_func, "orderbook", "V", "baseid", "relid", "allfields", "oldest", "maxdepth", "base", "rel", "gui", 0 };

"""#
        K0 = "requestType"
        P0 = "orderbook"
        try:
            K1 = "baseid"
            P1 = reqDict['baseid']
        except:
            P1 = ''


        try:
            K2 = "relid"
            P2 = reqDict['relid']
        except:
            P2 = ''


        try:
            K3 = "allfields"
            P3 = reqDict['allfields']
        except:
            P3 = ''


        try:
            K4 = "oldest"
            P4 = reqDict['oldest']
        except:
            P4 = ''


        try:
            K5 = 'maxdepth'
            P5 = reqDict['maxdepth']
        except:
            P5 = ''

        try:
            K6 = "base"
            P6 = reqDict['base']
        except:
            P6 = ''


        try:
            K7 = "rel"
            P7 = reqDict['rel']
        except:
            P7 = ''


        try:
            K8 = "gui"
            P8 = reqDict['gui']
        except:
            P8 = ''

        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  K5 : P5, K6 : P6,  K7 : P7, K8 : P8 }




    def placebid(self, reqDict):
        """ individual treatment of requests and their parms here

   static char *placebid[] = { (char *)placebid_func, "placebid", "V", "baseid", "relid", "volume", "price", "timestamp", "baseamount", "relamount", "gui", "automatch", "minperc", "duration", 0 };


 """#
        K0 = 'requestType'
        P0 = 'placebid'
        try:
            K1 = 'baseid'
            P1 = reqDict['baseid']
        except:
            P1 = ''

        try:
            K2 = 'relid'
            P2 = reqDict['relid']
        except:
            P2 = ''

        try:
            K3 = 'volume'
            P3 = reqDict['volume']
        except:
            P3 = ''

        try:
            K4 = 'price'
            P4 = reqDict['price']
        except:
            P4 = ''

        try:###
            K5 = 'timestamp'
            P5 = reqDict['timestamp']
        except:
            P5 = ''

        try:
            K6 = 'baseamount'
            P6 = reqDict['baseamount']
        except:
            P6 = ''

        try:
            K7 = 'relamount'
            P7 = reqDict['relamount']
        except:
            P7 = ''

        try:
            K8 = 'gui'
            P8 = reqDict['gui']
        except:
            P8 = ''

        try:
            K9 = 'automatch'
            P9 = reqDict['automatch']
        except:
            P9 = ''

        try:
            K10 = 'minperc'
            P10 = reqDict['minperc']
        except:
            P10 = ''


        try:
            K11 = 'duration'
            P11 = reqDict['duration']
        except:
            P11 = ''


        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  K5 : P5, K6 : P6,  K7 : P7, K8 : P8,  K9 : P9,  K10 : P10 ,  K11 : P11  }



    def placeask(self, reqDict):
        """ individual treatment of requests and their parms here
 static char *placeask[] = { (char *)placeask_func, "placeask", "V", "baseid", "relid", "volume", "price", "timestamp", "baseamount", "relamount", ",gui", "automatch", "minperc", "duration", 0 };


"""#
        K0 = 'requestType'
        P0 = 'placeask'
        try:
            K1 = 'baseid'
            P1 = reqDict['baseid']
        except:
            P1 = ''

        try:
            K2 = 'relid'
            P2 = reqDict['relid']
        except:
            P2 = ''

        try:
            K3 = 'volume'
            P3 = reqDict['volume']
        except:
            P3 = ''

        try:
            K4 = 'price'
            P4 = reqDict['price']
        except:
            P4 = ''

        try:###
            K5 = 'timestamp'
            P5 = reqDict['timestamp']
        except:
            P5 = ''

        try:
            K6 = 'baseamount'
            P6 = reqDict['baseamount']
        except:
            P6 = ''

        try:
            K7 = 'relamount'
            P7 = reqDict['relamount']
        except:
            P7 = ''

        try:
            K8 = 'gui'
            P8 = reqDict['gui']
        except:
            P8 = ''

        try:
            K9 = 'automatch'
            P9 = reqDict['automatch']
        except:
            P9 = ''

        try:
            K10 = 'minperc'
            P10 = reqDict['minperc']
        except:
            P10 = ''
        try:
            K11 = 'duration'
            P11 = reqDict['duration']
        except:
            P11 = ''


        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  K5 : P5, K6 : P6,  K7 : P7, K8 : P8,  K9 : P9,  K10 : P10 ,  K11 : P11  }




    def makeoffer3(self, reqDict):
        """ individual treatment of requests and their parms here
       static char *makeoffer3[] = { (char *)makeoffer3_func, "makeoffer3", "V", "baseid", "relid", "quoteid", "perc", "deprecated", "baseiQ", "reliQ", "askoffer", "price", "volume", "exchange", "baseamount", "relamount", "offerNXT", "minperc", "jumpasset", 0 };



 """#
        K0 = 'requestType'
        P0 = 'makeoffer3'
        try:
            K1 = 'baseid'
            P1 = reqDict['baseid']
        except:
            P1 = ''


        try:
            K2 = 'relid'
            P2 = reqDict['relid']
        except:
            P2 = ''


        try:
            K3 = 'quoteid'
            P3 = reqDict['quoteid']
        except:
            P3 = ''

        try:
            K4 = 'perc'
            P4 = reqDict['perc']
        except:
            P4 = ''


        try:
            K5 = 'deprecated'
            P5 = reqDict['deprecated']
        except:
            P5= ''


        try:
            K6 = 'baseiQ'
            P6 = reqDict['baseiQ']
        except:
            P6 = ''

        try:
            K7 = 'reliQ'
            P7 = reqDict['reliQ']
        except:
            P7 = ''


        try:
            K8 = 'askoffer'
            P8 = reqDict['askoffer']
        except:
            P8= ''


        try:
            K9 = 'price'
            P9 = reqDict['price']
        except:
            P9= ''

        try:
            K10 = 'volume'
            P10 = reqDict['volume']
        except:
            P10 = ''

        try:
            K11 = 'exchange'
            P11 = reqDict['exchange']
        except:
            P11 = ''


        try:
            K12 = 'baseamount'
            P12 = reqDict['baseamount']
        except:
            P12 = ''

        try:
            K13 = 'relamount'
            P13 = reqDict['relamount']
        except:
            P13 = ''

        try:
            K14 = 'offerNXT'
            P14 = reqDict['offerNXT']
        except:
            P14 = ''

        try:
            K15 = 'minperc'
            P15 = reqDict['minperc']
        except:
            P15 = ''


        try:
            K16 = 'jumpasset'
            P16 = reqDict['jumpasset']
        except:
            P16 = ''

        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  K5 : P5, K6 : P6,  K7 : P7 ,\
                   K8 : P8 ,  K9 : P9 ,  K10 : P10 ,  K11 : P11 ,  K12 : P12 ,  K13 : P13 ,  K14 : P14 ,  K15 : P15,  K16 : P16  }






    def respondtx(self, reqDict):
        """ individual treatment of requests and their parms here


    static char *respondtx[] = { (char *)respondtx_func, "respondtx", "V", "cmd", "assetid", "quantityQNT", "priceNQT", "triggerhash", "quoteid", "sig", "data", "minperc", "offerNXT", "otherassetid", "otherqty", 0 };


         """#
        K0 = 'requestType'
        P0 = 'respondtx'
        try:
            K1 = 'cmd'
            P1 = reqDict['cmd']
        except:
            P1 = ''


        try:
            K2 = 'assetid'
            P2 = reqDict['assetid']
        except:
            P2 = ''


        try:
            K3 = 'quantityQNT'
            P3 = reqDict['quantityQNT']
        except:
            P3 = ''

        try:
            K4 = 'priceNQT'
            P4 = reqDict['priceNQT']
        except:
            P4 = ''


        try:
            K5 = 'triggerhash'
            P5 = reqDict['triggerhash']
        except:
            P5= ''


        try:
            K6 = 'quoteid'
            P6 = reqDict['quoteid']
        except:
            P6 = ''

        try:
            K7 = 'sig'
            P7 = reqDict['sig']
        except:
            P7 = ''


        try:
            K8 = 'data'
            P8 = reqDict['data']
        except:
            P8= ''


        try:
            K9 = 'minperc'
            P9 = reqDict['minperc']
        except:
            P9= ''

        try:
            K10 = 'offerNXT'
            P10 = reqDict['offerNXT']
        except:
            P10 = ''

        try:
            K11 = 'otherassetid'
            P11 = reqDict['otherassetid']
        except:
            P11 = ''


        try:
            K12 = 'otherqty'
            P12 = reqDict['otherqty']
        except:
            P12 = ''


        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  K5 : P5, K6 : P6,  K7 : P7 ,\
                   K8 : P8 ,  K9 : P9 ,  K10 : P10 ,  K11 : P11 ,  K12 : P12    }


#
#
#     def processutx(self, reqDict):
#         """ individual treatment of requests and their parms here
#     static char *processutx[] = { (char *)processutx_func, "processutx", "V", "utx", "sig", "full", 0 };
# """#
#         K0 = 'requestType'
#         P0 = 'processutx'
#         try:
#             K1 = 'utx'
#             P1 = reqDict['utx']
#         except:
#             P1 = ''
#
#
#         try:
#             K2 = 'sig'
#             P2 = reqDict['sig']
#         except:
#             P2 = ''
#
#
#         try:
#             K3 = 'full'
#             P3 = reqDict['full']
#         except:
#             P3 = ''
#
#
#         try:
#             K4 = 'feeAtxid'
#             P4 = reqDict['feeAtxid']
#         except:
#             P4 = ''
#
#
#         try:
#             K5 = 'quoteid'
#             P5 = reqDict['quoteid']
#         except:
#             P5 = ''
#
#         return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  K5 : P5   }
#
#


    def bid(self, reqDict):
        """

    static char *bid[] = { (char *)bid_func, "bid", "V", "baseid", "relid", "volume", "price", "timestamp", "baseamount", "relamount", "gui", "automatch", "minperc", "duration", 0 };

individual treatment of requests and their parms here """#
        K0 = 'requestType'
        P0 = 'bid'
        try:
            K1 = 'baseid'
            P1 = reqDict['baseid']
        except:
            P1 = ''


        try:
            K2 = 'relid'
            P2 = reqDict['relid']
        except:
            P2 = ''


        try:
            K3 = 'volume'
            P3 = reqDict['volume']
        except:
            P3 = ''


        try:
            K4 = 'price'
            P4 = reqDict['price']
        except:
            P4 = ''


        try:
            K5 = 'timestamp'
            P5 = reqDict['timestamp']
        except:
            P5= ''


        try:
            K6 = 'baseamount'
            P6 = reqDict['baseamount']
        except:
            P6 = ''

        try:
            K7 = 'relamount'
            P7 = reqDict['relamount']
        except:
            P7 = ''


        try:
            K8 = 'type'
            P8 = reqDict['type']
        except:
            P8= ''


        try:
            K9 = 'gui'
            P9 = reqDict['gui']
        except:
            P9 = ''

        try:
            K10 = 'automatch'
            P10 = reqDict['automatch']
        except:
            P10 = ''

        try:
            K11 = 'minperc'
            P11 = reqDict['minperc']
        except:
            P11 = ''


        try:
            K12 = 'duration'
            P12 = reqDict['duration']
        except:
            P12 = ''


        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  K5 : P5, K6 : P6,  K7 : P7 ,\
                   K8 : P8 ,  K9 : P9 ,  K10 : P10 ,  K11 : P11 ,  K12 : P12    }




    def ask(self, reqDict):
        """

static char *ask[] = { (char *)ask_func, "ask", "V", "baseid", "relid", "volume", "price", "timestamp", "baseamount", "relamount", "gui", "automatch", "minperc", "duration", 0 };


individual treatment of requests and their parms here

"""#
        K0 = 'requestType'
        P0 = 'ask'
        try:
            K1 = 'baseid'
            P1 = reqDict['baseid']
        except:
            P1 = ''


        try:
            K2 = 'relid'
            P2 = reqDict['relid']
        except:
            P2 = ''


        try:
            K3 = 'volume'
            P3 = reqDict['volume']
        except:
            P3 = ''


        try:
            K4 = 'price'
            P4 = reqDict['price']
        except:
            P4 = ''


        try:
            K5 = 'timestamp'
            P5 = reqDict['timestamp']
        except:
            P5= ''


        try:
            K6 = 'baseamount'
            P6 = reqDict['baseamount']
        except:
            P6 = ''

        try:
            K7 = 'relamount'
            P7 = reqDict['relamount']
        except:
            P7 = ''


        try:
            K8 = 'type'
            P8 = reqDict['type']
        except:
            P8= ''

        try:
            K9 = 'gui'
            P9 = reqDict['gui']
        except:
            P9 = ''


        try:
            K10 = 'automatch'
            P10 = reqDict['automatch']
        except:
            P10 = ''

        try:
            K11 = 'minperc'
            P11 = reqDict['minperc']
        except:
            P11 = ''


        try:
            K12 = 'duration'
            P12 = reqDict['duration']
        except:
            P12 = ''


        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  K5 : P5, K6 : P6,  K7 : P7 ,\
                   K8 : P8 ,  K9 : P9 ,  K10 : P10 ,  K11 : P11 ,  K12 : P12    }




    def allsignals(self, reqDict):
        """



         static char *allsignals[] = { (char *)allsignals_func, "allsignals", "V", 0 };


        """#
        K0 = 'requestType'
        P0 = 'allsignals'


        return  { K0 : P0  }





    def lottostats(self, reqDict):
        """

    static char *lottostats[] = { (char *)lottostats_func, "lottostats", "V", "timestamp", 0 };

        """#
        K0 = 'requestType'
        P0 = 'lottostats'
        try:
            K1 = 'timestamp'
            P1 = reqDict['timestamp']
        except:
            P1 = ''



        return  { K0 : P0 , K1 : P1  }



    def tradehistory(self, reqDict):
        """



    static char *tradehistory[] = { (char *)tradehistory_func, "tradehistory", "V", "timestamp", 0 };


        """#
        K0 = 'requestType'
        P0 = 'tradehistory'
        try:
            K1 = 'timestamp'
            P1 = reqDict['timestamp']
        except:
            P1 = ''


        return  { K0 : P0 , K1 : P1   }



    def getsignal(self, reqDict):
        """
    static char *getsignal[] = { (char *)getsignal_func, "getsignal", "V", "signal", "start", "width", "resolution", "baseid", "relid", "base", "rel", "exchange", 0 };

        """#
        K0 = 'requestType'
        P0 = 'getsignal'
        try:
            K1 = 'signal'
            P1 = reqDict['signal']
        except:
            P1 = ''

        try:
            K2 = 'start'
            P2 = reqDict['start']
        except:
            P2 = ''

        try:
            K3 = 'width'
            P3 = reqDict['width']
        except:
            P3 = ''

        try:
            K4 = 'resolution'
            P4 = reqDict['resolution']
        except:
            P4 = ''

        try:
            K5 = 'baseid'
            P5 = reqDict['baseid']
        except:
            P5= ''

        try:
            K6 = 'relid'
            P6 = reqDict['relid']
        except:
            P6 = ''

        try:
            K7 = 'base'
            P7 = reqDict['base']
        except:
            P7 = ''

        try:
            K8 = 'rel'
            P8 = reqDict['rel']
        except:
            P8= ''

        try:
            K9 = 'exchange'
            P9 = reqDict['exchange']
        except:
            P9 = ''


        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  K5 : P5, K6 : P6,  K7 : P7,  K8: P8 ,  K9 : P9 }



    def cancelquote(self, reqDict):
        """


    static char *cancelquote[] = { (char *)cancelquote_func, "cancelquote", "V", "quoteid", 0 };

        """#
        K0 = 'requestType'
        P0 = 'cancelquote'
        try:
            K1 = 'quoteid'
            P1 = reqDict['quoteid']
        except:
            P1 = ''



        return  { K0 : P0 , K1 : P1   }




    def jumptrades(self, reqDict):
        """



 static char *jumptrades[] = { (char *)jumptrades_func, "jumptrades", "V", 0 };


        """#
        K0 = 'requestType'
        P0 = 'jumptrades'



        return  { K0 : P0   }






    #########################





    #     // Tradebot 3
    #########################


 



    def pricedb(self, reqDict):
        """ individual treatment of requests and their parms here
   static char *pricedb[] = { (char *)pricedb_func, "pricedb", "V", "exchange", "base", "rel", "stop", 0 };
 """#
        K0 = 'requestType'
        P0 = 'pricedb'
        try:
            K1 = 'exchange'
            P1 = reqDict['exchange']
        except:
            P1 = ''


        try:
            K2 = 'base'
            P2 = reqDict['base']
        except:
            P2 = ''


        try:
            K3 = 'rel'
            P3 = reqDict['rel']
        except:
            P3 = ''


        try:
            K4 = 'stop'
            P4 = reqDict['stop']
        except:
            P4 = ''



        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,  }


    def getquotes(self, reqDict):
        """ individual treatment of requests and their parms here
    static char *getquotes[] = { (char *)getquotes_func, "getquotes", "V", "exchange", "base", "rel", "oldest", 0 };
"""#
        K0 = 'requestType'
        P0 = 'getquotes'
        try:
            K1 = 'exchange'
            P1 = reqDict['exchange']
        except:
            P1 = ''


        try:
            K2 = 'base'
            P2 = reqDict['base']
        except:
            P2 = ''


        try:
            K3 = 'rel'
            P3 = reqDict['rel']
        except:
            P3 = ''

        try:
            K4 = 'oldest'
            P4 = reqDict['oldest']
        except:
            P4 = ''


        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,  K4 : P4,   }


    def tradebot(self, reqDict):
        """ individual treatment of requests and their parms here
    static char *tradebot[] = { (char *)tradebot_func, "tradebot", "V", "code", 0 };
"""#
        K0 = 'requestType'
        P0 = 'tradebot'
        try:
            K1 = 'code'
            P1 = reqDict['code']
        except:
            P1 = ''

            

        return  { K0 : P0 , K1 : P1 , }


    #########################
 #
    #     // # privatebet 1


    def lotto(self, reqDict):
        """ individual treatment of requests and their parms here
  static char *lotto[] = { (char *)lotto_func, "lotto", "V", "refacct", "asset", 0 };

"""#
        K0 = 'requestType'
        P0 = 'lotto'
        try:
            K1 = 'refacct'
            P1 = reqDict['refacct']
        except:
            P1 = ''
        try:
            K2 = 'asset'
            P2 = reqDict['asset']
        except:
            P2 = ''

        try:
            K3 = 'lottoseed'
            P3 = reqDict['lottoseed']
        except:
            P3 = ''

        try:
            K4 = 'prizefund'
            P4 = reqDict['prizefund']
        except:
            P4 = ''


        return  { K0 : P0 , K1 : P1 , K2 : P2 , K3 : P3,  K4 : P4,   }



    def trollbox(self, reqDict):
        """ individual treatment of requests and their parms here


    static char *trollbox[] = { (char *)trollbox_func, "trollbox", "V", "post", "whaleindex", 0 };


    """#
        K0 = 'requestType'
        P0 = 'trollbox'
        try:
            K1 = 'post'
            P1 = reqDict['post']
        except:
            P1 = ''
        try:
            K2 = 'whaleindex'
            P2 = reqDict['whaleindex']
        except:
            P2 = ''


        return  { K0 : P0 , K1 : P1 ,K2 : P2, }






    #########################



    #     // plugins 5
    #########################




    def passthru(self, reqDict):
        """ individual treatment of requests and their parms here

     static char *passthru[] = { (char *)passthru_func, "passthru", "V", "coin", "method", "params", "tag", "daemonid", 0 };

 """#
        K0 = 'requestType'
        P0 = 'passthru'
        try:
            K1 = 'coin'
            P1 = reqDict['coin']
        except:
            P1 = ''


        try:
            K2 = 'method'
            P2 = reqDict['method']
        except:
            P2 = ''


        try:
            K3 = 'params'
            P3 = reqDict['params']
        except:
            P3 = ''

        try:
            K4 = 'tag'
            P4 = reqDict['tag']
        except:
            P4 = ''


        try:
            K5 = 'daemonid'
            P5 = reqDict['daemonid']
        except:
            P5= ''


        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3,   K4 : P4, K5 : P5  }





    def remote(self, reqDict):
        """ individual treatment of requests and their parms here

    static char *remote[] = { (char *)remote_func, "remote", "V",  "coin", "method", "result", "tag", 0 };

 """#
        K0 = 'requestType'
        P0 = 'remote'
        try:
            K1 = 'coin'
            P1 = reqDict['coin']
        except:
            P1 = ''


        try:
            K2 = 'method'
            P2 = reqDict['method']
        except:
            P2 = ''


        try:
            K3 = 'result'
            P3 = reqDict['result']
        except:
            P3 = ''

        try:
            K4 = 'tag'
            P4 = reqDict['tag']
        except:
            P4 = ''

        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3, K4 : P4,}


    def python(self, reqDict):
        """ individual treatment of requests and their parms here
   static char *python[] = { (char *)python_func, "python", "V",  "name", "launch", "websocket", 0 };

"""#
        K0 = 'requestType'
        P0 = 'python'
        try:
            K1 = 'name'
            P1 = reqDict['name']
        except:
            P1 = ''

        try:
            K2 = 'launch'
            P2 = reqDict['launch']
        except:
            P2 = ''


        try:
            K3 = 'websocket'
            P3 = reqDict['websocket']
        except:
            P3 = ''

        return  { K0 : P0 , K1 : P1 , K2 : P2 , K3  : P3 }




    def syscall(self, reqDict):
        """ individual treatment of requests and their parms here
    static char *syscall[] = { (char *)syscall_func, "syscall", "V", "name", "launch", "websocket", "arg", 0 };


"""#
        K0 = 'requestType'
        P0 = 'syscall'
        try:
            K1 = 'name'
            P1 = reqDict['name']
        except:
            P1 = ''
        try:
            K2 = 'cmd'
            P2 = reqDict['cmd']
        except:
            P2 = ''

        try:
            K3 = 'launch'
            P3 = reqDict['launch']
        except:
            P3 = ''


        try:
            K4 = 'arg'
            P4 = reqDict['arg']
        except:
            P4 = ''

        return  { K0 : P0 , K1 : P1 ,K2 : P2, K3 : P3, K4 : P4,}





    def checkmsg(self, reqDict):
        """ individual treatment of requests and their parms here
       static char *checkmsg[] = { (char *)checkmsg_func, "checkmessages", "V", "daemonid", 0 };

    """#
        K0 = 'requestType'
        P0 = 'checkmessages'
        try:
            K1 = 'daemonid'
            P1 = reqDict['daemonid']
        except:
            P1 = ''


        return  { K0 : P0 , K1 : P1 , }


    #
##########################
##########################
##########################
##########################






class QC_777_pBet(QC_777Base):

    colon = ':'
    quot = '\\"'

    def placeLay(self, reqDict):
        """ individual treatment of requests and their parms here """#

        K0 = 'requestType'
        P0 = 'placeLay'
        # unwrap into tuple here, and take in the relevant function!
        parms = ( (K0,P0), ) # need the extra comma to force len(parms)==1 for ONE tuple
        jsonSpecs = self.assembleQuery(parms)
        #print("\n\n\n",jsonSpecs)
        return jsonSpecs





##################
################## 178.62.185.131
##################


class QueryComposer_777(QC_777Base):
    """

This is the wrapper class


    // glue 7
        // multisig 2
        // Kademlia DHT  8
        // MofNfs 3
        // Telepathy 9
        // Teleport 3
        // InstantDEX 6
        // Tradebot 3
        // # privatebet 1

    """ #
    # this list needs ALL API calls for routing to here from ServerFactory

    #API_callsRPC = ['start', 'stop']
    # these can be instantiated w/ different factories



    API_calls = [
                   '                 glue 7',\
                   'gotjson',\
                   'gotpacket',\
                   'gotnewpeer',\
                   'BTCDpoll',\
                   'GUIpoll',\
                   'stop',\
                   'start',\
                   'settings',\
                   '                  ramchains 13',\
                   'ramstatus',\
                   'ramaddrlist',\
                   'ramstring',\
                   'ramrawind',\
                   'ramblock',\
                   'ramscript',\
                   'ramtxlist',\
                   'ramrichlist',\
                    'ramcompress',\
                    'ramexpand',\
                   'rambalances',\
                   'rampyramid' ,\
                   'ramresponse',\
                   '                   MGW 7',\
                   'genmultisig',\
                   'getmsigpubkey',\
                   'MGWaddr',\
                   'MGWresponse',\
                   'setmsigpubkey',\
                   'cosign',\
                   'cosigned',\
                   '                   IPcomms 6',\
                   'ping',\
                   'pong',\
                   'sendfrag',\
                   'gotfrag',\
                   'startxfer',\
                   'getfile',\
                   '                   Kademlia DHT 8',\
                   'store',\
                   'findvalue',\
                   'findnode',\
                   'havenode',\
                   'havenodeB',\
                   'findaddress',\
                   'puzzles',\
                   'nonces',\
                   '                   MofNfs 3',\
                   'savefile',\
                   'restorefile',\
                   'publish',\
                   '                  Telepathy 9',\
                   'getpeers',\
                   'addcontact',\
                   'removecontact',\
                   'dispcontact',\
                   'telepathy',\
                   'getdb',\
                   'sendmessage',\
                   'sendbinary',\
                   '                   Teleport 3',\
                   'maketelepods',\
                   'telepodacct',\
                   'teleport',\
                                       'InstantDEX 17',\
                   'trollbox',\
                   'allorderbooks',\
                   'openorders',\
                   'orderbook',\
                   'placebid',\
                   'placeask',\
                   'makeoffer3',\
                   'respondtx',\
                   'processutx',\
                   'bid',\
                   'ask',\
                   'allsignals',\
                   'lottostats',\
                   'tradehistory',\
                   'getsignal',\
                   'cancelquote',\
                   'jumptrades',\
                   '                   Tradebot 3',\
                   'pricedb',\
                   'getquotes',\
                   'tradebot',\
                    '                     Privatebet',\
                    'lotto',\
                    '                     plugins'\
                    'checkmsg',\
                   'passthru',\
                   'remote',\
                    'syscall',\
                   ]




    def __init__(self, environ = {}):
        super(QueryComposer_777, self).__init__(environ)
        #self.scheduler = scheduler
        self.environ = environ

        self.BitcoinDarkRPCCreds = environ['BitcoinDarkRPCCreds']
        #self.create_base64_encoded_Creds()
        print("here we compose the specific details of the query that is sent to the data provider service")

        self.jl777_pBet = QC_777_pBet(environ)
        self.jl777_iDex = QC_777_iDex(environ)
        self.jl777_aAll = QC_777_aAll(environ)


    def lookUpQuery(self, reqDict):

        if reqDict['requestType'] == 'lotto':
        #     // # privatebet 1

            jsonSpecs = self.jl777_aAll.lotto(reqDict)
            return jsonSpecs

        # // glue 8 ! 'start' is routed through BTCD, not supernet core

        elif reqDict['requestType'] == 'gotjson':
            jsonSpecs = self.jl777_aAll.gotjson(reqDict)
            return jsonSpecs

        elif reqDict['requestType'] == 'gotpacket':
            jsonSpecs = self.jl777_aAll.gotpacket(reqDict)
            return jsonSpecs

        elif reqDict['requestType'] == 'gotnewpeer':
            jsonSpecs = self.jl777_aAll.gotnewpeer(reqDict)
            return jsonSpecs

        elif reqDict['requestType'] == 'BTCDpoll':
            jsonSpecs = self.jl777_aAll.BTCDpoll(reqDict)
            return jsonSpecs

        elif reqDict['requestType'] == 'GUIpoll':
            jsonSpecs = self.jl777_aAll.GUIpoll(reqDict)
            return jsonSpecs

        elif reqDict['requestType'] == 'stop':
           jsonSpecs = self.jl777_aAll.stop(reqDict)
           return jsonSpecs

        # NOTE: this is used by another parser!
        elif reqDict['requestType'] == 'start':
            jsonSpecs = self.jl777_aAll.start(reqDict)
            return jsonSpecs

        elif reqDict['requestType'] == 'settings':
            jsonSpecs = self.jl777_aAll.settings(reqDict)
            return jsonSpecs

        # ramchains 13


        elif reqDict['requestType'] == 'ramstatus':
            jsonSpecs = self.jl777_aAll.ramstatus(reqDict)
            return jsonSpecs

        elif reqDict['requestType'] == 'ramaddrlist':
            jsonSpecs = self.jl777_aAll.ramaddrlist(reqDict)
            return jsonSpecs

        elif reqDict['requestType'] == 'ramstring':
            jsonSpecs = self.jl777_aAll.ramstring(reqDict)
            return jsonSpecs

        elif reqDict['requestType'] == 'ramrawind':
            jsonSpecs = self.jl777_aAll.ramrawind(reqDict)
            return jsonSpecs

        elif reqDict['requestType'] == 'ramblock':
            jsonSpecs = self.jl777_aAll.ramblock(reqDict)
            return jsonSpecs

        elif reqDict['requestType'] == 'ramscript':
            jsonSpecs = self.jl777_aAll.ramscript(reqDict)
            return jsonSpecs

        elif reqDict['requestType'] == 'ramtxlist':
            jsonSpecs = self.jl777_aAll.ramtxlist(reqDict)
            return jsonSpecs

        elif reqDict['requestType'] == 'ramrichlist':
            jsonSpecs = self.jl777_aAll.ramrichlist(reqDict)
            return jsonSpecs

        elif reqDict['requestType'] == 'ramcompress':
            jsonSpecs = self.jl777_aAll.ramcompress(reqDict)
            return jsonSpecs

        elif reqDict['requestType'] == 'ramexpand':
            jsonSpecs = self.jl777_aAll.ramexpand(reqDict)
            return jsonSpecs

        elif reqDict['requestType'] == 'rambalances':
            jsonSpecs = self.jl777_aAll.rambalances(reqDict)
            return jsonSpecs

        elif reqDict['requestType'] == 'rampyramid':
            jsonSpecs = self.jl777_aAll.rampyramid(reqDict)
            return jsonSpecs

        elif reqDict['requestType'] == 'ramresponse':
            jsonSpecs = self.jl777_aAll.ramresponse(reqDict)
            return jsonSpecs


        #     //  MGW 7

        elif reqDict['requestType'] == 'genmultisig':
            jsonSpecs = self.jl777_aAll.genmultisig(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'getmsigpubkey':
            jsonSpecs = self.jl777_aAll.getmsigpubkey(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'MGWaddr':
            jsonSpecs = self.jl777_aAll.MGWaddr(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'MGWresponse':
            jsonSpecs = self.jl777_aAll.MGWresponse(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'setmsigpubkey':
            jsonSpecs = self.jl777_aAll.setmsigpubkey(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'cosign':
            jsonSpecs = self.jl777_aAll.cosign(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'cosigned':
            jsonSpecs = self.jl777_aAll.cosigned(reqDict)
            return jsonSpecs


        #     // IPcomms 5

        elif reqDict['requestType'] == 'ping':
            jsonSpecs = self.jl777_aAll.ping(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'pong':
            jsonSpecs = self.jl777_aAll.pong(reqDict)
            return jsonSpecs

        elif reqDict['requestType'] == 'sendfrag':
            jsonSpecs = self.jl777_aAll.sendfrag(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'gotfrag':
            jsonSpecs = self.jl777_aAll.gotfrag(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'startxfer':
            jsonSpecs = self.jl777_aAll.startxfer(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'getfile':
            jsonSpecs = self.jl777_aAll.getfile(reqDict)
            return jsonSpecs


        #     // Kademlia DHT  6

        elif reqDict['requestType'] == 'store':
            jsonSpecs = self.jl777_aAll.store(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'findvalue':
            jsonSpecs = self.jl777_aAll.findvalue(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'findnode':
            jsonSpecs = self.jl777_aAll.findnode(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'havenode':
            jsonSpecs = self.jl777_aAll.havenode(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'havenodeB':
            jsonSpecs = self.jl777_aAll.havenodeB(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'findaddress':
            jsonSpecs = self.jl777_aAll.findaddress(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'puzzles':
            jsonSpecs = self.jl777_aAll.puzzles(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'nonces':
            jsonSpecs = self.jl777_aAll.nonces(reqDict)
            return jsonSpecs

        #     // MofNfs 3

        elif reqDict['requestType'] == 'savefile':
            jsonSpecs = self.jl777_aAll.savefile(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'restorefile':
            jsonSpecs = self.jl777_aAll.restorefile(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'publish':
            jsonSpecs = self.jl777_aAll.publish(reqDict)
            return jsonSpecs

        #     // Telepathy 9

        elif reqDict['requestType'] == 'getpeers':
            jsonSpecs = self.jl777_aAll.getpeers(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'addcontact':
            jsonSpecs = self.jl777_aAll.addcontact(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'removecontact':
            jsonSpecs = self.jl777_aAll.removecontact(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'dispcontact':
            jsonSpecs = self.jl777_aAll.dispcontact(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'telepathy':
            jsonSpecs = self.jl777_aAll.telepathy(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'getdb':
            jsonSpecs = self.jl777_aAll.getdb(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'sendmessage':
            jsonSpecs = self.jl777_aAll.sendmessage(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'sendbinary':
            jsonSpecs = self.jl777_aAll.sendbinary(reqDict)
            return jsonSpecs

        #     // Teleport 3

        elif reqDict['requestType'] == 'maketelepods':
            jsonSpecs = self.jl777_aAll.maketelepods(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'telepodacct':
            jsonSpecs = self.jl777_aAll.telepodacct(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'teleport':
            jsonSpecs = self.jl777_aAll.teleport(reqDict)
            return jsonSpecs

        #     // InstantDEX 18

        elif reqDict['requestType'] == 'trollbox':
            jsonSpecs = self.jl777_aAll.trollbox(reqDict)
        elif reqDict['requestType'] == 'allorderbooks':
            jsonSpecs = self.jl777_aAll.allorderbooks(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'openorders':
            jsonSpecs = self.jl777_aAll.openorders(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'orderbook':
            jsonSpecs = self.jl777_aAll.orderbook(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'placebid':
            jsonSpecs = self.jl777_aAll.placebid(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'placeask':
            jsonSpecs = self.jl777_aAll.placeask(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'makeoffer3':
            jsonSpecs = self.jl777_aAll.makeoffer3(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'respondtx':
            jsonSpecs = self.jl777_aAll.respondtx(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'processutx':
            jsonSpecs = self.jl777_aAll.processutx(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'bid':
            jsonSpecs = self.jl777_aAll.bid(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'ask':
            jsonSpecs = self.jl777_aAll.ask(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'allsignals':
            jsonSpecs = self.jl777_aAll.allsignals(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'lottostats':
            jsonSpecs = self.jl777_aAll.lottostats(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'tradehistory':
            jsonSpecs = self.jl777_aAll.tradehistory(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'getsignal':
            jsonSpecs = self.jl777_aAll.getsignal(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'cancelquote':
            jsonSpecs = self.jl777_aAll.cancelquote(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'jumptrades':
            jsonSpecs = self.jl777_aAll.jumptrades(reqDict)
            return jsonSpecs

        #     // Tradebot 3

        elif reqDict['requestType'] == 'pricedb':
            jsonSpecs = self.jl777_aAll.pricedb(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'getquotes':
            jsonSpecs = self.jl777_aAll.getquotes(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'tradebot':
            jsonSpecs = self.jl777_aAll.tradebot(reqDict)
            return jsonSpecs

        # // plugins
        elif reqDict['requestType'] == 'checkmsg':
            jsonSpecs = self.jl777_aAll.checkmsg(reqDict)
            return jsonSpecs

        elif reqDict['requestType'] == 'passthru':
            jsonSpecs = self.jl777_aAll.passthru(reqDict)
            return jsonSpecs

        elif reqDict['requestType'] == 'remote':
            jsonSpecs = self.jl777_aAll.remote(reqDict)
            return jsonSpecs

        elif reqDict['requestType'] == 'python':
            jsonSpecs = self.jl777_aAll.python(reqDict)
            return jsonSpecs
        elif reqDict['requestType'] == 'syscall':
            jsonSpecs = self.jl777_aAll.syscall(reqDict)
            return jsonSpecs

        else:
            raise LookupError(str(reqDict))
            #return 'err'


    def make_777POST_Request(self, reqDict):
        """
        This return a dict for using python requests lib.
        But I do it rather awkward and know what I do than use some module I can't control
        The messages that are sent to the jl777 server are composed on the lowest level possible.
        Maybe a more elegant was can be found, but for now this works.
        """ #
        jsonSpecs = self.lookUpQuery(reqDict)
        # if jsonSpecs[:5] == 'error':
        #     raise LookupError(str(reqDict))
        #     return jsonSpecs
        return jsonSpecs #req777 # REQUESTS!!



    def make_rawBytes_Request(self, reqDict):
        """
        This looks really awkward!
        But I do it rather awkward and know what I do than use some module I can't control
        The messages that are sent to the jl777 server are composed on the lowest level possible.
        Maybe a more elegant was can be found, but for now this works.

        We use this for the STOP and START calls only. These go through RPC, not 777
        """ #

        jsonSpecs = self.lookUpQuery(reqDict)
        if jsonSpecs[:5] == 'error':
            raise LookupError(str(reqDict))
            return jsonSpecs

        # below are generic parts of the raw POST byte string that have to be added to the individual REQ part
        jsonStart='["{'
        jsonLast='}"]}'
        jsonPayl3 = jsonStart + jsonSpecs + jsonLast
        paylBase = '{"jsonrpc": "1.0", "id":"curltest", "method": "SuperNET", "params": '
        jsonPayL4 = paylBase + jsonPayl3
        contLen = str(len(jsonPayL4))
        reqString = self.reqBase + str(contLen) + '\r\n\r\n' + jsonPayL4
        #reqString = reqBase + str(contLen) + '\r\n\r\n' + jsonPayL4
        reqFull = reqString.encode("utf-8")
        newQuery = reqFull
        print( 3*"\nself.newQuery ---> ",str(newQuery))
        #log.msg("POST. making newQuery  query_jl777---> ",str(reqDict))
        return newQuery



##########################
##########################
##########################
##########################



class QueryComposer_LOC(object):
    """ The base class can be used for common functions and declarations if needed """#

    API_calls = [ 'soccer_schedule', 'MORE', ]

    def __init__(self, environ = {}):
        print("here we compose the specific details of the query that is sent to the data provider service")
        self.environ = environ
        self.CACHE_DIR = environ['localCacheDir']
        self.CACHE_FILENAMES = environ['CACHE_FILENAMES']

    def make_LOC_Request(self, reqDict):
        """  select requestType and send to filename composition method  load local cache """#

        try:
            cacheFileName = self.CACHE_FILENAMES[reqDict['requestType']]
        except:
            raise LookupError(str(reqDict))
            #cacheFileName =  'defaultFileNameWithErrorMsg.txt'

        cache = self.CACHE_DIR + cacheFileName
        xmlCacheFile = open(cache, 'r')
        xmlCached_unparsed = xmlCacheFile.read()
        xmlCacheFile.close()
        #print("loaded file:2 ", xmlCached_unparsed[:300])
        xmlCached_unparsed_bytes = xmlCached_unparsed.encode("utf-8")

        #self.parse() probably! Do! This!

        return xmlCached_unparsed_bytes
