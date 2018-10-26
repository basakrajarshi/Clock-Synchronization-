import socket
import datetime
from datetime import timedelta 
import sys
x1 = range(5)
x2 = range(5)
x3 = range(5)

#Creating an UDP socket
sc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address = ('10.201.16.200',10023)
#Running the program 5 times
for j in range(0,5):
    client_request_time = datetime.datetime.now()
    sc.sendto("add",('10.201.16.200',10023))
    s , addr = sc.recvfrom(4096)
    client_reply_time = datetime.datetime.now()
    #Printing the client and server times
    print('Client:')
    print('Connection established between client and server' + " " + 'Client request time' + " " + str(client_request_time) + " " + 'Client reply time' + " " + str(client_reply_time))
    print("Server:")
    print s
    x = s.split(",")
    #Adding server request and server reply time
    a = datetime.datetime.strptime(x[1],'%Y-%m-%d %H:%M:%S.%f')
    b = datetime.datetime.strptime(x[3],'%Y-%m-%d %H:%M:%S.%f')
    #Finding time at the server
    x1[j] = timedelta(seconds = (((b - a).total_seconds())/2.0)) + a
    print 'Time at the server is :' +str(x1[j])
    #Finding time at the client
    x2[j] = timedelta(seconds = ((client_reply_time - client_request_time).total_seconds()/2.0))
    client_new_time = x1[j] + (x2[j])
    print 'New time at the client is :' + str(client_new_time)
    #Finding Absolute minimum latency
    x3[j] = a - client_request_time
Tmin = min(x3[0],x3[1],x3[2],x3[3],x3[4])
Tmin1 = abs(Tmin)
print 'Absolute minimum latency between the client and the server is :' +str(Tmin1.total_seconds())
for k in range (0,5):
    #Finding the error bound the server and client
    terr = abs(x2[k] - Tmin1)
    print 'Error bound between server and client is :' +str(terr.total_seconds())
        
    
    
    
    
    
    



