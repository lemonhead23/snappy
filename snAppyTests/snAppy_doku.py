#!/usr/bin/python3
# -*- coding: utf-8 -*-


SuperNET_api_controller_doku = """



Snappy acts as a relay that receives and relays commands to SuperNET.

It also provides scripting facilities that are running on timers.



This SuperNET api controller his started with

./snApi17a.py start
./snApi17a.py stop


General command format:

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=settings'


Launches scripts in UseCase classes:


UC1_pingPong


./snAppy17c.py UC1






-console
- nohup ./snApi17a.py start  + tail -f nohup.txt
http://www.nxtfans.net/
-dedicated logfile (currently enter in pyDaemon3.py)
-logging can be done 'silent' = no outputs,



It uses a standard python daemonization method.

The file snApiConfig.py contains environment dictionaries with the ports and other config info, e.g. the BitcoinDarkd rpc auth

scripts/testCases can be started by using:

This instantiates a scheduler that runs the designated script/test class

#################################################################################################





 List of manual commands for quick function tests // often used



cd

    ./BitcoinDarkd  stop


    ./BitcoinDarkd  SuperNET '{"requestType":"stop"}'

    ./BitcoinDarkd  SuperNET '{"requestType":"start"}'

    ./BitcoinDarkd  SuperNET '{"requestType":"settings"}'





curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=stop'

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=start'

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=settings'

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=getpeers'

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=ping&destip=79.245.52.39'

 #178.62.185.131'




curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/stop?'

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/start?'



#########################################################


Running use cases and scripts:

 ./snappy.py UCxyz


Adding of test cases and scripts:

- make a class
- make schedule(s)
- add launch param in init functions


##########################################################



communication with SuperNET server:

 Done using python requests POST and deferred.

 Can also use compose POST requests on a raw bytes level (unused but kept).

Could be done with twisted agent. Works as is.



###########################################################


This SuperNET api controller has different operations modi.

This is achieved by instantiating different twisted protocols.

Currently:

- Protocol for querying xml feed getpage
- Protocol for querying SuperNET with POST
- Protocol for querying BitcoindarkD with RPC
- Twisted Scheduler for timer controlled operations
- direct loading from a locally cached file





###########################################################



--------->         6 steps to include new API calls into this api controller


~~~~~~~~~~~~~~~~~~~
in file Parsers.py:
~~~~~~~~~~~~~~~~~~~


1 make class for api call
-------------------------


eg 'settings':

    class Parser_jl777_settings(Parser_JL777_Base):

        def parse(self, data2parse):
            return data2parse

subclassing Parser_JL777_Base




2 register this class in Parser777
----------------------------------


class Parser_777(object):
    "" Parser_777
    // # privatebet
    ""#

    ql777_settings = Parser_jl777_settings()







3 add elif case for requestType in def parse_777()
--------------------------------------------------

    elif requestType2Parse == 'settings':
        parsed = self.ql777_settings.parse(data_result)





~~~~~~~~~~~~~~~~~~~~~~~~~~
in file QueryCOmposers.py:
~~~~~~~~~~~~~~~~~~~~~~~~~~


4 add api call to list in class declaration of class QueryComposer_777
----------------------------------------------------------------------


class QueryComposer_777(QC_777Base):


    API_calls = ['settings',]







5 add elif case for requestType in def lookUpQuery of class QueryComposer_777
-----------------------------------------------------------------------------


        elif reqDict['requestType'] == 'gotjson':
            jsonSpecs = self.jl777_aAll.gotjson(reqDict)






6 add def <callName> in class QC_777_aAll
-----------------------------------------



    def settings(self, reqDict):
        "" individual treatment of requests and their parms here ""#
        K0 = 'requestType'
        P0 = 'settings'
        try:
            K1 = 'field'
            P1 = reqDict['field']
        except:
            P1 = ''




------------------------------------------------------------
------------------------------------------------------------


###########################################################

###########################################################

###########################################################

###########################################################

Output of 'settings' command:


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
  "MAINNET":1,
  "MIN_NXTCONFIRMS":13,
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
      "pubaddr":"RHwBRZzbETNR3nyQjuVWgaLdaBNBu3gwbw",
      "srvpubaddr":"RWfwbc25mPTcSN4WgDXZeMnf3SFT1rN8tM",
      "al5":"RWW6FPcopt5va8TtGkPsPTK9GEr8r8QS9Q",
      "basil2":"RTib4uLAc9DfP2x6tGsQ9SZzFfXmcgGqZm",
      "grind1":"RMwvWWWRVgp7QBJuAwCpvmP6Q27kAYhnAc",
      "rarah4":"RVYtALDy7WspnvxFrdDDoVafAdTNuqipyH",
      "Lfactor":3
    }
  ]
}


##############################################################




SuperNET.conf


The "ciphers" field specifies a sequence of ciphers to encrypt your telepods with.
You can make any length sequence out of any of the following:

   "aes","blowfish","xtea","rc5","rc6","saferp","twofish","safer_k64","safer_sk64","safer_k128",
    "safer_sk128","rc2","des3","cast5","noekeon","skipjack","khazad","anubis","rijndael"

Not all of these ciphers have been tested, so do not use them willy nilly on any telepods with big amounts!

"Lfactor" is the default L value used for determining the number of onion layers, subject to a system max limit,
plus going much over 10 will overflow the packet size limit even for small messages.

"pubaddr" is a CRITICAL field and without it, nothing will work.
The first time you run ./BitcoinDarkd it will print out a set of addresses you can use for pubaddr and srvpubaddr
and the pubaddr needs to be addresses in your wallet

"privacyServer":"127.0.0.1" enables the loopback privacy server and also requires a "srvpubaddr" field
 this is the only configuration I have been testing so far.

You just need to use an address in your wallet

./BitcoinDarkd listreceivedbyaddress
./BitcoinDarkd listaddressgroupings
./BitcoinDarkd getaccountaddress "accountname"


SuperNET is embedded inside bitcoinDarkd <jl777> used the Bitcoin message system to bootstrap the SuperNET network

Stuff like Teleport would pretty much work for any bitcoind coin
but BTCD has some special stuff to make it work better,
in some cases much better, so that is the preferred coin to Teleport



the privkey to the BTCD addresses you put in the SuperNET.conf file are the NXT passwords


##############################################################


BTCD and SuperNET can be started and stopped independently.
SuperNET stop and start from BTCD and BTCD keeps running
ot BTCD start also starts SuperNET


########################################################################################



  examples CURL

curl --user azure:Ir9qDmicntTxH8C --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "SuperNET", "params": ["{\"requestType\":\"getpeers\"}"]  }' -H 'content-type: text/plain;' http://127.0.0.1:14632/

RAW bytes through socket:
 b'POST / HTTP/1.1\r\nAuthorization: Basic YXp1cmU6SXI5cURtaWNudFR4SDhD\r\nUser-Agent: curl/7.35.0\r\nHost: 127.0.0.1:14632\r\nAccept: */*\r\ncontent-type: text/plain;\r\nContent-Length: 103\r\n\r\n{"jsonrpc": "1.0", "id":"curltest", "method": "SuperNET", "params": ["{\\"requestType\\":\\"getpeers\\"}"]}'

#############################################################################################


##################################################################################################






confirmed calls


// glue 7

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=GUIpoll'

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=settings'

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=stop'

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=start'




curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=ping&destip=209.126.70.156'



    // MGW 6

./.



              // IPcomms',\



curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=ping&destip=178.62.185.131'

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=pong'





    // Kademlia DHT 8




curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=store&name=LUMBERJACK&data=FEEEEE123443534425AABB'

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=findnode&key=3571143576961987768'

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=havenode&key=2131686659786462901' Internal call

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=havenodeB&key=3571143576961987768' Internal call

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=getpeers&scan=1'





    // MofNfs 3



    // Telepathy 9



    // Teleport 3



    // InstantDEX 6

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=orderbook&baseid=4551058913252105307&relid=11060861818140490423'

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=placebid&baseid=11060861818140490423&relid=4551058913252105307&volume=1.005&price=0.004'


curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=placeask&baseid=11060861818140490423&relid=4551058913252105307&volume=1.005&price=0.014'


    // Tradebot 3


    // # privatebet 1







##################################################################################################
  // glue 7

                  'gotjson',\
                   'gotpacket',\
                   'gotnewpeer',\
                   'BTCDpoll',\
                   'GUIpoll',\
                   'stopDummy',\
                   'startDummy',\
                   'settings',\




1
    static char *gotjson[] = { (char *)gotjson_func, "BTCDjson", "", "json", 0 };
    ./BitcoinDarkd SuperNET '{"requestType":"BTCDjson", "json":""}'

------------------------------------------------------------------------------------------



2
    static char *gotpacket[] = { (char *)gotpacket_func, "gotpacket", "", "msg", "dur", "ip_port", 0 };
./BitcoinDarkd SuperNET '{"requestType":"gotpacket"}'
------------------------------------------------------------------------------------------




3
    static char *gotnewpeer[] = { (char *)gotnewpeer_func, "gotnewpeer", "", "ip_port", 0 };
./BitcoinDarkd SuperNET '{"requestType":"gotnewpeer"}'
------------------------------------------------------------------------------------------




4
    static char *BTCDpoll[] = { (char *)BTCDpoll_func, "BTCDpoll", "", 0 };
./BitcoinDarkd SuperNET '{"requestType":"BTCDpoll"}'
------------------------------------------------------------------------------------------




5

    static char *GUIpoll[] = { (char *)GUIpoll_func, "GUIpoll", "", 0 };




curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=GUIpoll'


I do assume only one external caller. There are some calls that return a "result":"pending" with a "txid", when you get such a response,

you need to call GUIpoll {"requestType":"GUIpoll"} until it gets a JSON return:


{"result":"<stringified>","txid":"<pendingtxid>"}
you need to destringify the result and that will be like the return result had the command completed without going through a pending stage.


------------------------------------------------------------------------------------------

6

    static char *stop[] = { (char *)stop_func, "stop", "", 0 };

!!! start is routed through BTCD RPC !!!


------------------------------------------------------------------------------------------




7


    static char *settings[] = { (char *)settings_func, "settings", "", "field", "value", "reinit", 0 };



 ./BitcoinDarkd SuperNET '{"requestType":"settings","field":"LIBTEST","value":"1"}'

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=setting' #s&field=LIBTEST&value=1'

{'active': ['BTCD'], 'MIN_NXTCONFIRMS': 13, 'debug': 2, 'LIBTEST': '1', 'whitelist': ['209.126.70.156', '209.126.70.159', '209.126.70.170', '104.40.137.20', '104.41.129.107', '162.248.163.43', '23.97.66.164', '100.79.14.220', '137.116.193.215', '80.82.64.135', '185.21.192.9', '94.102.63.149', '37.187.200.156', '199.193.252.103', '89.212.19.49', '128.199.183.249', '190.10.10.145'], 'coins': [{'pubaddr': 'RHwBRZzbETNR3nyQjuVWgaLdaBNBu3gwbw', 'maxevolveiters': 10, 'privacyServer': '127.0.0.1', 'clonesmear': 1, 'minconfirms': 3, 'nohexout': 1, 'estblocktime': 60, 'backupdir': '/home/azure/backups', 'conf': '/home/azure/.BitcoinDark/BitcoinDark.conf', 'asset': '11060861818140490423', 'name': 'BTCD', 'Lfactor': 3, 'ciphers': [{'skipjack': 'RNmF5YmUY81wWu1njRiYvJRoKMf1Ms9kN3'}, {'aes': 'RXcpYBAWbbNgNBSnr8kB9sufSfZDwttXwC'}, {'blowfish': 'RJgoTjReeE2ZKbymx4PyiyXmgsbTkW9sds'}], 'srvpubaddr': 'RWfwbc25mPTcSN4WgDXZeMnf3SFT1rN8tM', 'useaddmultisig': 1, 'rpc': '127.0.0.1:14632'}], 'MAINNET': 1}


  ./BitcoinDarkd SuperNET '{"requestType":"settings","field":"LIBTEST","value":"2"}'
  ./BitcoinDarkd SuperNET '{"requestType":"settings","value":"{\"LIBTEST\":\"1\"}"}'
  ./BitcoinDarkd SuperNET '{"requestType":"settings","value":"deadbeef"}'
  ./BitcoinDarkd SuperNET '{"requestType":"settings","field":"debug","value":"1"}'


"settings" has three modes. if you just call it without any fields, it will return the current SuperNET.conf
this way you can display to the user the current settings

now there is a replace mode, which is indicated by having a "field" parameter, eg. ./BitcoinDarkd SuperNET '{"requestType":"settings","field":"debug"}'
if you have no "value" field, the specified field will be deleted from the SuperNET.conf and it will be saved to HDD

an automatic backup is made to SuperNET.conf.old
also SuperNET.conf.old is copied to the backups directory, so this way there are the last two versions available,
but no provision to access them for now. will have to manually retrieve them

if you have a value field specified, it replaces the existing value or creates a new entry:

./BitcoinDarkd SuperNET '{"requestType":"settings","field":"debug","value":"3"}'

the final variation is if you have "value" but no "field" specified and if the value is a hexstr,
then this is converted to binary and the entire SuperNET.conf file is replaced with this
to use this, you probably have to create the desired JSON for the SuperNET.conf and convert to hex.
I had to do this due to too many levels of stringification and different paths, some having one less level. just too confusing.










------------------------------------------------------------------------------------------


    // passthru     2



                 'passthru',\
                   'remote',\

 call_NOT_TESTED

  static char *passthru[] = { (char *)passthru_func, "passthru", "", "coin", "method", "params", 0 };


call_NOT_TESTED

    static char *remote[] = { (char *)remote_func, "remote", "V",  "coin", "method", "result", "tag", 0 };








##################################################################################################

    //     MGW   7

##################################################################################################
------------------------------------------------------------------------------------------



                 'genmultisig',\
                   'getmsigpubkey',\
                   'MGWaddr',\
                   'setmsigpubkey',\
                   'MGWdeposits',\
                   'cosign',\
                   'cosigned',\





    static char *genmultisig[] = { (char *)genmultisig_func, "genmultisig", "V", "coin", "refcontact", "M", "N", "contacts", "destip", 0 };





    static char *getmsigpubkey[] = { (char *)getmsigpubkey_func, "getmsigpubkey", "V", "coin", "refNXTaddr", "myaddr", "mypubkey", 0 };





    static char *MGWaddr[] = { (char *)MGWaddr_func, "MGWaddr", "V", 0 };





    static char *setmsigpubkey[] = { (char *)setmsigpubkey_func, "setmsigpubkey", "V", "coin", "refNXTaddr", "addr", "pubkey", 0 };





    static char *MGWdeposits[] = { (char *)MGWdeposits_func, "MGWdeposits", "V", "NXT0", "NXT1", "NXT2", "ip0", "ip1", "ip2", "coin", "asset", "rescan", "actionflag", "specialNXT", "exclude0", "exclude1", 0 };




------------------------------------------------------------------------------------------



                                        cosign


8 call_NOT_TESTED

    static char *cosign[] = { (char *)cosign_func, "cosign", "V", "otheracct", "seed", "text", 0 };

cosign just has "otheracct", "seed", "text"

------------------------------------------------------------------------------------------


                                        cosigned



9 call_NOT_TESTED

    static char *cosigned[] = { (char *)cosigned_func, "cosigned", "V", "seed", "result", "privacct", "pubacct", 0 };


------------------------------------------------------------------------------------------





 '                   IPcomms',\





                   'ping',\
                   'pong',\
                   'sendfrag',\
                   'gotfrag',\
                   'startxfer',\






I implemented a variant of http://www.cs.rice.edu/Conferences/IPTPS02/109.pdf, using 64bit NXT addresses for the hash,

eg. least significant 64bits of sha256.

collision resolution is something for a layer above this level to do.

I plan to add some simple file API on top of this so we can get a nice decentralized storage along with sending of files.

of course all this is under heavy encryption, but still the IP addresses are not shielded yet.

The sendmessage API appears to be working in simple topologies, should work with more layers, but need a larger network to test this.



I have made some changes to protocol the PDF describes, but by and large I am following what it describes.

In addition to the recommended values (ip, port, nodeid),

I am also sending along the session based nacl pubkey that allows encrypted comms. the nodeid is the 64bit NXT address.


a lot of the fields are optional and/or internally generated, the following are the allowed fields for each command:

I had to tweak some things so that users can pass in "name" but internally it is mapped to a 64bit key (hashkey)

store -> if user invoked sends to nodes closest to the hashkey, otherwise it just stores it in a LRU fifo



The purpose of the DHT calls are to get the SuperNET routing reliable by decentralizing the routing table and

in the process of doing this, the nacl public keys are also propagated.

This allows the code to automatically encrypt even these DHT calls as soon as it establishes a link with the other node.


All packets the same size, thus removing a leak of info about the type of commands you are sending.


the first time, it terminates the search when another node sends a store API, which is exactly what happened.

The second search just returns the value that it has locally.



DHT working and this is all the current calls:

ping (pong),

findnode (havenode),

store,

findvalue (havenodeB).


To do it right required adding outof band binary data beyond the JSON inside the onion packet

and that was a good time to get all the packets to the same size and also get the data compression in the loop.






##################################################################################################



                                        ping


10 call_TESTED

    static char *ping[] = { (char *)ping_func, "ping", "V", "pubkey", "ipaddr", "port", "destip", 0 };



Internal Response Format:


bo-sto
<<<<<<<<<<< BTCD poll_for_broadcasts: narrowcast 360 bytes to 208.79.209.198:14631
nxtip.(85.178.203.111) {"requestType":"ping","NXT":"2131686659786462901","time":1416058308,"pubkey":"849c97e5b1e8c50429249eff867de5e6ded39d34a6ccc9c42ea720d927a12d18","ipaddr":"85.178.203.111","ver":"0.181"}
updated.nodestats.db (2131686659786462901) hp.0x7f3098000ce0 data.data 0x7f3098000ce0
PING.({"result":"kademlia_pong to (85.178.203.111/0)","txid":"8329037539464279084"})



curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=ping&destip=85.178.203.111'
curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=ping&destip=178.62.185.131'

{'result': 'kademlia_ping to 178.62.185.131', 'txid': '0'}

ping
curl -k --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "SuperNET", "params": [    "{\"requestType\":\"ping\",\"destip\":\"178.62.185.131\" }     "]  }' -H 'content-type: text/plain;' http://127.0.0.1:7776/

curl -k --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "SuperNET", "params": [    "{\"requestType\":\"ping\",\"destip\":\"85.178.203.158\" }     "]  }' -H 'content-type: text/plain;' http://127.0.0.1:7776/




------------------------------------------------------------------------------------------


                                                    pong




        GUIpoll ---> kademlia_pong

        {'args': '[{"requestType":"pong","NXT":"1978065578067355462","time":1419772744,"MMatrix":0,"yourip":"178.62.185.131","yourport":54640,"ipaddr":"89.212.19.49","pubkey":"c269a8b4567c0b3062e6c4be859d845c4b808a405dd03d0d1ac7b4d9cb725b40","ver":"0.399"},{"token":"aqqagqe2sph302rsgieobfm482580iqs386jrk2teb5tjd671ocgig2ru5ilgeo2i8mh9bi74a535tcsldc6v2g2mcmsrfi8b3rffigj21p0g2g572u31d1qdpq16oggc8qvqj22j4hcj0ahaa9toshhek4ci18m"}]', 'port': 0, 'result': '{"result":"kademlia_pong","tag":"","isMM":"0","NXT":"1978065578067355462","ipaddr":"89.212.19.49","port":0,"lag":"185.188","numpings":16,"numpongs":19,"ave":"3817.958"}', 'from': '89.212.19.49'}

        <class 'dict'>




    static char *pong[] = { (char *)pong_func, "pong", "V", "pubkey", "ipaddr", "port", "yourip", "yourport", 0 };



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













##################################################################################################






  '                   Kademlia DHT 8',\
                   'store',\
                   'findvalue',\
                   'findnode',\
                   'havenode',\
                   'havenodeB',\
                   'findaddress',\




------------------------------------------------------------------------------------------

                                                store

12  OK

DATA MUST BE HEX!


curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=store&name=star2&data=deadbeef'







    static char *store[] = { (char *)store_func, "store", "V", "pubkey", "key", "name", "data", 0 };


 curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=store&name=starbucks&data=c0ffee'

{'key': '1031470952125437106', 'txid': '0', 'result': 'kademlia_store', 'data': 'c0ffee', 'len': 3}






-----> {'data': 'deadbeef', 'result': 'kademlia_store', 'txid': '11658441434268696835', 'len': 4, 'key': '12827560090541683855'}




curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=getdb&key=4960459668609431904'


-----> {'data': 'deadbeef', 'NXT': '2131686659786462901', 'requestType': 'dbret', 'key': '12827560090541683855'}





curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=findvalue&name=star2'


-------> {'data': 'deadbeef', 'len': '4', 'key': '12827560090541683855'}




FULLRESULT?
{'result': '{"result":"kademlia_store","key":"1888203822199063024","data":"deadbeef","len":4,"txid":"16715866481694536540"}', 'from': '62.194.6.163', 'args': '[{"requestType":"store","NXT":"7837143510182070614","time":1417681759,"key":"1888203822199063024","data":4},{"token":"vrg8fulem0b0os32n0p3elmtt7p16nqsbkjfcb5u1n340v25tooi0gan4rvgrbg18rt6oq3d9m82nttaoeghkbtp0jjpalsh4miuir8s31bgo5hkmr0qih6skf785dghq6rjh9hvbvcoj350vge59cp197g0kjho"}]', 'port': 0}





./BitcoinDarkd SuperNET '{"requestType":"store","name":"starbucks","data":"c0ffee"}'

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=store&name=starbucks&data=c0ffee'

{"result":"kademlia_store","key":"1031470952125437106","data":"c0ffee","len":3,"txid":"1782911352449719975"}
./BitcoinDarkd SuperNET '{"requestType":"store","name":"starbucks","data":"c0ffee"}'
{"result":"kademlia_store","key":"1031470952125437106","data":"c0ffee","len":3,"txid":"0"}


{"requestType":"dbret","NXT":"2131686659786462901","key":"1031470952125437106","data":"c0ffee"}

./BitcoinDarkd SuperNET '{"requestType":"findvalue","name":"starbucks"}'
{"key":"1031470952125437106","data":"c0ffee","len":"3"}

./BitcoinDarkd SuperNET '{"requestType":"findvalue","key":"1031470952125437106"}'
{"key":"1031470952125437106","data":"c0ffee","len":"3"}







updated.nodestats.db (13434315136155299987) hp.0x7fb86001dfb0 data.data 0x7fb86001dfb0
do_localstore(9245776713305854803) <- (FAAA976987695876585875BBBBBBBBBBB)
updated.public.db (9245776713305854803) hp.0x7fb8666f2610 data.

{"result":"kademlia_findvalue from.(2131686659786462901) previp.() key.(12834072467348571675) datalen.0 txid.265657934412272939"}






./BitcoinDarkd SuperNET '{"requestType":"store","name":"jl777","data":"deadbeef"}'

./BitcoinDarkd SuperNET '{"requestType":"store","name":"TEEESTDATA","data":"FAAA976987695876585875BBBBBBBBBBB"}'
{"result":"kademlia_store","key":"9245776713305854803","data":"FAAA976987695876585875BBBBBBBBBBB","len":16,"txid":"16975292071954015358"}

do_localstore(9245776713305854803) <- (FAAA976987695876585875BBBBBBBBBBB)
(9245776713305854803) <- (FAAA976987695876585875BBBBBBBBBBB) already there


REPLIES at command line are longer than from snappy! check!
./BitcoinDarkd SuperNET '{"requestType":"store","name":"TEEESTDATA","data":"FAAA976987695876585875BBBBBBBBBBB"}'
{"result":"kademlia_store","key":"9245776713305854803","data":"FAAA976987695876585875BBBBBBBBBBB","len":16,"txid":"6917103578949200575"}
{"result":"kademlia_store","key":"9245776713305854803","data":"fffff97698769587658587ffffffffffff","len":17,"txid":"5089905564731578754"}



curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=store&name=LUMBERJACK&data=FEEEEE123443534425AABB'
{'key': '130410257679301898', 'len': 11, 'txid': '7320311997847871185', 'result': 'kademlia_store', 'data': 'FEEEEE123443534425AABB'}




------------------------------------------------------------------------------------------


                                                findvalue





    static char *findvalue[] = { (char *)findvalue_func, "findvalue", "V", "pubkey", "key", "name", "data", 0 };




SUCCESS:

 curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=store&name=starbucks&data=c0ffee'

{'key': '1031470952125437106', 'txid': '0', 'result': 'kademlia_store', 'data': 'c0ffee', 'len': 3}

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=findvalue&name=starbucks'

{'data': 'c0ffee'}


curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=findvalue&key=1031470952125437106'
{'data': 'c0ffee'}




./BitcoinDarkd SuperNET '{"requestType":"getdb","key":"1031470952125437106"}'
{"requestType":"dbret","NXT":"2131686659786462901","key":"1031470952125437106","data":"c0ffee"}




jl777 [6:23 PM]
basically a low level way to do a findvalue

./BitcoinDarkd SuperNET '{"requestType":"store","key":"116876777391303227","data":"deadbee32f"}'
./BitcoinDarkd SuperNET '{"requestType":"findvalue","key":"116876777391303227"}'



./BitcoinDarkd SuperNET '{"requestType":"store","key":"116876777391303227","data":"deadbee32f"}'
{"result":"kademlia_store","key":"116876777391303227","data":"deadbee32f","len":5,"txid":"9319704392032681039"}



curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=havenodeB&key=9245776713305854803'


NO SUCCESS


curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=findvalue&name=starbucks' 1031470952125437106




curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=findvalue&name=LUMBERJACK'
{'result': 'kademlia_findvalue from.(2131686659786462901) previp.() key.(130410257679301898) datalen.0 txid.5332200253572088539'}

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=findvalue&key=130410257679301898'
{'result': 'kademlia_findvalue from.(2131686659786462901) previp.() key.(130410257679301898) datalen.0 txid.9185203781652930076'}








curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=havenodeB&key=3571143576961987768'
{'result': 'kademlia_havenode from NXT.2131686659786462901 key.(3571143576961987768) value.()'} ?empty?


curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=havenodeB&key=2131686659786462901'



The

findnode  -> havenode
findvalue -> havenodeB returns the value from a previous store API call, if it has it. It does this by doing a store command to the initiator.


behave in almost the same way and mostly return havenode/havenodeB which follows the PDF.



to store data (max 256 bytes for now) in the SuperNET cloud:
./BitcoinDarkd SuperNET '{"requestType":"store","name":"<symbolic name>","value":"<up to 256 chars>"}'

to find the value for a symbolic name (max 64 bytes for now):
./BitcoinDarkd SuperNET '{"requestType":"findvalue","name":"<symbolic name>"}'




------------------------------------------------------------------------------------------


                                                findnode










curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=findnode&key=6249611027680999354'


curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=GUIpoll'




{'result': 'kademlia_findnode from.(2131686659786462901) previp.() key.(3571143576961987768) datalen.0 txid.15660482336477682725'}






13434315136155299987


    static char *findnode[] = { (char *)findnode_func, "findnode", "V", "pubkey", "key", "name", "data", 0 };

 curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=findnode&key=8894667849638377372'

{'result': 'kademlia_findnode from.(2131686659786462901) previp.() key.(16259399811509347173) datalen.0 txid.2674373594642163630'}


OKOK :
 curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=findnode&key=8894667849638377372'
{'result': 'kademlia_findnode from.(2131686659786462901) previp.() key.(8894667849638377372) datalen.0 txid.5440276930011618566'}


to find a node given NXT address:

./BitcoinDarkd SuperNET '{"requestType":"findnode","key":"3571143576961987768"}'
{"result":"kademlia_findnode from.(2131686659786462901) previp.() key.(3571143576961987768) datalen.0 txid.10630886535006363570"}


curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=findnode&key=6249611027680999354'
{'result': 'kademlia_findnode from.(2131686659786462901) previp.() key.(6249611027680999354) datalen.0 txid.5604720478451918878'}


6249611027680999354 Cassius





@l8orre: if you get a findnode you will send the findnode to the nodes that are closer to dest

all the samples are in the list

this is the raw data

I will add a field so you can get the open/high/low/close/ave per time period minute, 2 min, 5 min, 1hr etc




findnodes spawn more findnodes and also sends back a havenode

so 1 findnode can cascade through the network

@l8orre: now imagine the attacker's predicament!

only seeing 1400 byte encrypted packets without any visibility into the internals -confetti in a blizzard



args ok  [{'key': '6216883599460291148', 'requestType': 'havenode', 'data': [['6216883599460291148', '192.99.246.126', '7777', '0'], ['7067340061344084047', '94.102.50.70', '7777', '1418360786'], ['10694781281555936856', '209.126.70.170', '7777', '1418355574'], ['1978065578067355462', '89.212.19.49', '7777', '1418355275'], ['17265504311777286118', '184.175.25.117', '7777', '1418357608'], ['7108754351996134253', '167.114.2.171', '7777', '1418355385'], ['5624143003089008155', '192.99.212.250', '7777', '1418355291']], 'NXT': '6216883599460291148', 'time': 1418380319}, {'token': '7meqnnpffqh9272utch79ra8rvlih9mevl901qhml0phabmmv3cu07blu76g1681id5qgp3k8lsf9tqhv9glkk6i9u1fluohu919kb6qm8d0kpuk9af13dp684jud4u10iriovu36q2kj21l2js923v7tu6i02gf'}] <class 'list'>


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




------------------------------------------------------------------------------------------


reply to findnode


 CONTENT: GUIpoll ---> kademlia_havenode

 {'port': 0, 'result': '{"result":"kademlia_havenode from NXT.6216883599460291148 key.(6216883599460291148) value.([["6216883599460291148", "192.99.246.126", "7777", "0"], ["1785551413655174233", "192.99.151.160", "7777", "1419650453"], ["1978065578067355462", "89.212.19.49", "7777", "1419650429"], ["7108754351996134253", "167.114.2.171", "7777", "1419650429"], ["5624143003089008155", "192.99.212.250", "7777", "1419650428"], ["15178638394924629506", "167.114.2.206", "7777", "1419650459"], ["5499072856752811721", "88.179.105.82", "7777", "1419679664"]])"}', 'args': '[{"requestType":"havenode","NXT":"6216883599460291148","time":1419759443,"key":"6216883599460291148","data":[["6216883599460291148", "192.99.246.126", "7777", "0"], ["1785551413655174233", "192.99.151.160", "7777", "1419650453"], ["1978065578067355462", "89.212.19.49", "7777", "1419650429"], ["7108754351996134253", "167.114.2.171", "7777", "1419650429"], ["5624143003089008155", "192.99.212.250", "7777", "1419650428"], ["15178638394924629506", "167.114.2.206", "7777", "1419650459"], ["5499072856752811721", "88.179.105.82", "7777", "1419679664"]]},{"token":"7meqnnpffqh9272utch79ra8rvlih9mevl901qhml0phabmm1nih87blka41rfo2obvq4ask646v48guv5185cplefdi723u5qmd7mbo6hqgompsvl71o3po8ft9mg15icqkeekacuse36hlnfjgol4eipvpfu0n"}]', 'from': '192.99.246.126'}
 <class 'dict'>

# peersList =  kademlia_havenode['data']   [['6216883599460291148', '192.99.246.126', '7777', '0'], ['1785551413655174233', '192.99.151.160', '7777', '1419650453'], ['1978065578067355462', '89.212.19.49', '7777', '1419650429'], ['7108754351996134253', '167.114.2.171', '7777', '1419650429'], ['5624143003089008155', '192.99.212.250', '7777', '1419650428'], ['15178638394924629506', '167.114.2.206', '7777', '1419650459'], ['5499072856752811721', '88.179.105.82', '7777', '1419679664']]





                                            havenode




sn log:
HAVENODE.0 {"result":"kademlia_havenode from NXT.16196432036059823401 key.(16196432036059823401) value.([["16196432036059823401", "167.114.2.203", "7777", "0"], ["3571143576961987768", "89.212.19.49", "7777", "1416011411"], ["15178638394924629506", "167.114.2.206", "7777", "1415986068"], ["7108754351996134253", "167.114.2.171", "7777", "1415986068"], ["8923034930361863607", "192.99.246.33", "7777", "1415986069"], ["2131686659786462901", "178.62.185.131", "7777", "1415986805"], ["6216883599460291148", "192.99.246.126", "7777", "1415986069"]])"}

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=havenode&key=6249611027680999354'
{'result': 'kademlia_havenode from NXT.2131686659786462901 key.(2131686659786462901) value.()'}


    static char *havenode[] = { (char *)havenode_func, "havenode", "V", "pubkey", "key", "name", "data", 0 };



havenode
6249611027680999354


curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=havenode&key=6249611027680999354'
{'result': 'kademlia_havenode from NXT.2131686659786462901 key.(6249611027680999354) value.()'}







------------------------------------------------------------------------------------------


                                        havenodeB




16

    static char *havenodeB[] = { (char *)havenodeB_func, "havenodeB", "V", "pubkey", "key", "name", "data", 0 };




curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=havenodeB&key=2131686659786462901'

{'result': 'kademlia_havenode from NXT.2131686659786462901 key.(2131686659786462901) value.()'}

NOT GOOD!:

 curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=havenodeB&key=9245776713305854803'
{'result': 'kademlia_havenode from NXT.2131686659786462901 key.(9245776713305854803) value.()'}azure@boxfish:~/workbench/nxtDev/TEAM/btcd/libjl777$ ./BitcoinDarkd SuperNET '{"requestType":"store","name":"TEEESTDATA","data":"FAAA976987695876585875BBBBBBBBBBB"}'
{"result":"kademlia_store","key":"9245776713305854803","data":"FAAA976987695876585875BBBBBBBBBBB","len":16,"txid":"17024462303253575554"}


 curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=findvalue&key=9245776713305854803'
{'data': 'ffff976987695876585875ffffffffff'}

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=havenodeB&key=9245776713305854803'
{'result': 'kademlia_havenode from NXT.2131686659786462901 key.(9245776713305854803) value.()'}



6249611027680999354 Cassius




------------------------------------------------------------------------------------------


                                            findaddress

17



    static char *findaddress[] = { (char *)findaddress_func, "findaddress", "V", "refaddr", "list", "dist", "duration", "numthreads", 0 };



./BitcoinDarkd  SuperNET '{"requestType":"findaddress","refaddr":"10694781281555936856","numthreads":2,"duration":20000,"dist":28}'




curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=findaddress&      '






./BitcoinDarkd SuperNET '{"requestType":"findaddress","refaddr":"2131686659786462901","dist":24,"numthreads":20,"duration":6000,"list":["13434315136155299987","8894667849638377372","10694781281555936856","18429876966171494368","16163006958863727986","1838354277347686608","17572279667799017517","14815310753561302584"]}'





The refaddr is your privacyServer's NXT address, dist is the distance in bits (after xor),



numthreads is the number of parallel tasks doing the search, duration is in seconds and list is the reference list of public server addressees

This will run in the background until the time runs out and it will print out a password and stats for your super private account.

I havent done the storing in encrypted file or anything else yet. while it is running, if it finds a better acct, it will print:

>>>>>>>>>>>>>>> new best (super secret password) ...

so you can always search for this and get decent accounts to use while the findaddress keeps working in the background.

It is kind of like mining! But what it is doing is actually very useful.

It is finding the perfect address for you to use by making it look like an address that could be linked to any of the other public servers.

Due to the way the accounts are created, bruteforce random guessing is the best way to find such an address.

This is a good thing as it means that the encryption is quite good.

After all if the distance between the mined acct and the reference account went to zero, we have effectively hacked it!

The search is creating an N dimensional space where each dimension is the distance from one of the server accts in the list.

The metric function is a bit more complicated, but conceptually we want a point in N-space that is equidistant from as many public nodes as possible.

With the current number of nodes being so small, it is hard to come up with any address that meets this criteria,

but at a distance of 24, given enough time, it should be possible to find an address that is +/- 3 distance from most of the list.

I am hoping that with more nodes, it will be possible to find addresses that are around 20 bits distant and still have the above characteristic.

Now why on earth do we care about such things?

The reason is that this solves the "last mile" problem of how to establish totally private comms without resorting to broadcasting to everybody.

My coding the DHT is what allowed me to solve this, so those that think these seemingly unrelated things are slowing down the progress,

it is quite the opposite.

It is helping achieve the ultimate goal!

To understand how this allow comms without divulging the IP address, requires a bit of background on DHT,

especially the Kademlia XOR distance method.

Using XOR as a distance function sounds so simple, but it has some very powerful mathematical properties.

Namely, you can know if another node is closer or farther away from the desired location, totally in the abstract.

Imagine that you start searching for something. It gets a delivery address (in the abstract not IP).

Now you find all the nodes you know about that are closest to this address and ask them to deliver it.

You only know they are closer to the destination that you are.

That's it!

Of course a lot more details, but this is emergent behavior, eg. out of very simple behavior at the local level,

some powerful global functionality emerges.

Imagine you got the packet from someone that was farther away than you are.

Now you do the same thing and the packet keeps getting closer and closer to the destination.

Finally it gets to the nodes that are as close as possible that are in the network.

All the SuperNET nodes are part of this "bucket brigade", each passing the packet one step closer to the destination.

This means that your node is also going to be involved in this and everybody knows your public server's acct and IP address.

If not because you publish it, but if they wanted to the attacker can do sybil attacks and get this info.

It is simply unavoidable to get an account linked to the IP address if you are transacting with it.

However, we have the private address that only people you transact with know.

Your privacyServer's acct is known along with its IP address, but as long as you are careful with who finds out your privateaddress,

then it is just an address that happens to be equidistant from N other privacy servers.

Which one? Could be any of them as the way the DHT works is that it replicates the info to all the nodes closest to the destination, which in this case is your address.

Taking advantage of this property of the DHT and the fact that your privacyServer will be

handling the routing allows packets that are encrypted to your private address to be received by your computer and you can decrypt it as it is sent on to the closer nodes.

As the network grows, it will become harder and harder even to identify the set of possible nodes your private address belongs to.

So even if your private address is compromised, there isnt a way to link it to any IP address!

James


------------------------------------------------------------------------------------------








##################################################################################################
    // MofNfs 3


                  'savefile',\
                   'restorefile',\
                   'publish',\




I changed the name of "usbdir" to "backup" just because it is unlikely to actually be a usb
I also added a "pin" field, which is actually what password used to be. If you dont specify a pin, then it will just use one round of AES

now if the password is left off or blank, eg. "", then it will use your public server acct's password, so if you want it to not encrypt at all you need to set "password":"none"

got half of the telepathic send to work, at least I was able to properly encrypt a sample packet that decrypted and it went into the cloud. too tired for the other half as this is super tricky code

James

P.S. these are untested changes, so let me know if it actually works
Report to moderator   Logged



savefile saves to the cloud
it returns the locations (and order) of the fragments
even if not encrypted if the attacker doesnt know the locations, they cant get the file


of course, will be possible to do some sort of brute force search of all keys used if they are packet monitoring and can crack the base encryption
so adding a password will make it impossible (nearly) to recover all the fragments in the right order and decrypt the AES encryption
if worried about AES being cracked, the pin can apply a cipher sequence (of 18 ciphers)
restorefile does to opposite then
restore needs to know the sequence of fragments
you can send the key info and the other side can restorefile
if savefile is used without any encryption, then you can publish by publishing the locations

L, M, N are optional, so is password and pin, but they are all active


for savefile, L is lfactor for onion depth

M and N is the M of N with N=255 as max and M must be less than equal to N, password encrypts
pin is a short string that controls what algos are combined if null, then just AES


so filename is the only required field it will return the data needed to restorefile


[ANN - MofNfs: store files in the SuperNET cloud using fully encrypted M of N shared secret fragments]

Since there was no large network for me to test with today, I decided to make two new API calls that allow for cloud storage of files. They are massively encrypted and also M of N is supported to deal with hash collisions, sybil attacks, offline nodes, etc. With the proper M and N settings, I think this will be quite a resilient file storage appropriate for the files you just cant lose. The comms with the cloud are via the DHT API from this weekend and the L parameter is for the max number of onion layers to use and all the packets are the same size, so there is no leakage based on packet size.

Now I am not sure what all the other decentralized storage projects are doing and I am sure what I did today is just a small portion of a full system. Still, after I debug it tomorrow, it will be an easy way to safely put things in the cloud.

The savefile will print (and save in usbdir) the required sharenrs and txids JSON fields to use for the restorefile.
The "destfile" field is where the file will be reconstructed.

If the "usbdir" parameter is set, then local backups are made (highly recommended!) and it is used to check the data coming back from the cloud. After you verify that the cloud has a proper copy, then you can partition the various parts from the usbdir directory to various places to have two full backups, one under your local control and one in the cloud.

The max value for N is 254 and M has to be less than or equal to N. The M of N parameters are independent of the "password" field. If you are using M of N, then unless the attacker gets a hold of M pieces, they wont be able to reconstruct the file. Without the txid list, the attacker wont know how to reconstruct the file.


But why take any chances. so I made the password field use an iterative method to create what I think is a pretty practical encryption method, which is based on the name of the file, your pubNXT acct passphrase and the password itself. The length of the password determines the number of ciphers that are applied

        namehash = calc_txid(name,strlen(name));
        len = strlen(password);
        passwordhash = (namehash ^ calc_txid(keygen,strlen(keygen)) ^ calc_txid(password,len));
        for (i=0; i<len; i++)
        {
            expand_nxt64bits(key,passwordhash);
            cipherids = (password % NUM_CIPHERS);  // choose one of 18 ciphers
            privkeys = clonestr(key);
            if ( i < len-1 )
                passwordhash ^= (namehash ^ calc_txid(key,strlen(key)));
        }

Since the keygen is the pubNXT password, which in turn is a dumpprivkey for a BTCD address, this assures high entropy and the filename being encrypted is added to the passwordhash so that different files will have different encryption keys. By using the password to modify the initial password hash and to determine the number of ciphers and their sequence creates a lot of impact from even a short password, like a PIN

When M of N is combined with password, the attacker would need to get a hold of the name of the file, M fragments, the list of txids, the randomly generated sharenrs array and the password you used. Unless your computer is totally compromised and you divulge your short password, this seems like a pretty good level of security.

Now with the DHT there is the chance of collision, sybil attacks, inaccessible nodes, etc. I think using M of N side steps all of these issues. Also, the txid (calculated like NXT does) is based on the contents being stored, so it would take a lot of computation to be able to even get control of the nodes needed to block access to any specific content and near impossible to spoof anything. Maybe someone can come up with a sybil attack that can be done? However, without knowing the hash values of all the fragments, where will the sybils setup their attack? And will they be able to invalidate M copies that they dont know the txid for?

I hope for assistance in testing this API as it is quite important. Also, any method of attack that can be used against this would help me design a better system

James

###

The following are the ciphers:
    "aes","blowfish","xtea","rc5","rc6","saferp","twofish","safer_k64","safer_sk64","safer_k128",
    "safer_sk128","rc2","des3","cast5","noekeon","skipjack","khazad","anubis","rijndael"



./BitcoinDarkd SuperNET '{"requestType":"savefile","filename":"m_unix","L":0,"M":1,"N":1,"usbdir":"/tmp"}'                                {"result":"status.0","sharenrs":"","txids":["1666057801165456042", "232969103956564539"],"filesize":"296","descr":"mofn_savefile M.1 of N.1 sent with Lfactor.0 usbdir.(/tmp) usedpassword.0 dont lose the password, sharenrs or txids!"}

./BitcoinDarkd SuperNET '{"requestType":"restorefile","filename":"m_unix","L":0,"M":1,"N":1,"usbdir":"/tmp","txids":["1666057801165456042", "232969103956564539"],"destfile":"newfile"}'
{"result":"status.0","completed":1.000,"filesize":"592","descr":"mofn_restorefile M.1 of N.1 sent with Lfactor.0 usbname.(/tmp) usedpassword.0 reconstructed"}


[07:33] <jl777> what the M of N does is custom make N fragments
[07:33] <jl777> that magically can reconstruct the original if you have M or more of these fragments
[07:33] <jl777> one M of N for the same file will be different each time you do it, even if M and N are the same
[07:34] <jl777> certainly if anything about M or N changes, it will make totally new data
[07:34] <jl777> the sharenrs are lookup values in a galois field
[07:34] <SHossain> i dont know where it is coming from but i get it after the savefile cmd as in the result "sharenrs":"4d76a9"
[07:34] <jl777> yes that is for N = 3
[07:35] <jl777> it will only work with the exact txids and file and password
[07:35] <jl777> everything has to be matched
[07:35] <jl777> this is why I think MofNfs is immune to sybil attack, node failres, ets
[07:35] <SHossain> yep. without everything exact it doesn't work
[07:36] <jl777> it is not possible to even know what the magic txid's your file is made of
[07:36] <SHossain> any other test you want me to try?
[07:36] <jl777> of course if you are the only one using the cloud, I could figure it out now, but tomorrow I will make it so even if you are the only one using the cloud, it would take me a long time to figure out the order
[07:37] <jl777> try M 100 N 254
[07:37] <jl777> then try a 100kb file
[07:37] <jl777> basically see what works and what doesnt
[07:38] <jl777> also the password picks from the 18 possible ones, so if you just use letters "a", "b", "c", "d" ... it will test each cipher independently
[07:38] <jl777> there are 18 different ciphers
[07:38] <jl777> if you use two letter password it does one cipher then another so 18 *18 possible combinations



If anyone is interested, here is the whole conversation on testing SuperNET clound file save and restore testing.

You will find the problems and how it was solved by jl777.

If anyone is helping us with testing please do a ./m_unix to build the latest and the commands and instructions are in the http://pastebin.com/3Esq0KEB pastebin file.

However, you can try the following command to save a file. The file has to be in the path/folder where you are using it.


./BitcoinDarkd SuperNET '{"requestType":"savefile","filename":"BitcoinDark-qt.pro","L":0,"M":2,"N":3,"usbdir":"/tmp","password":"asdf1234"}'

Restore: you need the txids generated after the command.

./BitcoinDarkd SuperNET '{"requestType":"restorefile","filename":"m_unix","L":0,"M":2,"N":3,"usbdir":"/tmp","txids":["14641644028532519953", "11912799765614641787", "11174634834433195997"],"password":"1234","destfile":"newfile2"}'

You can try chaning the value of M, N and different password / without password. Just to let you know we did the value of N:254. There seem to be a small bug while restoring it. Try to scale up the value from the lower value.



Since without the 50 servers, I cant really debug the DHT and I need that for the next step, I decided to take a break and looked into curve25519


I figured out how to do 3 of 3 multisig!
I think I can also do 2 of 3, but still need to verify the 3 of 3.

I linked BitcoinDarkd to b to save on typing. I have three servers, with the following pubaddrs:
1st: 10694781281555936856
2nd: 8894667849638377372
3rd: 13434315136155299987

./b SuperNET '{"requestType":"cosign","otheracct":"10694781281555936856","text":"this is a test"}'
./b SuperNET '{"requestType":"cosign","otheracct":"8894667849638377372","text":"this is a test"}'
./b SuperNET '{"requestType":"cosign","otheracct":"13434315136155299987","text":"this is a test"}'
it returns:

1st server:
{"requestType":"cosigned","seed":"2e99758548972a8e8822ad47fa1017ff72f06f3ff6a016851f45c398732bc50c","result":"f193137b79a4993b40b0be6c7154cf2d559e3d6f974941cca657a45733435205","privacct":"10694781281555936856","pubacct":"10694781281555936856"}
{"requestType":"cosigned","seed":"2e99758548972a8e8822ad47fa1017ff72f06f3ff6a016851f45c398732bc50c","result":"b39af77f1b18389e9acb782ad41a365cf5ef48d63b7394f714742f7471b4d209","privacct":"10694781281555936856","pubacct":"8894667849638377372"}
{"requestType":"cosigned","seed":"2e99758548972a8e8822ad47fa1017ff72f06f3ff6a016851f45c398732bc50c","result":"681d2ff77944cb36db523e775f5fe7fb5519cc106ca3fafd6bb8a31d17d10d6f","privacct":"10694781281555936856","pubacct":"13434315136155299987"}

2nd server:
{"requestType":"cosigned","seed":"2e99758548972a8e8822ad47fa1017ff72f06f3ff6a016851f45c398732bc50c","result":"b39af77f1b18389e9acb782ad41a365cf5ef48d63b7394f714742f7471b4d209","privacct":"8894667849638377372","pubacct":"10694781281555936856"}
{"requestType":"cosigned","seed":"2e99758548972a8e8822ad47fa1017ff72f06f3ff6a016851f45c398732bc50c","result":"4a3bc59ad2f2ea5191447ce2ad2f6a2d877daebbc096c826eb2b40bfd8293502","privacct":"8894667849638377372","pubacct":"8894667849638377372"}
{"requestType":"cosigned","seed":"2e99758548972a8e8822ad47fa1017ff72f06f3ff6a016851f45c398732bc50c","result":"196d7054e987a0a8061d4b4d86db5e3dfe502066208bda98a3b1c834e4fc8071","privacct":"8894667849638377372","pubacct":"13434315136155299987"}

3rd server:
{"requestType":"cosigned","seed":"2e99758548972a8e8822ad47fa1017ff72f06f3ff6a016851f45c398732bc50c","result":"681d2ff77944cb36db523e775f5fe7fb5519cc106ca3fafd6bb8a31d17d10d6f","privacct":"13434315136155299987","pubacct":"10694781281555936856"}
{"requestType":"cosigned","seed":"2e99758548972a8e8822ad47fa1017ff72f06f3ff6a016851f45c398732bc50c","result":"196d7054e987a0a8061d4b4d86db5e3dfe502066208bda98a3b1c834e4fc8071","privacct":"13434315136155299987","pubacct":"8894667849638377372"}
{"requestType":"cosigned","seed":"2e99758548972a8e8822ad47fa1017ff72f06f3ff6a016851f45c398732bc50c","result":"d6bdcaf3d5890eb3839860d6eec1f8f151d6af7c94d7feb6691e9b4ebc26a20a","privacct":"13434315136155299987","pubacct":"13434315136155299987"}

####
note the matched pairs of results. Now I will submit one of them to the server that isnt listed, the following three, to each server:


./b SuperNET '{"requestType":"cosigned","seed":"2e99758548972a8e8822ad47fa1017ff72f06f3ff6a016851f45c398732bc50c","result":"196d7054e987a0a8061d4b4d86db5e3dfe502066208bda98a3b1c834e4fc8071","privacct":"8894667849638377372","pubacct":"13434315136155299987"}'

./b SuperNET '{"requestType":"cosigned","seed":"2e99758548972a8e8822ad47fa1017ff72f06f3ff6a016851f45c398732bc50c","result":"681d2ff77944cb36db523e775f5fe7fb5519cc106ca3fafd6bb8a31d17d10d6f","privacct":"13434315136155299987","pubacct":"10694781281555936856"}'

./b SuperNET '{"requestType":"cosigned","seed":"2e99758548972a8e8822ad47fa1017ff72f06f3ff6a016851f45c398732bc50c","result":"b39af77f1b18389e9acb782ad41a365cf5ef48d63b7394f714742f7471b4d209","privacct":"10694781281555936856","pubacct":"8894667849638377372"}'

and all three servers produced the same results! Note that each server had different inputs to create the same result.

{"seed":"2e99758548972a8e8822ad47fa1017ff72f06f3ff6a016851f45c398732bc50c","result":"5f176db34fce1b7812e97c13771d9c7767e839304d17c9611794343db76bc556","acct","10694781281555936856","privacct":"8894667849638377372","pubacct":"13434315136155299987","input":"196d7054e987a0a8061d4b4d86db5e3dfe502066208bda98a3b1c834e4fc8071"}

{"seed":"2e99758548972a8e8822ad47fa1017ff72f06f3ff6a016851f45c398732bc50c","result":"5f176db34fce1b7812e97c13771d9c7767e839304d17c9611794343db76bc556","acct","8894667849638377372","privacct":"13434315136155299987","pubacct":"10694781281555936856","input":"681d2ff77944cb36db523e775f5fe7fb5519cc106ca3fafd6bb8a31d17d10d6f"}

{"seed":"2e99758548972a8e8822ad47fa1017ff72f06f3ff6a016851f45c398732bc50c","result":"5f176db34fce1b7812e97c13771d9c7767e839304d17c9611794343db76bc556","acct","13434315136155299987","privacct":"10694781281555936856","pubacct":"8894667849638377372","input":"b39af77f1b18389e9acb782ad41a365cf5ef48d63b7394f714742f7471b4d209"}

now these are low level primitives and doesnt directly get us multisig tx, but it does allow 3 nodes to cooperate and verify that the other two are also signing the original text. by publishing the final result, it will prove to others that all three nodes reached agreement.

James





##################################################################################################


                                                savefile



18

    static char *savefile[] = { (char *)savefile_func, "savefile", "V", "filename", "L", "M", "N", "backup", "password", "pin", 0 };





------------------------------------------------------------------------------------------


                                                restorefile


19

    static char *restorefile[] = { (char *)restorefile_func, "restorefile", "V", "filename", "L", "M", "N", "backup", "password", "destfile", "sharenrs", "txids", "pin", 0 };


------------------------------------------------------------------------------------------


                                                sendfile


20

    static char *sendfile[] = { (char *)sendfile_func, "sendfile", "V", "filename", "dest", "L", 0 };

sendfile is stubbed now
l8orre 9:38 PM ok
------------------------------------------------------------------------------------------




priceDB is just creating DB of prices

jl777 [8:21 AM]
getDB is getting DB data from the public.db and private.db

jl777 [8:21 AM]8:21
so they share DB, but accessing different ones

jl777 [8:22 AM]
meaning they are ways to access DB, but different DB's





findnode -> havenode

jl777 [8:15 AM]8:15
findvalue -> havenodeB




##################################################################################################


    // Telepathy 9


                 'getpeers',\
                   'addcontact',\
                   'removecontact',\
                   'dispcontact',\
                   'telepathy',\
                   'getdb',\
                   'sendmessage',\
                   'sendbinary',\
                   'checkmsg',\




I think I just finished coding low level Telepathy transport layer.

Since I am using UDP and many things can go wrong due to no fault of anybody

(nodes dropping out, onion hopping to a node that is gone, etc)

it is quite likely that a packet sent to a destination might not get there, but ones after it could.

So I need to implement some sort of TCP like retry layer on top of UDP.


Due to the way the packets are sent, it is quite tricky to get it to work, but finally I managed to achieve this as follows:


When a contact is added (happens every init),

the published public key from the NXT blockchain is used to create a shared secret between two accounts.

These accounts are totally abstract and are not tied to any IP address at all and it also happens to be the key I use for the DHT traversal.


Now I could send an encrypted message between nodes to exchange the dead drop addresses,

but I think using a non-predictable (to anybody else) but deterministically calculated address

that only the two nodes can calculate is safe enough.

Even if this is somehow compromised, it is only for a bootstrap to get a decent deaddrop address to use.

Once the comms are established,
then the deaddrop address to use can be updated at anytime and there is a way to get it to the other side.



Each message between the two nodes will get a sequence number and each also gets its own onetime AESpassword that is calculated as follows:

    sprintf(buf,"%llu.%d",(long long)nxt64bits,sequenceid);
    calc_sha256cat(AESpassword->bytes,(uint8_t *)buf,(int32_t)strlen(buf),shared,(int32_t)sizeof(bits256));
    init_hexbytes(AESpasswordstr,AESpassword->bytes,sizeof(bits256));
    return(conv_NXTpassword(secret.bytes,pubkey.bytes,AESpasswordstr));

sha256cat is H(m || sharedsecret) where m is the acct number of the sender with the sequenceid



So, this means the password can only be created by the two nodes who know the shared secret.

I ran into a problem that the piggyback attachment was a totally encrypted blob with no header info at all.

I could have put a onetime pubkey, but since I am using the sharedsecret for AES cipher I didnt want to venture into unsure crypto things.

 So to keep things totally encapsulated in the onetime AES cipher,

 I needed some other way to let the receiving end know who was sending it.

Remember that in Telepathy, there is no destination address that is actually real.

It is an equidistant (in DHT space) address to N public IP privacyServers.

N will hopefully be 20+ and one of these IP addresses is the actual destinations, but it can never divulge which one,

so the bootstrap was tricky enough, but I solved that by putting it into the cloud at a location that is the curve25519 pubkey of the AES cipher.

Another oneway function and this also combined with the need to protect the sender. After all if the sender is making DHT calls with his address in the JSON, even though it is protected by encryption, the DHT node that handles the hop has to decrypt it and if the attacker is controlling the node, then this leaks the fact that the sender sent to a specific deaddrop address. Far more leakage than I am comfortable with.

I just used the same address for all such Telepathy payload packets.

But that is quite redundant and wastes precious space.

Also, I use the sender's address as an authentication method and using a static address loses that.

 Luckily, this protection of the sender can be achieved while also providing authentication by using the "location" of the packet's sequenceid!

Now without modifying the encrpted attachment and without leaking any info,

the receiver can use the "sender" field to figure out if a Telepathy packet is meant for him and most importantly

what AES password to use.

No need to brute force try all the possible contacts sequence id passwords,

as we know what the "location"/"sender" will be for all the expected sequence ids from all the contacts.

Still have a few small issues like how to send back retry requests safely,
but I am quite pleased at how all the pieces came together.

I think I will be able to debug this tomorrow and at that point I will be able to send sequences of packets
between any two contacts and have it reliably get there, well, assuming I can get all the bugs fixed.

Realistically in complex network topologies there will be bugs, but so far so good.

As you can see, with a reliable low level packet transport,

all sorts of things become very simple to do. Like file transfer (say telepod files!) or even low bandwidth audio.

That would be cool, to be able to stream voice over Telepathy connection


#### The following are the externally visible actions:
1. sending out a 1400 byte packet to a random node for the onion layered packet that contains the DHT storedata of the encrypted deaddrop address.

1b. some random hops later a random node will decrypt the DHT storedata and start a DHT sequence, which gets it to the secret location in the cloud.

2. sending out a 1400 byte DHT findvalue request for the secret address directly using the DHT sequence, so the DHT nodes will know that you requested something from the cloud. however, this will just look like all the other findvalue requests as it is just to a random address.

2b. the DHT nodes that are involved will find out the size of the encrypted data that you get. For now I am not making this all the same size, I probably should, but I need to first determine what the max size should be. At some point you get a 1400 byte packet back with the encrypted deaddrop address

3. you send 1400 by onion routed packets with the sender actually being the "location", so as long as the randomly selected nodes along the onion route are not colluding and sharing info about the source and destination, nobody will even know that you sent this packet out. The odds of the attacker control all randomly selected onion nodes is pretty small and they wont know for sure that you were not just forwarding, but in this worst case they will know that you sent some packets to a dead address.

4. your node participates in DHT routing following the same rules as all the other nodes. Even when you get a telepathy packet, there is no visible difference as any actions are deferred a bit and the output timing and even order of packets goint out of your node is randomized.

James
#
# telepathy encapsulates a JSON attachment
 # 	it is similar to protocol stack
  at the API level, you just need to issue and interpret the JSON fields you create
 # and all of the SuperNET core API is fully accessible via http, https, curl, wget
				# so SuperNET apps can be written in any language
				# accessing standa

To prevent the spoofing, I added a contacts list:

./BitcoinDarkd SuperNET '{"requestType":"addcontact","handle":"jl777","acct":"NXT-P3K3-M9XB-5MDG-DVNT8"}'

./BitcoinDarkd SuperNET '{"requestType":"addcontact","handle":"localH","acct":"2131686659786462901"}'

./BitcoinDarkd SuperNET '{"requestType":"removecontact","handle":"jl777"}'

./BitcoinDarkd SuperNET '{"requestType":"dispcontact","handle":"jl777"}'

./BitcoinDarkd SuperNET '{"requestType":"dispcontact","handle":"myhandle"}'

./BitcoinDarkd SuperNET '{"requestType":"dispcontact","handle":"jl777"}'

./BitcoinDarkd SuperNET '{"requestType":"addcontact","handle":"jl777","acct":"NXT-P3K3-M9XB-5MDG-DVNT8"}'
{"result":"(jl777) acct.(NXT-P3K3-M9XB-5MDG-DVNT8) (12927190866050319905) has pubkey.(45ec94823354d56c549b475c5e3ffd49c9c2cf4a366deed809bfba38dd756318)"}



./BitcoinDarkd SuperNET '{"requestType":"addcontact","handle":"jl777","acct":"NXT-P3K3-M9XB-5MDG-DVNT8"}'
{"result":"(jl777) acct.(NXT-P3K3-M9XB-5MDG-DVNT8) (12927190866050319905) unchanged"}


/BitcoinDarkd SuperNET '{"requestType":"addcontact","handle":"localH","acct":"2131686659786462901"}'
{"error":"(mypublic) already has 2131686659786462901"}


./BitcoinDarkd SuperNET '{"requestType":"dispcontact","handle":"jl777"}'




These are basically a way of mapping long acct numbers to easy to remember handles for use in other API calls.

Nothing fancy. Since they are not stored on HDD you need to put a "contacts":[{"jl777":""}....] field in SuperNET.conf

or have the GUI do it on startup.

calling addcontact again will just update the acct.

These accts have to be funded with at least 1 NXT I will add a display handle API

with a special handle called "me" that shows your private acct and public key.




There is a special handle "myhandle", which is set to your pubaddr -> NXT numerical address -> reed solomon RS address.
This is so you can let others know what address to set your handle to.




Also if you dispcontact "*" it will return all contacts

These API should allow a contacts GUI to be built

James

P.S. As the observant have observed, using handles -> accts allows us to generated a shared secret based on the public key of the acct and this lets us use the cloud using a location that nobody else will be able to find, at least not without a brute force search and we also skip a step as the public key can be used to exchange Telepathy addresses and this also gets us non-realtime transactions! Not bad for such a simple API
I "wasted" a bit of time recently while I waited for more servers to come online for expanded DHT testing and bruteforced some interesting curve25519 properties. https://bitcointalk.org/index.php?topic=820614.msg9170663#msg9170663
Also got a good education from andytoshi who really knows all this crypto math.

Anyway, as it often happens I get lucky and as I was battling the issue of how to do the key exchange and deaddrop address exchanges, the recent curve25519 lessons solved it nicely with the basic shared secret that automatically comes from curve25519.

On one node:
./b SuperNET '{"requestType":"addcontact","handle":"jl777","acct":"NXT-P3K3-M9XB-5MDG-DVNT8"}'
shared.(ad021e641e6c65e357921fe8348f4d0718f7f81e89a058071d0e73fb3873)
ADD.(jl777 -> NXT-P3K3-M9XB-5MDG-DVNT8)
{"result":"(jl777) acct.(NXT-P3K3-M9XB-5MDG-DVNT8) (12927190866050319905) has pubkey.(45ec94823354d56c549b475c5e3ffd49c9c2cf4a366deed809bfba38dd756318)"}

On another node:
./b SuperNET '{"requestType":"addcontact","handle":"s0","acct":"NXT-Z6JT-5TB6-EXSL-48JPG"}'
shared.(ad021e641e6c65e357921fe8348f4d0718f7f81e89a058071d0e73fb3873)
ADD.(s0 -> NXT-Z6JT-5TB6-EXSL-48JPG)
input.({"requestType":"addcontact","handle":"s0","acct":"NXT-Z6JT-5TB6-EXSL-48JPG"}') -> ({"result":"(s0) acct.(NXT-Z6JT-5TB6-EXSL-48JPG) (2834459742776037913) has pubkey.(7b689a7b0035bcaa944ac5d38415ebbe81a9fa2f3f3cb3898872a5075bed1a15)"})

I decided to just use the same pubkeys that is in the NXT blockchain. Since I can directly generate the pubkey and privkey and already auto-generate accounts via linked addresses, just by using a single coin address, you can get a universal pubkey that SuperNET can use to encrypt things to your node.

The blue shared secret is something that only the two nodes are able to generate and so now not only can I encrypt the comms directly between the two nodes, I can find a key to store these comms in the cloud without worry about it being spoofed, plus even if the address is figured out somehow, it has to be encrypted and only from the specific other party.

Another key advantage to using the permanent pubkeys is that now transactions can happen in non-realtime. This was one of the few weaknesses of Teleport, but now things would just progress as far as they can as each party is online. Basically, the cloud becomes a virtual fully encrypted bi-directional peer to peer communications channel for arbitrary data.

All built on top of onion routed Telepathy DHT comms to non-existent deaddrop addresses with an encrypted attachment. Also at the DHT level, all these Telepathy requests will look like they are coming from the same account. There is no need to authenticate the outer part of the packet as it will be fully authenticated inside the attachment. I think the fact that it decrypts using the shared secret is enough authentication, hopefully someone will correct me if I am wrong on this assumption.

I already have all packets the same size (1400 bytes) and they are randomly delayed/shuffled to prevent timing analysis and with nobody knowing the actual destination I believe we have unlinkable IP addresses while using IP packets.

The cloud location where the deaddrop addresses are exchanged will be calculated based on:
sha256(sha256(acct || sharedsecret))
The inside hash value will be the encryption key for the contents using AES. Maybe I will reverse that, yes that seems a bit better to make the encryption key one step beyond the location.

So a lot of progress!

James

changed all the contact API so that the "handle" field can accept handles, numerical NXT address or NXT-... RS addresses

I also changed the "handle" name to "contact" for dispcontact and removecontact:

    static char *addcontact[] = { (char *)addcontact_func, "addcontact", "V",  "handle", "acct", 0 };
    static char *removecontact[] = { (char *)removecontact_func, "removecontact", "V",  "contact", 0 };
    static char *dispcontact[] = { (char *)dispcontact_func, "dispcontact", "V",  "contact", 0 };

the "acct" for addcontact can be either numerical or RS

James
Report to moderator   Logged




##################################################################################################


                                                    getpeers



21

    static char *getpeers[] = { (char *)getpeers_func, "getpeers", "V",  "scan", 0 };



curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=getpeers&scan=1'

./BitcoinDarkd SuperNET '{"requestType":"getpeers"}'
curl -k --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "SuperNET", "params": ["{\"requestType\":\"getpeers\"}"]  }' -H 'content-type: text/plain;' https://127.0.0.1:7777/
curl --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "SuperNET", "params": ["{\"requestType\":\"getpeers\"}"]  }' -H 'content-type: text/plain;' http://127.0.0.1:7776/



------------------------------------------------------------------------------------------



                                                    addcontact



22 call_NOT_TESTED

    static char *addcontact[] = { (char *)addcontact_func, "addcontact", "V",  "handle", "acct", 0 };

# ./BitcoinDarkd  SuperNET '{"requestType":"addcontact","handle":"jl777","acct":"NXT-P3K3-M9XB-5MDG-DVNT8"}'
# ./BitcoinDarkd  SuperNET '{"requestType":"addcontact","handle":"s2","acct":"482478496576188177"}'

# ./BitcoinDarkd  SuperNET '{"requestType":"addcontact","handle":"s2","acct":"482478496576188177"}'




------------------------------------------------------------------------------------------



                                                    removecontact


23 call_NOT_TESTED

    static char *removecontact[] = { (char *)removecontact_func, "removecontact", "V",  "contact", 0 };
# ./BitcoinDarkd  SuperNET '{"requestType":"removecontact","handle":"jl777"}'


------------------------------------------------------------------------------------------



                                                dispcontact

24 call_NOT_TESTED

    static char *dispcontact[] = { (char *)dispcontact_func, "dispcontact", "V",  "contact", 0 };

# ./BitcoinDarkd  SuperNET '{"requestType":"dispcontact","contact":"jl777"}'
# ./BitcoinDarkd  SuperNET '{"requestType":"dispcontact","contact":"myhandle"}'
# ./BitcoinDarkd  SuperNET '{"requestType":"dispcontact","contact":"*"}'

------------------------------------------------------------------------------------------





                                                telepathy




25 call_NOT_TESTED

    static char *telepathy[] = { (char *)telepathy_func, "telepathy", "V",  "contact", "id", "type", "attach", 0 };
# ./BitcoinDarkd  SuperNET '{"requestType":"telepathy","contact":"s0","msg":"deadbeef"}'
# ./BitcoinDarkd  SuperNET '{"requestType":"telepathy","contact":"s2","msg":"beefdead"}'


# ./BitcoinDarkd SuperNET '{"requestType":"telepathy","contact":"s0","type":"test","attach":{"msg":"deadbeef"}}'
#
#
# ./BitcoinDarkd  SuperNET '{"requestType":"telepathy","contact":"s2","msg":"beefdead"}'
#
# ./BitcoinDarkd  SuperNET '{"requestType":"telepathy","contact":"s0","msg":"deadbeef"}'

------------------------------------------------------------------------------------------


                                            getdb






./BitcoinDarkd SuperNET '{"requestType":"getdb","key":"1031470952125437106"}'


Returns:


GETDB.({"requestType":"dbret","NXT":"6249611027680999354","key":"1031470952125437106","data":"c0ffee"})




cassius [12:32 PM]
So what am I looking at here? Is this the contact list held by the node that's storing  that value?

cassius [12:32 PM]



26 call_NOT_TESTED

    static char *getdb[] = { (char *)getdb_func, "getdb", "V",  "contact", "id", "key", "dir", "destip", 0 };

# ./BitcoinDarkd  SuperNET '{"requestType":"getdb","contact":"s0","id":0,"dir":"send"}'

#

./BitcoinDarkd SuperNET '{"requestType":"getdb","key":"8894667849638377372"}'

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=getdb&key=8894667849638377372'
{'error': 'cant find key', 'requestType': 'dbret', 'key': '8894667849638377372'}


curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=getdb&key=8894667849638377372'







------------------------------------------------------------------------------------------

                                        sendmsg







curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=sendmessage&dest=8894667849638377372&msg="THREE..TWO..ONE..LIFTOFF!!"'


./BitcoinDarkd SuperNET '{"requestType":"sendmessage","6216883599460291148":" ,"msg":"THREE..TWO..ONE..LIFTOFF!!","L":3}'

    static char *sendmsg[] = { (char *)sendmsg_func, "sendmessage", "V", "dest", "msg", "L", 0 };

 ./BitcoinDarkd  SuperNET '{"requestType":"sendmessage","dest":"2131686659786462901","msg":"hello---------------------------******************************"}'
{"status":"2131686659786462901 sends encrypted sendmessage to 3571143576961987768 pending via.(3571143576961987768), len.1396"}





------------------------------------------------------------------------------------------


                                                sendbinary



28 call_NOT_TESTED

    static char *sendbinary[] = { (char *)sendbinary_func, "sendbinary", "V", "dest", "data", "L", 0 };


------------------------------------------------------------------------------------------


                                                checkmsg


29 call_NOT_TESTED

    static char *checkmsg[] = { (char *)checkmsg_func, "checkmessages", "V", "sender", 0 };


------------------------------------------------------------------------------------------






##################################################################################################

##################################################################################################



    // Teleport 3
 Teleport 3',\
                   'maketelepods',\
                   'telepodacct',\
                   'teleport',\


                                                maketelepods


30 call_NOT_TESTED
    static char *maketelepods[] = { (char *)maketelepods_func, "maketelepods", "V", "amount", "coin", 0 };

# ./BitcoinDarkd SuperNET '{"requestType":"maketelepods","coin":"BTCD","amount":".0001"}'
#


things are running pretty stable for me.

also the first telepod created via SuperNET API via BitcoinDarkd

./b SuperNET '{"requestType":"maketelepods","coin":"BTCD","amount":".005"}'
got JSON.({"requestType":"maketelepods","coin":"BTCD","amount":".005"})


------------------------------------------------------------------------------------------


                                                telepodacct



31 call_NOT_TESTED

    static char *telepodacct[] = { (char *)telepodacct_func, "telepodacct", "V", "amount", "contact", "coin", "comment", "cmd", "withdraw", 0 };
# ./BitcoinDarkd SuperNET '{"requestType":"telepodacct","coin":"BTCD"}'
# ./BitcoinDarkd SuperNET '{"requestType":"telepodacct","coin":"BTC"}'

# ./BitcoinDarkd SuperNET '{"requestType":"telepodacct"}'

# ./BitcoinDarkd SuperNET '{"requestType":"telepodacct","coin":"LTC"}'
------------------------------------------------------------------------------------------


                                                teleport


32 call_NOT_TESTED

    static char *teleport[] = { (char *)teleport_func, "teleport", "V", "amount", "contact", "coin", "minage", "withdraw", 0 };


# ./BitcoinDarkd SuperNET '{"requestType":"teleport","coin":"BTCD","amount":".0001","contact":"s0"}'
------------------------------------------------------------------------------------------






##################################################################################################

                    'InstantDEX 6',\


                   'orderbook',\
                   'placebid',\
                   'placeask',\
                   'makeoffer',\
                   'respondtx',\
                   'processutx',\



do_localstore(12008998766472701676) <- (7b2274696d65223a313431363133373530302c2274797065223a322c224e5854223a2232313331363836363539373836343632393031222c2262617365223a223131303630383631383138313430343930343233222c2262617365616d6f756e74223a22313030343939393939222c2272656c223a2234353531303538393133323532313035333037222c2272656c616d6f756e74223a22343031393939222c227265717565737454797065223a22626964227d00)
updated.public.db (12008998766472701676) hp.0x7fb8666f6750 data.data 0x7fb8666f6750


curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=placebid&baseid=11060861818140490423&relid=4551058913252105307&volume=1.005&price=0.004'

{'result': 'success', 'txid': '5381385831070545076'}

curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=placeask&baseid=4551058913252105307&relid=11060861818140490423volume=1.005&price=0.014'


# #You can dynamically create any orderbook between any two assets and the pricing is using arbitrary precision volume and price.
this is converted internally to 64bit ints.
#


./BitcoinDarkd SuperNET '{"requestType":"placebid","baseid":"11060861818140490423","relid":"4551058913252105307","volume":"1.01","price":"0.006"}'
{"result":"success","txid":"11196094531373701159"}


curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=placeask&baseid=11060861818140490423&relid=4551058913252105307&volume=1.005&price=0.014'
{'result': 'success', 'txid': '15349840938110561982'}

##################################################################################################



                                                    orderbook



33 call_     _TESTED
    static char *orderbook[] = { (char *)orderbook_func, "orderbook", "V", "baseid", "relid", "allfields", "oldest", 0 };


curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=orderbook&baseid=4551058913252105307&relid=11060861818140490423'
{'baseid': '4551058913252105307', 'key': '12008998766472701676', 'bids': [], 'relid': '11060861818140490423', 'asks': [['250.00061940453', '0.00401999']]}


./BitcoinDarkd SuperNET '{"requestType":"orderbook","baseid":"11060861818140490423","relid":"4551058913252105307"}'
{"error":"no such orderbook.(11060861818140490423 ^ 4551058913252105307)"}



./BitcoinDarkd SuperNET '{"requestType":"orderbook","baseid":"4551058913252105307","relid":"11060861818140490423"}'
tosch 6:53 AM what does polarity mean?




curl   -H 'content-type: text/plain;' 'http://127.0.0.1:7800/nxt?requestType=orderbook&baseid=4551058913252105307&relid=11060861818140490423'


./BitcoinDarkd SuperNET '{"requestType":"orderbook","baseid":"4551058913252105307","relid":"11060861818140490423"}'
{
        "key":  "12008998766472701676",
        "baseid":       "4551058913252105307",
        "relid":        "11060861818140490423",
        "bids": [],
        "asks": [["250.00061940453", "0.00401999"]]
}
azure@boxfish:~/workbench/nxtDev/TEAM/btcd/libjl777$




jl777 6:54 AM the default polarity is assetA < assetB
negative polarity is it flipped
but really you just specify the baseid -> relid
that flips the orientation



# ./BitcoinDarkd  SuperNET '{"requestType":"orderbook","obookid":"12008998766472701676","polarity":1}'
?????????????
./BitcoinDarkd  SuperNET '{"requestType":"orderbook","obookid":"12008998766472701676","polarity":1}'
{"error":"no such orderbook.(0 ^ 0)"}





------------------------------------------------------------------------------------------

                                                placebid


34 call_NOT_TESTED

    static char *placebid[] = { (char *)placebid_func, "placebid", "V", "baseid", "relid", "volume", "price", 0 };


    ./BitcoinDarkd SuperNET '{"requestType":"placebid","baseid":"11060861818140490423","relid":"4551058913252105307","volume":"1.01","price":"0.006"}'
{"result":"success","txid":"10072729249155336376"}

# ./BitcoinDarkd  SuperNET '{"requestType":"placebid","baseid":"11060861818140490423","relid":"4551058913252105307","volume":"1.01","price":"0.006"}'
./BitcoinDarkd  SuperNET '{"requestType":"placebid","assetA":"11060861818140490423","assetB":"4551058913252105307"}'
{"error submitting":"placebid error 0/0 volume 0.000000 price 0.000000"}


# ./BitcoinDarkd  SuperNET '{"requestType":"placebid","assetA":"11060861818140490423","assetB":"4551058913252105307"}'
# ./BitcoinDarkd  SuperNET '{"requestType":"placebid","obookid":"12008998766472701676","volume":"1.01","price":"0.006"}'




------------------------------------------------------------------------------------------


                                                            placeask



35 call_NOT_TESTED



    static char *placeask[] = { (char *)placeask_func, "placeask", "V", "baseid", "relid", "volume", "price",0 };


./BitcoinDarkd SuperNET '{"requestType":"placeask","baseid":"11060861818140490423","relid":"4551058913252105307","volume":"1.1","price":"0.005"}'

the above are the user invoked InstantDEX API, orderbooks are created dynamically based on placebid/placeask
by changing the baseid <-> relid, you can flip the orderbook around
./BitcoinDarkd SuperNET '{"requestType":"orderbook","baseid":"11060861818140490423","relid":"4551058913252105307","allfields":1}'
adding allfields will show more info on each orderbook entry, including the NXT addresses and this is needed to know who to send the makeoffer to
# ./BitcoinDarkd  SuperNET '{"requestType":"placeask","baseid":"11060861818140490423","relid":"4551058913252105307","volume":"1.0","price":"0.0065"}'
# ./BitcoinDarkd  SuperNET '{"requestType":"placeask","obookid":"12008998766472701676","volume":"1.1","price":"0.005"}'
------------------------------------------------------------------------------------------



                                                            makeoffer



36 call_NOT_TESTED

    static char *makeoffer[] = { (char *)makeoffer_func, "makeoffer", "V", "baseid", "relid", "baseamount", "relamount", "other", "type", 0 };


------------------------------------------------------------------------------------------


                                                respondtx


37 call_NOT_TESTED

    static char *respondtx[] = { (char *)respondtx_func, "respondtx", "V", "signedtx", 0 };


------------------------------------------------------------------------------------------


                                                processutx



38 call_NOT_TESTED

    static char *processutx[] = { (char *)processutx_func, "processutx", "V", "utx", "sig", "full", 0 };


------------------------------------------------------------------------------------------


##################################################################################################






   Tradebot 3',\
                   'pricedb',\
                   'getquotes',\
                   'tradebot',\



the oldest is unix GMT timestamp
would be nice to be able to have a "allpricedb" command that adds all possible things to be gathered
this would require knowing the total list of what is traded on each exchange
for cryptsy, I have a horrible hard coded list that maps symbol to their id#


##################################################################################################


                                                pricedb


39 call_NOT_TESTED
    static char *pricedb[] = { (char *)pricedb_func, "pricedb", "V", "exchange", "base", "rel", "stop", 0 };



curl -k --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "SuperNET", "params": ["{\"requestType\":\"pricedb\",\"exchange\":\"bittrex\",\"base\":\"BTCD\",\"rel\":\"BTC\"}"]  }' -H 'content-type: text/plain;' https://127.0.0.1:7777/

curl -k --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "SuperNET", "params": ["{\"requestType\":\"pricedb\",\"exchange\":\"bittrex\",\"base\":\"BTCD\",\"rel\":\"BTC\",\"stop\":1}"]  }' -H 'content-type: text/plain;' https://127.0.0.1:7777/


curl -k --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "SuperNET", "params": ["{\"requestType\":\"pricedb\",\"exchange\":\"nxtae\",\"base\":\"BTC\",\"rel\":\"NXT\"}"]  }' -H 'content-type: text/plain;' https://127.0.0.1:7777/


./BitcoinDarkd SuperNET '{"requestType":"pricedb","exchange":"bter","base":"BTCD","rel":"BTC"}'

turned out to be a lot of little details and I still have some DB deadlock cases to fix, but if you have only one active pair it seems to be working. not sure if all the data is getting into the DB, but the dbput is coming back without error.

so what is this pricedb API? it creates an entry in a small db file which is just a list of exchanges and trading pair that is active. The cool part is that for all active pairs, it automatically polls the prices from the exchange and creates a database file locally. This way, over time you will get price data to analyze, but more near term a way to see the current market price.

The exchanges that are supported are: "NXT", "bter", "bittrex", "cryptsy", "poloniex", "mintpal"
for NXT, only the currencies with MGW assets are supported, for the others, any trading pair the exchange supports is supported. [I think cryptsy only works with a hardcoded list for now]

James
------------------------------------------------------------------------------------------



                                                        getquotes




40 call_NOT_TESTED

    static char *getquotes[] = { (char *)getquotes_func, "getquotes", "V", "exchange", "base", "rel", "oldest", 0 };



The first one starts the data gathering, the second one stops it


curl -k --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "SuperNET", "params": ["{\"requestType\":\"getquotes\",\"oldest\":0,\"exchange\":\"bter\",\"base\":\"NXT\",\"rel\":\"BTC\"}"]  }' -H 'content-type: text/plain;' https://127.0.0.1:7777/


curl -k --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "SuperNET", "params": ["{\"requestType\":\"getquotes\",\"exchange\":\"bter\",\"base\":\"NXT\",\"rel\":\"BTC\"}"]  }' -H 'content-type: text/plain;' https://127.0.0.1:7777/


------------------------------------------------------------------------------------------





                                                            tradebot



41 call_NOT_TESTED

    static char *tradebot[] = { (char *)tradebot_func, "tradebot", "V", "code", 0 };



------------------------------------------------------------------------------------------







##################################################################################################
calls only as inventory


// glue 7
// passthru 2
// MGW 7   ( // multisig 2 )
// Kademlia DHT  8
// MofNfs 3
// Telepathy 9
// Teleport 3
// InstantDEX 6
// Tradebot 3
// privatebet 1



http://jnxt.org/init/?requestType=status&pubkey=734b83479469164e6059b98c1679043a278c1ba8d18d1d42d348d255baf2f656&NXT=NXT-MEXA-RJSP-NKDU-FWWHM&coin=BTCD
http://jnxt.org/init/?requestType=newbie&pubkey=734b83479469164e6059b98c1679043a278c1ba8d18d1d42d348d255baf2f656&NXT=NXT-MEXA-RJSP-NKDU-FWWHM&email=&lt;emailaddr&gt;&convertNXT=1000

requestType=status
&pubkey=734b83479469164e6059b98c1679043a278c1ba8d18d1d42d348d255baf2f656
&NXT=NXT-MEXA-RJSP-NKDU-FWWHM
&coin=BTCD



requestType=newbie
&pubkey=734b83479469164e6059b98c1679043a278c1ba8d18d1d42d348d255baf2f656
&NXT=NXT-MEXA-RJSP-NKDU-FWWHM
&email=&lt;emailaddr
&gt;
&convertNXT=1000




api.h: list of all calls. date: 120714


char *SuperNET_json_commands(struct NXThandler_info *mp,char *previpaddr,cJSON *origargjson,char *sender,int32_t valid,char *origargstr)
{
    // local glue
    static char *gotjson[] = { (char *)gotjson_func, "BTCDjson", "V", "json", 0 };
    static char *gotpacket[] = { (char *)gotpacket_func, "gotpacket", "V", "msg", "dur", "ip_port", 0 };
    static char *gotnewpeer[] = { (char *)gotnewpeer_func, "gotnewpeer", "V", "ip_port", 0 };
    static char *BTCDpoll[] = { (char *)BTCDpoll_func, "BTCDpoll", "V", 0 };
    static char *GUIpoll[] = { (char *)GUIpoll_func, "GUIpoll", "V", 0 };
    static char *stop[] = { (char *)stop_func, "stop", "V", 0 };
    static char *settings[] = { (char *)settings_func, "settings", "V", "field", "value", "reinit", 0 };

    // passthru
    static char *passthru[] = { (char *)passthru_func, "passthru", "V", "coin", "method", "params", "tag", 0 };
    static char *remote[] = { (char *)remote_func, "remote", "V",  "coin", "method", "result", "tag", 0 };

    // MGW
    static char *genmultisig[] = { (char *)genmultisig_func, "genmultisig", "", "userpubkey", "coin", "refcontact", "M", "N", "contacts", "destip", "destport", "email", "buyNXT", 0 };
    static char *getmsigpubkey[] = { (char *)getmsigpubkey_func, "getmsigpubkey", "V", "coin", "refNXTaddr", "myaddr", "mypubkey", 0 };
    static char *MGWaddr[] = { (char *)MGWaddr_func, "MGWaddr", "V", 0 };
    static char *MGWresponse[] = { (char *)MGWresponse_func, "MGWresponse", "V", 0 };
    static char *setmsigpubkey[] = { (char *)setmsigpubkey_func, "setmsigpubkey", "V", "coin", "refNXTaddr", "addr", "userpubkey", 0 };
    static char *MGW[] = { (char *)MGW_func, "MGW", "", "NXT0", "NXT1", "NXT2", "ip0", "ip1", "ip2", "coin", "asset", "rescan", "actionflag", "specialNXT", "exclude0", "exclude1", "exclude2", "destip", "destport", "userpubkey", "email", "destNXT", 0 };
    static char *cosign[] = { (char *)cosign_func, "cosign", "V", "otheracct", "seed", "text", 0 };
    static char *cosigned[] = { (char *)cosigned_func, "cosigned", "V", "seed", "result", "privacct", "pubacct", 0 };

    // IP comms
    static char *ping[] = { (char *)ping_func, "ping", "V", "pubkey", "ipaddr", "port", "destip", "MMatrix", 0 };
    static char *pong[] = { (char *)pong_func, "pong", "V", "pubkey", "ipaddr", "port", "yourip", "yourport", "tag", "MMatrix", 0 };
    static char *sendfrag[] = { (char *)sendfrag_func, "sendfrag", "V", "pubkey", "name", "fragi", "numfrags", "ipaddr", "totalcrc", "datacrc", "data", "totallen", "blocksize", "handler", 0 };
    static char *gotfrag[] = { (char *)gotfrag_func, "gotfrag", "V", "pubkey", "name", "fragi", "numfrags", "ipaddr", "totalcrc", "datacrc", "totallen", "blocksize", "count", "handler", 0 };
    static char *startxfer[] = { (char *)startxfer_func, "startxfer", "V", "fname", "dest", "data", "timeout", "handler", 0 };

    // Kademlia DHT
    static char *store[] = { (char *)store_func, "store", "V", "pubkey", "key", "name", "data", 0 };
    static char *findvalue[] = { (char *)findvalue_func, "findvalue", "V", "pubkey", "key", "name", "data", 0 };
    static char *findnode[] = { (char *)findnode_func, "findnode", "V", "pubkey", "key", "name", "data", 0 };
    static char *havenode[] = { (char *)havenode_func, "havenode", "V", "pubkey", "key", "name", "data", 0 };
    static char *havenodeB[] = { (char *)havenodeB_func, "havenodeB", "V", "pubkey", "key", "name", "data", 0 };
    static char *findaddress[] = { (char *)findaddress_func, "findaddress", "V", "refaddr", "list", "dist", "duration", "numthreads", 0 };

    // MofNfs 3
    static char *savefile[] = { (char *)savefile_func, "savefile", "V", "fname", "L", "M", "N", "backup", "password", "pin", 0 };
    static char *restorefile[] = { (char *)restorefile_func, "restorefile", "V", RESTORE_ARGS, 0 };
    static char *publish[] = { (char *)publish_func, "publish", "V", "files", "L", "M", "N", "backup", "password", "pin", 0  };

    // Telepathy
    static char *getpeers[] = { (char *)getpeers_func, "getpeers", "V",  "scan", 0 };
    static char *addcontact[] = { (char *)addcontact_func, "addcontact", "V",  "handle", "acct", 0 };
    static char *removecontact[] = { (char *)removecontact_func, "removecontact", "V",  "contact", 0 };
    static char *dispcontact[] = { (char *)dispcontact_func, "dispcontact", "V",  "contact", 0 };
    static char *telepathy[] = { (char *)telepathy_func, "telepathy", "V",  "contact", "id", "type", "attach", 0 };
    static char *getdb[] = { (char *)getdb_func, "getdb", "V",  "contact", "id", "key", "dir", "destip", 0 };
    static char *sendmsg[] = { (char *)sendmsg_func, "sendmessage", "V", "dest", "msg", "L", 0 };
    static char *sendbinary[] = { (char *)sendbinary_func, "sendbinary", "V", "dest", "data", "L", 0 };
    static char *checkmsg[] = { (char *)checkmsg_func, "checkmessages", "V", "sender", 0 };

    // Teleport
    static char *maketelepods[] = { (char *)maketelepods_func, "maketelepods", "V", "amount", "coin", 0 };
    static char *telepodacct[] = { (char *)telepodacct_func, "telepodacct", "V", "amount", "contact", "coin", "comment", "cmd", "withdraw", 0 };
    static char *teleport[] = { (char *)teleport_func, "teleport", "V", "amount", "contact", "coin", "minage", "withdraw", 0 };

    // InstantDEX
    static char *orderbook[] = { (char *)orderbook_func, "orderbook", "V", "baseid", "relid", "allfields", "oldest", 0 };
    static char *placebid[] = { (char *)placebid_func, "placebid", "V", "baseid", "relid", "volume", "price", 0 };
    static char *placeask[] = { (char *)placeask_func, "placeask", "V", "baseid", "relid", "volume", "price",0 };
    static char *makeoffer[] = { (char *)makeoffer_func, "makeoffer", "V", "baseid", "relid", "baseamount", "relamount", "other", "type", 0 };
    static char *respondtx[] = { (char *)respondtx_func, "respondtx", "V", "signedtx", 0 };
    static char *processutx[] = { (char *)processutx_func, "processutx", "V", "utx", "sig", "full", 0 };

    // Tradebot
    static char *pricedb[] = { (char *)pricedb_func, "pricedb", "V", "exchange", "base", "rel", "stop", 0 };
    static char *getquotes[] = { (char *)getquotes_func, "getquotes", "V", "exchange", "base", "rel", "oldest", 0 };
    static char *tradebot[] = { (char *)tradebot_func, "tradebot", "V", "code", 0 };

    // Privatbet 1
    static char *lotto[] = { (char *)lotto_func, "lotto", "V", "refacct", "asset", 0 };

     static char **commands[] = { stop, GUIpoll, BTCDpoll, settings, gotjson, gotpacket, gotnewpeer, getdb, cosign, cosigned, telepathy, addcontact, dispcontact, removecontact, findaddress, ping, pong, store, findnode, havenode, havenodeB, findvalue, publish, getpeers, maketelepods, tradebot, respondtx, processutx, checkmsg, placebid, placeask, makeoffer, sendmsg, sendbinary, orderbook, teleport, telepodacct, savefile, restorefile, pricedb, getquotes, passthru, remote, genmultisig, getmsigpubkey, setmsigpubkey, MGW, MGWaddr, MGWresponse, sendfrag, gotfrag, startxfer, lotto };
    int32_t i,j;



"""
