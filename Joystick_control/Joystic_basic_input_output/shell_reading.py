import subprocess
#for this to work, jstest-gtk should be preinstalled 
# doesnt need any dfa -- as the state is stored -- > if pressed on --> it will reply with on until its on
# 

process = subprocess.Popen(['jstest', '--normal', '/dev/input/js0'], 
                           stdout=subprocess.PIPE,
                           universal_newlines=True)

while True:
    try:
        output = process.stdout.readline()
        print("hello ", output.strip())
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output 
            for output in process.stdout.readlines():
                print(output.strip())
            break
    except KeyboardInterrupt:
        print(" User Instrupt Generated ")
        