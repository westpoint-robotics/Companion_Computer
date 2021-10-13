#!/usr/bin/env python3.8

import rospy
import mavros
from start_up import Start
from mavros_msgs.msg import State  
from mavros_msgs.srv import CommandBool, SetMode

def set_RTL():

    set_mode_srv = rospy.ServiceProxy('mavros/set_mode', SetMode)
    #TODO: put in try/ except
    if  Start.get_state != 'RTL':
        mode = set_mode_srv(base_mode=0, custom_mode='RTL')
        if mode.mode_sent:
            rospy.loginfo('RTL mode set')
        else:
            rospy.loginfo('Failed to set mode to RTL')

if __name__ == '__main__':
    set_RTL()