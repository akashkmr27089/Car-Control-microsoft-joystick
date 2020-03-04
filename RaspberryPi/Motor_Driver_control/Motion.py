import RPi.GPIO as gpio

class Movement:
    def __init__(self):
        gpio.setmode(gpio.BCM) #bcm pin Layout
        #using pin 12,18 for forward and backward and pin 23,24 for turning
        #[a,b,c,d,e] ==> value of a and b [0:100]
        #value of c and d [0,1] --> no pwm for now
        #e ==> emergency stop
        gpio.setup(12,gpio.OUT)
        gpio.setup(18,gpio.OUT)
        gpio.setup(23,gpio.OUT)
        gpio.setup(24,gpio.OUT)
        self.pwm1 = gpio.PWM(18,1000)
        self.pwm2 = gpio.PWM(12,1000)
    
    def forward(self,dutycycle):
        print("Forward ", dutycycle)
        gpio.output(18,gpio.LOW)
        self.pwm1.stop()
        self.pwm2.start(dutycycle)

    def backward(self,dutycycle):
        print("backward ", dutycycle)
        gpio.output(12, gpio.LOW)
        self.pwm2.stop()
        self.pwm1.start(dutycycle)
    
    def stearing(self,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   left_right_data):
        if left_right_data[0] == left_right_data[1]:
            gpio.output(23,gpio.LOW)
            gpio.output(24,gpio.LOW)
        elif left_right_data[0] < left_right_data[1]:
            gpio.output(23,gpio.LOW)
            gpio.output(24,gpio.HIGH)
        else:
            gpio.output(24,gpio.LOW)
            gpio.output(23,gpio.HIGH)
    
    def hard_stop(self):
        print("hard stop")
        gpio.output(18, gpio.LOW)
        gpio.output(12, gpio.LOW)
        gpio.output(23, gpio.LOW)
        gpio.output(24, gpio.LOW)
        self.pwm1.stop()
        self.pwm2.stop()

        
    def move(self,motion):
        print("Movement called")
        self.motion = motion
        try:
            if self.motion[4] == 1:
                self.hard_stop()
            else:
                if self.motion[0] > self.motion[1]:
                    self.forward(self.motion[0])
                else:
                    self.backward(self.motion[1])
                self.stearing(self.motion[2:])
        except KeyboardInterrupt:
            print("User Generated Intruppt ")
            #call destructor to close all the port in use
        
        
