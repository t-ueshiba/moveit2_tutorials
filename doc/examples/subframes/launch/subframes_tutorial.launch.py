from launch                   import LaunchDescription
from launch_ros.actions       import Node
from launch.actions           import IncludeLaunchDescription, OpaqueFunction
from launch.substitutions     import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def launch_setup(context):
    return [
        # IncludeLaunchDescription(
        #     PathJoinSubstitution([
        #         FindPackageShare('moveit_resources_panda_moveit_config'),
        #         'launch', 'demo.launch.py'])),
        Node(name="subframes_tutorial",
             package="moveit2_tutorials",
             executable="subframes_tutorial",
             prefix=['gnome-terminal --tab --wait --active --'],
             output="screen"),
    ]

def generate_launch_description() -> LaunchDescription:
    return LaunchDescription([OpaqueFunction(function=launch_setup)])
