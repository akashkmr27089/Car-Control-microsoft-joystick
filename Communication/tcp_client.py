import socket    

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          
port = 12346             
s.connect(('192.168.43.163', port))
count = 0
while(True):
    try:
        h = s.recv(1024).decode('utf-8').split(',')
        if count !=5:
            count += 1
        else:
            left_right = int(h[2][2:-1])
            forward = int(h[3][2:-1])
            err_on = h[9][2:-1]
            err_off = h[10][2:-1]
            print(left_right, forward, err_on, err_off)
            print(type(err_on), type(err_on))
        
    except KeyboardInterrupt:
        s.close()
        print("Exit")   