#!/usr/bin/env python3.8

import rospy
import mavros
import math
import rosbag
from geometry_msgs.msg import PoseStamped, TwistStamped, Twist, Point
from mavros_msgs.msg import State, PositionTarget
from std_msgs.msg import Float32 
from mavros_msgs.srv import CommandBool, SetMode
import datetime as dt
from start_up import Start

def motion(length):
    
    pose_pub = rospy.Publisher('mavros/setpoint_raw/local', PositionTarget, queue_size=10)
    vel_pub = rospy.Publisher('mavros/setpoint_velocity/cmd_vel_unstamped', Twist, queue_size = 10)

    yaw = PositionTarget()
    vel = Twist()

    while not rospy.is_shutdown():
        
        yaw.yaw = math.pi/2

        pose_pub.publish(yaw)

if __name__ == '__main__':
    rospy.init_node('yaw')
    st = Start()
    st.set_mode()
    motion(2)
