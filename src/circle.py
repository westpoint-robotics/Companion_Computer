#!/usr/bin/env python3.8

import rospy
import mavros
from geometry_msgs.msg import PoseStamped, TwistStamped
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
    vel_pub = rospy.Publisher('mavros/setpoint_velocity/cmd_vel', TwistStamped, queue_size=1000)

    pose = PoseStamped()
    vel = TwistStamped()

    vel.angular.x = angular_velocity(0.5,radius)
    vel.linear.x = 0.5
    vel.linear.y = 0.5

    vel_pub.publish(vel)

    iter = 0

    while not rospy.is_shutdown():
        if iter-1 == len(X):
            pose.pose.position.x = 2
            pose.pose.position.y = 2
            pose.pose.position.z = 10
            break

        pose.pose.position.x = X[iter]
        pose.pose.position.y = Y[iter]
        pose.pose.position.z = 2
        
        pos_pub.publish(pose)
        
        iter += 1

        rate.sleep()


if __name__ == '__main__':

    rospy.init_node('circle', anonymous=True)
    rospy.loginfo('Circle Node initialized')
    set_mode_srv = rospy.ServiceProxy('mavros/set_mode', SetMode)
    
    rospy.wait_for_service('mavros/set_mode')

    try:
        mode_success = set_mode_srv(base_mode=0, custom_mode='GUIDED')
        if mode_success.mode_sent:
            rospy.loginfo('Guided Mode Set')
        else:
            rospy.loginfo('Unable to set Guided mode')
    except rospy.ServiceException as e:
            rospy.loginfo('Service Call Failed: %s' %e)
    try:
        motion(5)
    except rospy.ROSInterruptException:
        pass
