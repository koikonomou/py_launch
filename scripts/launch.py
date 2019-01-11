import rospy
import os
import rospy
import rospkg
import subprocess
import roslaunch


def init():

    rospy.init_node('launch', anonymous=True)
    package = 'pointcloud_distance'
    launch_file = 'distance.launch'
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    launch_file = os.path.join(rospkg.RosPack().get_path(package), 'launch', launch_file)
    launch = roslaunch.parent.ROSLaunchParent(uuid, [launch_file])
    launch.start()

    rospy.spin()

if __name__ == '__main__':
    init()

