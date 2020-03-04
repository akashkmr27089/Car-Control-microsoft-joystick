import socket                

s = socket.socket()          
print("Socket successfully created")
port = 12346               
s.bind(('', port))         
print("socket binded to %s" %(port))
s.listen(5)      
print("socket is listening")            
while True: 
   c, addr = s.accept()      
   print("Got connection from", addr)
   while(True):
       c.send('Thank you for connecting'.encode('utf-8'))
   c.close()