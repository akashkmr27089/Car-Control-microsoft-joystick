import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import subprocess
import time
import socket

#styling for matplotlib
style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

#Creation of subprocess to read data from joystick
process = subprocess.Popen(['jstest', '--normal', '/dev/input/js0'], 
                           stdout=subprocess.PIPE,
                           universal_newlines=True)

def check(data):
    if len(data) >= 1:
        if len(data)==2 and data[1]==":":
            return False
        elif len(data) >=2 and data[1] == ":":
            return (True,1)
        return True
    return False

count = 0
display_window = []
start = time.time()

#connection formation 
s1 = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) #TCP Connection
port = 12346
print(" Waiting for connection :")
s1.bind(('', port))
s1.listen(5)
c , addr = s1.accept()
print(" Connected to :")
#connecton formation end

while True:
    try:
        output = process.stdout.readline()
        #h = output.strip().split()
        h = output.strip().split(' ')
        g = []
        for i in h:
            response = check(i)
            if type(response) is bool:
                if response == True:
                    g.append(i)
            else:
                    g.append(i[2:])
        ##################### g is the main variable
        g.insert(0,time.time())
        c.send(str(g).encode('utf-8'))
        print(g)
        ##################### coading aread above
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output 
            for output in process.stdout.readlines():
                print(output.strip())
            break
        print()
    except KeyboardInterrupt:
        c.close()
        s1.close()
        print(" User Instrupt Generated ")
        

