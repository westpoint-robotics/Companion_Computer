#!/usr/bin/env python3.8

import rospy
import mavros
from geometry_msgs.msg import PoseStamped, TwistStamped, PositionTarget
from mavros_msgs.msg import State 
from mavros_msgs.srv import CommandBool, SetMode
import numpy as np
from start_up import Start

def coordinates(radius):
    theta = np.linspace(0,2*np.pi,1000)
    
    X = radius * np.cos(theta)
    Y = radius * np.sin(theta)
    
    return X,Y

def angular_velocity(x_y_vel,radius):
    circ = 2 * np.pi * radius
    circ_time = 1/x_y_vel
    return (2*np.pi)/circ_time

def motion(radius):

    rate = rospy.Rate(10.0)

    X,Y = coordinates(radius)
    pos_pub = rospy.Publisher('mavros/setpoint_position/local', PoseStamped, queue_size=1000)
    yaw_pub = rospy.Publisher('mavros/setpoint_raw/local', PositionTarget, queue_size=1000)
    vel_pub = rospy.Publisher('mavros/setpoint_velocity/cmd_vel_unstamped', Twist, queue_size = 10)

    pose = PoseStamped()
    yaw = PositionTarget()

    yaw.yaw = angular_velocity(0.5,radius)
    
    vel.linear.x = 0.5
    vel.linear.y = 0.5

    vel_pub.publish(vel)

    iter = 0

    while not rospy.is_shutdown():
        if iter-1 == len(X):
            pose.pose.position.x = 2
            pose.pose.position.y = 2
            pose.pose.position.z = 10
            pos_pub.publish(pose)
            break
        
        pose.pose.position.x = X[iter]
        pose.pose.position.y = Y[iter]
        pose.pose.position.z = 2
        
        pos_pub.publish(pose)
        yaw_pub.publish(yaw)

        iter += 1

        rate.sleep()


if __name__ == '__main__':

    rospy.init_node('circle', anonymous=True)
    rospy.loginfo('Circle Node initialized')
    set_mode_srv = rospy.ServiceProxy('mavros/set_mode', SetMode)
    
    rospy.wait_for_service('mavros/set_mode')
    
    st = Start()
    
    st.set_mode()

    try:
        motion(5)
    except rospy.ROSInterruptException:
        pass

