import socket
import datetime
import sys
#Creating an UDP socket
sc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address = ('10.201.16.200',10023)
#Running the program 5 times
for j in range(0,5):
    client_request_time = datetime.datetime.now()
    sc.sendto("add",('10.201.16.200',10023))
    s , addr = sc.recvfrom(40960)
    client_reply_time = datetime.datetime.now()
    #Printing the client and server times
    print('Client:')
    print('Connection established between client and server:' + "\n" + 'Client request time' + " " + str(client_request_time) + "\n" + 'Client reply time' + " " + str(client_reply_time))
    print("Server:")
    print s
    x = s.split(",")
    a = datetime.datetime.strptime(x[1],'%Y-%m-%d %H:%M:%S.%f')
    b = datetime.datetime.strptime(x[3],'%Y-%m-%d %H:%M:%S.%f')
    latency1 = a - client_request_time
    latency2 = client_reply_time - b
    delay = latency1 + latency2
    #Printing delay in seconds
    print 'Delay:' +str(delay.total_seconds())
    #Printing offset in seconds
    offset = abs(latency2 - latency1)/2
    print 'Offset:' +str(offset.total_seconds())
    
    



