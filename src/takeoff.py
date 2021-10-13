#!/usr/bin/env python3.8

import rospy
import mavros
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State, Altitude  
from mavros_msgs.srv import *
from start_up import *

def takeoff():
    """
    pos_pub = rospy.Publisher('setpoint_raw/local', PoseStamped, queue_size=10)
    rate = rospy.Rate(20.0)

    pose = PoseStamped()
    pose.pose.position.x = 0
    pose.pose.position.y = 0
    pose.pose.position.z = 2

    while not rospy.is_shutdown():
        pos_pub.publish(pose)
        rate.sleep()
    """
    try:
        tf_srv = rospy.ServiceProxy('mavros/cmd/takeoff',mavros_msgs.srv.CommandTOL)
        tf_srv(altitude=2)
    except rospy.ServiceException as e:
        print('Service takeoff call failed: %s' %e)

if __name__=='__main__':
    #rospy.init_node('Takeoff', anonymous=True)
    st = Start()
    takeoff()
    

