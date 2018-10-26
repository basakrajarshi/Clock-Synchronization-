import socket
import datetime
import sys
# Creating an UDP socket for the server
ss = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address =('',10023)
#Binding with the client's address
ss.bind(server_address)
while True:
    # Taking note of server request time and server reply time
    c, addr = ss.recvfrom(4096)
    server_request_time = datetime.datetime.now()
    server_reply_time = datetime.datetime.now()
    # Passing time values of the server to the client
    send = ss.sendto('Server Request Time:' + "," + str(server_request_time) + "," + 'Server Reply time:' + "," +str(server_reply_time),addr)
    
    
 
