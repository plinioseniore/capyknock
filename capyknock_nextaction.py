# This function is called once the SPA Authenthorization is completed
# is by default emply and can be configured based on user needs

def nextauthentication(ip, port):
    # At this stage the next authentication can be run
    # there are two option, run from here the client
    # using subprocess or alternatively you can run
    # pyknock_client from a batch file and let the
    # batch to call the next client once pyknock_client
    # is terminated, an example for Windows:
    #
    # @echo off
    # title pyknock
    # cls
    # cd %cd%\pyknock_client
    # pyknock_client.exe
    # cd..
    # cd %cd%\ssh
    # start sshclient.exe	  
    # exit
    print("")

