import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

import xacro


def generate_launch_description():
    
    # Check if we're told to use sim time
    use_sim_time = LaunchConfiguration('use_sim_time')

    pkg_path = os.path.join(get_package_share_directory('burgerbot_rev1'))
    xacro_file = os.path.join(pkg_path, 'urdf', 'robot_core.xacro')
    doc = xacro.process_file(xacro_file)
    robot_desc = doc.toxml()

    # # Process the URDF file
    # pkg_path = os.path.join(get_package_share_directory('burgerbot_rev1'))
    # xacro_file = os.path.join(pkg_path,'urdf','robot_core.xacro')
    # robot_description_config = xacro.process_file(xacro_file)

    # Create a robot_state_publisher node
    params = {'robot_description': robot_desc, 'use_sim_time': use_sim_time}
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params]
    )

    return LaunchDescription([
        # Start robot_state_publisher with the robot description.
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc}]
        ),
        # Launch RViz2 to visualize the robot.
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen'
        )
    ])

