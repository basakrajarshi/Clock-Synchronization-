import socket
import datetime
import math  
import sys
#Creating a UDP socket
sc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#Connecting to the server
server_address = ('10.201.16.200',10023)
#Defining arrays to store request and reply time
x1 = range(5)
x2 = range(5)
x3 = range(5)
a1 = range(5)
a2 = range(5)
a3 = range(5)
a4 = range(5)
sum1 = 0
sum2 = 0
#Running the program 5 times
for j in range(0,5):
    client_request_time = datetime.datetime.now()
    sc.sendto("add",('10.201.16.200',10023))
    s, addr = sc.recvfrom(40960)
    client_reply_time = datetime.datetime.now()
    #Printing client and server times
    print('Client:')
    print('Connection established between client and server' + " " + 'Client request time' + " "  + str(client_request_time) + " " + 'Client reply time' + " " + str(client_reply_time))
    print("Server:")
    print s
    x = s.split(",")
    a = datetime.datetime.strptime(x[1],'%Y-%m-%d %H:%M:%S.%f')
    b = datetime.datetime.strptime(x[3],'%Y-%m-%d %H:%M:%S.%f')
    x1[j] = a - client_request_time
    x2[j]= client_reply_time - b
    x3[j] = (client_reply_time - client_request_time)
    print 'Round Trip Time:' + str(x3[j])
    sum1 += x1[j].total_seconds() + x2[j].total_seconds() 
    
#Printing mean
mean = sum1/10
print 'Mean of pairwise latencies:' + " " +str(mean)
for k in range(0,5):
    a1[k] = x1[k].total_seconds() - mean
    a2[k] = x2[k].total_seconds() - mean
    a3[k] = float(a1[k] * a1[k])
    a4[k] = float(a2[k] * a2[k])
    sum2 += a3[k] + a4[k]
#Printing standard deviation
sd = math.sqrt(sum2)
print 'Standard deviation of pairwise latencies:' + " " +str(sd)
        



