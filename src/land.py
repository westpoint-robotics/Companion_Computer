#!/usr/bin/env python3.8

import rospy
import mavros
from start_up import Start
from mavros_msgs.msg import State  
from mavros_msgs.srv import CommandBool, SetMode

def setLand():

    rospy.init_node('land', anonymous = True) 
    
    set_mode_srv = rospy.ServiceProxy('mavros/set_mode', SetMode)
    rospy.wait_for_service('mavros/set_mode')

    rospy.loginfo('Ready to land')

    try:
        mode = set_mode_srv(base_mode=0, custom_mode='LAND')
            
        if mode.mode_sent:
            rospy.loginfo('LAND mode set')
        else:
            rospy.loginfo('Failed to set mode to LAND')

    except rospy. ServiceException as e:
        rospy.loginfo('Service call failed: %s' %e)

if __name__ == '__main__':
    setLand()
