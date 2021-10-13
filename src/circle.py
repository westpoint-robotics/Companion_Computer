#!/usr/bin/env python3.8

import rospy
import mavros
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State 
from mavros_msgs.srv import CommandBool, SetMode
import numpy as np
from start_up import Start

def coordinates(radius);
    theta = np.linspace(0,2*np.pi,1000)
    
    X = radius * np.cos(theta)
    Y = radius * np.sin(theta)

    return X,Y

def motion(X,Y):
    pos_pub = rospy.Publisher('setpoint_raw/local', PoseStamped, queue_size=10)
    rate = rospy.Rate(20.0)

    pose = PoseStamped()
    iter = 0

    while not rospy.is_shutdown():
        if iter == len(X):
            break

        pose.pose.position.x = X[iter]
        pose.pose.position.y = Y[iter]
        pose.pose.position.z = 5

        pos_pub.publish(pose)
        
        iter += 1

        rate.sleep()


if __name__ == __main__:
    st = Start()
    x, Y = coordinates(8)
    motion(X,Y)
