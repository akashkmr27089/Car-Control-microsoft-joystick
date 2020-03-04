import socket    
import Motion_pre as mo_pre
import Motion as mo


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          
port = 12346             
s.connect(('192.168.43.163', port))
count = 0

comm = mo_pre.Motion_pre()
motive_motion = mo.Movement()

while(True):
    try:
        h = s.recv(1024).decode('utf-8').split(',')
        if count !=5:
            count += 1
        else:
            print(" Debug ",h[2:4], h[9:11])
            print(" Debug ", h)
            left_right = int(h[2][2:-1])
            forward = int(h[3][2:-1])
            err_on = h[9][2:-1]
            err_off = h[10][2:-1]
            print(" Input :",left_right, forward, err_on, err_off)
            output = comm.input(forward, left_right, err_on, err_off)
            print(" Intermidiate Output :", output)
            motive_motion.move(output)  #the code fro final output
    except ValueError:
        print(" Will still continue")        
    except KeyboardInterrupt:
        s.close()
        print("Exit")   