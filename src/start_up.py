#!/usr/bin/env python3.8

import rospy
import mavros
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State, Altitude  
from mavros_msgs.srv import CommandBool, SetMode


class Start():

    def __init__(self):
        self.STATE = State()
        self.my_state = 'GUIDED_NOGPS'
        self.Altitude = Altitude()
        
        self.set_services()
        self.set_mode()
        self.set_arm()

    def get_state(self):
        return self.STATE


    def set_services(self):
        self.state_sub = rospy.Subscriber('mavros/state', State)
        self.arming_srv = rospy.ServiceProxy('mavros/cmd/arming', CommandBool)
        self.set_mode_srv = rospy.ServiceProxy('mavros/set_mode', SetMode)

    def set_arm(self):
        #TODO: Put this in try/except
        if not self.STATE.armed:
            arming = self.arming_srv(True)
            if arming.success:
                rospy.loginfo('Armed')
            else:
                rospy.loginfo('Failed To Arm')

    def set_mode(self):
        #TODO: put in try/ except
        if self.STATE.mode != self.my_state:
            mode = self.set_mode_srv(base_mode=0, custom_mode=self.my_state)
            if mode.mode_sent:
                rospy.loginfo(self.my_state +' mode set')
            else:
                rospy.loginfo('Failed to set mode to '+self.my_state)

    
if __name__=='__main__':

    st =  Start()