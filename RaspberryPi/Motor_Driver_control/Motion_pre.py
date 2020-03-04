#the following class is for converting the raw input to hardware form

import time

class Motion_pre:
    def __init__(self):
        self.motion_out = [0,0,0,0]
        self.emergency = False
        self.forw_direction = True
        self.forw_thrushold = 10000
        self.forw_maximum  = 25000 #indicates the maximum signal input
        self.min_dutycycle_forw = 20 #minimum allowed thrushold
        self.left_right_thrushold = 10000
    def forw_motion(self, motion_data):
        if(abs(motion_data) > self.forw_thrushold):
            if abs(motion_data) <= self.forw_maximum:
                data = int(self.min_dutycycle_forw + ((100 - self.min_dutycycle_forw)*(abs(motion_data) - self.forw_thrushold))/(self.forw_maximum - self.forw_thrushold))
            else:
                data = 100
            if motion_data//abs(motion_data) == -1:  #negative indicates frow_pitch
                return [data,0]
            else:
                return [0,data]
        else:
            return [0,0]
        
    def left_right_motion(self, motion_data):
        # considering motors are taking only left and right motion 
        if motion_data < -self.left_right_thrushold:
            return [1,0]
        elif motion_data > self.left_right_thrushold:
            return [0,1]
        else:
            return [0,0]

    def input(self, forw_back, left_right,  emer_on, emer_off):
        self.forw_back = forw_back
        self.left_right = left_right
        print(self.forw_back, self.left_right, self.emergency)
        if(emer_on == 'on' and emer_off == 'off'):
            self.emergency = True
        elif emer_on == 'off' and emer_off == 'on':
            self.emergency = False
        elif emer_on == 'on' and emer_off == 'on':
            self.emer_on = False
        if self.emergency == False:
            return self.forw_motion(self.forw_back) + self.left_right_motion(self.left_right) + [0]
        else:
            return [0,0,0,0,self.emergency]
        
            
            
        
        
        