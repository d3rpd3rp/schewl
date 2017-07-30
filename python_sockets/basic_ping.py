import os, sys, struct, time, select, binascii, threading
from socket import *

ICMP_ECHO_REQUEST = 8

def checksum(byte_str):
    csum = 0
    countTo = (len(byte_str) / 2) * 2
    #print('len of byte_str is {} and countTo is {}'.format(len(byte_str), countTo))
    count = 0
    #print('byte_str as string is {}'.format(str(byte_str)))
    while count < countTo:
        #print('str[count] is {} and of type {}.'.format(byte_str[count], type(str(byte_str[count]))))
        #print('str[count+1] is {} and of type {}.'.format(byte_str[count+1], type(str(byte_str[count+1]))))
        if type(str(byte_str[count])) == 1:
            first_byte = ord(str(byte_str[count]))
        else:
            first_byte = int(byte_str[count])
        if len(str(byte_str[count+1])) == 1:
            second_byte = ord(str(byte_str[count+1]))
        else:
            second_byte = int(byte_str[count+1])
        thisVal = second_byte * 256 + first_byte
        csum = csum + thisVal
        csum = csum & 0xffffffff
        count = count + 2

    if countTo < len(byte_str):
        print('ord(str(byte_str[len(byte_str) - 1])) value is: {} and type is {}'.format(byte_str[len(byte_str) - 1],\
        type(ord(str(byte_str[len(byte_str) - 1])))))
        csum = csum + ord(str(byte_str[len(byte_str) - 1]))
    
    csum = csum & 0xffffffff
    csum = (csum >> 16) + (csum & 0xffff)
    csum = csum + (csum >> 16)
    answer = ~csum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return (answer)

def receiveOnePing(pingSocket, ID, timeout, destAddr):
    print('mySocket in receiveOnePing...{}'.format(pingSocket))
    timeLeft = timeout
    while 1:
        startedSelect = time.time()
        #KEY ISSUE, pingSocket never lists in the readable list returned by select
        whatReady = select.select([pingSocket], [pingSocket], [], timeLeft)
        print('whatReady is socket is: {}'.format(whatReady))
        howLongInSelect = (time.time() - startedSelect)
        if whatReady[0] == []: # Timeout
            return "Request timed out from what ready."
        recPacket, addr = pingSocket.recvfrom(1024)
        timeReceived = time.time()
        #recPacket, addr = mySocket.recvfrom(1024)
        #Fill in start
        #Fetch the ICMP header from the IP packet
        icmpHeader = recPacket[20:28]
        type, code, checksum, id, sequence = struct.unpack("bbHHh", icmpHeader)
        if (id == ID):
            st = struct.calcsize("d")
            timeSent = struct.unpack("d", recPacket[28:28 + st])[0]
            print("Reply from " + str(destAddr) + ":" + " bytes = " + str(st))
            return (timeReceived - timeSent)
    # Fill in end
        #Fill in end
        #timeLeft = timeLeft - howLongInSelect
        if timeLeft <= 0:
            return ('Request timed out from timeLeft.')

def sendOnePing(pingSocket, destAddr, ID):
    #print('in sendOnePing creation of socket is: {}'.format(pingSocket))
    # Header is type (8), code (8), checksum (16), id (16), sequence (16)
    myChecksum = 0
    # Make a dummy header with a 0 checksum.
    # struct -- Interpret strings as packed binary data
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    data = struct.pack("d", time.time())
    # Calculate the checksum on the data and the dummy header.
    myChecksum = checksum(header + data)
    # Get the right checksum, and put in the header
    if sys.platform == 'darwin':
        myChecksum = htons(myChecksum) & 0xffff
    #Convert 16-bit integers from host to network byte order.
    else:
        myChecksum = htons(myChecksum)
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    packet = header + data
    pingSocket.sendto(packet, (destAddr, 1)) # AF_INET address must be tuple, not str
    timeout = 3
    ready = select.select([pingSocket], [pingSocket], [], timeout)
    print(ready)
    #Both LISTS and TUPLES consist of a number of objects
    #which can be referenced by their position number within the object
    print('sent ping...')

def doOnePing(destAddr, timeout):
    icmp = getprotobyname("icmp")
    pingSocket = socket(AF_INET, SOCK_RAW, icmp)
    pingSocket.bind(('', 0))
    myID = os.getpid() & 0xFFFF #Return the current process i
    print('the process ID is {}'.format(myID))
    sendOnePing(pingSocket, destAddr, myID)
    #testing here...adding longer timeout
    timeout = 2
    delay = receiveOnePing(pingSocket, myID, timeout, destAddr)
    pingSocket.close()
    return(delay)

def ping(host, timeout = 2.0):
    #timeout=1 means: If one second goes by without a reply from the server,
    #the client assumes that either the client’s ping or the server’s pong is lost
    dest = gethostbyname(host)
    print('dest is {}'.format(dest))
    print("Pinging " + dest + " using Python:")
    #Send ping requests to a server separated by approximately one second
    while 1 :
        delay = doOnePing(dest, timeout)
        print (delay)
        time.sleep(1)# one second
    return (delay)

dest_host = '127.0.0.1'
ping(dest_host)
