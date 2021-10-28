#!/usr/bin/env python3.8

import rospy
import mavros
from geometry_msgs.msg import PoseStamped, Twist
from mavros_msgs.msg import State, WaypointList, Waypoint
from mavros_msgs.srv import CommandBool, SetMode, WaypointPush
from sensor_msgs.msg import NavSatFix
import numpy as np
from start_up import Start

def coordinates(radius,center_x,center_y):
    theta = np.linspace(0,2*np.pi,1000)
    coords = []
    for i in range(1000):
        X = radius * np.cos(theta[i]) + center_x
        Y = radius * np.sin(theta[i]) + center_y
        coords.append((X,Y,2))
    return coords

def motion():

    rate = rospy.Rate(10.0)

    lat_long_sub = rospy.Subscriber('mavros/global_position/global', NavSatFix)
    waypoint_sub = rospy.Subscriber('mavros/mission/waypoints',WaypointList)
    

    waypoint_pub = rospy.Publisher('mavros/mission/waypoints', WaypointList, queue_size=10)
    vel_pub = rospy.Publisher('mavros/setpoint_velocity/cmd_vel_unstamped', Twist, queue_size=1000)
    waypoint_srv = rospy.ServiceProxy('mavros/mission/push', WaypointPush)

    vel = Twist()
    waypoint_l = WaypointList()
    wp = Waypoint()

    wp.frame = 0
    wp.command =16
    wp.is_current = False
    wp.autocontinue = True
    wp.y_long = -73.953220
    wp.x_lat = 41.390722
    wp.z_alt = 5
    waypoint_l.waypoints.append(wp)

    wp.frame = 0
    wp.command =16
    wp.is_current = False
    wp.autocontinue = True
    wp.y_long = -73.953122
    wp.x_lat = 41.390917
    wp.z_alt = 7
    waypoint_l.waypoints.append(wp)

    wp.frame = 0
    wp.command =16
    wp.is_current = True
    wp.autocontinue = True
    wp.y_long = -73.953449
    wp.x_lat = 41.391004
    wp.z_alt = 7
    waypoint_l.waypoints.append(wp)

    wp.frame = 0
    wp.command =16
    wp.is_current = True
    wp.autocontinue = True
    wp.y_long = -73.953519
    wp.x_lat = 41.390800
    wp.z_alt = 5
    waypoint_l.waypoints.append(wp)

    wp.frame = 0
    wp.command =16
    wp.is_current = True
    wp.autocontinue = True
    wp.y_long = -73.95000
    wp.x_lat = 41.50
    wp.z_alt = 5
    waypoint_l.waypoints.append(wp)

    rospy.wait_for_service('mavros/mission/push')

    try:
        push_success = waypoint_srv(start_index=0, waypoints=waypoint_l.waypoints)
        if push_success.success:
            rospy.loginfo('Waypoints Sent Successfully')
        else:
            rospy.loginfo('Unable to send waypoints')
    except rospy.ServiceException as e:
        rospy.loginfo('Service call faild: %s' %e)

    rospy.wait_for_service('mavros/set_mode')
    set_mode_srv = rospy.ServiceProxy('mavros/set_mode', SetMode)
    try:
        mode = set_mode_srv(base_mode=0, custom_mode='AUTO')
        if mode.mode_sent:
            rospy.loginfo('Auto mode set')
        else:
            rospy.logwarn('Failed to set Auto Mode')
    except rospy.ServiceException as e: 
            rospy.logwarn('Service Call Failed: %s' %e)

    while not rospy.is_shutdown():

        rate.sleep()


if __name__ == '__main__':

    rospy.init_node('rectangle', anonymous=True)
    rospy.loginfo('Rectangle node set')

    st = Start()
    st.set_mode()

    try:
        motion()
    except rospy.ROSInterruptException:
        pass
