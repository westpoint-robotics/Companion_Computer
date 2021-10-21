#!/usr/bin/env python3.8

import rospy
import mavros
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State, Altitude  
from mavros_msgs.srv import CommandBool, SetMode


class Start():

    def __init__(self):
        self.STATE = State()
        self.my_state = 'GUIDED'
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
        
        if not self.STATE.armed:
            try:
                arming = self.arming_srv(True)
                if arming.success:
                    rospy.loginfo('Armed')
                else:
                    rospy.loginfo('Failed To Arm')
            except rospy.ServiceException as e:
                    rospy.loginfo('Service call failed: %s' %e)

    def set_mode(self):
        
        rospy.wait_for_service('mavros/set_mdoe')

        if self.STATE.mode != self.my_state:
            try:
                mode = self.set_mode_srv(base_mode=0, custom_mode=self.my_state)
                if mode.mode_sent:
                    rospy.loginfo(self.my_state +' mode set')
                else:
                    rospy.loginfo('Failed to set mode to '+self.my_state)
            except rospy.ServiceException as e:
                    rospy.loginfo('Service Call Failed: %s' %e)
        else:
            rospy.loginfo('Guided mode already set')
if __name__=='__main__':

    st =  Start()
