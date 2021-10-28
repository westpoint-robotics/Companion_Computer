import rospy
import mavros
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

    pose = Point()
    vel = Twist()

    while not rospy.is_shutdown():
        vel.linear.y = 0.5
        pose.x = 0
        pose.y = length
        pose.z = 1

        vel_pub.publish(vel)
        pose_pub.publish(pose)

if __name__ == '__main__':
    rospy.init_node('line', anonymous=True)
    rospy.loginfo('Line Node Initizalized')

    motion(2)