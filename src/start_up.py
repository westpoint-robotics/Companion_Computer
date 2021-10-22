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
        

    def get_state(self):
        return self.STATE

    def get_my_state(self):
        return self.my_state


    def set_arm(self):
        
        arming_srv = rospy.ServiceProxy('mavros/cmd/arming', CommandBool)

        if not self.STATE.armed:
            try:
                arming = arming_srv(True)
                if arming.success:
                    rospy.loginfo('Armed')
                else:
                    rospy.loginfo('Failed To Arm')
            except rospy.ServiceException as e:
                    rospy.loginfo('Service call failed: %s' %e)

    def set_mode(self):
        
        rospy.wait_for_service('mavros/set_mode')
        set_mode_srv = rospy.ServiceProxy('mavros/set_mode', SetMode)

        if self.STATE.mode != self.my_state:
            try:
                mode = set_mode_srv(base_mode=0, custom_mode=self.my_state)
                if mode.mode_sent:
                    rospy.loginfo(self.my_state +' mode set')
                else:
                    rospy.logwarn('Failed to set mode to '+self.my_state)
            except rospy.ServiceException as e:
                    rospy.logwarn('Service Call Failed: %s' %e)
        else:
            rospy.loginfo(self.my_state + ' mode already set')
        return mode.mode_sent
if __name__=='__main__':

    st =  Start()
