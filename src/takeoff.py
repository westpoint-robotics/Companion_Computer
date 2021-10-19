#!/usr/bin/env python3.8

import rospy
import mavros
from geometry_msgs.msg import PoseStamped, Twist
from mavros_msgs.msg import State, Altitude, PositionTarget  
from mavros_msgs.srv import *
from start_up import *

def takeoff():
    
    local_pub = rospy.Publisher('mavros/setpoint_position/local',PoseStamped, queue = 10)
    target_pub = rospy.Publisher('setpoint_raw/local', PositionTarget, queue_size = 10)

    rate = rospy.Rate(20.0)

    target = PositionTarget()
    pose = PoseStamped()

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

    for _ in range(100):
        local_pub.publish(pose)

    while not rospy.is_shutdown():
        target_pub.publish(target)
        rate.sleep()
    
    #try:
    #    tf_srv = rospy.ServiceProxy('mavros/cmd/takeoff',mavros_msgs.srv.CommandTOL)
    #    tf_srv(altitude=1.5)
    #except rospy.ServiceException as e:
    #    rospy.loginfo('Service takeoff call failed: %s' %e)

if __name__=='__main__':
    rospy.init_node('Takeoff', anonymous=True)
    st = Start()
    takeoff()
    

