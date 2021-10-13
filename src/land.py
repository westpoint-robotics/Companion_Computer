#!/usr/bin/env python3.8

import rospy
import mavros
from start_up import Start
from mavros_msgs.msg import State  
from mavros_msgs.srv import CommandBool, SetMode

def setLand():

    set_mode_srv = rospy.ServiceProxy('mavros/set_mode', SetMode)
    #TODO: put in try/ except
    if  Start.get_state != 'LAND':
        mode = set_mode_srv(base_mode=0, custom_mode='LAND')
        if mode.mode_sent:
            rospy.loginfo('LAND mode set')
        else:
            rospy.loginfo('Failed to set mode to LAND')

if __name__ == '__main__'
    setLand()