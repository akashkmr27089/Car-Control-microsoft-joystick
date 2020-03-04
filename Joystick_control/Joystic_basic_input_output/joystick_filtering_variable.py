import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import subprocess

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

        print(g)
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output 
            for output in process.stdout.readlines():
                print(output.strip())
            break
        print()
    except KeyboardInterrupt:
        print(" User Instrupt Generated ")
        

