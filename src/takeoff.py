#!/usr/bin/env python3.8

import rospy
import mavros
from geometry_msgs.msg import PoseStamped, Twist
from mavros_msgs.msg import State, Altitude, PositionTarget, AttitudeTarget  
from mavros_msgs.srv import *
from start_up import *
import time

def takeoff():
    
    local_pub = rospy.Publisher('mavros/setpoint_position/local',PoseStamped, queue_size = 10)
    target_pub = rospy.Publisher('mavros/setpoint_raw/local', PositionTarget, queue_size = 10)
    att_pub = rospy.Publisher('mavros/setpoint_raw/attitude', AttitudeTarget, queue_size=10)

    rate = rospy.Rate(20.0)

    target = PositionTarget()
    pose = PoseStamped()
    att = AttitudeTarget()

    pose.pose.position.x = 0
    pose.pose.position.y = 0
    pose.pose.position.z = 0

    target.header.frame_id = 'home'
    target.header.stamp = rospy.Time.now()
    target.coordinate_frame = 1
    target.type_mask = 4088

    target.position.x = 0
    target.position.y = 0
    target.position.z = 2

    target.velocity.z = 0.5
    target.yaw = 0

    att.body_rate.x = 0
    att.body_rate.y = 0
    att.body_rate.z = 0
    att.thrust = 0.55
    

    for _ in range(100):
        local_pub.publish(pose)

    while not rospy.is_shutdown():
        target_pub.publish(target)
        att_pub.publish(att)
        rate.sleep()
    

if __name__=='__main__':
    rospy.init_node('Takeoff', anonymous=True)
    rospy.loginfo('Initialized takeoff node')
    
    st = Start()

    st.set_arm()
    st.set_mode()
    
    time.sleep(5)
    
    rospy.loginfo('Ready For Takeoff')
    
    takeoff()
    

