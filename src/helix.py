#!/usr/bin/env python3.8

import rospy
import mavros
import math
from geometry_msgs.msg import PoseStamped, TwistStamped
from mavros_msgs.msg import State 
from mavros_msgs.srv import CommandBool, SetMode
from start_up import Start

def motion(radius):

    rate = rospy.Rate(20.0)
    
    pos_pub = rospy.Publisher('mavros/setpoint_position/local', PoseStamped, queue_size=1000)
    vel_pub = rospy.Publisher('mavros/setpoint_velocity/cmd_vel', TwistStamped, queue_size=1000)

    #TODO: Set a desired velocity

    pose = PoseStamped()

    length = 100
    radius = 2   #vertical radius
    horizontal_seperation = 3  #seperation between apexes (m)
    min_altitude = 3

    min_altitude = min_altitude + radius
    length = length * horizontal_seperation

    iter = 0

    while not rospy.is_shutdown():

        pose.pose.position.x = horizontal_seperation * iter 
        pose.pose.position.y = radius * math.sin(iter) 
        pose.pose.position.z = radius * math.cos(iter) + min_altitude
        
        pos_pub.publish(pose)
        
        iter += 1

        rate.sleep()

if __name__ == '__main__':

    rospy.init_node('Helix', anonymous=True)
    rospy.loginfo('Helix Node initialized')
    set_mode_srv = rospy.ServiceProxy('mavros/set_mode', SetMode)
    
    st = Start()
    st.set_mode()

    try:
        motion(5)
    except rospy.ROSInterruptException:
        pass