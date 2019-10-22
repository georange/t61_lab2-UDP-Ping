from socket import *
import time
import sys

start = time.clock()
s = socket(AF_INET,SOCK_DGRAM)

# take command line arguments
ip = sys.argv[1]
port = int(sys.argv[2])

# messages will be sent here
server = (ip, port)

try:
    for i in range(1,11):
        # send 10 pings to server
        msg = "ping " + i + " " + time.asctime(time.localtime(time.time()))
        s.sendto(msg, server)
        s.settimeout(2)

        # TODO: wait for response OR TIMEOUT 
        data, addr = s.recvfrom(maxsize)
        end = time.clock()

        print("Reply from " + addr ": " + data)
        print("RTT: " + (end-start))
        
except socket.timeout:
    print ("Request timed out.")

s.close()
